import csv

def write_csv(filename, header1, header2, data):
    """Write data to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([header1, header2])
        for ttls in data:
            writer.writerow([ttls, round(data[ttls], 2)])