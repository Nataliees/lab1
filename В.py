#Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400. Напишите функцию, которая
# определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «Год ... -
# високосный», где вместо многоточия выведите год, иначе выведите «Это год не високосный».

year = int(input('Введите год'))
if(year%4==0 and year%100!=0 or year%400==0): print('Год ', year, ' - високосный')
else: print('Год ', year, ' - не високосный')