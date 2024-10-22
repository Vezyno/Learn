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
    """create record"""
    record = {
        'name': name,
        'phone': telephone,
        'adress': adress
    }
    return record

user1 = create_record('vasya', '+794561237', 'pushkina 52')
user2 = create_record('petya', '+795143243', 'bagrationa 45')
print(user1)
print(user2)

def give_award(medal, *persons):
    """Give medal to persons"""
    for person in persons:
        print('Tovaricsh ' + person.title() + ' nagrajdaetsya medaliyu ' + medal.title())

give_award('za berlin', 'vasya', 'petya')
give_award('za London', 'vasya', 'petya', 'nikita', 'misha')