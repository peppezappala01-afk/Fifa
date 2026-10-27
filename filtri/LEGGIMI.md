# Filtri per FC Enhancer (app sul telefono, mercato PC)

File: `filtri-carte-pc.json`. Contiene 23 filtri, uno per ogni carta della lista di Requiem. Non ci sono le Holo né le carte con prezzo dubbio.

## Come importarli

1. Scarica il file `.json` sul telefono.
2. Apri FC Enhancer → **Trader**.
3. Premi **Carica** e scegli il file.
4. Deve comparire "Filtri caricati con successo". I filtri si trovano nel menu a tendina dei filtri, sempre nella schermata Trader.

Attenzione: **Scarica** non aggiunge filtri. Serve a esportare quelli che hai già salvato.

Il file vale solo per l'app sul telefono (`"device": true`). L'estensione per browser sul PC rifiuta questo file e vuole `"device": false`.

## Impostazioni di ogni filtro

- **Search:** cerca quella versione esatta della carta tramite il suo codice EA, con il "Compralo ora" massimo uguale al prezzo d'acquisto consigliato.
- **Buy/Bid Settings:** prezzo "Compralo ora" uguale al prezzo d'acquisto consigliato. Nessuna offerta all'asta. Si ferma dopo 1 carta.
- **Selling Settings:** è attivo solo l'invio alla lista trasferimenti. Le carte comprate vanno lì e non vengono messe in vendita in automatico.

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

## Prezzi d'acquisto (PC)

Vengono dalla tabella PC della chat "Prezzi PC da Futbin", basata sui dati FUT Mind del 27/10 mattina.

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
| GRIEZMANN TOTW | 50526413 | 36.500 |
| NETO TOTW | 50570264 | 98.000 |
| DIAZ TOTW | 67349948 | 268.000 |
| HOWARD HERO | 16254 | 83.500 |
| DUDEK HERO | 44897 | 97.000 |
| RAYA IF | 67329765 | 302.000 |
| DONNARUMMA IF | 50562269 | 176.000 |
| SCOTT FS | 50592947 | 238.000 |
| GORDON DESTINY | 50574612 | 231.000 |
| JACOBO RAMON FS | 50402614 | 206.000 |

Carte escluse:

- **Prezzo PC dubbio:** Bellingham, Olise, Kvara.
- **Holo:** Diomande, Griezmann, Neto, Howard, Dudek, Scott, Mastantuono, Barcola, Rogers.

## Come cambiare un prezzo

Nel file, per il filtro che ti interessa, metti lo stesso valore in `criteria.maxBuy` e in `baseSetting.buySetting.buyPrice`.

In alternativa, cambialo nell'app e premi **Salva** con lo stesso nome.
