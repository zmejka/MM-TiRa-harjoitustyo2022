# Toteutusdokumentti
----

Tässä vaiheessa ohjelma on osittain tekstipohjainen. Algoritmien toiminnan visualisointi on toteutettu Pygame:lla. Ohjelmassa pystyy vertaamaan ja testaamaan A-star ja JPS (Jump Point Search) algoritmien toiminta.

## Sovelluksen rakenne
----
Sovellus koostuu pääohjelmasta, käyttöliittymästä sekä joukosta apuluokkia kuten algorithm_core, queue, jps tai a_star. 

![Rakenne1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/rakenne.png)

Dokumentaatiokansio sisältää ohjelman määrittely-, testaus- sekä toteutusdokumentit. Kuvat kansiossa on dokumenteihin liitettyjä kuvakaappauksia.

### Testit
----
Yksikkötestit on tallennettu src/tests kansioon. Käyttöliittymä ei ole yksikkötestauksessa mukana. Tässä vaiheessa yksikkötestaus on hyvin keskeneräistä.

## Parannettava
----
Ohjelma on keskeneräinen. Koodissa on vielä pajon toisteisuutta ja koodi ei ole vielä optimoitu. Tässä vaiheessa ohjelma kaatuu tilanteissa, jossa polkua ei löydy. Kartan resetoiminen ei vielä toteutettu.

## Suorituskyky
----

A-star algoritmi perustuu Dijkstran algoritmiin. Pahimmassa tapauksessa kuten sokkeloisessa kartassa, jossa on paljon kapeita käyttäviä, A-star algoritmin suoritusaika vastaa Dijkstran algoritmia. Tällöin, jos algoritmi joutuu käymään läpi kaikki ruudut, aikavaativuus on O(V^2). Kun käytetään minimikekoa voidaan kokonaisvaatuvuudeksi O((E+V) log(V)). A-star algoritmin suoritus riippuu heuristikasta. Väärin valittu heuristikka voi huonontaa suorituskykyä merkittävästi.

JPS algoritmi perustuu A-star algoritmiin, mutta käy läpi laskennallisesti vähemmän ruutuja. JPS algoritmi kuitenkin skannaa kaikki reitillä olevat ruudut, mutta lisää niistä vain murto-osan avoimelle listalle. Kartan rakenteesta riippuen JPS algoritmilla voidaan saavuttaa merkittävän suorituskyvyn parannuksen. 

## Lähteet
----
Wikipedia Dijkstra's algorithm https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Wikipedia A-star https://en.wikipedia.org/wiki/A*_search_algorithm

Wikipedia JPS https://en.wikipedia.org/wiki/Jump_point_search