"""appointments = {
    'Monday': ['9:00 am', '11:00 am', '2:00 pm'],
    'Tuesday': ['10:00 am', '1:00 pm', '3:00 pm'],
    'Wednesday': ['9:30 am', '12:00 pm', '4:00 pm'],
    'Thursday': ['11:00 am', '2:30 pm', '5:00 pm'],
    'Friday': ['9:00 am', '12:00 pm', '3:30 pm'],
    'Saturday': ['10:00 am', '1:30 pm', '4:30 pm'],
    'Sunday': ['11:30 am', '3:00 pm', '5:30 pm']
} """

"""
appointments = {
    'Monday': {
        'Brian': ['8:30 am', '10:00 am', '12:00 pm'],
        'Terry': ['9:00 am', '11:00 am', '1:00 pm'],
        'Irvine': ['2:00 am', '3:00 pm', '4:00 pm']
    },
    'Tuesday': {
        'Terry': ['12:00 am', '1:00 pm', '3:00 pm'],
        'Irvine': ['11:00 am', '9:00 am', '10:00 am'],
        'Brian': ['8:30 am', '2:00 pm', '4:00 pm']
    },
    'Wednesday': {
        'Terry': ['11:00 am', '2:00 pm', '3:00 pm'],
        'Irvine': ['8:30 am', '9:00 am', '10:00 am'],
        'Brian': ['12:00 am', '1:00 pm', '4:00 pm']
    },
    'Thursday': {
        'Terry': ['8:30 am', '9:00 am', '10:00 am'],
        'Irvine': ['11:00 am', '12:00 pm', '1:00 pm'],
        'Brian': ['2:00 pm', '3:00 pm', '4:00 pm']
    },
    'Friday': {
        'Terry': ['9:00 am', '11:00 am', '1:00 pm'],
        'Irvine': ['8:30 am', '10:00 am', '12:00 pm'],
        'Brian': ['2:00 pm', '3:00 pm', '4:00 pm']
    },
    'Saturday': {
        'Terry': ['12:00 pm', '1:00 pm', '2:00 pm'],
        'Irvine': ['9:00 am', '11:00 am', '3:00 pm', '4:00pm'],
        'Brian': ['8:30 am', '9:00 am', '10:00 am']
    },
    'Sunday': {None
               # 'Rickey': ['11:00 am', '1:00 pm', '3:00 pm'],
               # 'Irvine': ['10:00 am', '12:00 pm', '2:00 pm'],
               # 'Brian': ['9:30 am', '11:30 am', '1:30 pm']
               }
}

haircut_prices = {
    'Buzz Cut': 30,
    'Crew Cut': 35,
    'Fade': 40,
    'Mohawk': 44,
    'Bald Cut': 33
}

barber = {
    'Brian': {},
    'Rickey': {},
    'Irvine': {}
}


def calculate_price(service, barber_name, day, time, haircut_prices, appointments):
    # Check if the service exists in the haircut prices dictionary
    if service not in haircut_prices:
        return "Invalid service selected"

    # Check if the day exists in the appointments dictionary
    if day not in appointments:
        return "The selected day is not available"

    # Check if the barber exists in the appointments dictionary
    if barber_name not in appointments[day]:
        return "The selected barber is not available on {}".format(day)

    # Check if the selected time is available for the selected barber on the chosen day
    if time not in appointments[day][barber_name]:
        return "The selected time is not available for {} on {}".format(barber_name, day)

    # Calculate the price of the selected service
    price = haircut_prices[service]
    return "The price of {} by {} on {} at {} is ${}".format(service, barber_name, day, time, price)


# Example usage
service = 'Fade'
barber_name = 'Brian'
day = 'Saturday'
time = '10:00 am'

print(calculate_price(service, barber_name, day, time, haircut_prices, appointments)) """
# Dictionary of appointments
appointments = {
    'Monday': {
        'Brian': ['8:30 am', '10:00 am', '12:00 pm'],
        'Terry': ['9:00 am', '11:00 am', '1:00 pm'],
        'Irvine': ['2:00 am', '3:00 pm', '4:00 pm']
    },
    'Tuesday': {
        'Terry': ['12:00 am', '1:00 pm', '3:00 pm'],
        'Irvine': ['11:00 am', '9:00 am', '10:00 am'],
        'Brian': ['8:30 am', '2:00 pm', '4:00 pm']
    },
    'Wednesday': {
        'Terry': ['11:00 am', '2:00 pm', '3:00 pm'],
        'Irvine': ['8:30 am', '9:00 am', '10:00 am'],
        'Brian': ['12:00 am', '1:00 pm', '4:00 pm']
    },
    'Thursday': {
        'Terry': ['8:30 am', '9:00 am', '10:00 am'],
        'Irvine': ['11:00 am', '12:00 pm', '1:00 pm'],
        'Brian': ['2:00 pm', '3:00 pm', '4:00 pm']
    },
    'Friday': {
        'Terry': ['9:00 am', '11:00 am', '1:00 pm'],
        'Irvine': ['8:30 am', '10:00 am', '12:00 pm'],
        'Brian': ['2:00 pm', '3:00 pm', '4:00 pm']
    },
    'Saturday': {
        'Terry': ['12:00 pm', '1:00 pm', '2:00 pm'],
        'Irvine': ['9:00 am', '11:00 am', '3:00 pm', '4:00pm'],
        'Brian': ['8:30 am', '9:00 am', '10:00 am']
    },
    'Sunday': {None
               # 'Rickey': ['11:00 am', '1:00 pm', '3:00 pm'],
               # 'Irvine': ['10:00 am', '12:00 pm', '2:00 pm'],
               # 'Brian': ['9:30 am', '11:30 am', '1:30 pm']
               }
}

# Dictionary of haircut prices
haircut_prices = {
    'Buzz Cut': 30,
    'Crew Cut': 35,
    'Fade': 40,
    'Mohawk': 44,
    'Bald Cut': 33
}

# Dictionary of barbers
barber = {
    'Brian': {},
    'Rickey': {},
    'Irvine': {}
}


# Function to calculate the price of a haircut
def calculate_price(service, barber_name, day, time):
    # Check if the service exists in the haircut prices dictionary
    if service not in haircut_prices:
        return "Invalid service selected Please choose one of the following with the correct spelling"

    # Check if the day exists in the appointments dictionary
    if day not in appointments:
        return "The selected day is not available"

    # Check if the barber exists in the appointments dictionary for the selected day
    if barber_name not in appointments[day]:
        return "The selected barber is not available on {}".format(day)

    # Check if the selected time is available for the selected barber on the chosen day
    if time not in appointments[day][barber_name]:
        return "The selected time is not available for {} on {}".format(barber_name, day)

    # Calculate the price of the selected service
    price = haircut_prices[service]
    return "The estimated cost of a {} by your choosing Barber on {} at {} is ${}".format(service, day, time, price)
