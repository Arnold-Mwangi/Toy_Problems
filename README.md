# Toy_Problems



## Code Challenges

This repository contains solutions for three code challenges written in Python. Each challenge focuses on different programming concepts and problem-solving techniques.

### Challenge 1: Converting 12-hour Time to 24-hour Time

#### Problem Statement
Given a time in the 12-hour format (hh:mm am/pm), create a function that converts it into the 24-hour format (hhmm hrs).

#### Solution
The `convert_to_24_hour_time` function takes a time input in the 12-hour format and converts it into the 24-hour format. It splits the input into hours, minutes, and the period (am/pm), and then applies the necessary transformations based on the period.

### Challenge 2: Determining Positive Integers

#### Problem Statement
Write a function that takes three integers as input and returns `True` if exactly two out of the three numbers are positive; otherwise, it returns `False`.

#### Solution
The `positive_checker` function checks if exactly two out of the three provided integers are positive. It calculates the number of positive integers and compares it with the value 2 to determine if the condition is met.

### Challenge 3: Calculating Consonant Value

#### Problem Statement
Create a function that takes a string as input and calculates the highest value of a substring containing only consonant characters. Each consonant has a corresponding value (a=1, b=2, ..., z=26).

#### Solution
The `highest_consonant_string` function calculates the value of each substring composed of consonant characters, then returns the highest value among them.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the appropriate challenge directory.
3. Run the Python script corresponding to the challenge (e.g., `challenge1.py` for Challenge 1).
4. Follow the prompt to input the required data.
5. The script will display the output based on the input provided.

Feel free to explore the code for each challenge, modify it as needed, and experiment with different inputs.

## Note

These solutions were developed as part of a coding exercise and may not cover all edge cases. They serve as examples of how to approach the given problems and may require further testing and refinement for production use.
