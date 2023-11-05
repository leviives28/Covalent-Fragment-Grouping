# Covalent-Fragment-Grouping


## Description
Program was created for sorting covalent fragments in to groups based on their exact mass.

The program takes a set of data, in the form of a csv file, and sorts it into groups based on a predefined column, minimum difference between that column of each group item, and maximum group size, using the pulp library.

Once the data is optimized, then each group value is updated with a plate well location, based on further inputs provided by the user, such as plate format, ordering, starting plate etc.

The output is then saved to a csv file defined by the user.


## Getting Started
### To get started using this project, clone or download the repo onto your machine;

```
git clone https://github.com/leviives28/Covalent-Fragment-Grouping/
```


## Running the App

### Navigate to the location of the downloaded program files
```
python3 .\main.py
```

### Then you will be asked for inputs to define the file, group size, exact mass column, minimum difference, plate format, ordering etc.

```
Enter the location and name of the input CSV file: Covalent_Fragments.csv
Please enter the receiver plate location (number): 1
What is the format of the receiver plate? (96 or 384): 384
Are groups to be ordered horizontically or vertically in the plate? (h or v): v
What should be the maximum size of each group? (number): 5
What should be the minimum difference between each group members exact mass? (number - decimal or integer): 5
In which column of the input file is the exact mass? (number (0 indexed)): 4
```

### The program will attempt to optimize the data into groups based on the defined constraints, and then will ask for the path+name of the output file.

```
Enter the desired location and name of the CSV output file: Covalent_Fragments_Output.csv
```

### Repository includes sample data and output for running the program with above inputs

#### Input sample data
```
Covalent_Fragments.csv
```

#### Output sample data
```
Covalent_Fragments_Outputs.csv
```

## Status

This repository has been archived and is now read-only.
