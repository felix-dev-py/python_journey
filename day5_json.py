import json

data = [{"task": "Go to shop", "Done": False}, {"task":"Buy some food", "Done": False}, {"task": "Coding one hour on Python", "Done": True}]

with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("tasks.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)

print(f"\nLen: {len(data)}")