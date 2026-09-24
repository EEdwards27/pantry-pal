import json
from datetime import date, datetime, timedelta


def expiring_soon(pantry, days):
    today = date.today()
    latest_date = today + timedelta(days=days)

    return [
        ingredient
        for ingredient in pantry.get("items", [])
        if today <= datetime.strptime(ingredient["expiration"], "%m/%d/%Y").date() <= latest_date
    ]


with open("pantry.json", encoding="utf-8") as pantry_file:
    pantry = json.load(pantry_file)

for ingredient in pantry.get("items", []):
    print(f"{ingredient['name']}: {ingredient['expiration']}")
