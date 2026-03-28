# --- Step 1: Collect user inputs ---
user_id = input("Enter ID (numeric, e.g., 968): ")
name_input = input("Enter name (letters only, e.g., maria): ")
role_input = input("Enter role (letters and spaces, e.g., D@t@ Engineer): ")
age_input = input("Enter age (digits only, e.g., 27y): ")
city_input = input("Enter city (letters only, e.g., Brooklyn): ")
country_input = input("Enter country (letters only, e.g., USA): ")
phone_input = input("Enter phone (digits only, e.g., +27 49000002220): ")
gender_input = input("Enter gender (Female/Male): ")
date_input = input("Enter date (YYYY-MM-DD, e.g., 2026-03-28): ")

# --- Step 2: Combine into dirty string ---
data_dirty = f"{user_id}-{name_input}, {role_input}, {age_input}, {city_input} {country_input}, {phone_input}, {gender_input}, {date_input}"
print("\nRaw combined dirty data:")
print(data_dirty)

# --- Step 3: Split & clean ---
parts = [p.strip() for p in data_dirty.replace(";;", ",").split(",")]

# Name
name_raw = parts[0].split("-")[1] if len(parts) > 0 else "N/A"
name = "".join(ch for ch in name_raw if ch.isalpha()).upper()
if not name_raw.isalpha():
    print("Recommendation: Name contains unexpected characters. Only letters are recommended.")

# Role
role_raw = parts[1] if len(parts) > 1 else "N/A"
role = "".join(ch for ch in role_raw if ch.isalpha() or ch == " ").upper()
if any(not (ch.isalpha() or ch == " ") for ch in role_raw):
    print("Recommendation: Role should only include letters and spaces.")

# Age
age_raw = parts[2] if len(parts) > 2 else "N/A"
age = "".join(ch for ch in age_raw if ch.isdigit())
if not age.isdigit():
    print("Recommendation: Age should be numeric only.")

# City & Country
location = parts[3].split() if len(parts) > 3 else ["N/A", "N/A"]

# Clean city
city = "".join(ch for ch in location[0] if ch.isalpha())

# Clean country safely
if len(location) > 1:
    country = "".join(ch for ch in location[1] if ch.isalpha())
else:
    country = "N/A"

# Optional recommendations
if any(not ch.isalpha() for ch in location[0]):
    print("Recommendation: City should contain letters only.")
if len(location) > 1 and any(not ch.isalpha() for ch in location[1]):
    print("Recommendation: Country should contain letters only.")

# Phone
phone_raw = parts[4] if len(parts) > 4 else "N/A"
phone = "".join(ch for ch in phone_raw if ch.isdigit())
if any(not ch.isdigit() for ch in phone_raw if ch not in "+- ()"):
    print("Recommendation: Phone number should contain digits only.")

# Gender
gender = parts[5].lower() if len(parts) > 5 else "N/A"
if gender not in ("male", "female"):
    print("Recommendation: Gender should be Male or Female.")

# Date safe handling
if len(parts) > 6 and "-" in parts[6]:
    date_parts = parts[6].split("-")
    if len(date_parts) == 3 and all(p.isdigit() for p in date_parts):
        year = int(date_parts[0])
        month_num = int(date_parts[1])
        day = int(date_parts[2])
    else:
        print("Recommendation: Date format invalid, using default 2026-03-28")
        year, month_num, day = 2026, 3, 28
else:
    print("Recommendation: Date missing or invalid, using default 2026-03-28")
    year, month_num, day = 2026, 3, 28

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]
month = months[month_num-1]

# Days to expiry (simple)
today_day = 25
days_to_expiry = day - today_day

# --- Step 4: Print cleaned output ---
print("\nCleaned Data:")
print(f"Name: {name} | Role: {role}, Age: {age}, City: {city}, Country: {country}, "
      f"Phone number: {phone}, Gender: {gender}, Year: {year}, Month: {month}, "
      f"Day: {day}, day to expiry {days_to_expiry} days")