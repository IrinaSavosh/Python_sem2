# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint
n=int(input())
a=[randint(10,12) for i in range(n)]
print(a)
max1=1
k=1
for i in range(1,n):
    if a[i]==a[i-1]:
        k+=1
    else:
        if k>=max1:
            max1=k
        k=1
if k>max1:
    max1=k
print(max1)