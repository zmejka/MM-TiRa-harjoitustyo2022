# MM-TiRa harjotustyö 2022

![GitHub Actions](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/zmejka/MM-TiRa-harjoitustyo2022/branch/master/graph/badge.svg?token=46FQUTXEF5)](https://codecov.io/gh/zmejka/MM-TiRa-harjoitustyo2022)

----

[Määrittelydokumentti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/maarittelydokumentti.md)

[Testausdokumentti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/testausdokumentti.md)

[Viikko 1 raportti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/Viikko1_raportti.md)

[Viikko 2 raportti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/Viikko2_raportti.md)

[Viikko 3 raportti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/Viikko3_raportti.md)

[Viikko 4 raportti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/Viikko4_raportti.md)

----

### Asennus
----

1. Asennuskomento:

        poetry install

### Toiminnot
----

1. Käynnistys ja käyttö:

        poetry run invoke start

Ohjelma kysyy kommentorivin syötteet karttanumerolle (1-10) ja algoritmille (1-2 : 1 = A-star, 2 = JPS). Kun ohjelma käynnistyy, paina "Aseta aloituspiste" ja klikkaa kartalle aloituspiste. Sen jälkeen paina "Aseta kohdepiste" ja klikkaa kartalle kohdepiste. Visualisointi käynnistyy heti kohdepisteen asettamisen jälkeen.

![Kuva1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko_4_ohje1.png)
![Kuva2](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko_4_ohje2.png)

 Alkupisteen resetointia ja kartan resetointia ei vielä toteutettu. Tämän vuoksi, jos halua resetoida kartan, ohjelman tässä vaiheessa on käynnistävä uudelleen :( . 

2. Testaus

        poetry run invoke test

3. Testikattavuus

        poetry run invoke coverage-report

4. Pylint testaus

        poetry run invoke lint
