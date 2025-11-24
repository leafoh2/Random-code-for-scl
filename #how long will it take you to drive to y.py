#made by @67bf on discord

#how long will it take you to drive to your destination

print("How long will it take you to drive to your destination?")

def calcHours():
    miles_entered = input("Enter the number of miles of your destination    (or press Enter for 0): ")
    miles = int(miles_entered or "0")
    milesPerHour = 65
    # compute hours (use float for partial hours)
    hours = miles / milesPerHour if milesPerHour != 0 else None
    return hours
def checkHours():
    hours = calcHours()

    if hours is None:
        return

    print("Your drive is " + str(hours) + " hours.")
    if hours >= 10:
        print("You have a very long drive!  Stay awake.")
    
    elif hours >= 6:
        print("You have a long drive, but you can do it!")
    
    elif hours >= 3:
        print("A little long, but not that bad")
    
    elif hours >= 0:
        print("A pretty short drive")
    
    else:
        print("Please enter the number of miles to your destination.")

checkHours()
