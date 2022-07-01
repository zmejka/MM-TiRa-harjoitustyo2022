# Toteutusdokumentti
----

"Minne matka?" ohjelman avulla pystyy vertaamaan ja testaamaan Dijkstra, A-star ja Jump Point Search (JPS) algoritmien toimintaa annetuissa kartoissa. Karttojen kulku alueet ovat tasahintaisia, jolloin voidaan ruudusta ruutuun siirtymisen hinnaksi määrittää 1, jos ruutu on viereinen, tai neliöjuuri 2, jos naapuriruutu on kulmittainen naapuri.  Ohjelmassa käytetään Moving AI Lab 2D *Dragon Age: Origins* ja *Dragon Age 2* karttoja. Ohjelman käyttöliittymä on tekstipohjainen ja algoritmien toiminnan visualisointi on toteutettu Pygame:lla. 

______

## Sovelluksen rakenne

Sovellus koostuu pääohjelmasta, käyttöliittymästä sekä joukosta apuluokkia kuten algorithm_core, queue, jps tai a_star. Dijikstra algoritmin toiminta toteutetaan samassa luokassa A-star algoritmin kanssa.

![Rakenne1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/rakenne.png)

Dokumentaatiokansio sisältää ohjelman käyttöohjeen, määrittely-, testaus- sekä toteutusdokumentit. **Kuvat** kansiossa ovat dokumenteihin liitettyjä kuvakaappauksia. Visualisoinnin käyttöliittymä löytyy kansiosta **ui**. Yksikkötestit löytyvät kansiosta **tests**. Sovellus, algoritmiluokat sekä minimikeon luokka löytyvät kansiossa **src**.

### Käyttöliittymä

Käyttöliittymä on tekstipohjainen. Käyttöliittymä pyyttää syötteinä kartta, algoritmi ja heuristiikka tietoja. Algoritmien toiminnan visualisointi ja alku- ja loppupisteiden määritys on toteutettu Pygame:lla. Ohjelma tulostaa konsolille algoritmin suoritukseen kuulunut aika, kuinka monta ruutua on lisätty kekoon, kuinka monta ruutua on laajennettu sekä polun pituus.

### Minimikeko

Minimikeko toteutuksessa käytetty Python valmis tietorakenne *heapq*. Arvoa lisäessä (push), keko järjestää arvot minimijärjestykseen. Arvoa poimiessa (pop), rakenne poistaa minimiarvon keosta, palauttaa sen ja järjestää keon uudestaan.  

### Algoritmit

Dijkstra ja A-star algoritmit on toteutettu A-star luokassa. Algoritmit toimivat muuten samalla tavoin, mutta Dijkstra algoritmi ei laske heuristiista etäisyyttä tarkastettavasta ruudusta loppuruutuun. Algoritmi lisää minimikekoon alkuruudun ja aseta sen etäisyyskustannukseksi 0. Tämän jälkeen algoritmit poimivat minimikeosta pienemmän kustannuksen omaavan ruudun ja laajentavat sen 8 suuntaan (ylös, vasen, oikea, alas, vasen yläviisto, vasen alaviisto, oikea yläviisto, oikea alaviisto). Uusille suunnille lasketaan g-arvo (etäisyys alkupisteestä tarkastettavaan ruutuun) ja, jos g-arvoa ei ollut laskettu ennen tai etäisyyskustannuslistalla oleva arvo on suurempi kuin uusi arvo, lasketaan ruudun heuristiisen etäisyyden loppuruutuun ja lisätään kekoon. Jokaisen ruudun kohdalla tarkistetaan, että ruutu on kulkukelpoinen ja on kartalla. Toistetaan kunnes kohderuutu on löytynyt.

JPS toimii muuten samalla tavoin kuin A-star algoritmi, mutta kekoon lisätään vain ne pisteet, jotka täyttävät hyppypisteen määritelmän tai ovat kääntöpisteitä. Ruudun laajentamisen jälkeen pysty- ja vaakasuuntaan suoritetaan rekursiivisen skannauksen annettuun suuntaan, joka päätyy joko hyppypisteen palauttamiseen tai, jos hyppypistettä ei löydy, tyhjän palauttamiseen. Diagonaalisissa suunnissa rekursiivisesti skannataan kartta annettuun suuntaan. Jos tarkastettava ruutu on hyppypiste, se palautetaan, muuten suoritetaan pysty- (0, k + y-suunta) ja vaakasuunnan (k + x-suunta, 0) skannauksen. Tarkastettava ruutu palautetaan kääntöruutuna, jos jompi kumpi skannauksista palautta hyppypisteen. Jos diagonaalisessa suunnassa ei löydy hyppypisteitä tai kääntöpisteitä, palautetaan tyhjä. 

Algoritmien suorituskyky on arvioitu *Suorituskyky* osassa.

### Testit

Ohjelman testaus on kuvattu testausdokumentaatiossa. Yksikkötestauksesta on jäännyt pois joitakin pygame toimintoja. Käyttöliittymä ei ole yksikkötestauksessa mukana.

______

## Suorituskyky

Heapq tietotakenteen aikavaatimus push toiminnolle on O(log n) ja pop toiminnolle on O(log n), jossa n on tarkastettavien ruutujen määrä. Pahimmassa tapauksessa kuten esimerkiksi Dijkstran algoritmilla, jos kaikki tarkastettavat pisteet lisätään/poistetaan tietorakenteen aikavaativuus on O(n log n).

A-star algoritmi perustuu Dijkstran algoritmiin. Pahimmassa tapauksessa kuten sokkeloisessa kartassa, jossa on paljon kapeita käyttäviä, A-star algoritmin suoritusaika vastaa Dijkstran algoritmia. Tällöin, jos algoritmi joutuu käymään läpi kaikki ruudut, aikavaativuus on O(V^2). Kun käytetään minimikekoa voidaan kokonaisvaatuvuudeksi O((E+V) log(V)). A-star algoritmin suoritus riippuu heuristikasta. Väärin valittu esimerkiksi etäisyyden merkittävästi yläkanttiin arvioiva heuristikka voi huonontaa suorituskykyä merkittävästi.

JPS algoritmi perustuu A-star algoritmiin, mutta käy läpi laskennallisesti vähemmän ruutuja. JPS algoritmi kuitenkin skannaa kaikki reitillä olevat ruudut, mutta lisää niistä vain murto-osan avoimelle listalle. Kartan rakenteesta riippuen JPS algoritmilla voidaan saavuttaa merkittävän suorituskyvyn parannuksen. Etenkin tilavaativuuden nähden JPS algoritmilla saavutetaan monikertaiseen suorituskyvyn parannuksen.

______

## Parannettava

Koodissa on jonkin verran toisteisuutta.

______

## Lähteet

Wikipedia Dijkstra's algorithm https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Wikipedia A-star https://en.wikipedia.org/wiki/A*_search_algorithm

Wikipedia JPS https://en.wikipedia.org/wiki/Jump_point_search

Heapq dokumentaatio https://docs.python.org/3/library/heapq.html

Shortest Path https://harablog.wordpress.com/2011/09/07/jump-point-search/

Introduction to the A-star Algorithm https://www.redblobgames.com/pathfinding/a-star/introduction.html
