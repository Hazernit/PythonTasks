# with open('26-k1.txt') as file:
#     N, K = map(int, file.readline().split())
#     numbers = [int(line) for line in file]
#     numbers = sorted(numbers, reverse=True)
#     maxPrice = numbers[K]
#     totalDiscont = sum(numbers[:K])//5
#     print(maxPrice, totalDiscont)

# 22
# with open('26-k2.txt') as file:
#     N, K = map(int, file.readline().split())
#     numbers = [int(line) for line in file]
#     numbers = sorted(numbers)
#     ourNumbers = numbers[K:-K]
#     answer1 = ourNumbers[-1]
#     answer2 = sum(ourNumbers)//len(ourNumbers)
#     print(answer1, answer2)

# 23
# with open('26-k3.txt') as file:
#     N, K, M = map(int, file.readline().split())
#     result = [int(line) for line in file]
#     result = sorted(result, reverse=True)
#     winner = result[K-1]
#     prizeWinner = result[K+M-1]
#     print(winner, prizeWinner)

# 28
# with open('26-J3.txt') as file:
#     memory, users = map(int, file.readline().split())
#     busyMemory = [int(line) for line in file]
#     busyMemory = sorted(busyMemory, reverse = True)
#     place = 0
#     nFiles = 0
#     minFile = 100000
#     for f in busyMemory:
#         if place + f <= memory:
#             place += f
#             nFiles += 1
#             minFile = f
#
#     print(nFiles, minFile)             # Ответ: 1054 732


# 29

# with open(r"C:\Users\dimak\Downloads\26data\26-j4.txt", 'r', encoding='utf-8') as file:
#     N = int(file.readline())
#     memoryLeft = [int(line) for line in file]
#     memoryLeft = memoryLeft[N//10:-N//10]
#     savedFileMemory = sum(memoryLeft)
#     maxFileMemory = max(memoryLeft)
#     print(savedFileMemory, maxFileMemory)


# 30
# with open(r"C:\Users\dimak\Downloads\26data\26-J5.txt", 'r', encoding='utf-8') as file:
#     N = file.readline()
#     pits = [int(line) for line in file]
#     pitsRepaired = []
#     pitsRepaired.append(pits[0])
#     pitsRepaired.append(pits[-1])
#     for i in range(1, len(pits)-1):
#         totalFreePits = pits[i-1] + pits[i] + pits[i+1]
#         median = totalFreePits - pits[i-1] + pits[i+1]
#         pitsRepaired.append(median)
#     minV = min(pitsRepaired)
#     countMinV = 0
#     waterV = sum(pitsRepaired)
#     for i in range(len(pitsRepaired)):
#         if pitsRepaired[i] == minV:
#             countMinV += 1
#     print(countMinV, waterV)

# 31
# import math
#
# with open(r"C:\Users\dimak\Downloads\26data\26-s1.txt", "r", encoding="utf-8") as file:
#     N = file.readline()
#     price = [int(line) for line in file]  #Все цены
#     price = sorted(price)      # Отсортированные цены
#     discont = 0
#     discontPrices = []
#
#     ourTotal = 0         # Общая цена с учётом скидок
#
#     productDiscontIsProvided = []   # Продукты на которые предоставляется скидка
#     for j in range(len(price)):
#         if price[j] > 100:
#             productDiscontIsProvided.append(price[j])
#         else:
#             ourTotal += price[j]
#     for i in range(len(productDiscontIsProvided)//2):
#             discontPrice = math.ceil(productDiscontIsProvided[i] * 0.9)
#             discontPrices.append(discontPrice)
#             discont += discontPrice
#             maxDiscont = productDiscontIsProvided[i]    #Цена самого дорогого товара
#
#     for i in range(len(productDiscontIsProvided)//2, len(productDiscontIsProvided)):
#         ourTotal += productDiscontIsProvided[i]
#     ourTotal += sum(discontPrices) #Общая цена покупки
#     print(maxDiscont, ourTotal)     # Ответ: 499078 550


# 34
# with open(r"C:\Users\dimak\Downloads\26data\26-j6.txt", "r", encoding="utf-8") as file:
#     #TODO Определите максимально возможное
#     # количество файлов, которое может быть сохранено без сжатия,
#     # и максимально возможный размер такого файла
#
#     N = file.readline() # Кол-во пользоввателей
#
#     arrayAllUsersMemory = [int(line) for line in file] #значения объёмов файлов каждого пользователя
#
#       #Начальный объём затраченный памяти
#     memoryToSave = sum(arrayAllUsersMemory)*0.1    #После сжатия (минимум 10% от "startMemory)
#     arrayAllUsersMemory = sorted(arrayAllUsersMemory, reverse=True)
#
#     count = 0
#     startMemory = 0
#     i = 0
#     while startMemory < memoryToSave:
#         startMemory += arrayAllUsersMemory[i]*0.2
#         i += 1
#     freeSpace = startMemory-memoryToSave # 80% -> 100%
#
#     print(arrayAllUsersMemory)
#     j = i-1
#     print(freeSpace)
#     countUncompressedFiles = len(arrayAllUsersMemory)-i # Кол-во не сжатых файлов
#     maxUncompressedFiles = arrayAllUsersMemory[i] # наибольший размер сохраненного без сжатия файла.
#
#     print(countUncompressedFiles, maxUncompressedFiles)

# 35, 36
# with open(r'C:\Users\dimak\Downloads\26data\26-j7.txt', 'r', encoding="utf-8") as file:
#     N = file.readline() # Кол-во участников проекта
#     savings = [int(line) for line in file]
#     savings = sorted(savings, reverse=True)
#     MustSpend = sum(savings)*0.6 #Должны потратить
#     richPeoples = int(len(savings)*0.2) # 20% самых богатых участников
#     manyRichPeople = savings[:richPeoples]     # 80% от этих накоплений кол-во людей богатых
#     manyOtherPeople = savings[richPeoples:]    # Остаток - manyRichPeople кол-во людей бедных
#
#     spendManyRichPeople = 0  # Внесли богатые (80% от своих сбережений)
#     for i in manyRichPeople:
#         spendManyRichPeople += i*0.8
#     spendManyOtherPeople = MustSpend - spendManyRichPeople # Должны внести бедные
#
#     moneyOther = sum(manyOtherPeople)
#
#     spendPercentOtherPeople = spendManyOtherPeople/moneyOther  # Проценты для бедных
#
#     minSpend = spendPercentOtherPeople * savings[-1]
#     print(spendManyRichPeople, minSpend)

# 36
# TODO 1 акция
#     30% скидки от 70% самых дешёвых товаров
#     40% скидки от оставшихся товаров
#   2 акция
#     40% скидки от 50% самых дешёвых
#     35% скидки оставшиеся товары
# Что прибыльнее?
# with open(r'C:\Users\dimak\Downloads\26data\26-j8.txt', 'r', encoding='utf-8') as file:
#     N = file.readline() #Кол-во товаров
#     costOfGoods = [int(line) for line in file]
#     costOfGoods = sorted(costOfGoods)
#
#     cheap70 = int(len(costOfGoods)*0.7)      # 1 акция 70% товаров
#     discount30 = costOfGoods[:cheap70] # товары на которые предоставляется скидка 30%
#     discount40 = costOfGoods[cheap70:] # товары на которые предоставляется скидка 40%
#
#     profit1 = 0
#     priceDiscont1 = []
#     for i in discount30:
#         priceDiscont1.append(i)
#         profit1 += i*0.3
#     for i in discount40:
#         priceDiscont1.append(i)
#         profit1 += i*0.4
#     maxPrice1 = max(priceDiscont1)
#
#     # 2 Акция
#     cheap50 = int(len(costOfGoods)*0.5)
#     discount40 = costOfGoods[:cheap50]
#     discount35 = costOfGoods[cheap50:]
#
#     profit2 = 0
#     priceDiscont2 = []
#     for i in discount40:
#         priceDiscont2.append(i)
#         profit2 += i * 0.4
#     for i in discount35:
#         priceDiscont2.append(i)
#         profit2 += i * 0.35
#
#     maxPrice2 = max(priceDiscont2)
#
#     answer1 = profit2 - profit1
#     print(answer1, maxPrice1, maxPrice2)

# 37
# TODO сортируется по цене, от меньшей к большему
#     если цена одинакова, то беерётся макс вес
#
# with open(r'C:\Users\dimak\Downloads\26data\26-k6.txt', 'r', encoding='utf-8') as file:
#     N, K = map(int, file.readline().split())
#     weightAndPrice = [list(map(int, line.split())) for line in file]    # Как сделать генератор для двух значений
#     # languages = [line.strip() for line in file.readlines()]
#     # languages = list(map(str.strip, file.readlines()))
#
#     # >> > data = [[i * j for i in range(0, 3)] for j in range(0, 3)]
#     # >> > print(data)
#     # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
#
# #38
# #TODO
# # 1. Файл макс размера, который поместиться на диск
# # 2. Файл мин размера
# # 3. Пока не закончится место
#
# with open(r'C:\Users\dimak\Downloads\26data\26-j9.txt', 'r', encoding='utf-8') as file:
#     S, N = map(int, file.readline().split())
#     memory = [int(line) for line in file]
#     memoryMin = sorted(memory)
#     memoryMax = sorted(memory, reverse=True)
#
#     count = 0
#     i = 0
#     while S > 0:
#         S -= memory[i]
#         count += 1
#         i += 1
#     lastMemory = memory[i-1]
#     print(lastMemory, count) # Ответ: 230 718


