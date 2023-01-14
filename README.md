Password Generator and Strength Checker

This is a simple application built using Python Flask that allows users to generate and check the strength of their passwords.
Features

    Generate secure, random passwords of any desired length
    Check the strength of a given password

Requirements

    Python 3.x
    Flask
  

Installation

    Clone the repository

git clone 


    Install the required packages

pip install -r requirements.txt



    Run the program

python password generator

The application should now be running on http://localhost:5000
Usage

    To generate a password, visit http://localhost:5000/generate and enter the desired length of the password.
    To check the strength of a password, visit http://localhost:5000/check and enter the password. The application will return a score indicating the strength of the password.


    The passwords generated are cryptographically random and are not stored in any way, so the passwords generated cannot be retrieved.
    The strength checker uses a combination of checks including length, complexity, and common patterns to determine the strength of a password.

Contribution

Feel free to submit a pull request or open an issue if you find any bug or want to add any feature.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.