# If-invertering og tidlig returnering
*Hvordan skrive kode som Aleksander vil like*

Ta alt med en klype salt. Jeg er en juniorutvikler og har ikke så mye erfaring med dette. Det er bare mine tanker og meninger.

Jeg brenner for god kode. 
Mye av insperasjonen min kommer fra YouTube-ere som Code Aesthetic, No Boilerplate, ThePrimeagen, ArjanCodes og Fireship for å nevne noen.

Koding/programvareutvikling er en kunstform. Jeg tror av hele mitt hjerte at utvikling bør og må handle om noe mer enn å skrive kode som fungerer. Som utviklere burde vi ha stolthet i den koden vi skriver. Spesielt nå som KI skriver mye av koden vår, tror jeg vi trenger noen retningslinjer og prinsipper som kan hjelpe oss å kjenne igjen god kode. Derfor vil jeg fortelle litt om to av desginprinsippene jeg opplever hjelper meg å skrive god og "ren" kode. Nemlig: "if-invertering" og "tidlig returnering". Dette er to gode prinsipper som sammen lager en dødlig kombo for "dårlig", komplisert og nøstet vibe-kode.

## Plan for workshopen
1. Hvorfor er god kode viktig?
2. Introduksjon til if-invertering og tidlig returnering
3. Live refaktorisering
4. Opggavejobbing

[Eksemple på spagetti]

## Hvorfor er god kode viktig?
God kode er viktig av en rekke grunner. Jeg vil trekke frem noen av dem.

### 1. Vi har begrenset "mental RAM"
Når vi leser kode, bruker vi arbeidsminnet vårt – altså den delen av hjernen som holder informasjon «i lufta» mens vi prøver å forstå sammenhengen. Dette er en begrenset ressurs:

- Forskning viser at mennesker bare klarer å holde **4–7 konsepter** aktivt i arbeidsminnet samtidig.
- Hvis koden er tung, uklar eller full av unødvendige detaljer, fyller vi raskt opp denne kapasiteten og mister oversikten. Vi får en såkalt "cognitive overload" – altså at hjernen ikke klarer å følge med på alt som skjer.
- Resultatet? Vi gjør flere feil, det tar lengre tid å forstå, og hjernen blir fortere sliten.


### 2. Å skrive bedre kode skjerper deg som utvikler
- Å stadig jobbe med å skrive ryddigere, enklere og tydeligere kode, er ikke bare for teamets del – det er **hjernetrim**.
- Du blir bedre til å kommunisere tanker presist, og må stadig reflektere over egne valg («Kunne denne funksjonen vært enklere?»).
- Det gjør at du holder ferdighetene dine skarpe, lærer nye teknikker, og får øye på egne (dårlige) vaner – selv om du har programmert i 10 eller 20 år. Dette gir deg en følelse av progresjon og mestring, uansett hvor erfaren du er.

--- Spørsmål til salen ---

Hva er noen andre grunner til at vi skal bry oss om å skrive god kode?
Ta ett minutt og tenk gjennom.
Nå har det gått et minuttt. Snu deg til sidemannen og snakk om det.
Da er tiden over.
Noen som vil fortelle?

## Del 2
Mange gode inspill her. Så vi er alle enige om at god og lesbar kode er viktig. Men hvordan søren skriver vi god kode? Det tror jeg faktisk nesten ingen vet. Men jeg vet om noen prinsipper som kan hjelpe oss på veien:  if-invertering og tidlig returnering.

### Hva er if-invertering?
«If inversion» handler om å snu logikken i en betingelse (if-setning) for å forbedre lesbarheten eller redusere dybden i koden. Vanligvis gjør man dette når hoveddelen av koden befinner seg i en stor «if-blokk», slik at man heller inverterer betingelsen for å håndtere spesialtilfeller først og tydeligere.

Når vi snakker om å "invertere" eller "snu" en betingelse, handler det om å ta en logisk påstand og uttrykke den, eller sin logiske ekvivalente motsatte betingelsen.

**Eksempel**

La oss ta et konkret eksempel på if-invertering, sånn at vi ser hva det faktisk betyr i praksis.

---
Før invertering:

```js
function handleRequest(user, request) {
  if (user.isLoggedIn) {
    if (request.isValid) {
      process(request); // Funksjonens hovedlogikk
    } else {
      notifyUser("Ugyldig forespørsel.");
    }
  } else {
    notifyUser("Du må logge inn først.");
  }
}
```


Her har vi en klassisk funksjon som skal håndtere en forespørsel av et slag. Den tar inn et bruker-objekt og et forspørsel-objekt. Den ser ganske standard ut. Kanskje noen kjenner seg igjen?

Funksjonen sjekker først om brukeren er logget inn og hvis det er tilfellet så sjekker den om forspørselen er gyldig. Dersom både brukeren er logget inn og forspørselen er gyldig kaller vi på process-funksjonen. Er brukeren ikke logget inn så sender vi ute notifikasjon til brukeren om at han må logge inn først. Dersom det sendes en ugyldig forspørsel varsler vi om det.

Legg merke til hvordan hovedlogikken – altså det vi egentlig vil gjøre, process(request) – ligger dypt inni to if-setninger. Du må først sjekke om brukeren er logget inn, så sjekke om forespørselen er gyldig, før du i det hele tatt får lov å utføre selve handlingen.

Hvis vi skal lese denne koden, så må vi liksom “hoppe ned” gjennom flere nivåer med innrykk og blokker for å finne ut hva som faktisk skjer når alt er som det skal.