# 22
# 1
# for x in range(1000, 0, -1):
#     L = 0
#     M = 0
#     i = x
#     while x > 0:
#         L = L + 1
#         M = M + (x%10)
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break

# #2
# for x in range(1000, 0, -1):
#     L = 0
#     M = 0
#     i = x
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 8:
#         print(i)
#         break

# #3
# for x in range(1000, 0, -1):
#     L = 0
#     M = 0
#     i = x
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 0:
#         print(i)
#         break


# #4
# # for x in range(1000, 0, -1):
# #     L = 0
# #     M = 0
# #     i = x
# #     while x > 0:
# #         L = L + 1
# #         if x % 2 == 1:
# #             M = M + (x % 10)
# #         x = x // 10
# #     if L == 3 and M == 8:
# #         print(i)
# #         break

# #5
# for x in range(1000, 0, -1):
#     i = x
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10) // 2
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break


# #6
# for x in range(1000, 0, -1):
#     i = x
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 1:
#             M = M + (x % 10) // 2
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break

# 7

# for x in range(1000, 0, -1):
#     i = x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if M < x:
#             M = x % 10
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break

# 8
# for x in range(1000, 0, -1):
#     i = x
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if (M< x) and (x % 2 == 0):
#             M = x % 10
#         x = x // 10
#     if L == 3 and M == 8:
#         print(i)
#         break

# 9
# for x in range(1000, 0, -1):
#     i = x         # Нетронутый х
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if (M < x) and (x% 2 == 1):
#             M = (x % 10) * 2
#         x = x // 10
#     if L == 3 and M == 10:
#         print(i)
#         break

# 10
# Предполагаемый ответ 959
# for x in range(1000, 0, -1):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if M < x:
#             M = (x % 10) * 2
#         x = x // 10
#     if L == 3 and M == 10:
#         print(i)
#         break  # Ответ 959


# 11
# Ожидаемый ответ: 98
# for x in range(100, 1, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 2 and b == 72:
#         print(i)
#         break  # Ответ 98

# # 12 Ожидаемый ответ: 72
# for x in range(100, 1, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 2 and b == 14:
#         print(i)
#         break  # Ответ: 72

# # 13 Ожидаемый ответ: 711
# for x in range(1000, 1, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 3 and b == 7:
#         print(i)
#         break  # Ответ: 711

# # 14 Ожидаемый ответ: 990
# for x in range(1000, 1, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 3 and b == 0:
#         print(i)
#         break  # Ответ: 990


# # 15 Ожидаемый ответ: 115
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break  # Ответ 106


# # 16 Ожидаемый ответ: 116
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 8:
#         print(i)
#         break  # Ответ 108


# # 17 Ожидаемый ответ: 100
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 0:
#         print(i)
#         break  # Ответ 100

# # 18 Ожидаемый ответ: 107
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 1:
#             M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 8:
#         print(i)
#         break  # Ответ 107

# # 19 Ожидаемый ответ: 168
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10) // 2
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break  # Ответ 168

# # 20 Ожидаемый ответ: 681
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 1:
#             M = M + (x % 10) // 2
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break  # Ответ 179

# # 21 Ожидаемый ответ: 170
# for x in range(1000):
#     i=x
#     L=0
#     M=0
#     while x > 0:
#         L = L + 1
#         if M < x:
#             M = x % 10
#         x = x // 10
#     if L == 3 and M == 7:
#         print(i)
#         break  # Ответ 170

# # 22 Ожидаемый ответ: 118
# for x in range(1000):
#     i = x
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if (M < x) and (x % 2 == 0):
#             M = x % 10
#         x = x // 10
#     if L == 3 and M == 8:
#         print(i)
#         break  # Ответ 118

# # 23 Ожидаемый ответ: 105
# for x in range(1000):
#     i = x
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if (M < x) and (x % 2 == 1):
#             M = (x % 10) * 2
#         x = x // 10
#     if L == 3 and M == 10:
#         print(i)
#         break  # Ответ: 105

# # 24 Ожидаемый ответ: 195
# for x in range(1000):
#     i = x
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if M < x:
#             M = M + (x % 10) * 2
#         x = x // 10
#     if L == 3 and M == 28:
#         print(i)
#         break  # Ответ 177

# # 25 Ожидаемый ответ: 89
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 2 and b == 72:
#         print(i)
#         break  # Ответ 89

# # 26 Ожидаемый ответ: 27
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 2 and b == 14:
#         print(i)
#         break  # Ответ 27


# # 27 Ожидаемый ответ: 134
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 3 and b == 7:
#         print(i)
#         break  # Ответ 117

# # 28 Ожидаемый ответ: 166
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 3 and b == 36:
#         print(i)
#         break  # Ответ 149

# #TODO 29 Ожидаемый ответ: ? Как здесь работает 8%8=0 ?
# for x in range(1000, 0, -1):  641 - 8 сс -> 6*8^2 + 4*8^1 + 1*8^0 = 417 - 10cc
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 8)
#         x = x // 8
#     if a == 3 and b == 24:
#         print(i)
#         break  # Ответ 417

# 30 Ожидаемый ответ: ? 125 - 8cc - 1*8^2 + 2*8^1 + 5*8^0 = 64 + 16 + 5 = 85 - 10cc
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 8)
#         x = x // 8
#     if a == 3 and b == 10:
#         print(i)
#         break  # Ответ 85
# 31 Ожидаемый ответ: 124 - 6сс -> 1*6^2 + 2*6^1 + 6*6^0 = 36 + 12 + 6 = 51 - 10cc
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 6)
#         x = x // 6
#     if a == 3 and b == 6:
#         print(i)
#         break  # Ответ 51

# #32 Ожидаемый ответ: 331 - 5cc -> 3*5^2 + 3*5^1 + 1*5^0 = 75 + 15 + 1 = 91 - 10cc
# for x in range(1000, 0, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 5)
#         x = x // 5
#     if a == 3 and b == 9:
#         print(i)
#         break  # Ответ 51

# 33 Ориентировочный ответ: 37
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 2 and b == 21:
#         print(i)
#         break  # Ответ 37

# #34 Ориентировочный ответ: 157
# for x in range(1000):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 3 and b == 35:
#         print(i)
#         break  # Ответ 157

# #35 Ориентировочный ответ: 488
# for x in range(1000, 0, -1):
#     i = x
#     L = 0
#     M = 9
#     while x > 5:
#         L = L + 1
#         if M > (x% 10):
#             M = x % 10
#         x = x // 10
#     if L == 3 and M == 4:
#         print(i)
#         break #994

# #46 Ориентировочный ответ: 555
# for x in range(1000):
#     i = x
#     a = 0
#     b = 10
#     while x > 0:
#         c = x % 10   # min цифра = 5
#         a = a + c    # Сумма цифр = 15
#         if c < b:
#             b = c
#         x = x // 10
#     if a == 15 and b == 5:
#         print(i)
#         break  # Ответ 555

# #47 Ориентировочный ответ: 4333
# for x in range(1000000, 0, -1):
#     i = x
#     a = 0
#     b = 10
#     while x > 0:
#         c = x % 10   # min цифра = 3
#         a = a + c    # Сумма цифр = 13
#         if c < b:
#             b = c   # min цифра = 3
#         x = x // 10
#     if a == 13 and b == 3:
#         print(i)
#         break  # Ответ 43333

# #48 Ориентировочный ответ: 469
# for x in range(1000000):
#     i = x
#     a = 0
#     b = 10
#     while x > 0:
#         c = x % 10   # min цифра = 4
#         a = a + c    # Сумма цифр = 19
#         if c < b:
#             b = c   # min цифра = 4
#         x = x // 10
#     if a == 19 and b == 4:
#         print(i)
#         break  # Ответ 469

# 49 Ориентировочный ответ: 11000 - 2 c.c. -> 1*2^4 + 1*2^3 = 16 + 8 = 24 - 10 c.c.
# for x in range(1000000, 0, -1):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 2   # Чётность числа
#         if c == 0:
#             a = a + 1    # Кол-во чётных цифр == 3
#         else:
#             b = b + 1   # Кол-во нечётных цифр == 2
#         x = x // 10  # Отвечает за с.с.
#     if a == 3 and b == 2: # Всего цифр a + b = 5
#         print(i)
#         break  # Ответ 99888


