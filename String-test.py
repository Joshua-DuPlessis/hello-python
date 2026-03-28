import re

ALLOWED_CHARS = "+-() "

def clean_phone(phone: str) -> str:
    """Remove formatting characters from the phone number."""
    return re.sub(r"[^\d]", "", phone)


def is_valid_phone(phone: str) -> bool:
    """
    Validate phone input:
    - Only digits and common phone formatting characters allowed
    - Must contain a reasonable number of digits
    """
    if any(ch.isalpha() for ch in phone):
        return False

    if not all(ch.isdigit() or ch in ALLOWED_CHARS for ch in phone):
        return False

    digits = clean_phone(phone)
    return 7 <= len(digits) <= 15


def main():
    phone = input("Enter your phone number: ").strip()

    if not is_valid_phone(phone):
        print("Invalid phone number, please enter a valid phone number.")
        return

    phone_clean = clean_phone(phone)
    print("Hi, your phone number is:", phone_clean)


if __name__ == "__main__":
    main()