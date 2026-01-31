# 1.User Profile Validation System

Challenge Title:
User Profile Validation System

## Scenario:
This project implements a basic user profile validation system designed for a university web portal.
Before storing user information, the system validates the entered details according to predefined rules.
The objective of this project is to demonstrate the use of Python data types, conditional statements,
and string manipulation in solving a real-world problem.

## Problem Statement:
The program accepts the following inputs from the user:
1. Full Name (string)
2. Email ID (string)
3. Mobile Number (string)
4. Age (integer)

Based on the validation rules, the program determines whether the user profile is valid or invalid.

## Validation Rules:

## Full Name Validation:
- The full name must contain at least two words.
- The name must not start or end with a space.
## Email ID Validation:
- The email ID must contain both '@' and '.' characters.
- The '@' symbol must not be the first character.
## Mobile Number Validation:
- The mobile number must contain exactly 10 characters.
- It must consist only of digits.
- It must not start with the digit 0.
## Age Validation:
- The age must be between 18 and 60 inclusive.
## Expected Output:
If all validations pass, the program displays:
User Profile is VALID
If any validation fails, the program displays:
User Profile is INVALID
## How to Run:
1. Ensure Python 3 is installed on the system.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Execute the program using:
   python main.py

## Requirements:
Python 3.x
Author:
Naga Sree Pavan Alapati

# 2.Student Registration Validation

This program checks whether the user-entered details follow basic registration rules.

## It validates:
- Student ID
- Email ID
- Password
- Referral Code

Only when all conditions are satisfied, the registration is approved.

## Validation Rules
Student ID
- Must start with CSE
- Followed by -
- Ends with digits

Example: CSE-1023

Email ID
- Must contain exactly one @
- Should end with .edu
- @ should not be at the beginning or end

Example: student@college.edu

Password
- Minimum 8 characters
- First character must be an uppercase letter
- Must contain at least one digit

Referral Code
- Starts with REF
- Next two characters must be digits
- Must end with @

Example: REF12@

## Output
Prints APPROVED if all conditions pass
Prints REJECTED if any rule fails
##How to Run
python registration_validation.py

## Purpose
This program is created to practice:
- String slicing
- Conditional statements
- Input validation
- Logical operators in Python

