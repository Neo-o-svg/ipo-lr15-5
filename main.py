def countSum(list_of_numbers):
  sum = 0
  for num in list_of_numbers:
    sum += num
  return sum

n = int(input())
listN = [int(x) for x in str(n)]
sum = countSum(listN)
print(f"Сумма цифр {n} числа равна {sum}")
