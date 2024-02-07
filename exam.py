# Initialize variables to store the largest amount and corresponding name
largest_amount = 0
largest_name = ""

while True:
    # Read user inputs
    name = input("Enter your name: ")
    amount = float(input("Enter the amount for auction: "))

    # Check if the current amount is greater than the largest_amount
    if amount > largest_amount:
        largest_amount = amount
        largest_name = name

    # Ask the user if they want to continue
    user_input = input("Do you want to continue? (yes/no): ").lower()

    # Check if the user wants to continue
    if user_input != 'yes':
        break

# Display the result
print(f"\nWinner: {largest_name}")
print(f"Winning Amount: {largest_amount}")
