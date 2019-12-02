# Universalais riks dažām vajadzībām ar BME280 un raspberry pi 3
## Apraksts
     Šis brīnums radās izmantojot dažādas komponentes un vadus. Ar šo iekārtu var veikt dažādus aprēķinus, izmantojot sensora BME280 piedāvātos mērījumus un fizikas formulas. Tā darbības
princips ir vienkārš - savienojoties ar RPI 3 un tajā palaižot kodu1.py, ir iespēja izvēlēties darbību. Viena no tām ir vienkārša spēlēšanas ar pogām, otra - kalkulātors ar kuru var aprēķināt dažādas darbības izmantojot BME280 iegūtos datus.
## Shēma
![Shema] (https://raw.githubusercontent.com/JanisUnCo/BME280_SPV/master/bildes/Screenshot_5.png)

![Maize] (https://raw.githubusercontent.com/JanisUnCo/BME280_SPV/master/bildes/Screenshot_4.png)
    Spraužot visu kopā jāņem vēra, ka pini, pie krueim sprauž ir tie, kas ir GPIO nevis plates, attiecīgi pēc koda. Gadījumā, ja BME280 nedod datus vai nelasa, jāpārskata vai ri visi nepieciešamie driveri.

![Prototips] (https://raw.githubusercontent.com/JanisUnCo/BME280_SPV/master/bildes/prottop.jpeg)
    Šādi iekārta izskatās dzīvē.

## Blokshēma un darbība
![Blokshema] (https://raw.githubusercontent.com/JanisUnCo/BME280_SPV/master/bildes/blokshema.jpg)

Iekārta darbojas pavisam vienkārši. Kad teminālī uz RPI palaiž skriptu, tas uzdod 1. jautājumu, kur izvēlēties darbību - spēlēties ar pogām vai izmantot specializēto kalkulātoru. Ja izvēlas darbību ar pogām, tad spiežot attiecīgās pogas tiks veiktas attiecīgās darbības un rādījumi termināli, kā arī dzīvē, uz LED diodēm. Ja izvēlas darbību ar kalkulatoru, ir iespējams izvēlēties 3 tā veidus, kur ievadot nepieciešamos datus, programma aprēķinās gāzes masu telpā un tās ātrumu, izmantojot reālos spidiena un temperatūras rādījumus, kurus iegūst BME280.

## Saites
https://github.com/JanisUnCo/Hangman_Mehatronika_Kiploks
https://buildmedia.readthedocs.org/media/pdf/smbus2/latest/smbus2.pdf
Izmantotās RPI bibliotēkas:
smbus2
bme280
time
random
math
