
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
