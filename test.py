numbers = []
# the method add number to the array by the method append
def array1():
    for i in range(5):
        number = int(input("Donner un nombre positif: "))
        numbers.append(number)
    for j in numbers:
        print(j)


word = ['aloo', 'alassane', 'breezy']
def exmple():
    checked_name = str(input("Donner le nom a rechercher dans le tableau: "))
    if checked_name in word:
        print("le nom "+checked_name + " est dans le tableau")
    else:
        print("Ce nom ne se trouve dans le tableau")
        word.append(checked_name)

def elements():
    for i in word:
        print(i)


def comparaison():
    x = int(input("Donner la valeur de x: "))
    y = int(input("Donner la valeur de y: "))

    if x > y:
        print("{} is greater than {}".format(str(x),str(y)))
    elif x < y:
        print("{} is lower than {}".format(str(x),str(y)))
    else:
        print("{} is equal to {}".format(str(x),str(y)))

n = 0

def characters():
    #global inside a method will allow you to access to a global variable
    global n
    s = str(input("Donner le caractere: "))
    for j in word:
        for o in j:
            if s == o:
                n = n + 1
    print("le nombre de caracteres est: {}".format(str(n)))


def draw():
    for num in range(3):
        for nums in range(3):
            print("#",end="")
        
        print()

vowels = ['a','o','u','i','e','y','A','O','U','I','E','Y']


#the method count the number of vowel
v = 0
def vowel(mot):
    global v
    for i in mot:
        if i in vowels:
            v+= 1
    print("le nombre de voyelles est : " ,v)


mot = str(input("Donner un mot :"))
 
array1()
exmple()
elements()
comparaison()
characters()
draw()
vowel(mot)