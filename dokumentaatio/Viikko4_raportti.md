# Viikkoraportti 4
----

## Mitä on tehty?
----

- Toteutettu alustava versio JPS algoritmista (8 h)
- Testattu A* algoritmin toimivuutta (2 h)
- Molempien algiritmien virheiden etsintä ja korjaukset (4 h)
- Dokumentaation päivittäminen (1.5 h)

## Ohjelman edistyminen
----

Sovelluksen toteutusta on jatkettu. Ohjelmaan lisätty karttoja, mutta niiden vaihtamista käyttöliitymästä ei ole vielä toteutettu. Lisätty kartan ja algoritmin valinta komentoriviltä ensimmäistä vertaisarviointia varten. Ohjelman käyttäminen ei vielä mahdollista ilman kommentorivin syötteitä. Suoritusaika myös tulostuu terminaaliikkunaan eikä sovellusikkunaan. 

Toteutettu alustava versio JPS algiritmista. Algoritmi ei tässä vaiheessa toimi kuten pitäisi. Algoritmi löytää polun alkuruudusta  loppuruutuun, mutta reitti ei aina ole lyhyin mahdollinen. JPS visualisointi ei vielä toteutettu loppuun.

## Mitä olen oppinut?
----

Pääosin JPS algoritmin toiminnan ja toteutuksen opiskelua. 

## Lähteet
----
- T.H.Cormen, C.E.Leiserson, R.L.Rivest, C.Stein Introduction to Algorithms. 3rd edition (2009)
- Wikipedia, A * search algorithm. 2022 https://en.wikipedia.org/wiki/A*_search_algorithm
- A.Patel, 2022: Amit's A* Pages https://theory.stanford.edu/~amitp/GameProgramming/
- Jump Point Search, 2011 https://harablog.wordpress.com/2011/09/07/jump-point-search/
- Koulutusmateriaali http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf

## Mikä jäi epäselväksi? Vaikeuksia:
----

JPS algoritmin toteutus on tuottanut todella paljon vaikeuksia ja ei toimi vieläkään ihan toivotulla tavalla. Virheiden etsinta ja korjaus on osoittautunut ajoittain erittäin haastavaksi.


## Seuraavaksi:
----

JPS algoritmin viimestely. 
Koska JPS algoritmin toteutus vienyt suurimman osan ajasta, automaattitestien kirjoittaminen ja algiritmien testaus jäivät vajaaksi. Testauksen ajantasolle saattaminen. Käyttöliitymän viimestely.

