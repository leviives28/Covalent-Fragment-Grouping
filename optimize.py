import pulp
import warnings

# The function which optimizes the values into required groupings
def optimize (file: dict, group_size: int, exact_mass_column: int, minimum_difference: float) -> list:
    """
        Returns a list of lists, ie the ordered groups

        @file: the dictionary returned from the read_and_sort_file function, containing the data from the input file in dictionary key table_data
        @group_size: The maximum size of the groups, defined by user input
        @exact_mass_column: The 0 indexed column where the exact can be found in the input file, defined by user input
        @minimum_difference: The minimum difference between each group member, defined by user input
    """

    # Avoid logging of processes
    pulp.LpSolverDefault.msg = 0
    warnings.filterwarnings("ignore", message="Overwriting previously set objective")

    # Define the ideal number of groups, based on the size of the data, and the group_size constraint
    num_groups = len(file["table_data"]) // group_size

    # Create a new problem to be solved
    problem = pulp.LpProblem("NumberGrouping", pulp.LpMaximize)

    # Create variables with the min and max weightings for each of the items in the input data, for each of the groups defined in num_groups
    variables = {(i, j): pulp.LpVariable(f'x_{i}_{j}', 0, 1, pulp.LpBinary) for i in range(len(file["table_data"])) for j in range(num_groups + 1)}

    # Repeat for each item of the input data
    for i in range(len(file["table_data"])):
        # Add to the problem, the sum of the expression, in each group
        problem += pulp.lpSum(variables[(i, j)] for j in range(num_groups + 1)) == 1

    # Repeat for num_groups times
    for j in range(num_groups):
        # Add to the proble, the sum of the expression, for each item
        problem += pulp.lpSum(variables[(i, j)] for i in range(len(file["table_data"]))) <= group_size

    # Add to the problem, the sum of the expression, for each data item in the final group
    problem += pulp.lpSum(variables[(i, num_groups)] for i in range(len(file["table_data"]))) <= group_size

    # Repeat for num_groups + 1 times
    for j in range(num_groups + 1):
        print('Solving Optimal Groups:', round((j / num_groups) * 100, 1), '%', end='\r')
        # Repeat for each item in the input data
        for i in range(len(file["table_data"])):
            # Repeat for i + 1, for each item in the input data
            for k in range(i + 1, len(file["table_data"])):
                # Add to the problem, the weighting for two items of the group, if they are less than the minimum difference, else add 1
                problem += (variables[(i, j)] + variables[(k, j)]) <= 1 if file["table_data"][k][exact_mass_column] - file["table_data"][i][exact_mass_column] < minimum_difference else 1

    print('\nSolving Solution...')
    # Continue until breaks (optimization completes, successful or not)
    while True:
        # Set the value of status to the return value of calling the solve method of the problem object
        status = problem.solve()
        # If the problem is solved, then break the loop
        if status == pulp.LpStatusOptimal:
            break
        # Otherwise, if the problem is infeasible, break the loop
        elif status == pulp.LpStatusInfeasible:
            break
        # Otherwise, if the problem is undefined, break the loop
        elif status == pulp.LpStatusUndefined:
            break

    # Predefine the results list group, based on the value of num_groups
    result_groups = [[] for _ in range(num_groups + 1)]
    # Repeat for each item in the input file data
    for i in range(len(file["table_data"])):
        # Repeat for the defined number of groups
        for j in range(num_groups + 1):
            # If the value of the pulp value is 1 (it fits the constraints), then:
            if pulp.value(variables[(i, j)]) == 1:
                # Add the current item of the input data to the current group list
                result_groups[j].append(file["table_data"][i])
    
    # Return the sorted group
    return result_groups
