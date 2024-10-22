def napechatat_privetstvie(name):
    print('hello ' + name)

def summa(x,y):
    return x+y

def factorial(x):
    prois = 1
    for i in range(1,x+1):
        prois *= i
    print(prois)

napechatat_privetstvie('nikita')
x = summa(30,20)
print(x)

for i in range(15):
    factorial(i)

#------------------------------
print('----------------------------------')

def create_record(name, telephone, adress):
    record = {
        'name': name,
        'phone': telephone,
        'adress': adress
    }

user1 = create_record('vasya', 894561237, 'pushkina 52')
print(user1)