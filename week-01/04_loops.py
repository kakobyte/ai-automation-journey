def bewerte_lernzeit(stunde):
    if stunde < 10:
        return "Zu wenig für den Plan..."
    elif 10 <= stunde <= 20:
        return "Im Plan..."
    else:
        return "Achtung, Burnout-Gefahr!"

stunden_werte = [5, 10, 15, 20, 25]
im_plan = 0

for stunde in stunden_werte:
    bewertung = bewerte_lernzeit(stunde)
    print(f"{stunde} Stunden: {bewertung}")
    if bewertung == "Im Plan...":
        im_plan += 1

print(f"Anzahl der Lernstunden im Plan: {im_plan}")