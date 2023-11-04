# Ask for the file and verify it is a csv file
def file_input () -> str:
    """ 
        Returns the input file path, defined by user input
    """
    input_file_temp = ""
    input_file = ""
    while not (input_file_temp[-4:] == '.csv'):
        input_file = input("Enter the location and name of the input CSV file: ")
        input_file_temp = input_file
    return input_file

# Ask for the name of the output file
def file_output () -> str:
    """
        Returns the output file path, defined by user input
    """
    output_file = input("Enter the desired location and name of the CSV output file: ")
    output_file_temp = output_file
    if output_file_temp[-4:] != '.csv':
        output_file += '.csv'
    return output_file


# Ask for the receiver plate location and verify it is a number
def receiver_plate_location_input () -> int:
    """
        Returns the location of the receiver plate, defined by user input
    """
    receiver_plate_location = ""
    while not isinstance(receiver_plate_location, int):
        try:
            receiver_plate_location = int(input("Please enter the receiver plate location (number): "))
        except ValueError:
            print("Invalid input. Please enter an integer")
            print()
    return receiver_plate_location


# Ask for the receive plate format (number of wells)
def receiver_plate_format_input () -> int:
    """
        Returns the format of the receiver plate (96 or 384), defined by user input
    """
    receiver_plate_format = ""
    while not (receiver_plate_format == 96 or receiver_plate_format == 384):
        try:
            receiver_plate_format = int(input("What is the format of the receiver plate? (96 or 384): "))
        except ValueError:
            print("Invalid input. Please enter either 96, or 384")
            print()
    return receiver_plate_format


# Ask for the ordering of groups within the plate
def ordering_input () -> str:
    """
        Returns the ordering within the plates (horizontal or vertical), defined by user input
    """
    ordering = ""
    while not (ordering == "h" or ordering == "v"):
        ordering = input("Are groups to be ordered horizontically or vertically in the plate? (h or v): ")
    return ordering


# Ask for the size of groups within each well
def group_size_input () -> int:
    """
        Returns the maximum size of each group, defined by user input
    """
    group_size = ""
    while not isinstance(group_size, int):
        try:
            group_size = int(input("What should be the maximum size of each group? (number): "))
        except ValueError:
            print("Invalid input. Please enter a whole number")
            print()
    return group_size


# Ask for the minimum difference required between each groups elements exact mass
def minimum_difference_input () -> float:
    """
        Returns the minimum difference between each group member, defined by user input
    """
    minimum_difference = ""
    while not isinstance(minimum_difference, float):
        try:
            minimum_difference = float(input("What should be the minimum difference between each group members exact mass? (number - decimal or integer): "))
        except ValueError:
            print("Invalid input. Please enter either an integer or a decimal")
            print()
    return minimum_difference


# Ask which column the exact mass is in, in the input file
def exact_mass_column_input () -> int:
    """
        Returns the 0 indexed column in which the exact mass is found, defined by user input
    """
    exact_mass_column = ""
    while not (isinstance(exact_mass_column, int)):
        try:
            exact_mass_column = int(input("In which column of the input file is the exact mass? (number (0 indexed)): "))
        except ValueError:
            print("Invalid input. Please enter a whole number")
            print()
    return exact_mass_column

