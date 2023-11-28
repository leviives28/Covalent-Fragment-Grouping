import inputs
import files
import output
import optimize
import validate
import protein_sorting

# Call input functions and save their return values into relevant variables
input_file = inputs.file_input()
receiver_plate_location = inputs.receiver_plate_location_input()
receiver_plate_format = inputs.receiver_plate_format_input()
ordering = inputs.ordering_input()
group_size = inputs.group_size_input()
minimum_difference = inputs.minimum_difference_input()  
exact_mass_column = inputs.exact_mass_column_input()
protein_mass = inputs.protein_mass_input()
fragment_id_column = inputs.fragment_id_column_input()

# Call the read and sort file function and save its return value to the file variable
file = files.read_and_sort_file(input_file, exact_mass_column)

# Call the optimize function and save its return value to the result_groups variable
result_groups = optimize.optimize(file, group_size, exact_mass_column, minimum_difference)

# Call the validate function and save its return value to the status variable
status = validate.validate(file, result_groups, group_size, exact_mass_column, minimum_difference)

# Conditional statement to check if validation status is true (successful) or false (failed)
if not status:
    print('Optimization failed. Please check the data and alter constraints where possible')
else:
    print('Optimization successful')
    # Reorder groups from largest to smallets
    result_groups.sort(key=len, reverse=True)

    # Call the sort outputs function and save the return value to the well_outputs variable
    well_outputs = output.sort_outputs(result_groups, receiver_plate_location, receiver_plate_format, ordering)

    # Sort the protein total for each group item
    sorted_protein_values = protein_sorting.sort_protein_totals(well_outputs, protein_mass, exact_mass_column, group_size, fragment_id_column)
    
    # Add the output columns to the dict key column_names
    file["column_names"] += ["Output Well Plate", "Output Row", "Output Column"]

    # Call the save output function
    files.save_output(file["column_names"], well_outputs, sorted_protein_values)
