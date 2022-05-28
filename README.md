# MM-TiRa harjotustyö 2022

![GitHub Actions](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/zmejka/MM-TiRa-harjoitustyo2022/branch/master/graph/badge.svg?token=46FQUTXEF5)](https://codecov.io/gh/zmejka/MM-TiRa-harjoitustyo2022)

----

[Määrittely](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/maarittelydokumentti.md)

[Viikko 1 raportti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/Viikko1_raportti.md)


[Viikko 2 raportti](https://github.com/zmejka/MM-TiRa-harjoitustyo2022/blob/master/dokumentaatio/Viikko2_raportti.md)

----

### Asennus
----

1. Asennuskomento:

        poetry install

### Toiminnot
----

1. Käynnistys:

        poetry run invoke start

2. Testaus

        poetry run invoke test

3. Testikattavuus

        poetry run invoke coverage-report

4. Pylint testaus

        poetry run invoke lint
