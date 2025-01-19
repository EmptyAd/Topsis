import pandas as pd
import numpy as np
import sys

# Function to check input validity
def check_inputs(input_file, weights, impacts):
    try:
        df = pd.read_excel(input_file)  
        if df.shape[1] < 3:
            raise ValueError("Your file must have at least three columns.")
        
        if not all(df.iloc[:, 1:].applymap(np.isreal).all()):
            raise ValueError("There are non-numeric values in the data.")
        
        if len(weights) != df.shape[1] - 1:
            raise ValueError("The number of weights must match the number of criteria.")
        
        if len(impacts) != df.shape[1] - 1:
            raise ValueError("The number of impacts must match the number of criteria.")
        
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts can only be '+' or '-'.")
        
        return df
    
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Topsis
def topsis(input_file, weights, impacts, result_file):
    df = check_inputs(input_file, weights, impacts)  
    data = df.iloc[:, 1:].values.astype(float) 
    
    norm_data = data / np.sqrt((data**2).sum(axis=0))
    
    weights_array = np.array(weights)
    weighted_data = norm_data * weights_array
    
    pos_ideal = np.array([
        np.max(weighted_data[:, i]) if impacts[i] == '+' else np.min(weighted_data[:, i]) 
        for i in range(weighted_data.shape[1])
    ])

    neg_ideal = np.array([
        np.min(weighted_data[:, i]) if impacts[i] == '+' else np.max(weighted_data[:, i]) 
        for i in range(weighted_data.shape[1])
    ])
    

    pos_distance = np.sqrt(((weighted_data - pos_ideal) ** 2).sum(axis=1))
    neg_distance = np.sqrt(((weighted_data - neg_ideal) ** 2).sum(axis=1))
    
    scores = neg_distance / (neg_distance + pos_distance)
    
    df['Topsis Score'] = scores
    df['Rank'] = scores.argsort()[::-1] + 1  

    
    df.to_csv(result_file, index=False)
    print(f"Results saved to {result_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
    
    input_file = sys.argv[1]  
    weights = list(map(float, sys.argv[2].strip('[]"').split(',')))  
    impacts = sys.argv[3].strip('[]"').split(',')  
    result_file = sys.argv[4] 
    
    topsis(input_file, weights, impacts, result_file)  
