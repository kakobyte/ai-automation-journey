
def bewerte_lernzeit(stunden):
    if stunden < 10:
        return "Zu wenig für den Plan..."
    elif 10 <= stunden <= 20:
        return "Im Plan..."
    else:
        return "Achtung, Burnout-Gefahr!"

print(bewerte_lernzeit(5))
print(bewerte_lernzeit(10))
print(bewerte_lernzeit(15))
print(bewerte_lernzeit(20))
print(bewerte_lernzeit(25))