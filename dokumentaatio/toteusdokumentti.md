## Ohjelman yleisrakenne
Ohjelma on jaettu seuraaviin osiin:
- algorithms
- UI
- util

Algorithms pitää sisällään Dijkstran ja JPS algoritmit. UI ohjelman graaffisen toteuksen ja util karttojen lukemiseen tarvittavat toiminnallisuudet.

## Saavutetut aika- ja tilavaativuudet
Molemmille pätee:
* Aikavaativuus: O(n + m log m), jossa n = kaarien lukumäärä ja m = solmujen lukumäärä, vaikkakin JPS on noin kymmenen kertaa nopeampi suorituskykytestauksissa.
* Tilavaativuus: O(n + m)

## Parannuskohteet
* Suorituskykytestauksen olisi voinut integroida suoritettavaan ohjelmaan, jotta niitä olisi voinut ajaa graafisesti

## Lähteet
[Tirakirja](https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf)\
[Online Graph Pruning for Pathfinding on Grid Maps](https://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)\
[jps wikipedia](https://en.wikipedia.org/wiki/Jump_point_search)