# #50 Ориентировочный ответ: 2000
# for x in range(1000000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 2   # Чётность числа
#         if c == 0:
#             a = a + 1    # Кол-во чётных цифр == 3
#         else:
#             b = b + 1   # Кол-во нечётных цифр == 2
#         x = x // 10  # Отвечает за с.с.
#     if a == 4 and b == 0: # Всего цифр a + b = 5
#         print(i)
#         break  # Ответ 2000

# #51 Ориентировочный ответ: 10001 - 8 cc -> 1*8^4 + 1*8^0 = 4096 + 1 = 4097
# for x in range(1000000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 2   # Чётность числа
#         if c == 0:
#             a = a + 1    # Кол-во чётных цифр == 3
#         else:
#             b = b + 1   # Кол-во нечётных цифр == 2
#         x = x // 8  # Отвечает за с.с.
#     if a == 3 and b == 2: # Всего цифр a + b = 5
#         print(i)
#         break  # Ответ 4097

# #52 Ориентировочный ответ: 2000 - 6 c.c. -> 2*6^3 = 432 - 10 c.c.
# for x in range(1000000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 2   # Чётность числа
#         if c == 0:
#             a = a + 1    # Кол-во чётных цифр == 4
#         else:
#             b = b + 1   # Кол-во нечётных цифр == 0
#         x = x // 6  # Отвечает за с.с.
#     if a == 4 and b == 0: # Всего цифр a + b = 5
#         print(i)
#         break  # Ответ 432

# #53 Ожидаемый ответ: 1003
# for x in range(10000):
#     i = x
#     K = 0
#     R = 9
#     Y = x % 10 # Последняя цифра
#     while x > 0:
#         K = K + 1 # Кол-во цифр
#         if R > (x % 10): # Самая маленькая цифра
#             R = x % 10
#         x = x // 10
#     R = Y - R   # Последняя цифра - самая маленькая цифра
#     if K == 4 and R == 3:
#         print(i)
#         break  #Ответ: 1003

# TODO 54 Ожидаемый ответ: 997
# for x in range(10000, 0, -1):
#     i = x
#     K = 0
#     R = 9
#     Y = x % 10 # Последняя цифра
#     while x > 0:
#         K = K + 1 # Кол-во цифр
#         if R > (x % 10): # Самая маленькая цифра
#             R = x % 10
#         x = x // 10
#     R = Y - R   # Последняя цифра - самая маленькая цифра
#     if K == 3 and R == 7:
#         print(i)
#         break  #Ответ: 929
# TODO 55 ???? Ожидаемый ответ: 139
# for x in range(10000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1  # Кол-во нечётных цифр подходит: 9999 и 100 ?
#         b = b + (x % 100)
#         x = x // 100
#     if a == 2 and b == 13:
#         print(i)
#         break  #Ответ: 112

# # TODO 56 ???? Ожидаемый ответ: 906
# for x in range(10000, 0, -1):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1  # Кол-во нечётных цифр подходит: 9999 и 100 ?
#         b = b + (x % 100)
#         x = x // 100
#     if a == 2 and b == 13:
#         print(i)
#         break  #Ответ: 1300

# # TODO 57 Ожидаемый ответ: 4 (96, 87, 78, 69) ????????????
# count = 0
# for x in range(100):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1  # Кол-во цифр
#         b = b + (x % 10)
#         x = x // 10
#     if a == 2 and b == 15:
#         count += 1
# print(count)  # Ответ: 0
# TODO 58 Ожидаемый ответ: 20005
# for x in range(10000, 100000):
#     i = x
#     a = 0
#     b = 10
#     while x > 0:
#         y = x % 10
#         x = x // 10
#         if (y > a):
#             a = y     # Максимальное число
#         if (y < b):
#             b = y    # Минимальное число
#     if a == 5 and b == 2:
#         print(i)
#         break       # Ответ: 22225

# #59 Ожидаемый ответ: 121
# for x in range(1000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1
#         b = b + (x % 100)
#         x = x // 100
#     if a == 2 and b == 22:
#         print(i)
#         break          # Ответ: 121

# 60 TODO Ожидаемый ответ: 5111   ????
# for x in range(10000, 0, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 100)
#         x = x // 100
#     if a == 2 and b == 5:
#         print(i)
#         break          # Ответ: 501

# 61 Ожидаемый ответ:
# for x in range(1000000, 0, -1):
#     i = x
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 100)
#         x = x // 100
#     if a == 3 and b == 18:
#         print(i)
#         break    # Ответ 180101

# #63 TODO ожидаемый ответ: 99777        ?????
# for x in range(100000, 10000, -1):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         y = x % 10
#         if y > 3:
#             a = a + 1  # Кол-во чисел больше 3
#         if y < 8:
#             b = b + 1  # Кол-во чисел меньше 8
#         x = x // 10
#     if a == 4 and b == 3:
#         print(i)
#         break    # Ответ 99773

# #64   ожидаемый ответ: 95555
# for x in range(100000, 10000, -1):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         y = x % 10
#         if y > 4:
#             a = a + 1  # Кол-во чисел больше 4
#         if y < 6:
#             b = b + 1  # Кол-во чисел меньше 6
#         x = x // 10
#     if a == 5 and b == 4:
#         print(i)
#         break    # Ответ 95555


# # 65 TODO ожидаемый ответ: 10557     ???????????
# for x in range(10000, 100000):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         y = x % 10
#         if y > 4:
#             a = a + 1  # Кол-во чисел больше 4
#         if y < 6:
#             b = b + 1  # Кол-во чисел меньше 6
#         x = x // 10
#     if a == 3 and b == 4:
#         print(i)
#         break    # Ответ 10556

# Отправить
# #63 TODO ожидаемый ответ: 99777        ?????
# for x in range(100000, 10000, -1):
#     i = x
#     a = 0
#     b = 0
#     while x > 0:
#         y = x % 10
#         if y > 3:
#             a = a + 1  # Кол-во чисел больше 3
#         if y < 8:
#             b = b + 1  # Кол-во чисел меньше 8
#         x = x // 10
#     if a == 4 and b == 3:
#         print(i)
#         break    # Ответ 99773


# ЕГЭ 17
# 1
# count = 0
# maxNumber = 0
# for i in range(1012, 9639):
#     if i % 3 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
#         count += 1
#         if i > maxNumber:
#             maxNumber = i
# print(count, maxNumber) # Ответ 2151 9630 - получилось

# 25
# totalNumber = 0
# count = 0
# for i in range(3672, 9117):
#     if i % 3 == 2 and i % 5 == 4:
#         totalNumber += i
#         count += 1
# print(totalNumber, count) # Ответ 2319207 9104

# 27
# minNumber = 9999
# count = 0
# for i in range(3712, 8432):
#     if i % 2 == i % 4 and (i % 13 == 0 or i % 14 == 0 or i % 15 == 0):
#         if minNumber > i:
#             minNumber = i
#         count += 1
# print(minNumber, count) # Ответ 3720 471 - получилось

# 31
# 444444 - 4 * 5^5 + 4 * 5^4 + 4 * 5^3 + 4 * 5^2 + 4 * 5^1 + 4 * 5^0 = 15625 + 3125 + 625 + 125 + 20 + 1 = 19521
# minNumber = 10000
# count = 0
# for i in range(1000, 10000):
#     if i >= 5**5 and (i // 5) % 5 == 2 and (i % 5 == 1 or i % 5 == 3):
#         if minNumber > i:
#             minNumber = i
#         count += 1
# print(minNumber, count) # Ответ 1003 1800


# 37
# minNumber = 9999
# count = 0
# for i in range(3905, 7998):
#     if ((i // 10) % 10 != 0 and (i // 10) % 10 != 5) and 2 <= (i//100) % 10 <= 6:
#         if minNumber > i:
#             minNumber = i
#         count += 1
# print(minNumber, count) # Ответ 3910 1038


# #65
# maxNumber = 0
# count = 0
# for i in range(8800, 55535):
#     flag = False
#     x = i
#     composition = 1
#     while i > 0:
#         composition *= i % 10
#         if i % 10 == 7:
#             flag = True
#         i //= 10
#     if composition > 35 and flag:
#         if maxNumber < x:
#             maxNumber = x
#         count += 1
#
#
# print(maxNumber, count) # Ответ   Должно 55527 10958


# 66
# maxNumber = 0
# count = 0
# for i in range(333666, 666999):
#     countSeven = 0
#     flag = False
#     x = i
#     while i > 0:
#         if i % 10 == 7:
#             countSeven += 1
#         if countSeven >= 2:
#             flag = True
#         i //= 10
#     if x % 17 == 0 and flag:
#         if maxNumber < x:
#             maxNumber = x
#         count += 1
#
# print(maxNumber, count)  # Ответ 666774 1538

