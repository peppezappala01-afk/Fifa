# Filtri per FC Enhancer (app sul telefono, mercato PC)

File: `filtri-carte-pc.json`. Contiene 29 filtri, uno per ogni carta della lista di Requiem: 23 normali e 6 Holo. Le carte con prezzo PC dubbio sono escluse.

## Come importarli

1. Scarica il file `.json` sul telefono.
2. Apri FC Enhancer → **Trader**.
3. Premi **Carica** e scegli il file.
4. Deve comparire "Filtri caricati con successo". I filtri si trovano nel menu a tendina dei filtri, sempre nella schermata Trader. Quelli con lo stesso nome vengono sostituiti.

Attenzione: **Scarica** non aggiunge filtri. Serve a esportare quelli che hai già salvato.

Il file vale solo per l'app sul telefono (`"device": true`). L'estensione per browser sul PC rifiuta questo file e vuole `"device": false`.

## Impostazioni di ogni filtro

- **Search:** cerca quella versione esatta della carta tramite il suo codice EA, con "Compralo ora" massimo uguale al prezzo d'acquisto.
- **Buy/Bid Settings:** prezzo "Compralo ora" uguale al prezzo d'acquisto. Nessuna offerta all'asta. Si ferma dopo 5 carte comprate (Cards to Buy Count = 5).
- **Selling Settings:** è attivo solo l'invio alla lista trasferimenti. Le carte comprate non vengono messe in vendita in automatico.

## Safety Settings (uguali per tutti i filtri)

| Impostazione | Valore |
|---|---|
| Wait Time in Seconds | 2 – 4 |
| Stop After Minutes | 60 – 120 |
| Pause Cycle | 10 – 15 |
| Pause for Seconds | 3 – 6 |
| Max Bids Per Request | 1 |
| Delay After Bid (secs) | 0 – 0 |
| Error codes to stop | nessuno |

Il file contiene anche le altre impostazioni condivise (captcha, notifiche, log), con i valori predefiniti dell'app. Importandolo, se in quelle sezioni avevi inserito qualcosa (per esempio un bot Telegram o Discord), va reinserito.

## Holo nel Trader

Nel pannello del Trader non c'è una casella "Holo". Ogni versione Holo però ha un proprio codice EA, diverso da quello della carta normale (per esempio Diomande TOTW è 67186876, la sua Holo è 83964092). Un filtro con il codice della Holo cerca solo la Holo, e viceversa.

Anche la ricerca "Holographic only" del mercato di FC Enhancer funziona così: sostituisce la ricerca per giocatore con l'elenco dei codici delle Holo. L'app avvisa che questo filtro non esiste ancora nella web app EA e che al server viene mandata una richiesta modificata.

## Prezzi d'acquisto (PC)

Vengono dalla tabella PC della chat "Prezzi PC da Futbin": prezzi d'acquisto di Requiem riportati su PC con i prezzi console e PC di FUT Mind del 27/10 mattina. **Non sono i minimi toccati la notte su Futbin**: lo storico di Futbin non è raggiungibile dal server cloud.

| Filtro | Codice EA | Max "Compralo ora" |
|---|---|---|
| NUNO MENDES | 252145 | 252.000 |
| BONMATI | 241667 | 278.000 |
| HANSEN | 227102 | 218.000 |
| PEDRI | 251854 | 219.000 |
| GUIJARRO | 237289 | 208.000 |
| LAMINE YAMAL | 277643 | 140.000 |
| PACHO | 256196 | 151.000 |
| PAJOR | 241846 | 155.000 |
| HAKIMI | 235212 | 85.000 |
| KARCHAOUI | 233662 | 85.500 |
| MARIONA | 237288 | 46.750 |
| VALVERDE | 239053 | 286.000 |
| DIOMANDE TOTW | 67186876 | 244.000 |
| DIOMANDE TOTW HOLO | 83964092 | 306.000 |
| GRIEZMANN TOTW | 50526413 | 36.500 |
| GRIEZMANN TOTW HOLO | 67303629 | 80.000 |
| NETO TOTW | 50570264 | 98.000 |
| NETO TOTW HOLO | 67347480 | 142.000 |
| DIAZ TOTW | 67349948 | 268.000 |
| HOWARD HERO | 16254 | 83.500 |
| DUDEK HERO | 44897 | 97.000 |
| RAYA IF | 67329765 | 302.000 |
| DONNARUMMA IF | 50562269 | 176.000 |
| SCOTT FS | 50592947 | 238.000 |
| SCOTT FS HOLO | 67370163 | 295.000 |
| GORDON DESTINY | 50574612 | 231.000 |
| MASTANTUONO FS HOLO | 100942469 | 283.000 |
| BARCOLA MOTM HOLO | 84150732 | 736.000 |
| JACOBO RAMON FS | 50402614 | 206.000 |

Carte escluse:

- **Prezzo PC dubbio:** Bellingham, Olise, Kvara.
- **Holo con poche copie su PC:** Howard Hero Holo, Dudek Hero Holo.
- **Senza mercato PC:** Rogers Destiny Holo.

## Come cambiare i prezzi

- **Nel file:** modifica la colonna `acquisto` di `prezzi.csv` e rigenera il JSON con `python3 genera_filtri.py`. Lo script controlla che ogni prezzo rispetti gli scatti di FUT.
- **Nell'app:** cambia il valore e premi **Salva** con lo stesso nome.
