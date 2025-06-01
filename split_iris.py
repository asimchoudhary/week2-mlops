import pandas as pd
import os

def split_iris_csv(input_csv='iris.csv'):
    # Read the iris csv file
    df = pd.read_csv(input_csv)
    # Calculate the midpoint
    mid = len(df) // 2
    # Split the data into two parts
    iris_1 = df.iloc[:mid]
    iris_2 = df.iloc[mid:]
    # Get directory and filename
    directory = os.path.dirname(input_csv)
    iris_1_path = os.path.join(directory, 'iris-1.csv')
    iris_2_path = os.path.join(directory, 'iris-2.csv')
    # Save the two parts
    iris_1.to_csv(iris_1_path, index=False)
    iris_2.to_csv(iris_2_path, index=False)
    print(f"Saved {iris_1_path} and {iris_2_path}")

if __name__ == "__main__":
    split_iris_csv('iris.csv')