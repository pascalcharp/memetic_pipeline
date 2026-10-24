%
% Modèle optimal
% Canalisations minimalistes
% Contraintes linéarisées
% Pas de bris explicite de symétrie
%

include "globals.mzn" ;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PARAMÈTRES STRUCTURELS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Paramètres fournis

int: NB_EMPLOYES ;
int: NB_ACTIVITES ; 
int: NB_PERIODES ;

% Pour chaque période, le nombre requis d'employés pour une tâche donnée

array[1..NB_PERIODES, 1..NB_ACTIVITES] of 0..NB_EMPLOYES: demande ;

% Pour chaque période, le coût associé à ce que TROP d'employés soient affectés à une tâche

array[1..NB_PERIODES, 1..NB_ACTIVITES] of int: surcout ;

% Pour chaque période, le coût associé à ce que PAS ASSEZ d'employés soient affectés à une tâche

array[1..NB_PERIODES, 1..NB_ACTIVITES] of int: souscout ;

set of int: PERIODES = 1..NB_PERIODES ;

% Les domaines utiles

set of int: RPER = MIN_PERIODES..MAX_PERIODES ;
set of int: RACT = 1..NB_ACTIVITES ;
set of int: REMP = 1..NB_EMPLOYES ;

int: MIN_PERIODES = max([p | p in PERIODES where forall(a in RACT, p2 in PERIODES where p2 < p) (demande[p2,a] = 0 /\ surcout[p2,a] = 0 /\ souscout[p2,a] = 0)]) ;
int: MAX_PERIODES = min([p | p in PERIODES where forall(a in RACT, p2 in PERIODES where p2 > p) (demande[p2,a] = 0 /\ surcout[p2,a] = 0 /\ souscout[p2,a] = 0)]) ;


% Première période à laquelle un employé peut débuter son quart

int: MIN_DEBUT = MIN_PERIODES ;

% Dernière période à laquelle un employé peut commencer son quart

int: MAX_DEBUT = MAX_PERIODES - 27 ;

% Le plus tôt où un employé peut finir son quart

int: MIN_FIN = MIN_PERIODES + 27 ;

% Le plus tard où un employé peut finir son quart

int: MAX_FIN = MAX_PERIODES ;

% Période la plus précoce pour la première pause

int: MIN_P1 = MIN_PERIODES + 4 ;

% Heure la plus tardive possible de la première pause

int: MAX_P1 = MAX_PERIODES - 17 ;

% Période la plus précoce possible pour la deuxième pause

int: MIN_P2 = MIN_PERIODES + 17 ;

% Deuxième pause la plus tardive possible

int: MAX_P2 = MAX_PERIODES - 4 ;

% Dîner le plus précoce

int: MIN_DINER = MIN_PERIODES + 9 ;

% Dîner le plus tardif

int: MAX_DINER = MAX_PERIODES - 12 ;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% VARIABLES DE DÉCISION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Début du quart

array[REMP] of var MIN_DEBUT..MAX_DEBUT: debut ;

% Fin du quart

array[REMP] of var MIN_FIN..MAX_FIN: fin ;

 % Premières pause
  
array[REMP] of var MIN_P1..MAX_P1: pause1 ;

 % Deuxième pause
  
array[REMP] of var MIN_P2..MAX_P2: pause2 ;

 % Dîner 
 
array[REMP] of var MIN_DINER..MAX_DINER: diner ;

% Tâches affectées à chaque employé: chaque employé doit faire exactement 4 tâches par quart
% L'employé change de tâche aux pauses ou au dîner
% Les tâches NE sont PAS nécéssairement différentes: l'employé pourrait faire la même tâche avant et après sa pause, par exemple

array[REMP, 1..4] of var RACT: activites ;

% Ce tableau collige le nombre total d'employés faisant l'activité a à la période p
% Il sera utilisé dans la contrainte de demande, et le calcul du coût

array[RPER, RACT] of var 0..NB_EMPLOYES: total =
    array2d(RPER, RACT, [
          sum (e in REMP) (p >= debut[e] /\ p < pause1[e] /\ activites[e, 1] == a)
        + sum (e in REMP) (p > pause1[e] /\ p < diner[e] /\ activites[e, 2] == a)
        + sum (e in REMP) (p >= diner[e] + 4 /\ p < pause2[e] /\ activites[e, 3] == a)
        + sum (e in REMP) (p > pause2[e] /\ p <= fin[e] /\ activites[e, 4] == a) | p in RPER, a in RACT]) ;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CONTRAINTES STRUCTURELLES DE FAISABILITÉ
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Il doit y avoir une activité entre le début et la pause1, d'une durée d'au-moins une heure

