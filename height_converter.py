import os
os.system("cls" if os.name == "nt" else "clear")


print("""
╔══════════════════════════════════════════╗
║          Height Converter Pro            ║
╚══════════════════════════════════════════╝

  Convert your height across all units — instantly.
  Just enter your height and we'll do the rest.

──────────────────────────────────────────
""")

while True:
  try:
    height = float(input("What is your height?: "))
    break
  except ValueError:
    print("Please enter a valid number for height.")

while True:
  current_unit = input("What unit is that in? (m / cm / ft/ in): ").lower()
  if current_unit in ["m", "cm", "ft", "in"]:
    break
  print("Please enter a valid unit (m, cm, ft, in).")

while True:
  target_unit = input("What unit do you want it in?: ").lower()
  if target_unit in ["m", "cm", "ft", "in"]:
    break
  print("Please enter a valid target unit (m, cm, ft, in).")

def convert_height(height, current_unit, target_unit):
  # convert to meters first
  if current_unit == "m":
    meters =  height
  elif current_unit == "cm":
    meters = height / 100
  elif current_unit == "ft":
    meters = height * 0.3048
  elif current_unit == "in":
    meters = height * 0.0254
  else:
    return None

  # Convert from meters to target unit
  if target_unit == "cm":
    return meters * 100
  elif target_unit == "m":
    return meters
  elif target_unit == "ft":
    return meters  * 3.28084
  elif target_unit == "in":
    return meters / 0.0254
  else:
    return None

meters = convert_height(height, current_unit, target_unit)
print(meters)