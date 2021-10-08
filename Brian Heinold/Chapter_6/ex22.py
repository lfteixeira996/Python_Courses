"""
Write a program that asks the user to enter an email address. Assume for this problem that email
addresses are of the form username@somedomain.com, where there is a user name and a domain
name separate by the @ symbol. Print out the user name and domain name on separate lines.
"""

mail = input("Insert an e-mail: ")

lst = mail.split('@')
user = lst.pop(0)
dom = lst.pop(0)

print("Username: ", user)
print("Domain: ", dom)
