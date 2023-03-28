## Tarkoitus

Sovelluksen tarkoituksena on toimia lentosimulaattorin ohessa lokikirjana ja alkeellisena lentosuunnittelijana. Sovellukseen voi siis kirjata tietoja lennetyistä lennoista, ja tiedot tallentuvat ja ovat käyttäjälle saatavilla milloin tahansa. Lentoja voi myös suunnitella lentokentältä toiselle, ja tallentaa reittejä omaan 'kirjastoon'.

## Käyttäjät

Sovellukseen voi luoda useamman käyttäjän, joiden tiedot tallentuvat erikseen.

## Toiminnallisuudet

#### Kirjautuminen

- Kirjautuessa voi valita käyttäjän, jota haluaa käyttää
- Käyttäjillä uniikit käyttäjänimet
- Käyttäjillä ei aluksi tule olemaan salasanaa
  - Mikäli aika sen suo, salasanat voidaan lisätä

#### Kirjautumisen jälkeen

- Käyttäjä näkee yhteenvedon omista lennoistaan
- Käyttäjä voi avata näkymän, josta voi lisätä uuden lennon lokikirjaan
  - Tietoja: Päiväys, lähtö, loppu, lentokone
    - Pituuden voi merkitä itse, tai se voidaan automaattisesti laskea
- Käyttäjä voi avata näkymän, jossa voi suunnitella lennon paikasta A paikkaan B
  - Suunnittelija antaa lennon matkallisen pituuden
  - Lennon voi tallentaa pohjana, jota voi käyttää lokikirjaan lisäämisessä
- Käyttäjä voi kirjautua ulos tai vaihtaa käyttäjää milloin tahansa

## Jatkoideoita

- Salasanat
- Näkymässä voi erotella yleisilmailun (pienkoneet) ja lentoyhtiölennot (matkustajakoneet) lennot
- Lokikirjan järjestely eri kriteereillä: pituus, päiväys, lentokone, lähtö, loppu
- Lennon suunnittelussa voi lisätä välietappeja
  - Mikäli sopiva API tai muu tietokanta löytyy, voi lentoihin lisätä muitakin kohteita kuin lentokenttiä (esim. VOR)
- Käyttäjät voivat jakaa omia lentosuunnitelmiaan toisille käyttäjille
