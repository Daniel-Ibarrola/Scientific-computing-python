def add_time(start, duration, day=None):

    daysDict = {'monday': 1, 'tuesday': 2, 'wednesday': 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}

    #Split strings to find hour, min, and time period
    startTime = start.split()
    startMinHour = startTime[0].split(":")
    endTime = duration.split(':')
    #Time period is "AM" or "PM"
    timePeriod = startTime[1]

    hourSum = int(startMinHour[0])
    minutesSum = int(startMinHour[1]) + int(endTime[1])

    # print(hourSum)
    # print(minutesSum)

    daysPassed = ""
    newDay = False 
    hour = 0
    dayCount = 0
    
    #Calculate Minutes
    if minutesSum >= 60:
        hour = minutesSum // 60
        newMinutes = minutesSum % 60
        hourSum += hour
    else:
        newMinutes = minutesSum

    # print(newMinutes)
    # print(hourSum)

    hourDelta = int(endTime[0])
    totalDelta = hourDelta + hour
    # print(hourDelta)

    #Calculate Hour
    if hourSum + hourDelta >= 12:

        if totalDelta == 24:
            # print("24 hours delta")
            newHour = hourSum
            newDay = True    

        elif (hourSum + hourDelta) % 12 != 0:
            # print("Hour delta is not a multiple of 12")
            newHour = (hourSum + hourDelta) % 12
            if timePeriod == "AM":
                timePeriod = "PM"
            elif timePeriod == "PM":
                timePeriod = "AM"
                newDay = True

        else:
            # print("Hour delta is a multiple of 12")
            newHour = hourSum
            if (hourSum + hourDelta) % 24 != 0:
                if timePeriod == "AM":
                    timePeriod = "PM"
                elif timePeriod == "PM":
                    timePeriod = "AM"
                    newDay = True
    else:
        newHour = hourSum + hourDelta
    
    new_time = f"{newHour}:{newMinutes:02d} {timePeriod}"


    #Calculate days passed
    if newDay and totalDelta/24 <= 1:
        dayCount = 1
        daysPassed = "(next day)"
    elif newDay and totalDelta/24 > 1:
        dayCount = (totalDelta // 24) + 1
        daysPassed = f"({dayCount} days later)"

    if day:
        startDay = daysDict[day.lower()]
        dayIndex = startDay + dayCount % 7 
        #print(dayCount)
        if dayIndex > 7:
            dayIndex = dayIndex % 7
        #Get day from day index
        endDay = list(daysDict.keys())[list(daysDict.values()).index(dayIndex)]
        new_time += f", {endDay.capitalize()}"
    
    if daysPassed:
        new_time += f" {daysPassed}"

    print(f"TIME IS: {new_time}")

    return new_time

add_time("8:16 PM", "466:02", "tuesday")

# add_time("2:59 AM", "24:00")

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
 
# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday
 
# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM
 
# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)
 
# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)
 
# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)