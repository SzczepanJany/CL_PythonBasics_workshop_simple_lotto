def ask_for_a_numbers_set():
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
                if given_number < 1 or given_number > 49:
                    print("Number out of scope (1-49)")
                elif given_number in numbers_set:
                    print("Number already entered!")
                else:
                    numbers_set.append(given_number)
                    break
            except ValueError: 
                print("Input is not a number")

    return numbers_set


print(ask_for_a_numbers_set())
