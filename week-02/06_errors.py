values = ["65000", "52000", "abc", "", "58000"]
salaries = []
for value in values:
    try:
        salary = int(value)
        salaries.append(salary)
    except ValueError:
        print(f"'{value}' ist keine gültige Zahl")

print(f"Valid salaries: {salaries}")

print("Das Skript läuft weiter!")

path = "week-02/data/gibts_nicht.csv"
try:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Datei nicht gefunden: {path}")