# 67
# maxNumber = 0
# count = 0
# for i in range(100001, 900009):
#     x = i
#     if i % 7 + x % 10 == 10 and i % 11 == 0 and i % 55 != 0:
#         if maxNumber < x:
#             maxNumber = x
#         count += 1
# print(count, maxNumber)

# 68 -72

# TODO 68 ????
# minNumber = 44000
# count = 0
# # ourNumber = frozenset([0, 2, 5])
# ourNumber = {"0", "2", "5"}
# for i in range(2079, 43167):
#     x = i
#     if i % 7 == 0:
#         if "0" in str(i) and "2" in str(i) and "5" in str(i):
#             count += 1
#             if minNumber > int(i):
#                 minNumber = int(i)
# print(count, minNumber)


# 69
# maxNumber = 0
# count = 0
# ourNumberOne = {"7"}
# ourNumberTwo = {"4"}
# for i in range(1388, 63252):
#     x = i
#     if i % 12 != 0:
#         if ("4" in str(i) ) or ("7" in str(i)):  # Как проверять
#             count += 1
#             if maxNumber < int(i):
#                 maxNumber = int(i)   # Ответ: 37071 63249
# print(count, maxNumber)

# #70
# maxNumber = 0
# count = 0
# index = 0
# for i in range(2894, 174882):
#     x = i
#     i = str(i)
#     totalNumbers = 0
#     if int(i) % 10 == 8:
#         for j in range(len(i)):
#             totalNumbers += int(i[j])
#         if totalNumbers > 22:
#             count += 1
#             if count == 13:
#                 thirteenthNumber = x  # Ответ: 12524 3598
# print(count, thirteenthNumber)

# 72
# maxNumber = 0
# count = 0
# index = 0
# for i in range(2848, 109499):
#     x = i
#     i = str(i)
#     totalNumbers = 0
#     if "9" in i:
#         for j in range(len(i)):
#             if int(i[j]) > 5:
#                 totalNumbers += int(i[j])
#         if totalNumbers % 3 == 0:
#             count += 1
#             if int((str(x))[0]) == 8:
#                 if maxNumber < x:
#                     maxNumber = x  # Ответ: 20864 89997
# print(count, maxNumber)

# 73
# maxNumber = 0
# count = 0
# ourNumber = 0
# for i in range(147871, 1005, -1):
#     minDigit = 10
#     maxDigit = 0
#     x = i
#     i = str(i)
#     totalNumbers = 0
#     if "1" not in i:
#         for j in range(len(i)):
#             if int(i[j]) > maxDigit:
#                 maxDigit = int(i[j])
#             if int(i[j]) < minDigit:
#                 minDigit = int(i[j])
#         if maxDigit - minDigit < 4:
#             count += 1
#             if count == 25:
#                 ourNumber = x
#                                 # Ответ: 5272 99879
# print(count, ourNumber)


# 75
# minNumber = 604000
# count = 0
# ourNumber = 0
# maxTotalDigits = 0
# def degree(number):
#     while number % 3 == 0:
#         number //= 3
#     return number == 1
# for i in range(138, 603884):
#     totalDigits = 0
#     x = i
#     i = str(i)
#     setNumbers = set(i)
#     if degree(x) and len(i) > len(setNumbers):
#         count += 1
#         for j in range(len(i)):
#             totalDigits += int(i[j])
#         if maxTotalDigits < totalDigits:
#             maxTotalDigits = totalDigits
#             minNumber = x
#                                 # Ответ: 4 59049
# print(count, minNumber)

# 76
# maxNumber = 0
# count = 0
# ourNumber = 0
# maxTotalDigits = 0
# for i in range(1007, 746001):
#     totalDigits = 0
#     x = i
#     i = str(i)
#     countFife = 0
#     flag = True
#     for j in range(len(i)):
#         if int(i[0]) < int(i[j]):
#             flag = False
#         if int(i[j]) == 5:
#             countFife += 1
#     if flag and countFife >= 2 and countFife % 2 == 0:
#         count += 1
#         if x // 10**(len(i)-2) == 50:
#             if maxNumber < x:
#                 maxNumber = x
#                                 # Ответ: 9069 505554
# print(count, maxNumber)

# TODO 77-80
# 77
# maxNumber = 0
# count = 0
# maxTotalDigits = 0
# totalNumber = 0
# for i in range(2020, 647039):
#     totalDigits = 0
#     minDigit = 10
#     x = i
#     i = str(i)
#     for j in range(len(i)):
#         totalDigits += int(i[j])
#         if minDigit > int(i[j]):
#             minDigit = int(i[j])
#
#     if totalDigits < 10 and int(i[0]) > minDigit and int(i[1]) > minDigit and int(i[2]) > minDigit:
#         count += 1
#         totalNumber += x
#
# aritMean = totalNumber/count
# differenceAritMeanAndNumber = 1000000
# ourNumber = 0
# for i in range(2020, 647039):
#     if abs(i-aritMean) <= differenceAritMeanAndNumber:
#         differenceAritMeanAndNumber = abs(i-aritMean)
#         ourNumber = i
#
#                                 # Мой Ответ: 1248 148268  1248 148268
#                                 # Должно получится: 1248 151000
# print(count, ourNumber)

# 78
# maxNumber = 0
# count = 0
# ourNumber = 0
# maxTotalDigits = 0
# def decreasing(number):
#     number = str(number)
#     for j in range(len(number)-1):
#         if int(number[j]) <= int(number[j + 1]):
#             return False
#     return True
# def multipleOfTree(number):
#     number = int(number)
#     count = 0
#     for i in range(1, number+1):
#         if number % i == 0:
#             count += 1
#     return count % 3 == 0
#
# for i in range(129932, 1081, -1):
#     x = i
#     i = str(i)
#     if decreasing(i) and multipleOfTree(i):
#         count += 1
#         if int(i[0]) == 7 and maxNumber < int(i):
#             maxNumber = int(i)
#                                  # Не получилось:121 76540
#                                  # Правильный ответ: 121 76540
# print(count, maxNumber)

# 79
# def simpleOfNumber(number):
#     number = int(number)
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
# count = 0
# maxNumber = 0
# for i in range(19402, 2095, -1):
#     x = i
#     i = str(i)
#     if simpleOfNumber(i) and int(i[0]) > int(i[-1]):
#         count += 1
#         if maxNumber < int(i) and int(i) % 100 == 21:
#             maxNumber = int(i)
# print(count, maxNumber)     # Мой ответ: 455 9721
#                             # Должен получится: 455 9721

# 80
# def nonRepeatingDigits(i):
#     number = str(i)
#     flag = True
#     for j in range(len(number) - 1):
#         if int(number[j]) != int(number[j + 1]):
#             flag = True
#         else:
#             flag = False
#             break
#     return flag
# i = 27
# count = 0
# maxNumber = 0
# while i <= 90000:
#     if nonRepeatingDigits(i):
#         count += 1
#         if maxNumber < i:
#             maxNumber = i
#     i *= 2
# print(count, maxNumber)    # Мой ответ: 11 27648

# TODO 83 86 89 112

# 83
# def multiplesSumDigits(number):
#     number = str(number)
#     totalDigits = 0
#     for i in range(len(number)):
#         totalDigits += int(number[i])
#     return int(number) % totalDigits == 0
#
#
# def multiplesCompositionDigits(number):
#     number = str(number)
#     compositionDigits = 1
#     for i in range(len(number)):
#         compositionDigits *= int(number[i])
#     if compositionDigits > int(number) or compositionDigits == 0:
#         return False
#     else:
#         return int(number) % compositionDigits == 0
#
#
# count = 0
# maxNumber = 0
# for i in range(1111, 9999):
#     if multiplesCompositionDigits(i) and multiplesSumDigits(i):
#         count += 1
#         if maxNumber < i:
#             maxNumber = i
# print(count, maxNumber)  # Мой ответ: 19 9612
# 19 9612

# 86 ?????
# count = 0
# total = 0
# for i in range(20000, 30001):
#     x = i
#     countDivisors = 0
#     for j in [7, 11, 17, 19]:
#         if i % j == 0:
#             countDivisors += 1
#     if countDivisors >= 2:
#         count += 1
#         total += x
# answer2 = total // count
# print(count, answer2)         # Мой ответ: 381 25002
# Правильный ответ: 393 24988

# 89
# count = 0
# maxNumber = 0
# for i in range(1234567, 7654322):
#     x = i
#     i = str(i)
#     seniorRanks = int(i[0] + i[1])
#     lowerRanks = int(i[-2] + i[-1])
#     differenceRanks = abs(seniorRanks-lowerRanks)
#     if differenceRanks != 0 and x % differenceRanks == 0:
#         count += 1
#         if x > maxNumber:
#             maxNumber = x
# print(count, maxNumber)     # Мой ответ: 565701 7654318
# Правильный ответ: 565701 7654318

