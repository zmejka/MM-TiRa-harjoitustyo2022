## Minne matka? -ohjelman käyttöohje

### Sisältö:
1. Ohjelman asennus ja käynnistäminen
2. Ohjelman käyttäminen
3. Testien suorittaminen

_____

### Ohjelman asennus ja käynnistäminen

1. Suorita riippuvuuksien asennus komennolla:

    ``` poetry install ```

2. Ohjelma käynnistetään komennolla:

    ``` poetry run invoke start ```

    tai komennolla:

    ``` python3 src/index.py ```

-----

### Sovelluksen käyttäminen

Ohjelman käyttöliittymä on tekstipohjainen. Käynnistyksen jälkeen ohjelma kysyy kartan numero, algoritmi sekä heuristiikka. Jos käyttäjä valitse Dijkstra tai JPS-algoritmia, heuristiikka ei kysytä. 

![Kuva1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kayttoohje_1.png)

Jos käyttäjä antaa virheellisia syötteitä, ohjelma valitse automaattisesti ensimmäisen kartan, A-star algoritmin ja Eukliidisen heuristiikan.

Seuraavaksi käyttäjä määrittää kartalla lähtöpisteen ja kohdepisteen koordinaatit. Painetaan *Aseta aloituspiste* ja klikataan kartalle aloituspiste. Sen jälkeen painetaan *Aseta kohdepiste* ja klikataan kartalle kohdepiste. Visualisointi käynnistyy heti pisteiden asettamisen jälkeen.

![Kuva1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko_4_ohje1.png)
![Kuva2](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko_4_ohje2.png)

Suorituksen jälkeen konsolille tulostuvat laskentaan kuulunut aika, kuinka monta ruutua on lisätty minimikekoon, kuinka monta ruutua on tarkastettu ennen kuin reitti on löytynyt sekä polun pituus.

![Kuva3](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kayttoohje_3.png)

Visualisoinnissa tarkastetut ruudut muuttuvat harmaaksi ja reitti liilaksi. Painaamalla *Uusi kartta* painikettä, pääse alkuun valitsemaan uuden kartan. 

![Kuva4](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kayttoohje_2.png)

Ohjelma lopetetaan joko syöttämällä *Q* kartta valinnan yhteydessä.

-----

### Testien suorittaminen

#### Yksikkötestit

Yksikkötestit testaavat sovelluksen eri osat, käyttöliittymää lukuunottamatta. Testit sijaitsevat kansiossa src/tests
Ohjelamn yksikkötestit suoritetaan komennolla:

   ```
    poetry run invoke test
   ```

Testauksen kattavuusraportti saadaan komennolla:

   ```
    poetry run invoke coverage-report
   ```

#### Koodin laadun tarkastus


Koodin laatua on seurattu Pylint:llä ja se voidaan tarkastaa komennolla:

   ```
    poetry run invoke lint
   ```
