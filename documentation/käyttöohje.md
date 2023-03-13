# Käyttöohje

![](./images/readme/screencap_scientific_calculator.png)

## Asennusohje

Ohjelmisto on toteutettu ja testattu [Python](https://www.python.org/)-versiolla `3.10` sen Tkinter-kirjastolla sekä riippuvuuksien hallintaan käytettävällä [Poetry](https://python-poetry.org/)-versiolla `1.3`. Vanhemmilla versioilla ohjelmiston toiminnassa saattaa esiintyä ongelmia. 

- [Ohjeet Pythonin asentamiseksi](https://www.python.org/downloads/).
- [Ohjeet Poetryn asentamiseksi](https://python-poetry.org/docs/).
- Lataa tämä repositorio koneellesi ja pura se haluamaasi paikkaan.
- Navigoi komentoriviä käyttäen purkamasi kansion juureen.
- Asenna projektin käyttämät riippuvuudet komennolla: `poetry install`.

## Tieteellisen laskimen käyttäminen

### Käynnistäminen

- Siirry Poetryn virtuaaliympäristöön komennolla: `poetry shell`.
- Käynnistä laskin komennolla: `invoke start`.
- Ongelmatilanteessa katso tämän ohjeen loppuun.

### Perustoiminnot

Laskimen toiminta perustuu joko ruudulla olevien näppäinten käyttöön, tai kirjoittamalla laskutoimituksen suoraan `Expression` -kenttään. Kyseinen kenttä, kuten kaikki muutkin laskimen kentät, tukee laskutoimitusten kopiointia `ctrl + c` sekä liittämistä `ctrl + v`.

Laskimen peruslaskutoiminnot ovat itsestäänselvät jokaiselle nelilaskinta joskus käyttäneelle, mutta näiden toimintojen lisäksi laskimessa on mahdollista käyttää myös muuttujia sekä funktioita.

| Laskutoimitus | Selitys       |
| ------------- | ------------- |
| 1+2           | Yhteenlasku   |
| 7-4           | Vähennyslaksu |
| 10*3          | Kertolasku    |
| 1/2           | Jakolasku     |
| 2^8           | Potenssi      |
| 12 % 3        | Jakojäännös   |

### Muuttujat

Laskin tukee `Variables` -kenttään syötettyjä muuttujia, kuten esimerkiksi `x=1` tai `kissa=3.8`. Muuttujia voi siis käyttää todella vapaasti, eikä niiden lukumäärää ole rajoitettu. Muuttujien joukossa eri muuttujat eroitetaan toisistaan pilkulla, kuten esimerkiksi: `x=11,y=22,z=33` tai `kissa=8, koira=4, kani=6`. Edellä mainittuja muuttujia voisi käyttää `Expression` -kenttään kirjoitetussa laskukaavassa esimerkiksi: `(x*y)/(x^z)`

| Laskutoimitus | Muuttuja        |
| ------------- | --------------- |
| x + y         | x=10, y=8.2     |
| x^y + 14 - z  | x=3, y=8, z=0.2 |

### Funktiot

Laskin tukee `Expression` -kenttään syötettyjä funktioita muodossa `sin()`, `cos()` ja `tan()`. Funktioihin voi sisällyttää yhtälöitä sekä muuttujia, esimerkiksi: `sin(x*4.2)` tai `log(x+y)`.

| Funktio   | Selitys                             |
| --------- | ----------------------------------- |
| sind(12)  | Sini (asteet)                       |
| sinr(0.4) | Sini (radiaani)                     |
| cosd(63)  | Kosini (asteet)                     |
| cosr(0.2) | Kosini (radiaani)                   |
| tand(34)  | Tangentti (asteet)                  |
| tanr(0.7) | Tangentti (radiaani)                |
| sqrt(9)   | Neliöjuuri                          |
| log(23)   | Logaritmi (10-kantainen)            |
| ln(32)    | Luonnollinen logaritmi              |
| rand(100) | Satunnainen kokonaisluku (0-100)    |
| rand(2.3) | Satunnainen desimaaliluku (0.0-2.3) |
| fact(6)   | Kertoma                             |

### Matemaattiset vakiot

| Vakio | Selitys            |
| ----- | ------------------ |
| pi    | Pii                |
| phi   | Kultainen leikkaus |
| tau   | Tau                |
| e     | Eulerin numero     |

### Muistitoiminto

| Painike | Toiminto                                   |
| ------- | ------------------------------------------ |
| MC      | Muistin tyhjennys (ylikirjoittaa muistin)  |
| MR      | Muistin lukeminen                          |
| MS      | Muistiin tallennus (ylikirjoittaa muistin) |
| M+      | Muistiin lisääminen                        |
| M-      | Muistista vähentäminen                     |

### Laskimen sulkeminen

- Laskin suljetaan otsikkopalkissa olevasta ruksista.
- Komentorivillä auki olevasta Poetryn virtuaaliympäristöstä voi poistua komennolla `exit`.

## Mahdolliset ongelmatilanteet

Testauksessa on ilmennyt joidenkin Linux jakelujen sisältämä puuttellinen asennus Python 3:sta, joka ei jostain syystä sisällä kirjastoa `tkinter`. Jos projekti ei käynnisty `invoke start` komennolla, asenna kirjasto tkinter Poetry-virtuaaliympäristön ulkopuolella komennolla `sudo apt install python3-tk`.