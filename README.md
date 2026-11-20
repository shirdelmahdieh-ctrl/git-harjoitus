# Kivi, paperi, sakset

Pythonilla toteutettu peli, jossa pelaaja
pelaa tietokonetta vastaan.

Pelaaja valitsee kiven, paperin tai sakset.
Tietokone tekee satunnaisen valinnan.

Peli kertoo voittajan ja laskee pisteet.

## Projektin tavoite

Harjoitella Python-ohjelmointia ja
Git-versionhallintaa.
Pelin seuraava versio: useita kierroksia

## Git-harjoituksen dokumentointi

### Kaytetyt komennot

- git clone: Projektin kloonaaminen GitHubista SSH-yhteydella.
- git add: Muutosten lisaaminen tallennettavaksi.
- git commit: Muutosten tallentaminen Gitin historiaan.
- git branch ja git switch: Haarojen luominen ja vaihtaminen.
- git merge: Haarojen yhdistaminen.
- git stash ja git stash pop: Muutosten valiaikainen tallentaminen ja palauttaminen.
- git revert: Virheellisen commitin kumoaminen.
- git cherry-pick: Yksittaisen commitin poimiminen toisesta haarasta.
- git tag: Pelin version v1.0.0 merkitseminen.
- git rebase main: Haaran paivittaminen main-haaran paalle.
- git push: Muutosten lahettaminen GitHubiin.
- git pull: Muutosten hakeminen GitHubista.

### Ongelmien ratkaiseminen

Harjoituksen aikana SSH-yhteys ei aluksi toiminut oikein, koska GitHubissa oli kaksi eri kayttajatilia. Ongelma ratkaistiin luomalla uusi SSH-avain ja maarittamalla se oikealle tilille.

Harjoittelin myos merge-konfliktin ratkaisemista. Konflikti syntyi, kun README-tiedostoa muutettiin kahdessa eri haarassa. Ratkaisin konfliktin muokkaamalla tiedoston sisallon ja tallentamalla korjauksen uudella commitilla.

### Mita opin?

Opin kayttamaan Gitia Macin Terminalissa ja ymmarsin paremmin, miten versionhallinta toimii.

Opin luomaan haaroja, tallentamaan muutoksia ja yhdistamaan haaroja. Harjoittelin myos virheiden kumoamista, yksittaisten committien siirtamista ja muutosten valiaikaista tallentamista.

Opin lisaksi kayttamaan GitHubia SSH-yhteydella ja tekemaan Pull Requestin.

Harjoituksen aikana tein Pythonilla Kivi, paperi, sakset -pelin, johon lisasin pisteiden laskemisen.
