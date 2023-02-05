from datetime import date 

if __name__ == '__main__':
    current_date = date.today()                                    # Read the current date
    print("Today is :%d/%d/%d" % (current_date.day,current_date.month,current_date.year))            # Print the formatted date

