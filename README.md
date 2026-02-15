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

# 3.Student Performance Analyzer
## Description

A Python program to analyze student internal assessment marks using basic programming concepts.
Each mark is processed individually to classify student performance and generate a final summary.

## Concepts Used

- List
- for loop
- Conditional statements
- String output

## Classification Rules

- 90–100 → Excellent
- 75–89 → Very Good
- 60–74 → Good
- 40–59 → Average
- 0–39 → Fai
- <0 or >100 → Invalid

## Personalization Logic

- Based on Register Number last digit
- Even digit → marks increased
- Odd digit → marks decreased
- Applied before classification to ensure unique logic

## Constraints Followed

- for loop only
- list used
- no max(), min(), sum()
- no dictionary or set
- no try-except
## Sample Testcase:
## output:
Enter total number of students: 5

Enter marks of the student 1: 95

Enter marks of the student 2: 82

Enter marks of the student 3: 67

Enter marks of the student 4: 45

Enter marks of the student 5: 30

Enter your registration numbers last digit: 4

marks after updation: [97, 84, 69, 47, 32]

 97-Excellent

 84-Very Good
 
 69-Good
 
 47-Average
 
 32-Fail
 
 Total Valid students: 5
 
 Total Failed students: 1

# Cyber Activity Risk Analyzer

This project is a Python program developed to analyze student login activity intensity scores and detect suspicious behavior.

The program processes a list of integer activity scores, categorizes them into risk levels, and applies a personalized security filter based on the last digit of the register number.

## Project Objective
- The main objectives of this project are:
- Clean invalid data
- Categorize activity scores into risk levels
- Apply a personalized filtering rule
- Generate a final security report

Each student’s output is different because it depends on the last digit of their register number.

## Risk Categorization Rules
  For each activity score:
- If score is less than 0 → Ignored (Invalid Data)
- 0 to 30 → Low Risk
- 31 to 60 → Medium Risk
- 61 to 100 → High Risk
- Greater than 100 → Critical Risk

## The program creates four separate lists:
- low_risk
- medium_risk
- high_risk
- critical_risk

## Personalized Security Filter
- Let D be the last digit of my register number.
- If D is even, all Low Risk scores are removed after categorization.
- If D is odd, all Critical Risk scores are removed after categorization.
This makes each student’s implementation unique.

## Additional Features
- Counts total valid entries
- Counts ignored entries
- Counts entries removed due to personalization
- Displays final categorized lists after filtering

## Concepts Used
- Lists
- For loop
- Conditional statements
- Basic data validation
## sample testcase output:
Enter the total number of scores:8
- enter the score of 1:10
- enter the score of 2:45
- enter the score of 3:78
- enter the score of 4:120
- enter the score of 5:-5
- enter the score of 6:30
- enter the score of 7:99
- enter the score of 8:150
- Register Digit(D): 7
- Low Risk: [10, 30]
- Medium Risk: [45]
- High Risk: [78, 99]
- Critical Risk: [120, 150]
- After personalized Filtering:
- Low Risk: [10, 30]
- Medium Risk: [45]
- High Risk: [78, 99]
- Critical Risk: []
- Total valid entries: 7
- Ignored Entries: 1
- Removed Due to Personalization: 2

