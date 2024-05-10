# Q1
lst_data = [i for i in range(1, 13) if i % 2 == 0]
print(lst_data)
# Q2
for i in range(len(lst_data)):
    if i % 3 == 0:
        lst_data.pop(i-1)

print(lst_data)

# Q3 
lst_data[3:3] = [6, 7, 8]
for i in range(0, 3):
    lst_data.append(i+1)
print(lst_data)

# Q4
for i in range(len(lst_data)):
    if (lst_data[i] % 2 == 0) or (lst_data[i] % 5 == 0):
        lst_data[i] = 0
print(lst_data)