# 112    Не получилось
# count = 0
# differenceMax = 0
# maxNumber = 0
# minNumber = 3000
# for i in range(1213, 2224):
#     x = i
#     i = str(i)
#     maxDigit = 0
#     total = 0
#     for j in i:
#         j = int(j)
#         total += j
#         if maxDigit < j:
#             maxDigit = j
#     if maxDigit == 7 and total == 14 and x % 2 == 0:
#         count += 1
#         if maxNumber < x:
#             maxNumber = x
#         if minNumber > x:
#             minNumber = x
# difference = maxNumber - minNumber
#
# print(count, difference)         # Мой ответ:  8 900
# Правильный ответ: 8 900

# 135
# minNumber = 9999
# maxNumber = 0
# for i in range(1812, 9285):
#     x = i
#     if (i % 8 == 0 or i % 19 == 0) and i % 4 != 0 and i % 9 != 0:
#         i = str(i)
#         if int(i[0]) % 2 != 0:
#             if minNumber > x:
#                 minNumber = x
#             if maxNumber < x:
#                 maxNumber = x
# print(minNumber, maxNumber)         # 1843 7847
# 1843 9253


# 136
# count = 0
# total = 0
# maxNumber = 0
# minNumber = 99999
# for i in range(4855, 7856):
#     if i % 6 == 0 and i % 15 == 0 and i % 7 != 0 and i % 16 != 0:
#         if (((i // 10)%10) + ((i // 100) % 10)) % 2 == 0:
#             count += 1
#             total += i
#             if minNumber > i:
#                 minNumber = i
#             if maxNumber < i:
#                 maxNumber = i
# answer2 = total//count
# answer = answer2 + maxNumber + minNumber
# print(answer)                            # 18979
# Правильный ответ: 18979

# 137
# count = 0
# minNumber = 99999
# for i in range(4565, 13347):
#     if i % 7 == 0 and i % 6 != 0 and i % 3 != 0 and ((i % 10) + (i // 10) % 10) % 2 == 0:
#          count += 1
#          if minNumber > i:
#              minNumber = i
# print(count, minNumber)     # Мой ответ: 419 4571
# Правильный ответ: 419 4571

# 140
# count = 0
# minNumber = 99999
# for i in range(4413, 10154):
#     if i % 5 == 0 and i % 23 == 0 and i % 7 != 0 and i % 10 != 0 and (i // 10) % 10 in [1, 2, 3]:
#         count += 1
# TODO 141 - 144

# 141
# minNumber = 9999
# arithmeticMean = 0
# count = 0
# total = 0
# for i in range(4391, 9876):
#     if (i % 11 == 0 or i % 17 == 0) and i % 2 != 0 and i % 13 != 0 and (i // 10) % 10 % 2 == 1 and ((i // 100) % 10) % 2== 0:
#         total += i
#         count += 1
#         if minNumber > i:
#             minNumber = i
# arithmeticMean = total // count
# print(arithmeticMean, minNumber)   # Мой ответ: 6861 6095 - Не правильно 7062 4411
# Правильный 7062 4411

# 142
# minNumber = 8888
# maxNumber = 0
# for i in range(1412, 7866):
#     x = i
#     x = str(x)
#     if (i % 8 == 0 or i % 19 == 0) and i % 4 != 0 and i % 9 != 0:
#         total = 0
#         for j in range(len(x)):
#             total += int(j)
#         if total % 5 != 0:
#             if minNumber > i:
#                 minNumber = i
#             if maxNumber < i:
#                 maxNumber = i
#
# print(minNumber, maxNumber)    # Не получилось 1425 7847
# Правильный 1425 7847

# 143 - Получился
# arithmeticMean = 0
# count = 0
# total = 0
# maxNumber = 0
# minNumber = 8888
# for i in range(4735, 8757):
#     if i % 5 == 0 and i % 17 == 0 and i % 7 != 0 and i % 14 != 0 and ((i//10)%10) >= ((i//100)%10):
#         total += i
#         count += 1
#         if minNumber > i:
#             minNumber = i
#         if maxNumber < i:
#             maxNumber = i
# arithmeticMean = total // count
# answer = arithmeticMean + minNumber + maxNumber
# print(answer)                                  # Мой ответ: 20510
# 20510 - Правильно

# # 144 Не очень понял условие
# oneSet = [9, 11, 13, 15]
# twoSet = [25, 33, 40, 45]
# count = 0
# total = 0
# arithmeticMean = 0
# for i in range(45000, 46001):
#     countOne = 0
#     countTwo = 0
#     for j in oneSet:
#         if i % j == 0:
#             countOne += 1
#     for j in twoSet:
#         if i % j == 0:
#             countTwo += 1
#     if countOne < countTwo:
#         count += 1
#         total += i
# arithmeticMean = total // count
# print(count, arithmeticMean)             # Мой ответ: 35 45489
# Правильный: 35 45489

# 1
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7-1.txt") as file:
#     s = file.read()
#     maxCount = 0
#     count = 0
#     print(s)
#     for i in s:
#         if i == "A":
#             count += 1
#         if maxCount < count:
#             maxCount = count
#         if i != "A":
#             count = 0
#     print(maxCount)

# 23
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7a-3.txt") as file:
#     s = file.read()
#     countMax = 0
#     count = 0
#     for i in s:
#         if i in "ABEF":
#             count += 1
#         else:
#             count = 0
#         if countMax < count:
#             countMax = count
#     print(countMax)

# 29
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7b-3.txt") as file:
#     s = file.read()
#     countBAFE = 0
#     countMax = 0
#     count = 0
#     for i in range(len(s)):
#         if s[i : i+4] == "BAFE":
#             countBAFE += 1
#         if countBAFE == 2 and s[i] == "B":


# TODO 33, 38, 43, 48
# 33
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7c-1.txt") as file:
#     s = file.read()
#     count = 0
#     for i in range(2, len(s)):
#         a, b, c = s[i-2], s[i-1], s[i]
#         if a in "BCD" and b in "BDE" and c in "BCE" and b != a and c != b:
#             count += 1
# print(count)                            # Ответ: 1280
# Правильный: 1280
# 38
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7c-6.txt") as file:
#     s = file.read()
#     count = 0
#     for i in range(2, len(s)):
#         a, b, c = s[i-2], s[i-1], s[i]
#         if a != b and b != c and a != c:
#             count += 1
#     print(count)                           # Мой ответ: 5563
# Правильный ответ: 5563

# 43
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7-m5.txt") as file:
#     s = file.read()
#     newS = ""
#     cLen = 0
#     count = 0
#     for i in range(len(s)):
#         c = s[i]
#         if c == "C":
#             cLen += 1
#         else:
#             if cLen > 0:
#                 newS += str(cLen) + "c"*cLen
#                 count += 1
#             cLen = 0
#         if c != "C":
#             newS += c
#     if cLen > 0:
#         newS += str(cLen) + "c" * cLen
#         count += 1
#     print(s[:15] + " " + s[-15::])
#     print(newS[:15] + " " + newS[-15::])
#     print(count)

# AAACCAAABBBCBBB BBBCCCCCCABCCCC
# AAA2ccAAABBB1cB B6ccccccAB4cccc
# 18

# 48
# with open(r"C:/Users/dimak/Downloads/24data/k7data/k7-m23.txt") as file:
#     s = file.read()
#     index = 0
#     count = 0
#     for i in range(2, len(s)):
#         letter, letter2, letter3 = s[i-2], s[i-1], s[i]
#         if ord(letter) <= ord(letter2) <= ord(letter3):     # ABCA - 2-index,1-count
#             index = i-2                                                       # ABCD - 3,2
#             count += 1
#     print(count, index)                                     # 72 148


# 56 TODO
# with open(r"C:\Users\dimak\Downloads\24data\k8data\k8-18.txt") as file:
#     s = file.read()
#     lenChain = 0
#     lenChainMax = 0
#     letter = 0
#     ourLetter = 0
#     for i in range(1, len(s)):
#         letter1, letter2 = s[i-1], s[i]
#         if letter1 == letter2:
#             lenChain += 1
#             letter = ord(s[i])
#         else:
#             if lenChainMax < lenChain:
#                 lenChainMax = lenChain
#                 ourLetter = letter
#             lenChain = 1
#     ourLetter = chr(ourLetter)
#     print(ourLetter, lenChainMax)       # Мой ответ: K 7
# Правильный ответ: K 7

# 74
# with open(r"C:\Users\dimak\Downloads\24data\k8data\k8-6.txt") as file:
#     s = file.read()
#
#     count, maxCount = 0, 0
#     letter = ""
#     for i in range(1, len(s)):
#         if s[i-1] == s[i]:
#             count += 1
#         else:
#             if count > maxCount:
#                 maxCount = count
#             count = 1
#
#     for i in range(1, len(s)):
#         letter = s[i-1]
#         if s[i-1] == s[i]:
#             count += 1
#         else:
#             if count == maxCount:
#                 print(f"{letter} - {count}")
#             count = 1                          # Мой ответ: 9 - 5
#             N - 5
# Правильный ответ:  9 5
# N 5

