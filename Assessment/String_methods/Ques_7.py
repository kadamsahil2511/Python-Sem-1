# Ques_7 Write a program which read incoming email, all emails not sent from the "@itm.edu" domain
# should be moved to the spam box.

emails = []
n_emails = int(input("Enter the number of emails: "))

for i in range(n_emails):
    email = input(f"Enter email {i+1}: ")
    emails.append(email)

v_emails = []
s_emails = []

for email in emails:
    if "@itm.edu" in email:
        v_emails.append(email)
    else:
        s_emails.append(email)

print("\nValid Emails:")
for email in v_emails:
    print(email)

print("\nSpam Emails:")
for email in s_emails:
    print(email)
