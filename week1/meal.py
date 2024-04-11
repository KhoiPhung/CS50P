def main():
    time = convert(input("What time is it? "))

    #comparing convertted time from convert function
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        pass        


def convert(time):
    hours, minutes = time.split(":")

    #check if there's an am or pm in the time
    if minutes.endswith("m"):
        min, aorp = minutes.split()
        convertted_minute = int(min) / 60
        convertted_time = float(int(hours) + convertted_minute)
    
        #converting time to suit main function
        if aorp == "pm":
            convertted_time = convertted_time + 12
            return convertted_time
        else:
            return convertted_time
    else:
        convertted_minute = int(minutes) / 60
        convertted_time = float(int(hours) + convertted_minute) 
        return convertted_time


if __name__ == "__main__":
    main()
