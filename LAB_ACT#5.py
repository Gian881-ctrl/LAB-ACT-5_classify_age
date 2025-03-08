def classify_age(age):
    if age < 0:
        print("Boss, bawal yan.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    elif age >= 64:
        print("You are senior.")