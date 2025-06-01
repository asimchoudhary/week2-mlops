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
    os.makedirs('part1',exist_ok=True)
    os.makedirs('part2',exist_ok=True)
    directory = os.path.dirname(input_csv)

    iris_1.to_csv("part1/iris.csv", index=False)
    iris_2.to_csv("part2/iris.csv", index=False)
    print(f"Saved {iris_1_path} and {iris_2_path}")

if __name__ == "__main__":
    split_iris_csv('iris.csv')
