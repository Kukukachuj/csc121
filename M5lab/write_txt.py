def write_txt(filename, header, data):
    """Write data to a TXT file."""
    with open(filename, "w") as file:
        file.write(header + "\n")
        for ttls in data:
            file.write(ttls + "          " + str(round(data[ttls], 2)) + "\n")