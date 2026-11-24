
print("====== Currency Converter =====")

rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90
}

while True:
    print("\nAvailable currencies:")
    print("1. INR - Indian Rupee")
    print("2. USD - US Dollar")
    print("3. EUR - Euro")
    

    choice = input("Enter your choice: ")


    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    currency_list = ["INR", "USD", "EUR"]
    from_currency = currency_list[int(choice)-1]

    to_choice = input("Convert into which currency? (1-3): ")

    if to_choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    to_currency = currency_list[int(to_choice)-1]

    if from_currency == to_currency:
        print("Please select two different currencies.")
        continue

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        amount_inr = amount * rates[from_currency]
        result = amount_inr / rates[to_currency]

        print("\n==== Conversion Result ====")
        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

    except ValueError:
        print("Please enter a valid number.")
