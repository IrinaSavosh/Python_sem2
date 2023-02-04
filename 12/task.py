# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3


import random

x = random.randint(0, 1000)
y = random.randint(0, 1000)
sum = x+y
prod = x*y
print(f"Петя загадал числа, произведение которых равно {prod}, а сумма - {sum}")
i = j = 0
for i in range(1001):
   for j in range(1001):
      if i+j == sum and i*j == prod:
         x = i
         y = j
      else:
         j += 1
   i += 1

print(f"Катя назвала числа, которые загадал Петя. Первое число равно {x}, а второе - {y}")
# a, b = map(int, input().split())
# res = []
# for i in range(a + b):
#     if i == (a * i - b)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)











# from random import randint
# n=int(input())
# a=[randint(10,12) for i in range(n)]
# print(a)
# max1=1
# k=1
# for i in range(1,n):
#     if a[i]==a[i-1]:
#         k+=1
#     else:
#         if k>=max1:
#             max1=k
#         k=1
# if k>max1:
#     max1=k
# print(max1)