# 78
# with open(r"C:\Users\dimak\Downloads\24data\k8data\k8-2.txt") as file:
#     s = file.read()
#
#     count, countMax = 1, 1
#     for i in range(1, len(s)):
#         if s[i-1] != s[i]:       # Второй вар: s[i-2] != s[i]    ответ: 182
#             count += 1
#         else:
#             if countMax < count:
#                 countMax = count
#             count = 1
#     print(countMax)            # Мой ответ: 166
# Правильный: 166

# 87
# with open(r"C:\Users\dimak\Downloads\24data\24-1.txt") as file:
#     s = file.read()
#     maxNumberOdd = 0
#     number = ""
#     for i in range(len(s)):
#         possibleNumber = s[i]
#         if possibleNumber.isdigit():
#             number += possibleNumber
#         elif number != "":
#             number = int(number)
#             if number % 2 != 0 and maxNumberOdd < number:
#                 maxNumberOdd = number
#             number = ""
#     print(maxNumberOdd)        # Мой ответ: 7642289
# Правильный ответ: 7642289

# 90
# with open(r"C:\Users\dimak\Downloads\24data\24-1.txt") as file:
#     s = file.read()
#
#     minNumberEven = 10**6
#     number = ""
#     for i in range(len(s)):
#         digit = s[i]
#         if digit.isdigit():
#             number += digit
#         elif number != "":
#             number = int(number)
#             if number % 2 == 0 and minNumberEven > number:
#                 minNumberEven = number
#             number = ""
#     print(minNumberEven)             # Мой ответ: 888
#   888

# 93
# print("A" < "B")
# with open(r"C:\Users\dimak\Downloads\24data\24.txt") as file:
#     s = file.read()
#     maxLen = 0
#     line = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i-1] < s[i]: # Как запомнить первую букву
#             count += 1
#             if count-1==1:
#                 line += s[i-1]
#             line += s[i]
#         else:
#             # if maxLen < count:
#             #     maxLen = count
#             # count = 1
#             if maxLen < len(line):
#                 maxLen = len(line)
#             line = ""
#     print(maxLen)           # Мой ответ: 2
# Правильный ответ: 3

# 106
# with open(r"C:\Users\dimak\Downloads\24data\24-3.txt") as file:
#     s = file.read()
#
#     maxLen = 0
#     lenLine = 0
#     flag = True
#     letter = ""
#     for i in range(1, len(s)):
#         if s[i-1] < s[i]:
#             if flag:
#                 index = i
#                 flag = False
#             lenLine += 1
#         else:
#             if maxLen < lenLine:
#                 maxLen = lenLine
#                 letter = index
#             flag = True
#     print(letter)             # Мой ответ: 994
# 994

# 124
# print(ord("A"))   # ord - из буквы в число; chr - из числа в букву
# with open(r"C:\Users\dimak\Downloads\24data\24-1.txt") as file:
#     s = file.read()
#     s = s[1 : len(s)-1]
#
#     maxLetter = 0
#     minLetter = 10**6
#
#     index = 0
#     index2 = 0
#     lenIndexMax = 0
#     flag = True
#     count = 0
#     differenceIndexes = 0
#     for i in range(2, len(s)):
#         if s[i-2] > s[i-1] < s[i] and flag:
#             index = count
#             flag = False
#         elif s[i-2] > s[i-1] < s[i] and not flag:
#             index2 = count
#             flag = True
#         if index != 0 and index2 != 0:
#             differenceIndexes = abs(index - index2)
#             if lenIndexMax < differenceIndexes:
#                 lenIndexMax = differenceIndexes
#         count += 1
#     print(lenIndexMax)                 # Мой ответ: 24     29
# Правильный: 29

# 135
# with open(r"C:\Users\dimak\Downloads\24data\24-j4.txt") as file:
#
#     test = "BOSSdsvjdsjJBOSSsg"
#     print(test[4])
#
#     s = file.read()
#     # s = test
#     count = 0
#     for i in range(5, len(s)):
#         if s[i-5] != "J" and s[i-4:i] == "BOSS" and s[i] != "J":
#             count += 1
#     if s[:4] == "BOSS" and s[4] != "J":
#         count += 1
#     if s[-4:] == "BOSS":
#         count += 1
#     print(count)            # 2198 = 2198

# 145
# with open(r"C:\Users\dimak\Downloads\24data\24-j7.txt") as file:
#     s = file.read()
#
#     lenMaxEven = 0
#     lenMaxOdd = 0
#     lenEven = 0
#     lenOdd = 0
#     for i in range(len(s)-1):
#         digit = int(s[i])
#         if digit % 2 == 0:
#             lenEven += 1
#             if lenMaxOdd < lenOdd:
#                 lenMaxOdd = lenOdd
#             lenOdd = 0
#         else:
#             lenOdd += 1
#             if lenMaxEven < lenEven:
#                 lenMaxEven = lenEven
#             lenEven = 0
#     answer = lenMaxEven if lenMaxOdd < lenMaxEven else lenMaxOdd
#     print(answer)       # Мой ответ: 49982  18
# Правильный ответ: 18

# 146
# with open(r"C:\Users\dimak\Downloads\24data\24-j8.txt") as file:
#     s = file.read()
#
#     count = 1
#     maxCount = 0
#     for i in range(1, len(s)-1):
#         digit = int(s[i-1])
#         digit2 = int(s[i])
#         if digit+digit2 >= 10:
#             count += 1
#             if maxCount < count:
#                 maxCount = count
#         else:
#             count = 1
#     print(maxCount)            # Мой ответ: 26
# Правильный ответ: 26

# 147
# with open(r"C:\Users\dimak\Downloads\24data\24-s2.txt") as file:
#     s = file.read()
#     dictionary = dict()
#
#     for i in range(1, len(s)):
#         letter = s[i]
#         if s[i-1] == "A":
#             dictionary[letter] = dictionary.get(letter, 0) + 1
#     maxCount = max(dictionary.values())
#     letters = [letter for (letter, count) in dictionary.items() if count == maxCount]
#     minLetter = min(letters)
#     print(minLetter, maxCount)         # L 1567

# TODO 149, 162, 156, 160, 173
# 149
# with open(r"C:\Users\dimak\Downloads\24data\24-s2.txt") as file:
#     s = file.read()
#     dictionary = dict()
#
#     for i in range(2, len(s)):
#         if s[i-2] == "X" and s[i] == "Z":
#             dictionary[s[i-1]] = dictionary.get(s[i-1], 0) + 1  # Как мы добавляем с помощью get()
#     maxCount = max(dictionary.values())
#     letters = [letter for (letter, count) in dictionary.items() if count == maxCount]
#
#     print(*letters, maxCount)     # Почему-то только цифры выводятся  X 73
# Правильный ответ: X73

# 156
# with open(r"C:\Users\dimak\Downloads\24data\24-153.txt") as file:
#     s = file.read()
#     count = 0
#     for i in range(7, 11):
#         for j in range(len(s)-1):
#             newLine = s[j:j+i]
#             if newLine[0] == "A" and newLine[-1] == "F":
#                 count += 1
#     print(count)                 # Мой ответ: 3703
# Правильный ответ: 3703

# 160
# with open(r"C:\Users\dimak\Downloads\24data\24-s1.txt") as file:
#     minCount = 10**6
#     dictionaryAllLetters = dict()
#     for line in file:
#         count = line.count("A")
#         if minCount > count:
#             minCount = count
#             s = line
#         for i in line:
#             if i != "\n":
#                 dictionaryAllLetters[i] = dictionaryAllLetters.get(i, 0) + 1
#     dictionary = dict()
#     for i in range(len(s)):
#         dictionary[s[i]] = dictionary.get(s[i], 0) + 1
#     maxCount = max(dictionary.values())
#     letters = [letter for letter, count in dictionary.items() if count == maxCount]
#     letter = max(letters)
#
#     print(letter, dictionaryAllLetters[letter])       # Мой ответ: V 38429
# Правильный ответ: V38429

# 162
# with open(r"C:\Users\dimak\Downloads\24data\24-s1.txt") as file:
#     minCount = 10**6
#     dictionaryAllLetters = dict()
#     for line in file:
#         count = 0
#         for i in range(1, len(line)):
#             if ord(line[i]) - ord(line[i-1]) == 1:
#                 count += 1
#         if minCount > count:
#             minCount = count
#             s = line
#         for i in line:
#             dictionaryAllLetters[i] = dictionaryAllLetters.get(i, 0) + 1
#     dictionary = dict()
#     for i in s:
#         dictionary[i] = dictionary.get(i, 0) + 1
#     maxLetterCount = max(dictionary.values())
#     lettersWithMaxValue = [letter for letter, count in dictionary.items() if count == maxLetterCount]
#     ourLetter = max(lettersWithMaxValue)
#     print(ourLetter, dictionaryAllLetters[ourLetter])             # Мой ответ: W 38473
# Правильный ответ:  W 38473

