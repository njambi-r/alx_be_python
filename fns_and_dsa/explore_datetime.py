import datetime
def display_current_datetime():
    current_date=datetime.datetime.now()
    current_date=current_date.strftime("%Y-%M-%D, %H:%M:%S")
    print ("Current date and time:", current_date)


def calculate_future_date():
    number_of_days=int(input("Enter the number of days to add to the current date: "))
    future_date=datetime.datetime.now() + datetime.timedelta(days=number_of_days) 
    print("Future date: ", future_date)

display_current_datetime()
calculate_future_date()