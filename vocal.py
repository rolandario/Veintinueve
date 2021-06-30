'''4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def word(i):
    i.lower()
    if i == "a" or i == "e" or i =="i" or i=="o" or i=="u":
        return True
    else:
        return False


i=input("Enter the character: ")
print(word(i))




        