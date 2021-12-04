# PDF-PCR-COVID-19-BRUTEFORCE

Après avoir recu un test COVID avec le mauvais mot de passe le weekend et un départ tot. J'étais obilgé de faire un bruteforce pour déverouiller le document.
Je met en ligne le code au cas où ca arrive à d'autres.

A utilser à des fins éducatives uniquement !

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

After getting a french COVID test with the wrong password attached to the pdf over the weekend and an early departure abroad I need to bruteforce the document to unlock it.
I am putting the code online in case it happens to other.

For educational purposes only


# TO READ

Avant de l'utiliser, il vous aidera à savoir comment fonctionne l'algorithme et s'il correspond à ce que vous recherchez.

Pour le moment ce brutforce est réservé aux mots de passe avec ce format :

`[Lettre][Lettre][Lettre][Jour][Jour][Mois][Mois][ANNEE][ANNEE][ANNEE][ANNEE]`

- Les trois premieres lettres correspondent aux trois premieres lettre du nom de famille
- Les jours, mois et année à l'année de naissance du patient

Je commence par incrémenter la **date** jusqu'à ce que j'atteigne **max_date**

Une fois que j'ai atteint **max_date** j'incrémente **lettres** et réinitialise la date à sa date initiale ou par défaut **date**

Exemple:

** Début: **
`` ``
À partir des lettres : ABB
date de début : 31111999
date maximale : 01012000

mot de passe testé : ABB31111999
`` ``

**Incrément:**
`` ``
À partir des lettres : ABB
date de début : 31111999
date maximale : 01012000

mot de passe testé : ABB01121999
`` ``

**Incrément:**
`` ``
À partir des lettres : ABB
date de début : 31111999
date maximale : 01012000

mot de passe testé : ABB02121999
`` ``

continuer à incrémenter ** date ** jusqu'à ce que nous atteignions la ** date max ** donnée

**Incrément:**
`` ``
À partir des lettres : ABB
date de début : 31111999
date maximale : 01012000


mot de passe testé : ABB01012000
`` ``

** La date max ** a été atteinte donc je vais maintenant ** incrémenter ** les ** lettres ** de * ABB * à * ABC * et remettre la date de * 01012000 * à * 31111999 *


**Incrément:**
`` ``
À partir des lettres : ABB
date de début : 31111999
date maximale : 01012000


mot de passe testé : ABC31111999
`` ``


**Incrément:**
`` ``
À partir des lettres : ABB
date de début : 31111999
date maximale : 01012000


mot de passe testé : ABC01121999
`` ``

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Before using it will help you to know how the algorythm works and if it is what you are looking for.

For the moment this brutforce is only for passwords with this format :

`[Letter][Letter][Letter][Day][Day][Month][Month][YEAR][YEAR][YEAR][YEAR]`

- The first three letters corresponding to the first three letters of the last name
- The days, months and year of the patient's year of birth

I start by incrementing the **date** until I attain **max_date**

Once I have attained **max_date** I increment **letters** and reset the date to it's inital given or default **date**

Example:

**Start:**
```
Starting at letters: ABB
date start: 31111999
max date:   01012000

tested password: ABB31111999
```

**Increment:**
```
Starting at letters: ABB
date start: 31111999
max date:   01012000

tested password: ABB01121999
```

**Increment:**
```
Starting at letters: ABB
date start: 31111999
max date:   01012000

tested password: ABB02121999
```

continue incrementing **date** until we attain the given **max date**

**Increment:**
```
Starting at letters: ABB
date start: 31111999
max date:   01012000


tested password: ABB01012000
```

**Max date** has been attained so I will now **increment** the **letters** from  *ABB* to *ABC* and reset the date from *01012000* to *31111999*


**Increment:**
```
Starting at letters: ABB
date start: 31111999
max date:   01012000


tested password: ABC31111999
```


**Increment:**
```
Starting at letters: ABB
date start: 31111999
max date:   01012000


tested password: ABC01121999
```




# Dependencies / Requirements

Le lien de téléchargment est en bas de cette page:

https://www.python.org/downloads/release/python-3100/

lancer ceci dans votre terminal

```
pip3 install -r requirements.txt
```

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The download link is at the bottom of this page:

https://www.python.org/downloads/release/python-3100/

Once installed run this in your terminal

```
pip3 install -r requirements.txt
```

# Usage

```
python3 crack.py

usage: crack.py [-h] [--filename FILENAME] [--letters LETTERS] [--date DATE] [--max_date MAX_DATE]

Crack numeric passwords of PDFs

optional arguments:
  -h, --help           show this help message and exit
  --filename FILENAME  Full path of the PDF file
  --letters LETTERS    Start name 3 CAPITAL letters that will increment until ZZZ default is AAA
  --date DATE          Start date format: DDMMYYYY "01011900" for 1st Jan 1900
  --max_date MAX_DATE  End date format: DDMMYYYY "01012025" for 1st Jan 2025

```

# Example 

```
python3 crack.py --filename test.pdf
```

En supposant que je sache que les 3 premières lettres du nom de famille sont ABC et que la personne est née entre 01011999 (1er janvier 1999) et 01052002 (1er mai 2002)

```
python3 crack.py --filename test.pdf --date 01011999 --max_date 01052002 --lettres ABC
```

Si tu souhaite faire passer sur toutes les combinaisons possibles **Ceci risque de prendre des semaines à trouver la réponse**

```
python3 crack.py --filename test.pdf --date 01010001 --max_date 3112999 --lettres AAA
```

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

```
python3 crack.py --filename test.pdf
```

Assuming I know that the first 3 letters of the last name are ABC and that the person is born between 01011999 (1st of Jan 1999) and 01052002 (1st of May 2002)

```
python3 crack.py --filename test.pdf --date 01011999 --max_date 01052002 --letters ABC
```

If you want to pass on all the possible combinations ** This may take weeks to find the answer **

```
python3 crack.py --filename test.pdf --date 01010001 --max_date 3112999 --letters AAA
```



# Future evolutions

- Allow document format to be specified eg: %Y%Y%Y%Y-%M%M-%DD-%Letter%Letter%Letter
- Provide dictionary attack and database creation script