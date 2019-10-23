"""WAP that asks the user the day number in a year in the range 2 to 365 and asks the first day of the year- Sunday or Monday etc.
Then the program should display the day on the day-number that has been input.
"""
def day_check():
    ch = 'y'
    while ch == 'Y' or ch == 'y':
        n = int(input("Enter a number from (2-365) : "))
        w_ends = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
        if 2 <= n <= 365:
            fd = input("Enter the first day of the year : ")
            if fd.upper() in w_ends:
                print(w_ends[(w_ends.index(fd.upper()) + n - 1) % 7])
            else:
                print("Not a day!!!")
        else:
            print("Out of Input Range!!!")
        ch = input("Do you want to continue?(y/n) : ")


day_check()
