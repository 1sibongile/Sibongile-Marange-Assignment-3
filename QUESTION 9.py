import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

# II. Validate a date in the format "YYYY-MM-DD"
def validate_date(date):
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_pattern, date):
        return "Valid date"
    else:
        return "Invalid date"

# III. Replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    return re.sub(rf'\b{re.escape(old_word)}\b', new_word, text)

# IV. Split a string by all non-alphanumeric characters
def split_by_non_alphanumeric(text):
    return re.split(r'\W+', text)  # \W matches any non-alphanumeric character

# Example Usage
text = "Here are some emails: test@example.com, info@company.com. Also, 2022-12-01 is a date and 2023-01-15 is another."

# I. Extract all email addresses
emails = extract_emails(text)
print("Extracted Emails:", emails)

# II. Validate date
date1 = "2022-12-01"
date2 = "12-01-2022"
print(f"Date validation for {date1}: {validate_date(date1)}")
print(f"Date validation for {date2}: {validate_date(date2)}")

# III. Replace word "date" with "event"
replaced_text = replace_word(text, "date", "event")
print("Text after replacing 'date' with 'event':", replaced_text)

# IV. Split by non-alphanumeric characters
split_text = split_by_non_alphanumeric(text)
print("Text after splitting by non-alphanumeric characters:", split_text)