---
Hvis vi inverterer if-setningene, så får vi dette:


Etter:
```js
function handleRequest(user, request) {
  if (!user.isLoggedIn) {
    notifyUser("Du må logge inn først.");
  } else if (!request.isValid) {
    notifyUser("Ugyldig forespørsel.");
  } else {
    process(request); // Funksjonens hovedlogikk
  }
}
```

Nå gjør vi nesten det motsatte:
I stedet for å sjekke alle “de gode tilfellene” først, så sier vi: Hvis noe er feil, håndter det med én gang og kom deg ut!
Og bare hvis alt er som det skal, så havner vi nederst i funksjonen – og der ligger hovedlogikken.

Vi spør: “Er brukeren **ikke** logget inn?”
Ja? Da gir vi beskjed om det, og så er vi ferdig.

Hvis brukeren er logget inn, men forespørselen **ikke** er gyldig, så gir vi beskjed om det.

Bare hvis alt er i orden, altså brukeren er innlogget og forespørselen er gyldig, havner vi nederst – og da gjør vi hovedjobben.

Istedenfor å bry oss om når forsepørselen er gydlig, fokuserer vi på når den er ugyldig. For å gi en litt dårlig analogi, så tenk hvis det var sånn at man skulle ringe brannvesenet hver dag og fortelle dem om det brenner eller ikke. Det blir mange unødvendige samtaler. Det er bedre at man kun ringer når noe er feil, altså at det brenner. Ellers gjør vi som alltid.

Fordeler:
- Ofte mindre nesting/innrykk av koden
- Lettere å lese og forstå ved å håndtere spesialtilfeller først.
- Standardiserer hvor man finner funksjonens hovedlogikk (på bunnen)

### Hva er tidlig returnering?
«Early return» handler om å avslutte en funksjon eller metode tidlig når en betingelse er oppfylt, i stedet for å bygge opp store, innfløkte betingelser eller dype blokkstrukturer. Det handler om å avbryte en funksjon så raskt som mulig, når vi allerede vet hva resultatet blir.

**Eksempel**

La oss se på et enkelt eksempel hvor vi sjekker om et tall er lik 7.

---
Før tidlig retur:
```py
def is_seven(num: int) -> bool:
    result = None
    if num == 7:
        result = True
    else:
        result = False

    return result
```

Her har vi en funksjon `is_seven` som tar inn en variable `num` og returner enten `True` eller `False`,

Vi oppretter først en variabel result, og setter den til None.

Så har vi en if-setning hvor vi setter result til enten True eller False – avhengig av om tallet er 7 eller ikke.

Til slutt returnerer vi resultatet.

Det fungerer, men det er en del “omveier” her.
Vi lagrer resultatet i en ekstra variabel bare for å returnere det til slutt.

---
Hvis skriver om til å bruke tidlig returnering får vi dette:

Etter:
```py
def is_seven(num: int) -> bool:
    if num == 7:
        return True

    return False
```

Her gjør vi det mye enklere og mer rett på sak:
- Med én gang vi vet at num == 7, så returnerer vi True.
- Hvis vi ikke har returnert da, så vet vi at svaret er False – og returnerer det direkte.

Vi slipper å lage ekstra variabler, og koden er både kortere og lettere å lese.

---

Fordeler:
- Koden blir mer direkte: man returnerer svaret straks man har det, uten å mellomlagre det «bare for å returnere det til slutt».
- Man slipper ofte å definere ekstra variabler kun for å holde på mellomresultater.
- Funskjoner blir ofte mer kompakte
- Potensielt noe mindre minnebruk og økt ytelse

### Hvorfor passer if-invertering og tidlig returnering så godt sammen?

If-invertering og tidlig returnering er gode prinsipper hver for seg, men når du kombinerer dem, forsterker de hverandres positive egenskaper.

- Med if-invertering håndterer du først alle spesialtilfeller og "negative" scenarioer. Dette gjør at hovedflyten, altså den mest sentrale logikken, ender opp tydelig nederst i funksjonen din.
- Når du samtidig bruker tidlig returnering, kan du umiddelbart avslutte funksjonen med en gang du finner et spesialtilfelle eller en feil. Dette sikrer at funksjonen din ikke fortsetter med unødvendige sjekker eller operasjoner etter at du allerede vet resultatet.

Ved å kombinere prinsippene får du:

- Tydeligere logikk: Du vet nøyaktig hva som går galt med en gang, uten å navigere gjennom dype if-blokker.
- Redusert kompleksitet: Du unngår kompliserte og dype innrykk.
- Økt lesbarhet og vedlikeholdbarhet: Hovedlogikken blir enkel og lett tilgjengelig.

Disse prinsippene er som to gode venner – de fungerer helt greit alene, men sammen blir de en skikkelig effektiv og elegant duo.


--- Spørsmål til salen ---

**Hva er galt med denne koden?**

```py
def handle_order(order):
    if order is not None:
        if order.is_paid:
            if len(order.items) > 0:
                if order.customer.is_active:
                    print("Ordren behandles")
                else:
                    print("Kunde er ikke aktiv")
            else:
                print("Ordren har ingen varer")
        else:
            print("Ordren er ikke betalt")
    else:
        print("Ingen ordre mottatt")
```

Ta ett minutt og tenk gjennom.
Nå har det gått et minuttt. Snu deg til sidemannen og snakk om det.
Da er tiden over.
Noen som vil fortelle?

# Del 3

###  Live refaktorering

# Del 4

### Praktisk oppgave

