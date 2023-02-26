Tällä hetkellä testataan dijkstran algoritmia yksikkötesteillä.\
![](./kuvat/testikattavuus.png)
Lisäksi algoritmien oikeellisuutta testataan moving ai:n scen tiedostoilla, joissa on valmiiksi ratkaistuja reittejä.

## Suorituskyky
Suorituskykyä on testattu kolmella eri kokoisella kartalla:

256x256
| Algoritmi           | Kulunut aika (100 iteraatiota keskiarvo) |
| ------------------- | ---------------------------------------- |
| Dijkstran algoritmi | 0.1915 sekuntia |
| Jump Point Search   | 0.0288 sekuntia |

512x512
| Algoritmi           | Kulunut aika (100 iteraatiota keskiarvo) |
| ------------------- | ---------------------------------------- | 
| Dijkstran algoritmi | 0.8491 sekuntia |
| Jump Point Search   | 0.0822 sekuntia |

1024x1024
| Algoritmi          | Kulunut aika (100 iteraatiota keskiarvo) |
| ------------------ | ---------------------------------------- |
|Dijkstran algoritmi | 3.4546 sekuntia |
| Jump Point Search  | 0.5964 sekuntia |