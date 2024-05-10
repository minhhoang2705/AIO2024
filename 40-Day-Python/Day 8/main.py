food_list = [
    ["Bơ", "Pizza", "Sữa"],
    ["Đường", "Cafe", "Nuoc"],
    ["Cà rốt", "Bánh dâu", "Cupcake"],
]

search_items = ["Cà rốt", "Đường", "Sữa"]

# method 1
print("Method 1")
for i in range(len(food_list)):
    for j in range(len(food_list[i])):
        if food_list[i][j] in search_items:
            print(f"{food_list[i][j]} được tìm thấy ở hàng " f"{i+1} và cột {j+1}")

# method 2
print("Method 2")
for i, row in enumerate(food_list):
    for j, item in enumerate(row):
        if item in search_items:
            print(f"{item} được tìm thấy ở hàng {i+1} và cột {j+1}")