constraint forall (e in REMP) (pause1[e] - debut[e] >= 4) ;

 % Il doit y avoir une activité entre la fin de la pause1 et le dîner.  
 % Elle doit durer au-moins une heure (4 périodes).
 
constraint forall (e in REMP) (diner[e] - pause1[e] >= 5) ;

% Il doit y avoir au-moins une activité entre la fin du dîner et la pause 2, d'au-moins une heure
% Il faut donc considérer la durée du dîner plus l'activité

constraint forall (e in REMP) (pause2[e] - diner[e] >= 8) ;

% Il doit y avoir au-moins une activité entre la pause 2 et la fin du quart, d'au-moins une heure

constraint forall (e in REMP) (fin[e] - pause2[e] >= 4) ;

% Le quart de travail doit durer de 6 à 8 heures.  Attention les bornes sont incluses dans la durée totale d'ou le -1

constraint forall (e in  REMP) (let {var int: duree = fin[e] - debut[e]} in duree >= 27 /\ duree <= 35)  ;

% Au-moins 1 employé est affecté à une tâche ayant une demande.

constraint forall (p in RPER, a in RACT where demande[p, a] != 0) (total[p, a] >= 1) ;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CONTRAINTES DE BRIS DE SYMÉTRIE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Les employés sont interchangeables, il y a donc symétrie complète de permutation entre les employés
% On brise cette symétrie en forçant les horaires de chaque employé à être ordonnés.

%constraint forall (i in 1..NB_EMPLOYES - 1) (
%    lex_lesseq(
%        [debut[i], activites[i,1], pause1[i], activites[i,2], diner[i], activites[i,3], pause2[i], activites[i,4], fin[i]],
%        [debut[i+1], activites[i+1,1], pause1[i+1], activites[i+1,2], diner[i+1], activites[i+1,3], pause2[i+1], activites[i+1,4], fin[i+1]]
%    )
%) ;

% Étant donné que dans nos données élaguées, un employé doit être présent en tout temps, il doit absolument y avoir un
% employé qui débute à 1.  Ce sera l'employé 1.

% constraint debut[1] = MIN_PERIODES ;
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Fonction de coût
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



var int: cout_total = sum(p in RPER, a in RACT) (
    max(0, demande[p, a] - total[p, a]) * souscout[p, a] +
    max(0, total[p, a] - demande[p, a]) * surcout[p, a]
) ;

solve minimize cout_total;



output [
  "{\n",
  "  \"NB_EMPLOYES\": " ++ show(NB_EMPLOYES) ++ ",\n",
  "  \"NB_PERIODES\": " ++ show(NB_PERIODES) ++ ",\n",
  "  \"NB_ACTIVITES\": " ++ show(NB_ACTIVITES) ++ ",\n",
  "  \"debut\": " ++ show(debut) ++ ",\n",
  "  \"fin\": " ++ show(fin) ++ ",\n",
  "  \"pause1\": " ++ show(pause1) ++ ",\n",
  "  \"diner\": " ++ show(diner) ++ ",\n",
  "  \"pause2\": " ++ show(pause2) ++ ",\n",
  "  \"activites\": " ++ show(activites) ++ ",\n",
  "  \"demande\": " ++ show(demande) ++ ",\n",
  "  \"Cout\": " ++ show(cout_total) ++ "\n",
  "}\n"
] ;

output [
  "Employé " ++ show(e) ++ "\t" ++
  concat([
    if p < fix(debut[e]) then show(0)
    elseif p < fix(pause1[e]) then show(fix(activites[e,1]))
    elseif p = fix(pause1[e]) then show(0)
    elseif p < fix(diner[e]) then show(fix(activites[e,2]))
    elseif p < fix(diner[e]) + 4 then show(0)
    elseif p < fix(pause2[e]) then show(fix(activites[e,3]))
    elseif p = fix(pause2[e]) then show(0)
    elseif p <= fix(fin[e]) then show(fix(activites[e,4]))
    else show(0) endif
  | p in 1..NB_PERIODES]) ++ "\n"
| e in REMP
];
 
