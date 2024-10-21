from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Check special number route
@app.route('/check_special_number', methods=['GET'])
def check_special_number():
    number = int(request.args.get('number'))
    special_type = request.args.get('special_number')

    # Choose the correct check function
    if special_type == 'prime':
        result = check_prime(number)
    elif special_type == 'armstrong':
        result = check_armstrong(number)
    elif special_type == 'perfect':
        result = check_perfect(number)
    elif special_type == 'harshad':
        result = check_harshad(number)
    elif special_type == 'automorphic':
        result = check_automorphic(number)
    else:
        result = "Unknown special number type"

    # Render the result in the same page
    return render_template('index.html', result=result)
    
# Generate series route
@app.route('/generate_series')
def generate_series():
    number = int(request.args.get('number'))
    series_type = request.args.get('series')

    if series_type == 'fibonacci':
        result = fibonacci_series(number)
    elif series_type == 'prime':
        result = prime_series(number)
    elif series_type == 'factorial':
        result = factorial_series(number)
    elif series_type == 'armstrong_series':
        result = armstrong_series(number)
    elif series_type == 'pell':
        result = pell_series(number)
    else:
        result = "Unknown series"
    # Render the result in the same page
    return render_template('index.html', result=result)



# Functions for series
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def prime_series(n):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
        num += 1
    return primes

def factorial_series(n):
    result = [1]
    for i in range(2, n+1):
        result.append(result[-1] * i)
    return result

def armstrong_series(n):
    result = []
    for i in range(1, n + 1):
        num_digits = len(str(i))  # Number of digits
        if sum(int(digit) ** num_digits for digit in str(i)) == i:
            result.append(i)
    return result



def pell_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, 2*b + a
    return series

# Functions for checking special numbers
def check_prime(num):
    if num < 2:
        return f"{num} is not a Prime Number."
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a Prime Number."
    return f"{num} is a Prime Number."

def check_armstrong(num):
    if num == sum(int(digit) ** len(str(num)) for digit in str(num)):
        return f"{num} is an Armstrong Number."
    else:
        return f"{num} is not an Armstrong Number."

def check_perfect(num):
    if num == sum(i for i in range(1, num) if num % i == 0):
        return f"{num} is a Perfect Number."
    else:
        return f"{num} is not a Perfect Number."

def check_harshad(num):
    if num % sum(int(digit) for digit in str(num)) == 0:
        return f"{num} is a Harshad Number."
    else:
        return f"{num} is not a Harshad Number."

def check_automorphic(num):
    if str(num ** 2).endswith(str(num)):
        return f"{num} is an Automorphic Number."
    else:
        return f"{num} is not an Automarphic Number."


if __name__ == '__main__':
    app.run(debug=True)
