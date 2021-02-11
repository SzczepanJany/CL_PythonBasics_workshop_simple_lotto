from random import shuffle

def ask_for_a_numbers_set(min_number,max_number):
    """
    Function is asking user for 6 numbers from 1 to 49 and checkig if they are unique and in scope
    """
    input_question = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
    numbers_set = []
    for i in range(6):
        while True:
            given_number = input(f"Please, input {input_question[i]} number: ")
            try:
                given_number = int(given_number)
                if given_number < min_number or given_number > max_number:
                    print("Number out of scope (1-49)")
                elif given_number in numbers_set:
                    print("Number already entered!")
                else:
                    numbers_set.append(given_number)
                    break
            except ValueError: 
                print("Input is not a number")
    result = sorted(numbers_set)
    return result

def choose_winning_numbers(min_number,max_number):
    numbers = [i for i in range(min_number,max_number)]    
    shuffle(numbers)
    rand_num = [numbers[i] for i in range(6)]
    result = sorted(rand_num)
    return result

def compare_results(user_input, computer_input):
    result = []
    for i in user_input:
        if i in computer_input:
            result.append(i)
        
    return result

min_number = 1
max_number = 49
user_in = ask_for_a_numbers_set(min_number,max_number)
print(user_in)
comp_in = choose_winning_numbers(min_number, max_number)
print(comp_in)
result = compare_results(user_in, comp_in)
if len(result) > 2:
    print(f'Yo won! You guessed {len(result)} : {result}')
else:
    print(f'Yo lost! You guessed only {len(result)} : {result}')