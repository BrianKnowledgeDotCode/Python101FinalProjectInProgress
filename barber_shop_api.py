from flask import Flask, render_template, request

from calculate_api.calculator import appointments, haircut_prices, barber, calculate_price

import logging

logging.basicConfig(level=logging.DEBUG)  # This line is to Set logging level to DEBUG

app = Flask(__name__)


# Define route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')


# Define route to handle form submission and render the appointmentDetails.html, error.html, or weAreClosed.html
# template
@app.route('/calculate_price', methods=['POST'])
def calculate_price_route():
    # Retrieve form data
    if request.method == "POST":
        print("POST METHOD WORKS")  # testing to see is the code is getting to this line of code
    selected_service = request.form['cutStyle']
    print("Test Selected_Service Request Works")  # testing to see is the code is getting to this line of code
    selected_barber = request.form['barber']
    print("Test Selected_Barber Request Works")  # testing to see is the code is getting to this line of code
    selected_day = request.form['day']
    print("Test Selected_Dey Request Works")  # testing to see is the code is getting to this line of code
    selected_time = request.form['appointment']
    print("Test Selected_Time Request Works")  # testing to see is the code is getting to this line of code

    # Call calculate_price function and render the appropriate template based on the result
    result = calculate_price(selected_service, selected_barber, selected_day, selected_time)
    print("Test Rendering AppointmentDetails Template Works")
    print(result)  # testing to see is the code is getting to this line of code
    print(selected_day)  # testing to see is the code is getting to this line of code
    print(appointments)  # testing to see is the code is getting to this line of code

    # if selected_service not in haircut_prices:
    # return render_template('error.html')
    # Check if the selected day is available for appointments if not render the weAreClosed template
    if selected_day == 'Sunday':
        return render_template('weAreClosed.html')
    else:
        return render_template('appointmentsDetails.html', selected_day=selected_day, selected_time=selected_time,
                               result=result, selected_barber=selected_barber, )
        # return render_template('error.html', result={'error_message': result})


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode

"""
from flask import Flask, render_template, request
# from calculate_api import calculator
import logging

logging.basicConfig(level=logging.DEBUG)  # This line is to Set logging level to DEBUG

app = Flask(__name__)  # This line is to activate the Flask application / instantiate the Flask object


@app.route('/')
def client_form():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    best_day = request.form['selectbasic']
    best_time = request.form['appointment']
    service_needed = request.form['textinput']

    # Assuming you have the appointment details available
    appointment_details = {
        'day_of_appointment': 'Monday',
        'time_of_appointment': '12:00 pm',
        'cost_of_appointment': '$150',
        'name_of_employee': 'James'
    }

    return render_template('result.html', best_day=best_day, best_time=best_time, service_needed=service_needed,
                           result=appointment_details)


@app.route('/appointment_details')
def appointment_details():
    # Assuming you have the appointment details available
    appointment_details = {
        'date_of_appointment': 'Monday',
        'time_of_appointment': '12:00 pm',
        'cost_of_appointment': '$150',
        'name_of_employee': 'James'
    }

    print(appointment_details)  # Add this line to check the appointment details data

    return render_template('appointmentDetails.html', result=appointment_details)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode """
