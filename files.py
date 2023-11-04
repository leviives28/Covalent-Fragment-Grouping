import csv
import inputs

# Function to read the given file
def read_and_sort_file (file: str, column: int) -> dict:
    """
        Returns an object with column_names and table_data keys,
        derived from the provided csv file.

        @file: Path to the csv file containing the values
        @column: The 0 indexed integer value of the column in the file the groups are to be ordered by, defined by user input
        
    """
    data = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader: data.append(row)
        tableHeaders = data[0]
        data.pop(0)
        for row in data: row[column] = float(row[column])
        data.sort(key=lambda x: x[column])
    return {"column_names": tableHeaders, "table_data": data}


# Function to save the output to a given file
def save_output (headers: list, groups: list):
    """
        Saves the headers and sorted groups into a new csv file.

        @headers: The column names to be output to the new file
        @groups: The sorted groups that are to be output to a new csv file
    """
    output_file = inputs.file_output()
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for group in groups:
            writer.writerow(' ')
            for item in group:
                writer.writerow(item) 
        writer.writerow('')

    print(f"Saving file to '{output_file}'.")


