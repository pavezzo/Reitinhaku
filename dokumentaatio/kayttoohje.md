# Käyttöohje
## Ohjelman suorittaminen
Ohjelman riippuvuudet asennetaan seuraavasti:
```bash
poetry install
```
Ohjelma käynnistetään seuraavasti:
```bash
poetry run invoke start 
```
Ohjelman aloitusnäkymä näyttää seuraavalta:
![](./kuvat/aloitus.png)
Vasemmalta valitaan kartta ja tämän jälkeen kartta piirtyy ruudulle:
![](./kuvat/valittu.png)
Seuraavaksi valitaan aloitus- ja lopetuskoordinaatit ja valitaan kummalla algoritmilla reitti halutaan selvittää. Jos reitti on olemassa piirtyy algoritmin löytämä reitti punaisella, sekä sinisellä ne ruudut joissa algoritmi on käynyt:
![](./kuvat/reitti.png)
Vasemmalta nähdään myös tietoa, kuten etäisyys ja aika joka algoritmilta kului.