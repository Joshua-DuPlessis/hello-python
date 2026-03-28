data = "968-maria, ( D@t@ Engineer ) ;; 27y, Brooklyn USA, +27 49000002220, Female, 2026-03-28"

# Step 1: Replace ';;' with ',' so we can split everything reliably
data_clean = data.replace(";;", ",")

# Step 2: Split by comma and strip spaces
parts = [p.strip() for p in data_clean.split(",")]

# Step 3: Extract fields safely
name = parts[0].split("-")[1].upper() if len(parts) > 0 else "N/A"
role = "".join(ch for ch in parts[1] if ch.isalpha() or ch == " ").upper().strip() if len(parts) > 1 else "N/A"
age = "".join(ch for ch in parts[2] if ch.isdigit()) if len(parts) > 2 else "N/A"

location = parts[3].split() if len(parts) > 3 else ["N/A", "N/A"]
city = location[0]
country = location[1] if len(location) > 1 else "N/A"

phone = "".join(ch for ch in parts[4] if ch.isdigit()) if len(parts) > 4 else "N/A"
gender = parts[5].lower() if len(parts) > 5 else "N/A"

date_parts = parts[6].split("-") if len(parts) > 6 else ["2026","03","28"]
year = int(date_parts[0])
month_num = int(date_parts[1])
day = int(date_parts[2])

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]
month = months[month_num-1]

# Days to expiry (simple subtraction, assume same month/year)
today_day = 25
days_to_expiry = day - today_day

# Step 4: Print clean result
print(f"Name: {name} | Role: {role}, Age: {age}, City: {city}, Country: {country}, "
      f"Phone number: {phone}, Gender: {gender}, Year: {year}, Month: {month}, "
      f"Day: {day}, day to expiry {days_to_expiry} days")