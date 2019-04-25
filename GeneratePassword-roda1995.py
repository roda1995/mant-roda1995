def generatePassword():
    import random
    import string

    while True:
        print("Generación de contraseñas aleatoreas")
        for x in range(1):
            longi=random.randint(4, 16)
        caracteres=string.ascii_letters+string.digits+string.punctuation
        while True:
            passw=("").join(random.choice(caracteres)for i in range(longi))
            if(sum(c.islower() for c in passw)>=1
                and sum(c.isupper() for c in passw)>=1
                and sum(c.isdigit() for c in passw)>=1):
                break
        print("")
        print("Contraseña aleatorea:",passw)
        print("")
        break

generatePassword()
