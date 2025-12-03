# Basic
first_name = "agustín"
last_name = "braco"
full_name = f"{first_name} {last_name}"

print("First name:", first_name)
print("Last name:", last_name)
print("Full name:", full_name)

# Escaping
message = f"Hola, {full_name.title()}.\nEstas son tus cuentas:\n\t- Caja de ahorro\n\t- Cuenta corriente"
print(message)

# Methods
title = full_name.title()
upper = full_name.upper()
lower = full_name.lower()

print("Title:", title)
print("Upper:", upper)
print("Lower:", lower)

# White spaces
word = " Hola "
rstrip = word.rstrip()
lstrip = word.lstrip()
strip = word.strip()

print("Word:", word)
print("R-Strip:", rstrip)
print("L-Strip:", lstrip)
print("Strip:", strip)

# Prefixes
url = "https://someurl.com"
url_clean = url.removeprefix("https://")

print(url)
print(url_clean)
