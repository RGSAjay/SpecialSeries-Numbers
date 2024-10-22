# Special Series Generator and Special Number Checker

## Overview
The **Special Series Generator and Special Number Checker** is a Flask web application that allows users to generate special numeric series and check whether a given number is a specific type of special number. The app supports various series like Fibonacci and Armstrong, as well as special number checks such as prime, perfect, and automorphic numbers.

## Features
- **Generate Series**: Users can generate special series, including:
  - Fibonacci series
  - Prime series
  - Factorial series
  - Armstrong series
  - Pell series

- **Check Special Number**: Users can check if a number is one of the following special types:
  - Prime number
  - Armstrong number
  - Perfect number
  - Harshad number
  - Automorphic number

## Technology Stack
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Deployment**: Render for web hosting

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python (version 3.x)
- Flask
- A code editor (e.g., Visual Studio Code)

### Installation
1. Clone the repository:
   
   git clone https://github.com/RGSAjay/SpecialSeries-Numers.git

2.Navigate to the project directory:

   cd SpecialSeries-Numers

3.Create and activate a virtual environment:

   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate

4.Install the required packages:

   pip install -r requirements.txt

## To run the Flask app locally, use the following command:

   python app.py

## Deployment
This app is deployed on Render. If you want to deploy it yourself, ensure you create a requirements.txt and Procfile for the deployment process.

Requirements.txt
List all dependencies in this file.

Procfile
Specify the command to run the app:

  web: python app.py

Contributing
Feel free to contribute by forking the repository and submitting a pull request.

Acknowledgments
Flask documentation for the framework guidance.
Bootstrap for responsive design.
