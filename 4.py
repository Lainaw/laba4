import random
group1 = ['Ельцин','Беготина','Чернышева','Котков','Шнайдер','Антпович','Красов','Титов','Мадков','Радионова']
group2 = ['Катушкин','Модин','Денисова','Веселова','Иванов','Терешкова','Линик','Соболева','Ковалева','Щербаков']

gp1 = random.sample(group1,5)
gp2 = random.sample(group2,5)
team = gp1 + gp2
tupleTeam = tuple(team)
print('Списки 1 группы:', group1,'\n','Списки 2 группы:', group2,'\n','Cпортивная команда по алфавиту:',  tuple(sorted(tupleTeam)) )
print('Длина кортежа:', len(tupleTeam))

fam = input('Введите фамилию,которую вы ищите:')
def countX(tupleTeam, x):
    count = 0
    for ele in tupleTeam:
        if (ele == x):
            count = count + 1
    return count

print('Фамилия встречается',countX(tupleTeam, fam),'раз')
