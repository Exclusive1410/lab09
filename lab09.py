import string
#1 Напишіть функцію, яка поверне максимальне значення зі списку чисел.
def max_number(arr):
    max = arr[0]
    for elements in arr:
        if elements > max:
            max = elements
            return max

list1= [11,55,77,99,8]
result = max_number(list1)
print(result)
print('-----------')
#2 Реалізуйте функцію, параметрами якої є - два числа і рядок. Повертає вона конкатенацію рядки з сумою чисел.

print('-----------')
#3 Реалізуйте функцію, що виводить на екран прямокутник з зірочок «*». Її параметрами будуть цілі числа, які описують довжину і ширину такого прямокутника.
w = int(input('Enter w : '))
h = int(input('Enter h : '))

for i in range(h):
    if i == 0 or i == h - 1:
        for j in range(w):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, w - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print('')

print('-----------')
#4 Напишіть функцію, яка реалізує лінійний пошук елемента в списку цілих чисел. Якщо такий елемент в списку є, то поверніть його індекс, якщо немає, то поверніть число «-1».
def linear_search(arr, search):
    for val in enumerate(arr):
        if val[1] == search:
            return val[1]
    return -1
n = int(input('Enter number (1-9) : ' ))
print (linear_search([1,2,3,4,5,6,7,8,9,], n))

print('-----------')
#5 Напишіть функцію, яка поверне кількість слів у рядку тексту.
s = 'Hello , how%are you?. Im, fine, '
for i in string.punctuation:
    s = s.replace(i, ' ')
print(len(s.split()))