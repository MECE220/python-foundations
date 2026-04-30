# day8.py
import pandas as pd    # pd is the standard alias — everyone uses pd
import numpy as np     # np is the standard alias for numpy

print("pandas version:", pd.__version__)
print("numpy version:", np.__version__)

# Creating a DataFrame from a dictionary
data = {
    "name":   ["Reiko", "Maria", "Pedro", "Juan", "Ana"],
    "age":    [25, 23, 22, 24, 26],
    "score":  [88, 95, 72, 65, 91],
    "passed": [True, True, True, False, True],
    "city":   ["Manila", "Cebu", "Manila", "Davao", "Manila"]
}

df = pd.DataFrame(data)
print(df)

# Essential DataFrame exploration commands
print("\n--- Shape ---")
print(df.shape)     # (rows, columns)

print("\n--- Column names ---")
print(df.columns.tolist())

print("\n--- Data types ---")
print(df.dtypes)

print("\n--- First 3 rows ---")
print(df.head(3))

print("\n--- Last 2 rows ---")
print(df.tail(2))

print("\n--- Quick statistics ---")
print(df.describe())    # count, mean, min, max automatically

# SELECTING COLUMNS
print("\n--- Single column ---")
print(df["name"])   # returns a Series (one column)

print("\n--- Multiple columns ---")
print(df[["name", "score"]])    # returns a DataFrame (use double brackets)

# FILTERING ROWS - like SQL WHERE clause
print("\n--- Students who passed ---")
print(df[df["passed"] == True])

print("\n--- Score above 80 ---")
print(df[df["score"] > 80])

print("\n--- From Manila AND score > 80 ---")
print(df[(df["city"] == "Manila") & ( df["score"] > 80)])

print("\n--- From Manila OR Cebu ---")
print(df[(df["city"] == "Manila") | (df["city"] == "Cebu")])

# SELECTING SPECIFIC ROWS AND COLUMNS
print("\n--- Row 0, all columns ---")
print(df.iloc[0])   # iloc = by position number

print("\n--- Rows 1-3, name and score only ---")
print(df.iloc[1:3][["name", "score"]])

# ADDING A NEW COLUMN
df["grade"] = df["score"].apply(lambda x:
    "A" if x >= 90 else
    "B" if x >= 80 else
    "C" if x >= 70 else
    "D" if x >= 60 else "F"
)
print("\n--- With grade column ---")
print(df)

# MODIFYING VALUES
df["score"] = df["score"] + 2    # give everyone 2 bonus points
print("\n--- After bonus points ---")
print(df[["name", "score"]])

# HANDLING MISSING DATA — critical in real datasets
data_with_nulls = {
    "name":  ["Reiko", "Maria", "Pedro", None],
    "score": [88, None, 72, 65],
    "city":  ["Manila", "Cebu", None, "Davao"]
}
df2 = pd.DataFrame(data_with_nulls)
print("\n--- Data with missing values ---")
print(df2)

print("\n--- Check missing values ---")
print(df2.isnull().sum())        # count nulls per column

print("\n--- Drop rows with any null ---")
print(df2.dropna())

print("\n--- Fill nulls with a value ---")
print(df2.fillna({"score": 0, "name": "Unknown", "city": "Unknown"}))

# GROUP BY — summarize data by category
print("\n--- Average score by city ---")
print(df.groupby("city")["score"].mean())

print("\n--- Count students per city ---")
print(df.groupby("city")["name"].count())

print("\n--- Multiple aggregations ---")
print(df.groupby("city")["score"].agg(["mean", "min", "max", "count"]))

print("\n--- Pass rate by city ---")
pass_rate = df.groupby("city")["passed"].mean() * 100
print(pass_rate.round(1))

# SORTING
print("\n--- Sort by score descending ---")
print(df.sort_values("score", ascending=False))

print("\n--- Top 3 scorers ---")
print(df.sort_values("score", ascending=False).head(3))

# Save your DataFrame to CSV
df.to_csv("students.csv", index=False)
print("\n--- Saved to students.csv ---")

# Read it back
df_loaded = pd.read_csv("students.csv")
print("\n--- Loaded from CSV ---")
print(df_loaded)
print(f"\nLoaded {len(df_loaded)} rows and {len(df_loaded.columns)} columns")

# Real-world workflow — always do this first on any new dataset
print("\n=== FIRST LOOK AT ANY DATASET ===")
print("Shape:", df_loaded.shape)
print("Columns:", df_loaded.columns.tolist())
print("Missing values:\n", df_loaded.isnull().sum())
print("Sample:\n", df_loaded.head())
print("Stats:\n", df_loaded.describe())

# 1. Show only students from Davao
print(df[df["city"] == "Davao"])

# 2. Show students with score between 70 and 90
print(df[(df["score"] >= 70) & (df["score"] <= 90)])

# 3. Show only the name and score of students who failed
print(df[df["passed"] == False][["name", "score"]])

# 4. Show students NOT from Manila
print(df[df["city"] != "Manila"])