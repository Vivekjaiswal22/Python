password = input("Enter a password :")
special = ("@" in password,
           "#" in password,
           "$" in password,
           "*" in password)

upper = False
lower = False
digit = False

for ch in password:
    if ch.isupper():
        upper = True
    if ch.islower():
        lower = True
    if ch.isdigit():
        digit = True

if len(password)>= 8 and upper and lower and digit and special:
    print("Password is strong.")

else:
    print("Weak Password.")