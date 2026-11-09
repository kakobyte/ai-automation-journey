lernstunden_pro_tag = [2.5, 4, 5, 0, 7, 8, 0]

def ist_gueltig_woche(liste):
    datencheck_wochentage = False
    if len(liste) == 7:
        datencheck_wochentage = True
    return datencheck_wochentage

def summe_lernstunden_pro_woche(liste):
    gesamtstunden_pro_woche = 0
    for stunden in liste:
        gesamtstunden_pro_woche += stunden
    return gesamtstunden_pro_woche

def durchschnitt_pro_tag(lernstunden_pro_tag):
    durchschnitt = summe_lernstunden_pro_woche(lernstunden_pro_tag) / len(lernstunden_pro_tag)
    return durchschnitt

def bewerte_lernzeit(stunden):
    if stunden < 10:
        return "Zu wenig für den Plan..."
    elif 10 <= stunden <= 20:
        return "Im Plan..."
    else:
        return "Achtung, Burnout-Gefahr"

def anzahl_nuller_tage(liste):
    nuller_tage = 0
    for stunden in liste:
        if stunden == 0:
            nuller_tage += 1
    return nuller_tage

datencheck_wochentage = ist_gueltig_woche(lernstunden_pro_tag)

if datencheck_wochentage == True:
    gesamtstunden_pro_woche = summe_lernstunden_pro_woche(lernstunden_pro_tag)
    durchschnitt = durchschnitt_pro_tag(lernstunden_pro_tag)
    bewertung = bewerte_lernzeit(gesamtstunden_pro_woche)
    nuller_tage = anzahl_nuller_tage(lernstunden_pro_tag)
    print(f"Die Summe der Stunden pro Woche ist {gesamtstunden_pro_woche}, der Durchschnitt pro Tag beträgt {durchschnitt:.2f}. Insgesamt wäre das dann: {bewertung}. An {nuller_tage} Tag(en) hast du gar nichts gelernt.")
else:
    print("Die Liste muss genau 7 Werte enthalten, einen für jeden Wochentag.")
