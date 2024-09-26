n = int(input()) 
first_num = n // 10000000
second_num =  n // 1000000 % 10
print(second_num)
third_num =   n // 100000 % 10
print(third_num)
fourth_num =   n // 10000 % 10
print(fourth_num)
fifth_num =   n // 1000 % 10
print(fifth_num)
sixth_num =   n // 100 % 10
print(sixth_num)
seventh_num = n // 10 % 10
print(seventh_num)
eighth_num = 
print(eighth_num)
sum = first_num + second_num + third_num + fourth_num + fifth_num + sixth_num + seventh_num + eighth_num
print(f"Сумма всех цифр числа {n} равна {sum}")

