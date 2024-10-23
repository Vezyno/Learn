import sys
inputfile = "user-names.txt"
outputfile = "my-passwords.txt"

while True:
    try:
        print('Inside TRY')
        myfile1 = open(inputfile, mode='r', encoding='latin_1')
        myfile2 = open(outputfile, mode='w', encoding='latin_1') # еще есть 'a' то есть append-добавить
    except Exception:
        print('Inside EXCEPT')
        print('Error found in 6-8 stroks')
        print(sys.exc_info()[1])
        inputfile = input('Enter correct file name : ')
    else:
        print('Inside ELSE')
        listok = []
        for num, line in enumerate(myfile1, 1):
            if '66' in line:
                listok.append(num)
                myfile2.write(line)
            print(str(num) + ' hello ' + line.strip())
        print(listok)
        myfile1.close()
        myfile2.close()
        sys.exit() # останавливает файл
    finally: # не обязательно
        print('Inside FINALLY')

print('==========================EOF=====================')