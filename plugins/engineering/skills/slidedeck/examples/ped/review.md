# Revue de cohérence — Présentation Top Management

**Objectif de la présentation :** expliquer en quoi une plateforme DevEx aide à apporter de la valeur au métier (indirectement, en apportant des fondations pour les équipes de développement).

---

## 1. Le lien plateforme → valeur métier est trop faible

Le discours reste presque entièrement dans la sphère technique/développeur. Un directeur entend « les développeurs démarrent plus vite » et « les développeurs sont plus satisfaits », mais n'entend jamais clairement : **« vos applications métier arrivent plus vite en production, avec moins de bugs, pour un coût maîtrisé. »**

**Slides concernées :**

- **Titre** : « permettre à nos équipes de développement de livrer plus vite » — OK comme intro, mais on parle aux équipes de dev, pas au métier.
- **Chiffres clés** : les 4 métriques sont toutes centrées développeur. Il manque la traduction business : « 3 semaines gagnées sur l'onboarding = le projet Gescaff livre son premier sprint 3 semaines plus tôt. »
- **Vision** : « place le développeur au centre » — un top manager entend « on fait plaisir aux développeurs », pas « on accélère la livraison de valeur pour le citoyen. »
- **Framework** : « la standardisation libère du temps pour le métier » est la **seule phrase** de toute la présentation qui fait le pont explicite plateforme → métier. Et elle passe en une seconde sans être développée.

**Suggestion :** Ajouter une phrase de pont systématique dans les notes des slides clés :

- *Chiffres clés :* « Concrètement, quand un nouveau projet démarre, la première livraison arrive 3 semaines plus tôt. Ça veut dire que le métier voit du concret plus vite. »
- *Portail :* « Sans ce portail, chaque équipe réinvente la roue. Le métier attend pendant que les développeurs cherchent comment se connecter à Gestia. »
- *Framework :* « Quand un développeur intègre Alfresco en 2h au lieu de 2 semaines, c'est 2 semaines de fonctionnalités métier en plus. »

---

## 2. Contradiction : « niveau de qualité et de sécurité suffisant »

Slide Vision :

> *« livrer plus vite, plus souvent, avec un **niveau de qualité et de sécurité suffisant** »*

Le mot « suffisant » est dangereux devant un top management du service public. Il donne l'impression qu'on va couper les coins sur la qualité pour aller plus vite. C'est probablement l'inverse de ce que l'on veut dire.

**Suggestion :** Reformuler en « **tout en garantissant** qualité et sécurité » ou « **sans compromettre** la qualité et la sécurité ».

---

## 3. Déséquilibre : NSI prend ~8 slides sur ~25 visibles

La section NSI + Approche Hybride représente un tiers de la présentation. Le risque : le top management retient « il veut nous expliquer pourquoi ne pas prendre NSI » au lieu de « la plateforme apporte de la valeur au métier ».

Le message anti-lock-in revient dans **trois slides** :

- **Principes :** « On ne veut pas se retrouver dans une situation où c'est NSI qui détient la clé »
- **Conclusion :** « On ne veut pas de lock-in sur un framework propriétaire comme JCube ou NgCube dont la migration serait coûteuse »
- **Garder la maîtrise :** « fondamentalement différent d'un modèle où le prestataire reste indéfiniment »

C'est dit trois fois avec des formulations de plus en plus directes. Ça risque de sonner défensif/adversarial plutôt que constructif.

**Suggestion :** Garder un seul passage clair sur le risque de lock-in (dans « Principes »), et reformuler les deux autres de manière positive : ce qu'on **gagne** plutôt que ce qu'on **évite**.

---

## 4. Incohérence structurelle : les 5 dimensions vs les 3 blocs

La slide « Écosystème complet » définit **5 dimensions** : Outillage, Documentation, Standards & Qualité, Support, Culture DevSecOps.

Mais la section « Ce qu'on a déjà » montre **3 blocs** : Portail, Framework, Apps Démo. Puis séparément Utilisateurs et Support.

Le public ne peut pas faire le mapping. Où sont passés « Standards & Qualité » et « Culture DevSecOps » ? Si la plateforme est censée couvrir 5 dimensions et qu'on n'en montre que 3 dans la réalité, le top management peut conclure qu'on est loin du compte.

**Suggestion :** Soit aligner les catégories (ce qu'on définit = ce qu'on montre), soit dans la note de « Vue d'Ensemble » expliquer le mapping explicitement.

---

## 5. La slide « Problèmes » est cachée : le « pourquoi » manque

La slide « Problèmes rencontrés aujourd'hui » est en `data-visibility="hidden"`. Du coup, la présentation passe directement de « voici les attentes d'un développeur » aux chiffres clés, sans jamais montrer **la douleur actuelle**.

Pour un top management, c'est le moment le plus important : « voici ce qui ne va pas, voici combien ça coûte ». Sans cette slide, les chiffres clés arrivent dans le vide. −75 % de temps de productivité, c'est bien, mais −75 % par rapport à quoi ? Le public n'a pas vu le problème.

**Suggestion :** Réactiver cette slide, ou intégrer les points de douleur dans la note de la slide Persona avec des exemples concrets orientés impact métier (« un développeur qui passe 3 semaines à configurer son poste, c'est 3 semaines où le projet métier n'avance pas »).

---

## 6. L'ordre Vision → État des lieux serait plus percutant

Actuellement : Persona → Chiffres → Définition → **Ce qu'on a** → **Vision** → NSI

Le top management se demande « pourquoi je suis là ? » pendant 15 minutes avant d'arriver à la vision. Inverser Vision et État des lieux donnerait :

Persona → Chiffres → Définition → **Vision** (voici où on veut aller) → **Ce qu'on a** (et on est déjà en route) → NSI

C'est mineur mais ça change la perception : « on a une ambition, et on a déjà commencé » est plus fort que « voici ce qu'on a fait, et au fait voici pourquoi ».

---

## 7. Détails dans les notes

| Slide | Problème | Suggestion |
|---|---|---|
| Constat Objectif | L'exemple « DEX avec VKS » est trop interne, un DG ne sait pas ce qu'est VKS | Remplacer par un exemple compréhensible : « quand une nouvelle techno arrive, comment informer 7 équipes en même temps ? » |
| Conclusion | « les développeurs choisissent en fonction de l'outillage » — argument d'attractivité RH au milieu d'une conclusion stratégique | Le placer plus tôt (persona ou vision), pas en conclusion |
| Portail | « méthodologie Diátaxis » — terme inconnu du top management | Dire simplement « on a structuré la doc en 4 types complémentaires » sans nommer la méthodologie |

---

## Résumé des recommandations prioritaires

1. **Ajouter le pont « développeur → métier »** dans les notes des slides Chiffres, Portail, Framework, Vision
2. **Remplacer « suffisant »** par « tout en garantissant » dans la vision
3. **Réduire la redondance anti-lock-in** (3 occurrences → 1 seule claire)
4. **Réactiver ou intégrer les problèmes actuels** pour que les chiffres aient un contexte
5. **Simplifier les références internes** (VKS, Diátaxis) dans les notes
