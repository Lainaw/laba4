week = ('понедельник','вторник','среда','четверг','пятница','суббота','воскресенье')
input = int(input('Введите кол-во выходных: '))
try:
    if input ==7 :
        raise ValueError
    print ('Ваши выходные дни:',week[-input:])
    print ('Ваши рабочие дни:',week[:7-input])
except ValueError:
    print('ВЫ не можете отдыхать целую неделю!')