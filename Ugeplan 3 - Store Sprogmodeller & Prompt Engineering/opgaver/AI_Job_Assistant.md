# Udvikling af en AI Job Assistant med Python

## Indledning

Jobsøgning kan være en langsom og stressende proces. Man skal dagligt gennemgå mange jobannoncer, vurdere om stillingerne passer til ens erfaring og skrive forskellige ansøgninger. Hvis man samtidig arbejder omkring ti timer om dagen, kan det være svært at finde tid og energi til en effektiv jobsøgning.

Formålet med dette projekt er derfor at udvikle en AI Job Assistant med Python. Systemet skal automatisere dele af jobsøgningen og hjælpe brugeren med at finde, vurdere og organisere relevante jobmuligheder.

## Problemformulering

Hvordan kan man udvikle en AI-baseret Job Assistant i Python, som reducerer den tid, en jobsøgende bruger på at finde relevante stillinger og udarbejde ansøgninger?

## Projektets mål

Målet er at udvikle et enkelt system, der kan:

1. Indsamle jobannoncer fra udvalgte jobsider.
2. Søge efter stillinger ved hjælp af jobtitel, kompetencer og geografisk område.
3. Sammenligne jobannoncer med brugerens CV.
4. Give hvert job en relevansscore.
5. Skrive et forslag til en målrettet ansøgning.
6. Gemme oplysninger om fundne og sendte ansøgninger.
7. Give brugeren mulighed for at godkende alt før afsendelse.

## Systemets funktioner

### 1. Brugerprofil

Brugeren opretter en profil med oplysninger som:

- Uddannelse
- Erhvervserfaring
- Kompetencer
- Foretrukne jobtitler
- Geografisk område
- Ønsket lønniveau
- Mulighed for hjemmearbejde

Disse oplysninger bruges til at finde passende job.

### 2. Automatisk jobsøgning

Programmet søger regelmæssigt efter nye jobannoncer. Det kan eksempelvis anvende offentlige API'er eller hente oplysninger fra jobsider, hvis sidernes betingelser tillader det.

Systemet skal kunne fjerne dubletter, så den samme stilling ikke bliver vist flere gange.

### 3. AI-baseret vurdering

AI-systemet sammenligner brugerens profil og CV med kravene i jobannoncen. Derefter beregner det en score fra 0 til 100.

Vurderingen kan blandt andet baseres på:

- Match mellem kompetencer
- Relevant erfaring
- Uddannelseskrav
- Arbejdssted
- Sprogkrav
- Andre vigtige kvalifikationer

Systemet forklarer også, hvorfor et job passer eller ikke passer til brugeren.

### 4. Udarbejdelse af ansøgning

Når brugeren vælger et relevant job, kan AI-assistenten lave et udkast til en ansøgning. Ansøgningen skal være baseret på både CV'et og jobannoncen.

AI'en må ikke opfinde erfaringer eller kompetencer. Brugeren skal altid kunne læse, ændre og godkende teksten.

### 5. Overblik over ansøgninger

Systemet gemmer alle job i en database. Hvert job kan få en status som:

- Nyt job
- Skal vurderes
- Ansøgning under udarbejdelse
- Klar til afsendelse
- Ansøgning sendt
- Afslag
- Indkaldt til samtale

På den måde får brugeren et samlet overblik over hele jobsøgningen.

## Teknologier

Systemet kan udvikles med følgende teknologier:

- Python som programmeringssprog
- Flask eller FastAPI til programmets backend
- Streamlit til en enkel brugergrænseflade
- SQLite til lagring af job og ansøgninger
- Pandas til behandling af data
- Beautiful Soup eller Scrapy til tilladt indsamling af jobannoncer
- En sprogmodel til analyse af jobannoncer og udarbejdelse af ansøgninger
- Git og GitHub til versionsstyring

## Systemets arbejdsgang

1. Brugeren uploader sit CV og udfylder sine jobønsker.
2. Programmet søger efter nye job.
3. Jobannoncerne gemmes i databasen.
4. AI'en sammenligner annoncerne med brugerens profil.
5. De bedste job vises øverst.
6. Brugeren vælger et interessant job.
7. AI'en skriver et udkast til en ansøgning.
8. Brugeren kontrollerer og godkender ansøgningen.
9. Systemet registrerer ansøgningens status.

## Sikkerhed og etik

Systemet skal beskytte brugerens personlige oplysninger. CV, kontaktoplysninger og API-nøgler må ikke offentliggøres eller gemmes ukrypteret.

Programmet skal desuden respektere jobsidernes vilkår og regler. Det bør anvende officielle API'er, når de findes. Automatisk afsendelse af mange ansøgninger bør undgås, fordi det kan føre til upræcise ansøgninger eller være i strid med en platforms regler.

Det anbefales derfor, at AI'en fungerer som assistent, mens brugeren træffer den endelige beslutning.

## Udviklingsplan

Projektet kan opdeles i fire faser:

### Fase 1: Grundsystem

- Opret brugerprofil
- Upload og læs CV
- Gem oplysninger i en database

### Fase 2: Jobsøgning

- Hent jobannoncer
- Filtrer efter jobtitel og område
- Fjern dubletter

### Fase 3: AI-funktioner

- Sammenlign CV med jobannoncer
- Beregn en relevansscore
- Lav forslag til ansøgninger

### Fase 4: Test og forbedring

- Test systemet med forskellige jobannoncer
- Kontrollér kvaliteten af AI'ens tekster
- Forbedr brugergrænsefladen
- Undersøg datasikkerhed og fejlhåndtering

## Forventet resultat

Det forventes, at AI Job Assistant kan reducere den tid, brugeren bruger på gentagne opgaver. Systemet kan ikke garantere et job, men det kan skabe struktur, finde relevante muligheder hurtigere og hjælpe med at skrive mere målrettede ansøgninger.

## Konklusion

En AI Job Assistant kan gøre jobsøgningen mere overskuelig og effektiv. Python er velegnet til projektet, fordi sproget har mange værktøjer til kunstig intelligens, dataindsamling, databaser og udvikling af brugergrænseflader.

Den bedste løsning er ikke et system, som foretager alle handlinger uden kontrol. Det bør være en personlig assistent, som udfører det tidskrævende arbejde, mens brugeren godkender job og ansøgninger.
