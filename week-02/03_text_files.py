with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Mein Lernziel 1\n")
    f.write("Mein Lernziel 2\n")
    f.write("Mein Lernziel 3\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

with open("notes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Mein Lernziel 4\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)