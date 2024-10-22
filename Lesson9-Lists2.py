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
