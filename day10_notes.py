# day10_notes.py
# SQL Cheat Sheet — Day 10

sql_commands = {
    "SELECT":   "Read data from a table",
    "FROM":     "Which table to read from",
    "WHERE":    "Filter rows by condition",
    "JOIN":     "Combine two tables",
    "GROUP BY": "Group rows and aggregate",
    "ORDER BY": "Sort results",
    "HAVING":   "Filter after grouping",
    "INSERT":   "Add new rows",
    "CREATE":   "Make a new table",
    "LIMIT":    "Restrict number of rows returned"
}

print("=== SQL COMMAND REFERENCE ===")
for command, description in sql_commands.items():
    print(f"  {command:<12} → {description}")

# SQL vs pandas equivalents
print("\n=== SQL vs PANDAS ===")
equivalents = [
    ("SELECT * FROM table",          "df"),
    ("SELECT col FROM table",        "df['col']"),
    ("WHERE col = value",            "df[df['col'] == value]"),
    ("ORDER BY col DESC",            "df.sort_values('col', ascending=False)"),
    ("GROUP BY col",                 "df.groupby('col')"),
    ("COUNT(*)",                     "len(df)"),
    ("AVG(col)",                     "df['col'].mean()"),
    ("JOIN",                         "pd.merge(df1, df2)"),
]

for sql, pandas in equivalents:
    print(f"  SQL   : {sql}")
    print(f"  pandas: {pandas}")
    print()