
while True:
    age_input = input("Enter your age (1-120): ")

    if not age_input.strip():
        print("Empty input not allowed")
        continue

    try:
        age = int(age_input)
        if 1 <= age <= 120:
            print(f"You enterd a valid age : {age}")
            break;
        else:
            print("Out of range. Plese enter a number between 1 and 120")

    except ValueError:
        print("Invalid input. Please enter a valid number")


    





# def type_validate(age_input):
#     try:
#         int(age_input)
#         return True
#     except Exception as e:
#         return False

# def range_validate(age_input):
#     age = int(age_input)
#     if age >= 1 and age <= 120:
#         return True
#     else:
#         return False
    
# def empty_input(age_input):
#     if age_input:
#         return True
#     else:
#         return False
