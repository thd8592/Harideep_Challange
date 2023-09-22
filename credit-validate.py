import re

def validate_credit_card(card_number):
    # Define a regular expression pattern to match valid credit card numbers
    pattern = r'^[456]\d{3}(-?\d{4}){3}$|^[456]\d{15}$'
    
    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        # Remove hyphens and check for consecutive repeated digits
        cleaned_number = card_number.replace('-', '')
        if re.search(r'(\d)\1{3,}', cleaned_number):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"

# Example usage:
input_count = int(input())
for _ in range(input_count):
    card_number = input()
    result = validate_credit_card(card_number)
    print(result)
	

