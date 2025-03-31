def display_totals(title, data):
    """Display totals in the console."""
    print(title)
    for ttls in data:
        print(ttls + ":      $" + str(round(data[ttls], 2)))
    print()