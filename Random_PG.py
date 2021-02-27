import random, string
password_length = int(input("How long would does your password need to be?"))
password_characters =string.ascii_uppercase + string.digits + string.punctuation
password = []
for x in range(password_length):
    password.append(random.choice(password_characters))
print(''.join(password))