# 173
# with open(r"C:\Users\dimak\Downloads\24data\24-173.txt") as file:
#     maxCount = 0
#     for line in file:
#         count = 0
#         for i in range(5, len(line)):
#             if line[i-5:i-2] != line[i-2:i+1]:
#                 count += 1
#             else:
#                 if maxCount < count:
#                     maxCount = count
#                 count = 0
#     maxCount += 5
#     print(maxCount)                 # Мой ответ: 2278
# Правильный ответ: 2278

# 179
# with open(r"C:\Users\dimak\Downloads\24data\24-179.txt") as file:
#     s = file.read()
#
#     dictionary = dict()
#     for i in range(5, len(s)):
#         if s[i-5:i-3] == "CB" and s[i-2:i] == "BC" and s[i-3] not in "ABF":
#             dictionary[s[i-3]] = dictionary.get(s[i-3], 0) + 1
#
#     print(dictionary)
#
#     maxCount = max(dictionary.values())
#     letters = [letter for letter, count in dictionary.items() if count == maxCount ]
#     print(*letters, sum(dictionary.values()))           # Мой ответ: C 6347
# Правильный ответ: C6347


# 12
# 112
# line = "8"*65
#
# while("888" in line or "222" in line):
#     if "222" in line:
#         line = line.replace("222", "8", 1)
#     elif "888" in line:
#         line = line.replace("888", "2", 1)
# print(line)


# 113
# line = "5"*65
#
# while ("333" in line or "555" in line):
#     if "555" in line:
#         line = line.replace("555", "3", 1)
#     elif "333" in line:
#         line = line.replace("333", "5", 1)
# print(line)                                 # 53355

# 128
# line = "222"+"5"*18
#
# while "222" in line or "888" in line:
#     while "555" in line:
#         line = line.replace("555", "8", 1)
#     if "222" in line:
#         line = line.replace("222", "8", 1)
#     elif "888" in line:
#         line = line.replace("888", "2", 1)
# print(line)

# 131
# line = 9*"4"+12*"5"
#
# while "444" in line or "888" in line:
#     if "444" in line:
#         line = line.replace("444", "8", 1)
#     while "555" in line:
#         line = line.replace("555", "8", 1)
#     while "888" in line:
#         line = line.replace("888", "3", 1)
#
# print(line)

# TODO 105, 173, 213, 223, 226, 227, 232, 235, 244, 252, 263, 270, 278, 283, 287

# 105
# x = 0
# y = 0
# x += 1
# y -= 1
# for i in range(3):
#     x += 4
#     y += 5
# x += 17
# y += 31
#
# a = x // 3
# b = y // 3
# print(a, b)     # 10 15

# 173
# j = 0
# dictionary = {0: 3, 1: 7, 2: 2, 3: 1, 4: 6, 5: 0,6: 4, 7: 5}
# number = str(32006)
# newNumber = ""
#
# count = 0
# while count <= 12:                # Почему на 1 меньше
#     for i in range(len(number)):
#         newNumber += str(dictionary[int(number[i])])
#     number = newNumber
#     newNumber = ""
#     count += 1
# print(number)             # 52774
# Правильный ответ: 52774


# 213

# line = 80*"1"
#
#
# for i in range(81, 200):
#     line = "1"*i
#     while "111" in line:
#         line = line.replace("111", "2", 1)
#         line = line.replace("222", "1", 1)
#     if line == "21":
#         countOne = i
#         break
#
# print(countOne)               #84
# 84

# 223 - ?
# count = 0
# for i in range(1, 36):
#     line = "1" * i
#     while "111" in line:
#         line = line.replace("111", "33", 1)
#         line = line.replace("333", "1", 1)
#     if line == "131":
#         count += 1
#
# print(count)                            # 5
# 5


# 226

# 33333333332222222222222222222222222222222222

# print(82/7)
# print(7*11)
# result = str(7777777777222222)
#
# while "7" in result:
#     result = result.replace("7", "23", 1)
#
# print(result.count("2"))                 # 16


# 227

# 333333333333333311111111111111111111
#
# 15(3)
# 5*15 = 75
#
# 63/5 = 12
# 63-12 = 51
# 48/5 = 9
# 333333
# 131313131313131313 333333
# 63
# 3133333333333333
# "3"*14 = 42 + 5 = 47
#          39 + 2*"5" = 49
#               3        51
#               4         53
#               5         55
#               6          57
#               7          59
#               8          61
#               9          63

# 232
# print(3+3+3+3+3+7+2+2+2)       # 28

# line = "1111111111112222"
# while "11" in line:
#     if "112" in line:
#         line = line.replace("112", "7", 1)
#     else:
#         line = line.replace("11", "3", 1)
# line = line
# total = sum(map(int, line))
# # total = 0
# # for i in line:
# #     total += int(i)
# print(total)                       # 28


# 235

# 1111111111222222222222222222223333333333333333333333333333333
# 22>111111111222222222222222222223333333333333333333333333333333
# 22>22>22>22>22>22>22>22>22>22>222222222222222222223333333333333333333333333333333
#                    40
# 10*"1" -> 20*"2" = 40
# 30*"3" -> 30*"1" = 30
#
#
# 100*"2"
#
# 2222222222222222222222222222222222222222>>>>>>>>22"2"*62>>
# myAnswer = 2*104 #"2"*40+"2"*64  208
#                                 # 110
# line

# 244
# line = "1"*50 + "2"*50 + "3"*50
#
# while "21" in line or "31" in line or "23" in line:
#     if "21" in line:
#         line = line.replace("21", "12", 1)
#     if "31" in line:
#         line = line.replace("31", "13", 1)
#     if "23" in line:
#         line = line.replace("23", "32", 1)
# print(line[9], line[89], line[129])            # Мой ответ: 132
# 132

# 252
# maxCount = 0
# for i in range(138, 1000):
#     line = "1"*i
#
#     while "111" in line:
#         line = line.replace("111", "2", 1)
#         line = line.replace("2222", "1", 1)
#     count = line.count("1")
#     if maxCount < count:
#         maxCount = count
#         index = i
#
# print(index)                      # 140
# Правильный ответ: 140

# TODO 263, 270, 278, 283, 287

# 263
# line = "0"
# for i in range(1, 1000):
#     for j in range(1, 1000):
#         for n in range(1, 1000):
#             line += i*"1" + j*"2" + n*"3"
#             while "01" in line or "02" in line or "03" in line:
#                 line = line.replace("01", "2302", 1)
#                 line = line.replace("02", "10", 1)
#                 line = line.replace("03", "201", 1)
# проверить количество, если совпадает, то брэйк

# 0111111112222233333    1*"0" + 8*"1" + 5*"2" + 5*"3"
# 2312011111111222223333 1*"0" + 9*"1" + 7*"2" + 5*"3"
#
# 0123
# 23023
# 23103
# 231201  1->23 2->1 3->2
# 23122302
# 23122310 1->23(2)  2->
#
# 01
# 2302
# 2310  1 -> 2310
#
# 02
# 10    2 -> 10
#
# 03
# 201
# 22302
# 22310 3 -> 22310
#
# x = 58 (1)
# y = 23 (2)
# z = 15 (3)
#
# 58 = x + y + z
# 23 = x + 2z
# 15 = x + z
#
# z = 15 - x
#
# 23 = x + 2(15-x)
# 23 = x + 30 - 2x
# x = 7
#
# 58 = 7 + y + 15 - 7
# y = 43
#
# z = 58 - 43 - 7
# z = 8


# 265

# 01
# 302
# 33103
# 33120  1 -> 3312
#
# 02
# 3103
# 3120 2 -> 312
#
# 03
# 20  3 -> 2
#
# x = 28(1)
# y = 34(2)
# z = 45(3)
#
# 45 = 2x + y
# 34 = x + y + z
# 28 = x + y
#
# y = 28-x
#
# 45 = 2x + 28 - x
# x = 17
#
# 34 = 17 + 28 - 17 + z
# z = 6
#
# y = 28 - 17
# y = 11

# 271

# 5343
#
# 43 - 33
# 4 - 3
#
# 53 - 433
# 5 - 43
#
# 17 раз пременится 53

# 272

# 12 - 21
# 13 -23
#
# 3111111
#
# 2+3 =5
# 404/5 = 80
# 404-3
# 401(1)
# 1(3)
# 3111111

# 273

# 222333444
# 4443322
# 3332224
# 333333333332222222222222
#
# 61*10 = 610

# 276

# for i in range(101, 1000):
#     line = "5"*i
#     while "555" in line or "888" in line:
#         line = line.replace("555", "8", 1)
#         line = line.replace("888", "55", 1)
#     if "8" not in line:
#         print(i)
#         break

# 287

