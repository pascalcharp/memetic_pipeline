```Text
Memetic(NR, NM):

    Initialiser population P

    while not terminé(P):

        for j in NR:
            Parents = SelectParent(P)
            Enfants = Recombine(Parents)
            Enfants = SolveurLocal(Enfants)
            Evaluer(Enfants)
            P = P + Enfants

        for j  in NM:
            i = SelectMutable(P)
            Mute(i)
            i = SolveurLocal(i)
            Evaluer(i)
            P = P + {i}
        P = SelectPop(P)
        if (P a convergé)
            P = Restart(P)
   ```
