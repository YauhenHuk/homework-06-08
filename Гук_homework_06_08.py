def task_1(accept):
    from datetime import date
    d, m, y = accept.split(' ')
    day_week=date(int(y),int(m),int(d)).isoweekday()
    week={'1':['Понедельник'],'2':['Вторник'],'3':['Среда'],'4':['Четверг'],
          '5':['Пятница'],'6':['Суббота'],'7':['Воскресенье']}
    month={'01':['Январь'],'02':['Февраль'],'03':['Март'],'04':['Апрель'],'05':['Май'],'06':['Июнь'],
           '07':['Июль'],'08':['Август'],'09':['Сентябрь'],'10':['Октябрь'],'11':['Ноябрь'],'12':['Декабрь']}
    dot='.'
    flash='/'
    hyphen='-'
    space=' '
    print(y,dot,m,dot,d)
    print(d,dot,m,dot,y)
    print(m,hyphen,d,hyphen,y)
    print(d,hyphen,m,hyphen,y)
    print(y,hyphen,m,hyphen,d)
    print(m,hyphen,d,hyphen,y[-2:])
    print(d,flash,m,flash,y)
    print(m,flash,d,flash,y[-2:])
    print(d,space,*month[m],space,y)
    print(*week[str(day_week)],space,d,space,m,space,y)

def task_2(file,*argum):
    import openpyxl as xl
    F = xl.open(file, data_only=True)
    sheet = F['man inform']
    for j in range(1, sheet.max_row):
        if sheet['A'][j].value is None:
            for i in range(len(argum)):
                sheet[j+1][i].value= argum[i]
                F.save(file)
            print('Данные успешно записаны в фaйл!')
            break
    F.close()

def task_3(lst,bl):
    for i in lst:
        if float(i) >= 0:
            bl += float(i)
        else:
            square = (lambda x: x ** 2 if '-' in str(x) else x)
            bl += square(float(i))
    return bl

flag=True
while flag:
    menu=input('Введите номер задачи (s - остановить программу): ')
# 1 конвертировать даты (дд мм гггг) в разные форматы
    if menu=='1':
        data=input('Введите дату (дд мм гггг): ')
        task_1(data)

# 2. сделать функцию которая принимает неограниченное количество именованных параметров с информацией о
# человеке и выводит их в файл имя которого также передаётся при вызове
    elif menu=='2':
        name_man=input('Введите имя человека: ')
        info_age=input('Введите возраст человека: ')
        info_status=input('Введите семейное положение человека: ')
        info_profession=input('Введите профессию человека: ')
        info_additional=input('Введите дополнительную информацию про человека: ')
        path_file=input('Введите путь для записи в файл: ')
        task_2(path_file,name_man,info_age,info_status,info_profession,info_additional)

# 3 функция принимает список и баланс
# Прoходится по списку, если число положительное то оно прибавляется к балансу , если отрицательное то
# вызывается другая функция которая возвращает квадрат отрицательно числа и также прибавляет к балансу ,
# сделать проверку что число приходит именно отрицательное , первая функция в итоге должна вернуть баланс
    elif menu=='3':
        numbers=list(input('Введите числа через пробел: ').split(' '))
        balance=float(input('Введите баланс: '))
        print('Новый баланс: ',task_3(numbers,balance))

    elif menu=='s':
        flag =False