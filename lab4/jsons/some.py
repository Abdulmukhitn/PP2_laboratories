import json

with open("sample.json", "r") as file:
    data = json.load(file)



print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
