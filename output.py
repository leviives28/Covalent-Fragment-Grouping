# A dict of the plate formats available
plates = {
    96: {"rows": ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'), "cols": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)},
    384: {"rows": ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'), "cols": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)},
}

# A function to sort the groups into their wells
def sort_outputs (groups: list, location: int, format: int, ordering: str) -> list:
    """
        Returns groups with update group members -> their well locations

        @groups: The sorted groups returned from the optimize function
        @location: The location of the first receiver plate, defined by user input
        @format: The format of the well plate (96 or 384), defined by user input
        @ordering: The ordering (h or v) in which to place groups in plate wells, defined by user input.
    """
    plateNumber = location
    colPosition = 0
    rowPosition = 0
    
    for group in groups:
        col = plates[format]["cols"][colPosition]
        row = plates[format]["rows"][rowPosition]
        for member in group:
            member.append(plateNumber)
            member.append(row)
            member.append(col)
        if (ordering == "v"):
            rowPosition += 1
            if rowPosition == len(plates[format]["rows"]):
                rowPosition = 0
                colPosition += 1
            if colPosition == len(plates[format]["cols"]):
                colPosition = 0
                plateNumber += 1
        else:
            colPosition += 1
            if colPosition == len(plates[format]["cols"]):
                colPosition = 0
                rowPosition += 1
            if rowPosition == len(plates[format]["rows"]):
                rowPosition = 0
                plateNumber += 1
            
    return groups