# Määrittelydokumentti
Ohjelman idea on toteuttaa ainakin Jump Point Search ja Djikstra algoritmi, sekä vertailla niiden suorituskykyä erilaisilla kartoilla.\
Ohjelma toteutetaan python-kielellä ja lisäksi osaan javaa/c++ sen verran, että voin vertaisarvioida niitä.\
Projektin kieli on suomi.
Kuulun tietojenkäsittelytiedeen kandiohjelmaan.

## Tavoitellut aika- tilavaativuudet 
Koska jump point search on optimointi A* -algoritmille tavoittelen sen kohdalla A*:in aika- ja tilavaatimuksia eli molemmilla algoritmeilla pätee seuraava:
* Aikavaativuus: O(n + m log m), jossa n = kaarien lukumäärä ja m = solmujen lukumäärä
* Tilavaativuus: koska tulen tallentamaan kartat 2d listaan on tilavaativuus O(n + m)

JPS nopeuttaa ruudukossa reitin muodostamista hypyillä, sekä rajoittamalla tutkittavia solmuja joten sen kertoimet tulevat olemaan pienemmät kuin dijkstran algoritmilla. 


## Lähteet

- Dijkstran algoritmi: [Tirakirja](https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf)
- JPS: [Online Graph Pruning for Pathfinding on Grid Maps](https://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf) ja [wikipedia](https://en.wikipedia.org/wiki/Jump_point_search)