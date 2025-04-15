import store_fun as fn

def menu():
    """
    function displays menu options

    Returns
    -------
    None.

    """
    print("1) Calculate Cost")
    print("2) Exit")

def main():
    print("\nIMPORTANT How cost is calculated:\n")
    print("Each item in the store costs $1 dollar")
    print("Customer buying 10 or more items receives 5% discount")
    print("Customer LESS than 10 items, receives 0 discount")
    print("6.2% sales tax is applied")

    choice = 0
    while choice != 2:
        # call menu function
        menu()

        # enter choice
        try:
            choice = int(input("\nEnter Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # evaluate what user entered
        if choice == 1:
            # get input
            try:
                count = int(input("Enter number of items: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            # calculate cost, tax rate, and tax
            cost = fn.calcCost(count)
            taxRate = .062
            tax = cost * taxRate

            # display results
            print(f"Cost: ${cost:.2f}, Tax: ${tax:.2f}, Total: ${cost + tax:.2f}")
        elif choice == 2:  # exit
            print("\nProgram Terminating....")
        else:
            print("Invalid Entry!!!!\n")

if __name__ == "__main__":
    main()