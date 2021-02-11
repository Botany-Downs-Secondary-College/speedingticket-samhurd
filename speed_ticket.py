warrants = ["James Wilson", "Helga Norman", "Zachary Conroy"]
fines = []


def checkWarrants(name):
    for driver in warrants:
        if driver == name:
            print(driver.upper(), "WANTED FOR ARREST")

def speed_limits(speed_limit, actual_speed):

    return actual_speed - speed_limit

def conditions():

    if speed_over >= 1 and speed_over < 50:

        owe = speed_over * 10

        print("You owe ${}".format(owe))

        print("You were going {}km/h!".format(actual_speed))

      

    elif speed_over >= 50 and speed_over < 80:

        print("Give me your licence")

        print("You were going {}km/h!".format(actual_speed))

      

    elif speed_over >= 80:

        print("You are going to jail!")

        print("You were going {}km/h!".format(actual_speed))

  

    else:

        print("You are not speeding")


name = input("What is your full name?")

while True:

    try:

        speed_limit = int(input("What is the speed limit in this area?"))

        if speed_limit <= 0 or speed_limit >= 150:

            speed_limit = ValueError

            print("That is not a valid speed limit")

        else:

            break

    except ValueError:

        print("That is not a valid speed")

while True:

    try:

        actual_speed = int(input("What speed is the driver going at?"))

        if actual_speed <= 0 or actual_speed >= 400:

            actual_speed = ValueError

            print("That is not a valid speed")

        else:

            break

    except ValueError:

        print("That is not a valid speed")


speed_over = speed_limits(speed_limit, actual_speed)

checkWarrants(name)
conditions()