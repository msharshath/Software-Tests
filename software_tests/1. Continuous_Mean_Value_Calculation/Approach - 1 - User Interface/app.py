# app.py (Python backend)
from flask import Flask, request, render_template

app = Flask(__name__)

# Variables to store the sum and count
total_sum = 0
count = 0

# Function to check if the input value is a valid floating-point number
def is_valid_float(value):
    return '.' in value

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")

# Route for calculating the mean
@app.route("/calculate", methods=["POST"])
def calculate_mean():
    global total_sum, count

    try:
        input_value = request.json["value"]

        # Check if the entered value is a valid floating-point number
        if not is_valid_float(input_value):
            raise ValueError("Please enter a valid floating-point number.")

        new_value = float(input_value)

    except ValueError:
        return "Invalid input. Please enter a valid floating-point number."

    # Update variables
    total_sum += new_value
    count += 1

    # Calculate the current mean
    current_mean = total_sum / count

    return f"Current mean: {current_mean}"

# Route to reset calculations (triggered by the "End Input" button)
@app.route("/reset", methods=["POST"])
def reset_calculations():
    global total_sum, count

    # Reset total sum and count to 0
    total_sum = 0
    count = 0

    return "Calculations reset. You can start again."

if __name__ == "__main__":
    app.run(debug=True)
