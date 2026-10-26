# Image de développement et de test : Python 3.13 + MiniZinc 2.10 (CP-SAT, Gecode, Chuffed, HiGHS).
#
# MiniZinc est copié depuis l'image officielle plutôt que compilé : ses binaires ne dépendent que de
# libc, libstdc++, libgcc, libm et libz, compatibles entre Ubuntu noble (glibc 2.39) et Debian trixie (glibc 2.41).
# Les deux images de base existent pour amd64 (GitHub Actions) et arm64 (Mac Apple Silicon).

ARG MINIZINC_VERSION=2.10.0
ARG PYTHON_VERSION=3.13

FROM minizinc/minizinc:${MINIZINC_VERSION}-noble AS minizinc

FROM python:${PYTHON_VERSION}-slim-trixie

RUN apt-get update \
    && apt-get install --yes --no-install-recommends libstdc++6 zlib1g \
    && rm -rf /var/lib/apt/lists/*

# Pilote MiniZinc, exécutables des solveurs, bibliothèque HiGHS et bibliothèque standard MiniZinc.
COPY --from=minizinc /usr/local/bin/minizinc /usr/local/bin/fzn-cp-sat /usr/local/bin/fzn-gecode /usr/local/bin/fzn-chuffed /usr/local/bin/
COPY --from=minizinc /usr/local/lib/libhighs.so /usr/local/lib/
COPY --from=minizinc /usr/local/share/minizinc /usr/local/share/minizinc
RUN ldconfig

# Chemin explicite de MiniZinc, lu par src.utils.minizinc_env (MiniZincConfig.EXECUTABLE_ENV_VAR).
ENV MINIZINC_PATH=/usr/local/bin/minizinc \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt

COPY src/ src/
COPY data/ data/
COPY tests/ tests/

CMD ["python", "-m", "unittest", "discover", "--verbose"]
