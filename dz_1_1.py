# https://drive.google.com/file/d/1RWE0QduzjFQVtRMB8Ryp3Np8ldcdyGrq/view?usp=sharing

number = input("Введите натуральное трехзначное число: ")
number = int(number)
a = (number // 100)
b = (number % 100 // 10)
z = (number % 100 % 10)
sum = a + b + z
mult = a * b * z
print(f"Сумма = {sum}" )
print(f"Произведение = {mult}")