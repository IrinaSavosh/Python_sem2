# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек.

number = int(input("Введите цифру от двух до девяти: "))
lst_a = list() 
for i in range(number): 
   n = int(input("Введите координату первой точки: ")) 
   lst_a.append(n) 

lst_b = list() 
for i in range(number): 
   n = int(input("Введите координату второй точки: ")) 
   lst_b.append(n)

print(lst_a)
print(lst_b)

squ = list()
for i in range(len(lst_a)) and range(len(lst_b)):
   n = (lst_b[i] - lst_a[i]) ** 2 
   squ.append(n)

print(squ)

sum = 0
for i in range(len(squ)):
   sum = sum + squ[i]
   
from decimal import Decimal
distance = Decimal(sum ** (0.5))
distance = distance.quantize(Decimal("1.00"))
print(distance)

