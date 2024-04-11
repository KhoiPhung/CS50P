months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    #get the input in month/day/year, check conditions, and output by calling other functions to format
    while True:
        try:
            date = input("Date: ")
            print(check_date(date))
        except UnboundLocalError:
            pass
        else:
            break


def month_formatting(month):
    #formatting worded month to numberred month
    if month.isdigit():
        return month
    else: 
        if month in months:
            return str(months.index(month) + 1)


def day_check(day):
    if 31 >= int(day) >= 1:
        return day
    else:
        return False


def check_date(date):
    #formatting the inputted date to the output of year-month-day
    date_parts = date.split()
    if len(date_parts) == 1:
        month, day, year = date.split("/")
    elif len(date_parts) == 3 and date_parts[0].capitalize() in months:
        month, day_with_comma, year = date_parts
        day = day_with_comma.strip(",")
        month = month_formatting(month)

    day = day_check(day)
    if len(month) == 1:
        return f"{year}-{int(month):02}-{int(day):02}"
    else:
        return f"{year}-{month}-{day}" 


main()


'''
    The program will have 3 functions: main (which calls the input, check the formatting, and outputting the result), 
    month from months list to number, and month number to formatted number (09 for example).
'''