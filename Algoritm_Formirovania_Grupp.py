#from openpyxl import load_workbook
#import openpyxl
#wb = openpyxl.load_workbook(filename = 'Data.xlsx')
#print(wb)
#sheet = wb['Sheet1']
#val = sheet['G2'].value
#print(val)


#АЛГОРИТМ ФОРМИРОВАНИЯ ГРУПП И ПОДСЧЕТ ЧАСОВ НА ДИСЦИПЛИНУ
import math

def streams(stud, lekc):
    if stud > 100:
        stream = math.ceil(stud/100)
        time_stream = stream*lekc
        return time_stream
    else:
        time_stream = lekc
        return time_stream

def groups(stud, prakt):
    if stud > 30:
        group = math.ceil(stud/30)
        time_group = group*prakt
        return time_group
    else:
        time_group = prakt
        return time_group

def podgroups(stud, lab):
    if stud > 15:
        podgroup = math.ceil(stud/15)
        time_podgroup = podgroup*lab
        return time_podgroup
    else:
        time_podgroup = lab
        return time_podgroup

dis = input('Введите наименование дисциплины:' )
stud = int(input('Введите кол-во студентов: '))
lekc = int(input('Введите кол-во часов лекций: '))
prakt = int(input('Введите кол-во часов практических занятий: '))
lab = int(input('Введите кол-во часов лабораторных занятий: '))
srs = int(input('Введите 1 если есть КП или КР, иначе 0: '))
attest = int(input('Введите вид аттестации (зачет - 1, экзамен - 2, атестация - 3: '))

time_str = streams(stud, lekc)
print('Часы лекций для всех потоков =', streams(stud, lekc))

time_gr = groups(stud, prakt)
print('Часы практических занятий для всех групп =', groups(stud, prakt))

time_podgr = podgroups(stud, lab)
print('Часы лабораторных занятий для всех подгрупп =', podgroups(stud, lab))

time_attest = 0.25*stud
print('Часы для аттестации =', time_attest)
time_srs = 0
if srs == 1:
    time_srs = stud
print('Часы для CРС =', time_srs)
kolvo_clock = time_str+time_gr+time_podgr+time_srs+time_attest
print('Для дисциплины', dis, 'необходимо', kolvo_clock, 'часов')



#АЛГОРИТМ РАСПРЕДЕЛЕНИЯ МЕЖДУ ППС
PPS = input('Введите фамилию преподавателя: ')
dolg = input('Введите должность преподавателя: ')
stavka = int(input('Введите ставку преподавателя: '))
zan_clock1 = int(input('Введите занятые часы преподавателя в 1 семестре: '))
zan_clock2 = int(input('Введите занятые часы преподавателя во 2 семестре: '))


sem = int(input('Введите семестр дисциплины: '))

svob_clock1, svob_clock2 = 0, 0

if dolg == 'профессор':
    if stavka == 1:
        svob_clock1 = 425 - zan_clock1
        svob_clock2 = 425 - zan_clock2
    elif stavka == 0.75:
        svob_clock1 = 318.75 - zan_clock1
        svob_clock2 = 318.75 - zan_clock2
    elif stavka == 0.5:
        svob_clock1 = 212.5 - zan_clock1
        svob_clock2 = 212.5 - zan_clock2
else:
    if (stavka == 1):
        svob_clock1 = 450 - zan_clock1
        svob_clock2 = 450 - zan_clock2
    elif (stavka == 0.75):
        svob_clock1 = 337.5 - zan_clock1
        svob_clock2 = 337.5 - zan_clock2
    elif (stavka == 0.5):
        svob_clock1 = 225 - zan_clock1
        svob_clock2 = 225 - zan_clock2



print('Свободных часов у преподавателя в 1 семестре =', svob_clock1)
print('Свободных часов у преподавателя во 2 семестре =', svob_clock2)

#from get_data import data
#for i in data.iloc:
    #print(i)

if (kolvo_clock <= svob_clock1) and (sem == 1):
    print('Дисциплина', dis, 'назначается ', PPS)
    svob_clock1_changed = svob_clock1 - kolvo_clock
    zan_clock1 = zan_clock1 + svob_clock1_changed
elif (kolvo_clock > svob_clock1) and (sem == 1):
    #Преподаватель меняется, то есть break
    #Если есть другой свободный преподаватель, способный вести эту дисциплину
    #Если нет, то нагружаем
    if (time_str <= svob_clock1):
        print("Лекции дисциплины", dis, 'назначается', PPS)
    elif (time_str+time_gr <= svob_clock1) or (time_str+time_podgr <= svob_clock1):
        print("Лекции и практические/лабораторные занятия дисциплины", dis, 'назначаются', PPS)


    
