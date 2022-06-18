# Testausdokumentti
----

## Testaus

Ohjelmaa on testattu tässä vaiheessa vain yhdellä koneella, jossa on Linux OpenSuse käyttöjärjestelmä. Ohjelman asentaminen ja  käyttö onnistuu testausalustalla. 

## Yksikkötestaus

Tässä vaiheessa (viikko 6) yksikkötestauskattavuus. Testikattavuutta on tarkoitus vielä parantaa ennen loppupalautusta.

![Coverage](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/coverage_vko6.png)

## Suorituskykytestaus

Jatkettu algoritmien vertaileva testausta.

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko6_tulokset.png)

Käytetyt kartat ja reitit.

![Kartta2](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta2.png)
![Kartta4](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta4.png)
![Kartta8](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta8.png)
![Kartta3](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta3.png)

### Viikolla 3 tehdy heuristiikkatestaus.

![Kartta1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta1_vko3.png)

Aloitettu toteuttamaan suorituskykytestausta. Koska tässä vaiheessa on käytössä vain yksi algoritmi, testaus tehtiin vertaamalla eri heuristiikojen vaikutusta suoritusaikoihin.

Testausta tehtiin kolmella eri kartalla. Kahdessa kartassa on suoraviivaiset kapeat käyttäväreitit ja sokkeloinen ympäristö, kun taas yhdessä kartassa on luolatyyppinen ympäristö, jossa on paljon pieniä esteitä. Näissä testeissä ei algoritmin suorituksille eri heuristikoilla saatu merkittäviä eroja. 

### Ensimmäinen kartta - leveät käyttävät luolastossa

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
