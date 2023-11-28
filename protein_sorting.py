# Sort groups into rows, adding the mass of the protein to each group items exact mass
def sort_protein_totals (fragment_groups: list, protein_mass: float, exact_mass_column: int, group_size: int, id_column: int) -> list:
    """
        Return a list of the groups, where each groups item has the proteins mass added to its exact mass

        @fragment_groups: the list of lists of the sorted covalent fragment groups
        @protein_mass: the value of the proteins mass
        @exact_mass_column: the column in which the exact mass resides
        @group_size: the defined size of each group
        @id_column: the column in which the fragments id resides
    """
    group_count = 1
    protein_groups = [[]]

    # Set the datasets headers
    protein_groups[0].append('Group')
    for count in range(1, group_size+1):
        protein_groups[0].append('C' + str(count))
    for count in range(1, group_size+1):
        protein_groups[0].append('P+C' + str(count))
    protein_groups[0].append('Protein Mass')

    # Loop through each of the groups
    for group in fragment_groups:
        protein_group_row = []
        protein_group_row.append(group_count)
        # Try and add the value of each group item to the list, if there is not an existing item at the specified index, then add an empty field
        for index in range(group_size):
            try:
                protein_group_row.append(group[index][id_column])
            except:
                protein_group_row.append('')
        # Try and add the value of each group item to the list, if there is not an existing item at the specified index, then add an empty field
        for index in range(group_size):
            try:
                protein_group_row.append((group[index][exact_mass_column] + protein_mass))
            except:
                protein_group_row.append('')
        protein_group_row.append(protein_mass)
        protein_groups.append(protein_group_row)
        group_count += 1
    # Return the completed list of groups
    return protein_groups
