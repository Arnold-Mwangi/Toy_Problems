# Challenge 1: Converting 12-hour time to 24-hour time
'''
pseudocode:
##          define a function that recives time in hours and minutes and a period (Am/pm )as input
##convert the time to 24 hour time 
Testcases
08: 30 pm : >= 2030
12: 00 am : >= 0015
12: 00 pm : >= 1200 

'''

# def convert_to_24_hour_time(time_in_hours):
#     #split time
#     splited_time = time_in_hours.split()
#     period = splited_time[1]

#     splited_mins_hrs = splited_time[0].split(":")
#     hour = int(splited_mins_hrs[0])
#     minute = int(splited_mins_hrs[1])

#     #check if its midnight/midday
#     if period.lower() == 'pm' and hour !=12:
#         hour +=12
#     elif period.lower() == 'am' and hour ==12:
#         hour = 0
#     elif period.lower() == 'am' and hour != 12:
#         hour = hour

#     #add zeros to hours and minutes if user didnt pass one
#     hour_str = str(hour).zfill(2)

#     minute_str = str(minute).zfill(2)

#     return hour_str + minute_str + "hrs"

# time_input = input("Enter time in 12-hour format (e.g.. 4:30 pm): ")
# print(f"Time in 24-hour format: {convert_to_24_hour_time(time_input)}")


# Challenge 2: Two numbers are positive.
'''

pseudocode
define a function that takes 2 arguments a,b,c
Return true if exactly two of the three integers are positive numbers
Otherwise return False

'''

# def positive_checker(a, b,c):
#     positive_numbers = (sum([1 for x in [a, b,c] if x >0]))

#     print (positive_numbers == 2)

# positive_checker(0, 2, -7)



# Challenge 3: Consonant value
'''
pseudocode: 

'''
def highest_consonant_string(str):
    vowels = "aeiou"
    consonant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
                        'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    def calculate_value(substring):
        return sum(consonant_values[char] for char in substring)
    
    consonant_substrings = [substring for substring in str.split(vowels) if substring != ""]
    
    highest_value = max(calculate_value(substring) for substring in consonant_substrings)
    
    return highest_value

# Test cases
str = input("Enter a random name: ")
print(f"{str}, {highest_consonant_string(str)}")  


