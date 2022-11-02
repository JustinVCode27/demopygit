# Name:Justin Vu
# PSID: 1823121

def get_month_as_int(month_string):
    if month_string == 'January':
        month_int = 1
    elif month_string == 'February':
        month_int = 2
    elif month_string == 'March':
        month_int = 3
    elif month_string == 'April':
        month_int = 4
    elif month_string == 'May':
        month_int = 5
    elif month_string == 'June':
        month_int = 6
    elif month_string == 'July':
        month_int = 7
    elif month_string == 'August':
        month_int = 8
    elif month_string == 'September':
        month_int = 9
    elif month_string == 'October':
        month_int = 10
    elif month_string == 'November':
        month_int = 11
    elif month_string == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


input_file = open('C:\\Users\\justi\\PycharmProjects\\Code\\inputDates.txt', 'r')
print(input_file.read())
