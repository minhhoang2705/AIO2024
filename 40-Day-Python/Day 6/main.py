time =  input("Enter the time: ")

# method 1: if-else 
# Day 6/main.py
print("Method 1: if-else")
if time == "7:00":
    print("Wake up")
elif time == "7:30":
    print("Breakfast")
elif time == "8:00":
    print("Work")
else:
    print("Do something else")


#  method 2:  Dictionary
print("Method 2: Dictionary")
todo = {
    "7:00": "Wake up",
    "7:30": "Breakfast",
    "8:00": "Work",
}
print(todo.get(time, "Do something else"))

#  method 3:  switch-case
print("Method 3: switch-case")
match time:
    case "7:00":
        print("Wake up")
    case "7:30":
        print("Breakfast")
    case "8:00":
        print("Work")
    case _:
        print("Do something else")
