"""Genera i filtri del Trader di FC Enhancer (app sul telefono) da prezzi.csv.

Uso: python3 genera_filtri.py [prezzi.csv] [filtri-carte-pc.json]

Ogni riga di prezzi.csv diventa un filtro che cerca quella versione esatta
della carta (codice EA, quindi la Holo resta separata dalla normale) con
"Compralo ora" massimo uguale al prezzo d'acquisto.
"""
import copy
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Campi di UTSearchCriteriaDTO (web app FC 27), ricerca giocatore
CRITERIA = {
    "academyOnly": False, "_authenticity": "any", "_category": "any", "_position": "any",
    "_sort": "desc", "_subtypes": [], "_type": "player", "_untradeables": "", "_zone": -1,
    "academySlotId": -1, "club": -1, "count": 20, "defId": [], "evolutionStatus": "any",
    "excludeDefIds": [], "excludeLimitedUse": False, "isExactSearch": False, "excludeTimeEvo": False,
    "league": -1, "level": "any", "maskedDefId": 0, "maxBid": 0, "maxBuy": 0, "minBid": 0,
    "minBuy": 0, "nation": -1, "offset": 0, "playStyle": -1, "preferredPositionOnly": False,
    "primaryColor": 0, "rarities": [], "secondaryColor": 0, "sbcChallengeId": 0,
    "pileSearchType": "", "isFavorite": None, "sortBy": "ovr", "icontraits": "any",
    "ovrMin": 45, "ovrMax": 99,
}
# Buy/Bid Settings: solo "Compralo ora" al prezzo d'acquisto, si ferma dopo 5 carte
BUY = {
    "buyPrice": 0, "bidPrice": 0, "noOfCards": 5, "buyPricePercentage": 95, "buyPriceSteps": 0,
    "searchResultThreshold": 21, "bidExactPrice": False, "findBuyPrice": False, "findBidPrice": False,
    "skipGoalKeeper": False, "skipBasicChemistry": False, "skipClubPlayers": False,
    "bidItemsExpiringIn": 3600,
}
# Selling Settings: solo invio alla lista trasferimenti
SELL = {
    "sellPrice": [0, 0], "clearSoldItemThreshold": 10, "ratingThreshold": 100,
    "sellPricePercentage": 100, "sellPriceSteps": 0, "listDuration": 3600, "checkBuyPrice": False,
    "findSellPrice": False, "relistUnSoldItems": False, "quickSell": False, "dontMoveWonItems": False,
    "moveToTransferList": True, "clearSoldItems": False,
}
SEARCH = {
    "randomMinBuy": 300, "randomMinBid": 300, "searchResultPageLimit": 1, "useRandomMinBuy": True,
    "useRandomMinBid": False, "runForeGround": False, "ratingRange": [10, 99], "filterRating": 0,
}
# Impostazioni condivise: sicurezza come da screenshot, il resto ai valori predefiniti dell'app
SHARED = {
    "captchaSetting": {"antiCaptchaKey": "", "proxyAddress": "", "proxyPort": "", "proxyUsername": "",
                       "proxyPassword": "", "closeWebAppOnCaptcha": False, "autoSolveCaptcha": False},
    "commonSetting": {"autoClearLog": True, "autoClearExpired": True, "showSearchLog": True,
                      "showMilliSecond": True, "logTypes": ["ALL"], "sellPriceRange": False},
    "notificationSetting": {"telegramBotToken": "", "telegramChatId": "", "discordBotToken": "",
                            "discordChannelId": "", "discordWebHookUrl": "", "futMarketAlertToken": "",
                            "notificationType": ["ALL"], "sendDesktopNotification": False,
                            "sendListingNotification": False, "sendNotification": False,
                            "soundNotification": False, "customDiscordWHName": False},
    "safeSetting": {"waitTime": [2, 4], "maxPurchasesPerSearchRequest": 1, "pauseCycle": [10, 15],
                    "pauseFor": [3, 6], "stopAfter": [60, 120], "showSearchExceedWarning": False,
                    "disableSafetyLimits": False, "delayAfterBidFor": [0, 0], "errorCount": 1,
                    "errorTypes": []},
}


def step(price):
    """Scatto di prezzo valido sul mercato FUT."""
    if price < 1000:
        return 50
    if price < 10000:
        return 100
    if price < 50000:
        return 250
    if price < 100000:
        return 500
    return 1000


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "prezzi.csv"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "filtri-carte-pc.json"
    filters = {"device": True}  # app sul telefono; l'estensione per browser vuole False
    with open(src, encoding="utf8", newline="") as f:
        for row in csv.DictReader(f):
            name, def_id, buy = row["nome"].strip(), int(row["codice_ea"]), int(row["acquisto"])
            if buy % step(buy):
                sys.exit(f"{name}: {buy} non è un prezzo valido (scatto {step(buy)})")
            criteria = copy.deepcopy(CRITERIA)
            criteria.update({"defId": [def_id], "maxBuy": buy})
            buy_setting = copy.deepcopy(BUY)
            buy_setting["buyPrice"] = buy
            filters[name] = {"criteria": criteria, "baseSetting": {
                "buySetting": buy_setting, "sellSetting": copy.deepcopy(SELL),
                "searchSetting": copy.deepcopy(SEARCH)}}
            print(f"{name:20} {def_id:>10}  max compralo ora {buy:>7}")
    filters["shared"] = copy.deepcopy(SHARED)
    with open(dst, "w", encoding="utf8") as f:
        json.dump({"filters": filters}, f, ensure_ascii=False, indent=1)
    print(len(filters) - 2, "filtri ->", dst)


if __name__ == "__main__":
    main()
