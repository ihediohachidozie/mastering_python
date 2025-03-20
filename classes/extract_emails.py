import re

def extract_emails(text):
    # Regex pattern to match email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Find all matches in the input text
    emails = re.findall(email_pattern, text)

    return emails

# Example usage
def main():
    sentence = "Please contact us at support@example.com or sales@domain.co.uk for futher assistance."

    # Extract email addresses
    extracted_emails = extract_emails(sentence)

    # Print the extracted email addresses
    print("Extracted Emails Addresses.")
    for email in extracted_emails:
        print(email)

if __name__ == "__main__":
    main()