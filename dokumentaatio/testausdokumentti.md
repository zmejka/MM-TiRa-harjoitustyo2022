# Testausdokumentti
----

## Testaus

Ohjelmaa on testattu kahdella koneella, jossa on Linux OpenSuse ja Mint käyttöjärjestelmät. Ohjelman asentaminen ja  käyttö onnistuu testausalustoilla. 

## Yksikkötestaus

Ohjelman yksikkötestaus on suoritettu unittestillä ja se kattaa muut osat paitsi käyttöliittymän. Yksikkötestauskattavuus on jäänyt matalaksi ainoastaan 84%. Visualisointi-ikkunan kautta saatujen syötteiden, kuten hiiren klikkauksien, toimintojen toimivuutta en osanut toteuttaa. En myöskään onnistunut testaamaan print-toimintojen toimivuutta. Tämän vuoksi main.py testikattavuus on jäänyt ainoastaan 62%. Muiden luokkien testikattavus on yli 90%.

![Coverage](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/coverage_end.png)

Kuva päivitetty 31.7.2022

Yksikkötestit ajetaan automaattisesti githup push- ja pull- toimintojen yhteydessä. Yksikkötestiraportit ovat luettavissa Codecov:ssa.

### Polun pituuden yksikkötestaus 
Lisätty 31.7.2022
Yksikkötesteihin lisättiin 32x32 kartta. Kartassa alkun ja kohdepisteiden välillä on useita lyhyintä reittiä. Kuvassa esitetty kaksi esimerkkiä reitteistä. Lyhyimmän reitin pituus on laskettu käsiin 65.1126983722. Kaikki kolme algoritmiä löytävät saman pituisen lyhyimmän reitin tästä kartasta. Tarkastus on tehty 6 desimaalin tarkkuudella.

![Polku](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/polku_kartta.png)  

## Polun pituuden testaus MovingAI kartalla (valmis scenaario)

Lisätty 31.7.2022
 

## Koodin laatu

Koodin laatua tarkasteltiin pylint:n avulla. Viimeisin pylint raportti antoi arvosanan 9.79/10. Koodin laatuvirheitä olivat esimerkiksi liian monta atribuuttia ja liian monta sisäkkäistä lohkoa. Lisäksi koodissa on jonkin verran toisteisuutta.

## Suorituskykytestaus

Algoritmien suorituskyvyn mittaaminen on toteutettu testaamalla eri karttapohjia. Karttapohjissa suoritettiin satunnaisia, mutta näennäisesti saman pituisia reitteja. Toistoja tehtiin 30 kpl/algoritmi/kartta. Mittareina käytettiin algotritmin suoritukseen käytettyä aikaa, tarkastettujen (laajennettujen) ruutujen määrää ja löytyneen polun pituutta. Käytetyt algoritmit olivat Dijkstra, A-star euklidisella heuristiikalla ja JPS. Esimerkkinä tässä raportissa on kartassa 5 suoritetut testit.

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta5_results.png)

Esimerkit kartta 5 testatuista reitteista:

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta5_paths.png)

Suoritusajan ja polun pituuden viiksilaatikkodiagrammina:

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta5_charts.png)

Kartan 5 tyyppisessä avoimessa näkymässä saavutettiin Dijkstra algoritmiin nähden 2,9 kertainen parannus nopeudessa käyttämällä A-star algoritmia ja 8,8 kertainen parannus JPS algoritmilla. Dijkstra ja A-star algoritmit tuottivat yhtä lyhyet polut, mutta JPS algoritmilla polut sisäsivät noin 10 kertaa vähemmän pisteitä. Suurin muutos tarkastettavien ruutujen määrässä saavutettiin JPS algoritmilla. A* algoritmilla tarkistettiin (laajennettiin) keskimääriin 4 kertaa vähemmän ruutuja ja JPS algoritmilla tarkistettiin noin 425 kertaa vähemmän ruutuja kuin Dijkstran algoritmilla. 

Vastaavasti kartan 3 tyyppisessa sokkeloisessa labyrintissa JPS algoritmi suiriutui ajallisesti heikoiten. JPS oli noin 1,4 kertaa hitaampi kuin Dijkstra ja 2 kertaa hitaampi kuin A-star algoritmi. JPS:n polut sisälsivät noin 2 kertaa vähemmän ruutuja kuin Dijkstran ja A-star algoritmien polut. JPS algoritmilla tarkistettiin noin 6 kertaa vähemmän ruutuja kuin Dijkstran algoritmilla ja noin 5 kertaa vähemmän ruutuja kuin A-star algoritmilla.

Kartan 3 viiksilaatikkodiagrammit:

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta3_charts.png)

Kaikissa testeissa JPS algoritmilla saavutettiin 0.7 - 12 kertainen muutos suoritusajassa verrattuna Dijkstran algoritmin ja 0,7 - 8 kertainen muutos A-star algoritmin verrattuna.  

#### Aikaisemmat testaukset

Projektin alkuvaiheessa on testattu myös eri heuristiikojen vaikutusta A-star algoritmin suorituskykyyn ja toimintaan.

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko6_tulokset.png)

Käytetyt kartat ja reitit.

![Kartta2](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta2.png)
![Kartta4](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta4.png)
![Kartta8](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta8.png)
![Kartta3](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta3.png)


#### Heuristiikkatestaus (toteutettu viikolla 3)

Heuristiikan valinnalla on suuri vaikutus A-star algoritmin suorituskykyyn. Manhattan heuristiikka soveltuu parhaiteen 4 pääsuuntaan (ylös, alas, vasen, oikea) laajeneviin hakuihin, kuten suoria ja kapeita käyttäviä sisältävissa karttoissa. Diagonaalinen ja Euklididinen heuristiikat lajenevaat 8 suuntaan ja niiden välissä ei yleensä ole suurempia erojä. 

![Kartta1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta1_vko3.png)

Testausta tehtiin kolmella eri kartalla. Kahdessa kartassa on suoraviivaiset kapeat käyttäväreitit ja sokkeloinen ympäristö, kun taas yhdessä kartassa on luolatyyppinen ympäristö, jossa on paljon pieniä esteitä. Näissä testeissä ei algoritmin suorituksille eri heuristikoilla saatu merkittäviä eroja. Manhattan heuritiikkaa käyttämällä usein miten polku ei ollut lyhyin mahdollinen, kun taas diagonaalisen ja euklidisen heuristikoiden polkujen pituudet vastasivat toisiaan.

#### Ensimmäinen kartta - leveät käyttävät luolastossa

Tässä scenaariossa parhaimmaksi osoitautui diagonaalinen laskentatapa. 

- Euclidean: 0.164 s
- Diagonal: 0.089 s (paras suoritus)
- Manhattan: 0.207 s

![Kartta1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta1_vko3.png)

Toinen kartta - kapeat käyttävät luolastossa

Tässä skenaariossa ei heuristikoiden välissä ollut merkittäviä eroja.

- Euclidean: 0.197 s
- Diagonal: 0.188 s (paras suoritus)
- Manhattan: 0.203 s

![Kartta1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta2_vko3.png)

Kolmas kartta - luolaympäristö, jossa on paljon pieniä esteitä.

Tässä skenaariossa parhaiksi osoitautui manhattan laskentatapa. 

- Euclidean: 0.426 s
- Diagonal: 0.462 s (löydetty reitti poikkea muista)
- Manhattan: 0.027 s (paras suoritus)

![Kartta1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta3_vko3.png)