# for i in range(301, 1000):
#     line = "8" * i
#     while "555" in line or "888" in line:
#         line = line.replace("555", "8", 1)
#         line = line.replace("888", "55", 1)
#     countFive = line.count("5")
#     countEight = line.count("8")
#     if countEight == 1 and countEight == 1:
#         print(i)
#         break


# i = int(input())
# answer = []
# if i > 8:
#     answer.append(i-8)
# if i % 8 != 1:
#     answer.append(i-1)
# if i % 8 != 0:
#     answer.append(i+1)
# if i <= 56:
#     answer.append(i+8)
#
# print(*answer)


# scores = int(input())
#
# if scores % 6 == 0:
#     minScores = scores//6
# else:
#     minScores = scores//6
#     minScores += 7-(scores%6)
#
# maxTotalScores = scores * 6
# print(minScores, maxTotalScores)


# stations, start, finish = map(int, input().split())
# if start > finish:
#     start, finish = finish, start
# countStations = min(finish-start-1, stations-finish+start-1)
# print(countStations)
# number = int(input())
# berries = list(map(int, input().split()))
# for i in range(1, len(berries)):
#


# n, m, y, x = map(int, input().split())
#
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         if i % 2 == 0:
#             row.append(m*i + j)     # 1, 3, 5, 7
#         else:
#             row.append(m*i - j+m-1)
#     matrix.append(row)
# # for row in matrix:
# #     print(*row)
# #
# # print(matrix)
# print(matrix[y-1][x-1])


# import math
#
# a, b = map(int, input().split())
#
# square = a*b
# answer = 0
# if math.sqrt(square).is_integer():
#     answer = math.sqrt(square)
#     answer = int(answer)
# print(answer)
# import math
#
# x1, y1, long1 = map(int, input().split())
# x2, y2, long2 = map(int, input().split())
# # p = 3.14
# # s1 = 2*p*long1**2
# # s2 = 2*p*long2**2
# answer = "NO"
#
# pythagoras = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#
# if pythagoras <= long2+long1:
#     answer = "YES"
# print(answer)

# 943

# n, m, y, x = map(int, input().split())
#
# matrix = []
# y -= 1
# x -= 1
#
# for i in range(n):
#     row = []
#     for j in range(m*i, m+(m*i)):
#         row.append(j)
#     matrix.append(row)
#
#
# # print(matrix)
#
# index = 0
# for i in matrix:
#     if index % 2 == 1:
#         matrix[index].reverse()
#     index += 1
#     # print(i)
#
# print(matrix[y][x])

# 844

# a, b = map(int, input().split())
#
# rectangleArea = a * b
# squareRoot = rectangleArea ** 0.5
# if squareRoot.is_integer():
#     squareRoot = int(squareRoot)
#     print(squareRoot)
# else:
#     print(0)


# 26

# x, y, radius = map(int, input().split())
# x2, y2, radius2 = map(int, input().split())
#
# distanceBetweenCenters = ((x2 - x)**2 + (y2 - y)**2)**0.5
# minRadius = min(radius, radius2)
# maxRadius = max(radius, radius2)
# if distanceBetweenCenters > radius + radius2 or distanceBetweenCenters + minRadius < maxRadius:
#     print("NO")
# else:
#     print("YES")

# 10 TODO

# a, b, c, d = map(int, input().split())
#
# answer = []
# for x in range(-100, 101):
#     equation = a*x**3 + b*x**2 + c*x + d
#     if equation == 0:
#         answer.append(x)
# print(*answer)                # Не знаю как проверить на кратность


# 778

# array = list(map(int, input().split()))   # Как добавить в массив числа, которые считываем
# lenArray = len(array)-4
# answer = sum(array)//lenArray
#
# print(answer)


# 340

# a, b, c = sorted(map(int, input().split()))
# a2, b2, c2 = sorted(map(int, input().split()))
#
#
#
# if a == a2 and b == b2 and c == c2:
#     print("Boxes are equal")
# elif a >= a2 and b >= b2 and c >= c2:
#     print("The first box is larger than the second one")
# elif a <= a2 and b <= b2 and c <= c2:
#     print("The first box is smaller than the second one")
# else:
#     print("Boxes are incomparable")      # Как определить, когда выводить его


# 895
# array = []
# for i in range(3):
#     array.append(input())
#
# # print(array)
# # print(array[0][1])
# # print(array[1][0])
#
# if (array[0][0] == "X" and array[0][0] == array[1][1] and array[0][0] == array[2][2]) \
#         or (array[0][2] == "X" and array[0][2] == array[1][1] and array[1][1] == array[2][0]) \
#         or (array[0][0] == "X" and array[0][0] == array[0][1] and array[0][1] == array[0][2]) \
#         or (array[1][0] == "X" and array[1][0] == array[1][2] and array[1][1] == array[1][2]) \
#         or (array[2][0] == "X" and array[2][0] == array[2][1] and array[2][1] == array[2][2]) \
#         or (array[0][0] == "X" and array[0][0] == array[1][0] and array[1][0] == array[2][0]) \
#         or (array[0][1] == "X" and array[0][1] == array[1][1] and array[1][1] == array[2][1]) \
#         or (array[0][2] == "X" and array[0][2] == array[1][2] and array[1][2] == array[2][2]):
#     print("Win")
# elif (array[0][0] == "O" and array[0][0] == array[1][1] and array[0][0] == array[2][2]) \
#         or (array[0][2] == "O" and array[0][2] == array[1][1] and array[1][1] == array[2][0]) \
#         or (array[0][0] == "O" and array[0][0] == array[0][1] and array[0][1] == array[0][2]) \
#         or (array[1][0] == "O" and array[1][0] == array[1][2] and array[1][1] == array[1][2]) \
#         or (array[2][0] == "O" and array[2][0] == array[2][1] and array[2][1] == array[2][2]) \
#         or (array[0][0] == "O" and array[0][0] == array[1][0] and array[1][0] == array[2][0]) \
#         or (array[0][1] == "O" and array[0][1] == array[1][1] and array[1][1] == array[2][1]) \
#         or (array[0][2] == "O" and array[0][2] == array[1][2] and array[1][2] == array[2][2]):
#     print("Lose")
# else:
#     print("Draw")

# 63

# s, p = map(int, input().split())
#
# for x in range(1, 1001):
#     for y in range(1, 1001):
#         if x + y == s and x * y == p:
#             answer1 = x
#             answer2 = y
#             break
# if answer2 < answer1:
#     answer1, answer2 = answer2, answer1
# print(answer1, answer2)

# 28

# x1, y1, x2, y2 = map(int, input().split())
#
# xa, ya = map(int, input().split())
#
# if x1 == x2:
#     if xa > x1:
#         xb = x2 - xa
#         yb = ya
#     else:
#         xb = x2 + xa
#         yb = ya
# else:
#     if ya > y1:
#         yb = y1 - ya
#         xb = xa
#     else:
#         yb = y1 + ya
#         xb = xa
#
# print(xb, yb)


# 688

# gopherX, gopherY = map(int, input().split())
# dogX, dogY = map(int, input().split())
# countMink = int(input())
#
# for index in range(countMink):
#     currentMinkX, currentMinkY = map(int, input().split())
#     currentMinkGopher = (currentMinkX-gopherX)**2 + (currentMinkY-gopherY)**2
#     currentMinkDog = (currentMinkX-dogX)**2 + (currentMinkY-dogY)**2
#     if currentMinkGopher * 4 <= currentMinkDog:
#         ourMink = index + 1
#         print(ourMink)
#         break
# else:
#     print("NO")


# 633

# nameCommand = input()
#
# firstName = input()
# secondName = input()
# thirdName = input()
#
# names = []
# names.append(firstName)
# names.append(secondName)
# names.append(thirdName)
# names = sorted(names)
#
#
# print(nameCommand + ": " + names[0] + ", " + names[1] + ", " + names[2])

# 643

# s = int(input())
# initialS = s
# answer = 1
# binarySystem = []
# while answer != 0:
#     remains = s % 2
#     binarySystem.append(remains)
#     s //= 2
#     answer = s
# binarySystem = reversed(binarySystem)
#
# total = 0
# for i in binarySystem:
#     if i == 1:
#         total += 1
#
# newS = initialS + total
# print(newS)

# 675

# row, line = map(int, input().split())
# lineDoth = line
# for i in range(row):
#     lineString = input()
#     if lineString.count(".") < lineDoth:
#         lineDoth = lineString.count(".")
#
# print(lineDoth)

# a = list(map(int, input().split()))
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# count = 0
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if i < j and a[i] > a[j]:
#             count += 1
# print(count)


class MyClass(object):
    def containsNeardbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            for j in range(i + k):
                if nums[i] == nums[j]:
                    return True
        return False


nums = [1, 2, 3, 1]
k = 3

test = MyClass.containsNeardbyDuplicate(nums, k)
print(test)
