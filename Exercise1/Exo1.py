import json
import csv

with open("data.json", "r", encoding="UTF8") as f:
    data = json.load(f)

header = ["reel", "imaginaire"]

with open("nb_complexe.csv", "w", newline='', encoding="UTF8") as c:
    writer = csv.writer(c, delimiter=",")
    writer.writerow(header)
    writer.writerows(data)
