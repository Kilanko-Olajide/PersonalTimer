import time
while True:

    print("Enter h for hours, m for minutes.")
    time_unit = input("Do you want to input in hours or minutess: ")
    desired_time = int(input("What is the time you want to set: "))
    if time_unit == "h":
        desired_time *= 3600
        break
    elif time_unit == "m": 
        desired_time *= 60
        break
    else:
        print("You need to enter a valid input")

for number in range(desired_time, 0, -1):
    
    
    seconds = number % 60
    hours = number // 3600
    remainder = number % 3600
    minutes = remainder // 60

    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Times up, mothefucker.")
