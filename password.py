num_passwords = 5
password_list = []
numeric_password_count = 0
alpha_password_count = 0
for i in range(num_passwords):
    password = input("Enter password: ")
    while len(password) < 12:
        password = input("Invalid password! Make sure your password is at least 12 characters long! \nEnter password: ")
    password_list.append(password)
    if password.isnumeric():
        numeric_password_count += 1
    elif password.isalpha():
        alpha_password_count += 1
print("There are {} numerical passwords.".format(numeric_password_count))
print("There are {} alphabetical passwords.".format(alpha_password_count))
print("Reversed form of last password: {}".format(password_list[-1][::-1]))
num_special_chars = 0
for password in password_list:
    for letter in password:
        if letter in ("@", "$", "!", "&"):
            num_special_chars += 1
            break
print("Number of passwords that includes at least one of the following special characters('@', '$', '!', '&'): {}".format(num_special_chars))