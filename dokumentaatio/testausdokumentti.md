# Testausdokumentti
----

## Testaus

Ohjelmaa on testattu yhdellä koneella, jossa on Linux OpenSuse käyttöjärjestelmä. Ohjelman asentaminen ja  käyttö onnistuu testausalustalla. 

## Yksikkötestaus

Ohjelman yksikkötestaus on suoritettu unittestillä ja se kattaa tällä hetkellä muut osat paitsi käyttöliittymän. Yksikkötestauskattavuus on jäänyt matalaksi ainoastaan 84%. Visualisointi-ikkunan kautta saatujen syötteiden, kuten hiiren klikkauksien, toimintojen toimivuutta en osanut toteuttaa. En myöstkään onnistunut testaamaan print-toimintojen toimivuutta.

![Coverage](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/coverage_vko6.png)

Yksikkötestit ajetaan automaattisesti githup push- ja pull- toimintojen yhteydessä. Yksikkötestiraportit ovat luettavissa Codecov:ssa.

## Suorituskykytestaus

Algoritmien suorituskyvyn mittaaminen on toteutettu testaamalla eri karttapohjia sekä eri reitti vaihtoehtoja. Tulokset kirjattiin talteen. Mittarina käytettiin algotritmin suoritukseen mennyt aika, tarkastettujen (laajennettujen) ruutujen määrä ja löytyneen polun pituutta. Projektin alkuvaiheessa on testattu myös eri heuristiikojen vaikutusta A-star algoritmin suorituskykyyn ja toimintaan.

![Results](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/vko6_tulokset.png)

Käytetyt kartat ja reitit.

![Kartta2](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta2.png)
![Kartta4](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta4.png)
![Kartta8](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta8.png)
![Kartta3](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta3.png)

## Koodin laatu

Koodin laatua tarkasteltiin pylint:n avulla. Viimeisin pylint raportti antoi arvosanan 9.79/10. Koodin laatuvirheitä olivat esimerkiksi liian monta atribuuttia ja liian monta sisäkkäistä lohkoa. Lisäksi koodissa on jonkin verran toisteisuutta.

### Heuristiikkatestaus (toteutettu viikolla 3)

Heuristiikan valinnalla on suuri vaikutus A-star algoritmin suorituskykyyn. Manhattan heuristiikka soveltuu parhaiteen 4 pääsuuntaan (ylös, alas, vasen, oikea) laajeneviin hakuihin, kuten suoria ja kapeita käyttäviä sisältävissa karttoissa. Diagonaalinen ja Euklididinen heuristiikat lajenevaat 8 suuntaan ja niiden välissä ei yleensä ole suurempia erojä. 

![Kartta1](https://github.com/zmejka/MM-Tira-harjoitustyo2022/blob/master/dokumentaatio/kuvat/kartta1_vko3.png)

Testausta tehtiin kolmella eri kartalla. Kahdessa kartassa on suoraviivaiset kapeat käyttäväreitit ja sokkeloinen ympäristö, kun taas yhdessä kartassa on luolatyyppinen ympäristö, jossa on paljon pieniä esteitä. Näissä testeissä ei algoritmin suorituksille eri heuristikoilla saatu merkittäviä eroja. Manhattan heuritiikkaa käyttämällä usein miten polku ei ollut lyhyin mahdollinen, kun taas diagonaalisen ja euklidisen heuristikoiden polkujen pituudet vastasivat toisiaan.

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
