numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
user_number = input("Введите, пожалуйста, число : ")
user_number = int(user_number)
numbers.append(user_number)
for i in range(len(numbers)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(numbers)):
        if numbers[j] < numbers[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        numbers[i], numbers[idx_min] = numbers[idx_min], numbers[i]
def find(numbers, user_number):
    for i, a in enumerate(numbers):
        if a == user_number:
            return i
    return False
print ('отсортированный список в порядке возрастания: ', numbers)
print('число пользователя имеет индекс: ',find(numbers, user_number))

r_num = find(numbers, user_number) + 1
l_num = find(numbers, user_number) - 1
max_num = max(numbers)
x = numbers.index(max_num)
if find(numbers, user_number) == x:
    print('ближайший больший элемент отсутствует')
else: print('ближайший больший элемент имеет индекс: ',r_num)
if l_num < 0:
    print('ближайший наименьший элемент отсутствует')
else: print('ближайший наименьший элемент имеет индекс: ',l_num)
