import csv
from write_csv import write_csv  # Import write_csv from write_csv.py
from write_txt import write_txt  # Import write_txt from write_txt.py
from display_totals import display_totals  # Import display_totals from display_totals.py

# Initialize dictionaries
products = {}
customers = {}

# Function to process each row in the sales.csv file
def process_sales_row(row):
    customerID = row[3]  # Customer ID
    productID = row[2]  # Product ID
    units = int(row[4])  # Units sold
    price = float(row[5])  # Price per unit
    totalSales = units * price  # Calculate total sales for the row

    # Update the total sales for the product
    if productID in products:
        products[productID] += totalSales
    else:
        products[productID] = totalSales

    # Update the total sales for the customer
    if customerID in customers:
        customers[customerID] += totalSales
    else:
        customers[customerID] = totalSales

# Main function to read the CSV file and process the data
def main():
    # Open the sales.csv file and process rows
    with open("M5lab/sales.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            process_sales_row(row)

    # Display and write total sales by product
    display_totals("Total Sales by Product ID", products)
    write_csv("M5lab/ProgramOutput/total_sales.csv", "Product ID", "Total Sales", products)
    write_txt("M5lab/ProgramOutput/total_sales.txt", "Product ID Total Sales", products)

    # Display and write total sales by customer
    display_totals("Total Sales by Customer ID", customers)
    write_csv("M5lab/ProgramOutput/customer_sales.csv", "Customer ID", "Total Sales", customers)
    write_txt("M5lab/ProgramOutput/customer_sales.txt", "Customer ID Total Sales", customers)


# Call the main function
if __name__ == "__main__":
    main()