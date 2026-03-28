#cleaning data with re and datetime
import re
from datetime import datetime

data = "968-maria, ( D@t@ Engineer ) ;; 27y, Brooklyn USA, +27 49000002220, Female, 2026-03-28"

# First, split by comma
parts = [p.strip() for p in data.split(",")]

# If parts[2] has both role and age together, split it manually
if ";;" in parts[1]:
    role_part, age_part = parts[1].split(";;")
else:
    role_part = parts[1]
    age_part = parts[2]

# Name
name = parts[0].split("-")[1].upper()

# Role
role = re.sub("[^A-Za-z ]", "", role_part).upper().strip()

# Age
age_match = re.search(r"\d+", age_part)
age = age_match.group() if age_match else "N/A"

# City and country
city, country = parts[2].split() if len(parts) > 3 else ("N/A", "N/A")

# Phone
phone = re.sub(r"\D", "", parts[3] if len(parts) > 4 else "")

# Gender
gender = parts[4].strip().lower() if len(parts) > 5 else "N/A"

# Date
date_str = parts[5].strip() if len(parts) > 6 else "2026-03-28"
date = datetime.strptime(date_str, "%Y-%m-%d")
days_to_expiry = (date - datetime(2026, 3, 25)).days

print(
    f"Name: {name} | Role: {role}, Age: {age}, City: {city}, Country: {country}, "
    f"Phone number: {phone}, Gender: {gender}, "
    f"Year: {date.year}, Month: {date.strftime('%B')}, Day: {date.day}, "
    f"day to expiry {days_to_expiry} days"
)