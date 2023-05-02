# Ohjelmistotekniikan harjoitustyö

Sovellus on lentosimulaattorin ohessa käytettävä lentolokikirja, sekä myöhemmin myös lentosuunnittelutyökalu.

## Dokumentaatio

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)  
[Changelog](dokumentaatio/changelog.md)  
[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

## Käyttöönotto

Riippuvuuksien asennus:
```poetry install```

Sovelluksen käynnistys:
```poetry run invoke start```

### Huomio sovelluksen toiminnasta

Sovellus tallentaa käyttäjien tiedot tiedostoihin, jotka sijaitsevat sovelluksen kotikansion sisällä olevassa kansiossa ```userfiles```.
