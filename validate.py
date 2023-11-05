# A function to validate the optimization of the groups
def validate(file: dict, result_groups: list, group_size: int, exact_mass_column: int, minimum_difference: float) -> bool:
    """
        Returns true or false dependent on the success of the grouping

        @file: This should be the dictionary containing the input files initial data (stored in key: table_data)
        @result_groups: This is the sorted groups returned from the optimize function. A list of lists (groups) of lists (group members)
        @group_size: The maximum size of groups, defined by user input
        @exact_mass_column: The 0 indexed column of the input file in which exact_mass exists, defined by user input
        @minimum_difference: The minimum difference between each member in a group, defined by user input
    """
    count = 0
    status = True
    for group in result_groups:
        for item in group:
            count += 1
        if len(group) > group_size:
            status = False
            return status
        for index in range(1, len(group)):
            if abs(group[index][exact_mass_column] - group[index - 1][exact_mass_column]) < minimum_difference:
                status = False
                return status
    if (count != len(file["table_data"])):
        status = False
        return status
    return status