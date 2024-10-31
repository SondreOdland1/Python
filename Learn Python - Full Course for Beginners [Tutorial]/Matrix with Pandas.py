import pandas as pd

matrix = [
    [1, 2, 4],
    [2, 4, 5],
    [1, 4, 7]
]

df = pd.DataFrame(matrix)

print(df.head())

print(matrix[1])