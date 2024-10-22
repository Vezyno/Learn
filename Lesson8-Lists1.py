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

delited_city = sities.pop() #вырезать элемент списка
print('Delited city is '+ delited_city)
print(sities)

sities.sort(reverse=True) #сортировать по алфавиту
print(sities)

sities.reverse() #обратный порядок
print(sities)
