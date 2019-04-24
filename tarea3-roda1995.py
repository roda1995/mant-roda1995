import random
import string
def generatePassword():
    password = ''.join(random.choice(string.punctuation + string.digits+string.ascii_letters) for x in range(4,16))
    print(password)

generatePassword()