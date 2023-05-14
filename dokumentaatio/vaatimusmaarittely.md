## Tarkoitus

Sovelluksen tarkoituksena on toimia lentosimulaattorin ohessa lokikirjana ja alkeellisena lentosuunnittelijana. Sovellukseen voi siis kirjata tietoja lennetyistä lennoista, ja tiedot tallentuvat ja ovat käyttäjälle saatavilla milloin tahansa. Lentoja voi myös suunnitella lentokentältä toiselle, ja tallentaa reittejä omaan 'kirjastoon'.

## Käyttäjät

Sovellukseen voi luoda useamman käyttäjän, joiden tiedot tallentuvat erikseen.

## Toiminnallisuudet

#### Kirjautuminen

- Kirjautuessa voi valita käyttäjän, jota haluaa käyttää (tehty)
- Käyttäjillä uniikit käyttäjänimet (tehty)
- Käyttäjillä ei ole salasanaa (tehty)

#### Kirjautumisen jälkeen

- Käyttäjä näkee yhteenvedon omista lennoistaan (tehty)
- Käyttäjä voi avata näkymän, josta voi lisätä uuden lennon lokikirjaan (tehty)
  - Tietoja: Päiväys, lähtö, loppu, kesto, lentokone (tehty)
- Käyttäjä voi avata näkymän, jossa voi suunnitella lennon paikasta A paikkaan B (tehty)
  - Lennon voi tallentaa pohjana, jota voi käyttää lokikirjaan lisäämisessä (tehty)
- Lokikirjan järjestely eri kriteereillä: pituus, päiväys, lentokone, lähtö, loppu (tehty)
- Käyttäjä voi kirjautua ulos tai vaihtaa käyttäjää milloin tahansa (tehty)

## Jatkoideoita

- Salasanat
- Näkymässä voi erotella yleisilmailun (pienkoneet) ja lentoyhtiölennot (matkustajakoneet) lennot
- Lennon lisäämisessä voi merkitä matkan pituuden itse, tai antaa sovelluksen laskea se
- Lennon suunnittelussa voi lisätä välietappeja
  - Mikäli sopiva API tai muu tietokanta löytyy, voi lentoihin lisätä muitakin kohteita kuin lentokenttiä (esim. VOR)
- Suunnittelija antaa lennon matkallisen pituuden
- Käyttäjät voivat jakaa omia lentosuunnitelmiaan toisille käyttäjille
