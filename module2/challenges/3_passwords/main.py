import eoi_passwords


# 1.- Contraseña
password1 = eoi_passwords.create_password()
print(f'Password: {password1}')
print(f'Length: {len(password1)}')

# 2.- Comprobando una contraseña
if eoi_passwords.validate_password(password1):
    print('Valid password')
else:
    print('Invalid password')

# 3.- Validador de contraseñas
password2 = eoi_passwords.create_password()
attempts = 1

while not eoi_passwords.validate_password(password2):
    password2 = eoi_passwords.create_password()
    attempts += 1

print('--')
print(f'Valid password: {password2}')
print(f'Password length: {len(password2)}')
print(f'Attempts made: {attempts}')
