# Задача 1
# import math
# n=int(input("Расстояние в день: "))
# s=int(input("Расстояние общее: "))
# x=s/n
# print("Количество дней: ", math.ceil(x))

# Задача 2
# a=int(input("Количество учеников в 1-м классе: "))
# b=int(input("Количество учеников в 2-м классе: "))
# c=int(input("Количество учеников в 3-м классе: "))

# if a%2==0:
#     x1=a/2
# else:
#     x1=a/2+0.5       
 
# if b%2==0:
#     x2=b/2
# else:
#     x2=b/2+0.5
     
# if c%2==0:
#     x3=c/2
# else:
#     x3=c/2+0.5 
    
# print("Минимальное кол-во парт:", x1+x2+x3)  


# Задача 2: Найдите сумму цифр трехзначного числа.

# num = (input("Просьба ввести 3-х значное число: "))
# result=int(num[0])+int(num[1])+int(num[2])
# print(result)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s=int(input("Просьба ввести число журавликов: "))
# if s%6!=0:
#     print("Просьба ввести число кратное 6")
# else:
#     print("Петя сделал ",int(s/6)," журавликов")
#     print("Сережа сделал ",int(s/6)," журавликов")
#     print("Катя сделала ",int(s/6*4)," журавликов")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# n = (input("Просьба ввести 6-ти значный номер билета: "))

# if int(n[0])+int(n[1])+int(n[2])==int(n[3])+int(n[4])+int(n[5]):
#     print("Билет счастливый")
# else:
#     print("Повезёт в другой раз")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n=int(input("Просьба ввести длинну шоколадки "))
m=int(input("Просьба ввести ширину шоколадки "))
k=int(input("Просьба ввести кол-во отломанных долек "))

res=m*n-k

if res/m-round(res/m)==0 or res/n-round(res/n)==0:
    print("Шоколад получилось поделить ровно.")
else:
    print("Шоколад не получилось поделить по прямой.")
    
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no