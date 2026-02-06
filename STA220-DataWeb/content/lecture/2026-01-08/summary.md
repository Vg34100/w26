# STA220 DATA WEB - Preparing Canvas Data Files

## Action Items

- Download the lecture solutions once they’re uploaded
- Review examples of loc vs iloc indexing in pandas
- Practice subsetting a DataFrame using boolean masks, slices, and column names
- Try resetting the index on a DataFrame and observe the new column created
- Experiment with reading and writing CSV files using different file modes (r, w, a, r+) and the with statement

## DataFrame Subsetting

- Use square brackets for simple column selection, but beware of key errors
- df\['col'\] returns a Series; df\[\['col1','col2'\]\] returns a DataFrame
- Boolean mask (df\[mask\]) filters rows based on condition (e.g., scores &gt; 95)
- Slice syntax (df\[start:stop\]) selects a range of rows
- loc works with label‑based indexing, iloc works with integer positions

## Indexing with loc and iloc

- df.loc\[row_label, col_label\] accesses by explicit index/column names
- df.iloc\[row_pos, col_pos\] accesses by numeric position (0‑based)
- Example: first row, first column → df.iloc\[0,0\] returns 90 % score
- Mixing label and position in the same call raises errors

## Data Types and dtypes

- type() is Python’s built‑in function, returns the object’s class
- df.dtypes shows each column’s data type (int, float, object)
- Columns like “total points” and “homework” are integers in the example
- Warning messages appear when pandas tries to cast incompatible types

## Handling Null / Missing Values

- df.isnull() identifies NaNs; df.notnull() does the opposite
- Summing df.isnull().sum() gives count of missing values per column
- Use df.dropna() to remove rows with any nulls, or df.fillna(value) to replace them
- Resetting the index after dropping rows creates a fresh sequential index

## Reading and Writing Files

- pd.read_csv('file.csv') loads a CSV into a DataFrame
- File modes:
  - r – read (default)
  - w – write, truncates existing file
  - a – append
  - r+ – read/write without truncating
- Always close files; best practice is using with open(...) as f:

## Context Managers for File I/O

- with open('path', mode) as f: automatically closes the file after block
- Prevents resource leaks, especially with large datasets
- Can be combined with pandas I/O functions for safer handling

## Miscellaneous Tips

- Reset index with df.reset_index(drop=True) to drop the old index column
- Multiplying two Series aligns on index; mismatched indices produce NaNs
- Changing index to a column (set_index) can simplify grouping operations
- Use df.describe() for quick statistical summary (mean, std, quantiles)
