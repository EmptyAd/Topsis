# Topsis Method Implementation

This repository contains a Python implementation of the Topsis method, a popular multi-criteria decision-making technique. This implementation reads data from an Excel file, processes it, and outputs the results to a CSV file.

#Usage
1. Create an Excel file with your data. The first column should be the names of the items (like fund names), and the next columns should have the criteria values.
2. Run the script from the command line:
   ```bash
   python "102203269.py <InputDataFile> <Weights> <Impacts> <ResultFileName>"
   ```
   Example Command
   ```bash
   python 102203269.py data.xlsx "0.3,0.4,0.3,0.2,0.6" "+,+,-,+,-" results.csv
   ```

#Output
The result will be stored in the result.csv file

