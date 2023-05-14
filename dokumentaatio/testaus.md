# Testaus

## Yksikkö- ja integraatiotestaus

Suuri osa testauksesta tapahtuu [TestFileManager](../src/tests/datamanager/filemanager_test.py):n `FileManager`-luokan testien kautta. Testausta varten ei luoda erillistä kopioluokkaa, vaan luokasta luodaan sellaisenaan olio joka tallentaa sovelluksen tavoin testeissä tapahtuvat tiedot levylle. Testitiedostot kuitenkin poistetaan testien jälkeen.

### Testauskattavuus

Testauskattavuus on 88%.

![](./kuvat/tests.png)


## Järjestelmätestaus

Sovellusta on testattu manuaalisesti. Testaus on suoritettu Windows- sekä Linux-ympäristöissä käyttöohjeen mukaisesti. Testaus on lähinnä pohjautunut vain peruskäyttöön ja perustoiminnallisuuden varmistamiseen.

### Toiminnallisuus

Vaatimusmäärittelydokumentin mukaiset toiminnallisuudet on lisätty, ja niiden perustoiminnallisuus on testattu. Osa toiminnallisuudesta perustuu syötteisiin ja niiden käsittelyyn, mutta erilaisia virhesyötteitä ei ole kuitenkaan testattu.


## Laatuongelmat

- Jos `FileManager` ei pysty oikeuksien vuoksi luomaan tarpeellisia kansioita ja tiedostoja, kaikki toiminnallisuus hajoaa
- Tiedostonkäsittelyssä tapahtuvat virheet eivät ilmoita virheistään
- Syötteiden käsittely on paikoitellen puutteellista ja epäkonsistenttia, joka saattaa johtaa virheelliseen toimintaan

