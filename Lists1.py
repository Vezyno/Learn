sities = ['New York', 'Moscow', 'rim', 'Irkutsk', 'Toronto']
print(sities)
print(len(sities))
print(sities[-1])
print(sities[2].title())

sities[2] = 'Tula'
sities.append('Yalta') #добавить элемент справа
sities.append('Kursk')
print(sities)

sities.insert(2,'Feodosiya') #вставить элемент 
print(sities)

del sities[-1]
sities.remove('New York') #удалить элемент
print(sities)

delited_city = sities.pop() #вырезать элемент списка и выделить для него память
print('Delited city is '+ delited_city)
print(sities)

sities.sort(reverse=True) #сортировать по алфавиту и по значению
print(sities)

sities.reverse() #обратный порядок
print(sities)


# ==============================================
print("==================================================")


cars = ['BMW', 'folswagen', 'fiat', 'SKODA', 'lada']
print(cars)
for car in cars:
    print(car.upper())


for x in range(1,6):
    print(x)

mynnumber_list = list(range(len(cars)))
print(mynnumber_list)
print('===============================================')
for x in mynnumber_list:
    x *= 2
    print(x)

mynnumber_list.sort(reverse=True)
print(mynnumber_list)
print('Max number is '+ str(max(mynnumber_list)))
print('Min number is '+ str(min(mynnumber_list)))
print('Sum of list is '+ str(sum(mynnumber_list)))

print('===============================================')
cars = ['BMW', 'folswagen', 'fiat', 'SKODA', 'lada']
mycars = cars[:3]
print(mycars)
mycars = cars[-3:]
print(mycars)

print('===============================================')
cars = ['BMW', 'folswagen', 'fiat', 'SKODA', 'lada']
mycars = cars[:]  #этот список иизменяется отдельно
cars.append('mitsubishi')
print(mycars)