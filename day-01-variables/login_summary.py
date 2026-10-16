username = (input("Enter your username: "))
failed_login = int(input("How many failed login attempts were found? "))
max_attempts = int(input("What is the maximum number of login attempts allowed? "))

remaining_attempt = max_attempts - failed_login

print(f"username: {username}")
print(f"failed attempts: {failed_login}")
print(f"maximum allowed: {max_attempts}")
print(f"remaining attempts: {remaining_attempt}")



