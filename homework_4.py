# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем через пробел позициях.
from random import randint

list = [ ]     
n = int(input("input number: "))  
for i in range (n):  
    number = randint(-n,n)   
    list.append (number)    
print (list)
list_1=[]
list_1 = input('input position: ').split()
print(list_1)
p = 1
for i in range(0, len(list_1)):
    p *= list[int(list_1[i])]
print(p)

    
    
    



