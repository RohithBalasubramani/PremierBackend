import pandas as pd

def get_unique_prefixes(excel_file, sheet_name=0, column_index=1):
    """
    Reads an Excel file and extracts unique prefixes from a specified column.
    
    Args:
        excel_file (str): Path to the Excel file.
        sheet_name (str or int, optional): Name or index of the sheet to read. Defaults to first sheet.
        column_index (int, optional): Zero-based index of the column to process. Defaults to 1 (second column).
    
    Returns:
        set: A set of unique prefixes.
    """
    try:
        # Read the Excel file, treating all data as strings to avoid type issues
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, dtype=str)
        print(f"Excel file '{excel_file}' read successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{excel_file}' was not found.")
        return set()
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return set()
    
    print(f"Sheet: {sheet_name}, Shape: {df.shape}")
    
    # Check if the specified column exists
    if column_index >= df.shape[1]:
        print(f"Error: Column index {column_index} is out of bounds for the Excel file with {df.shape[1]} columns.")
        return set()
    
    # Extract the specified column
    column_data = df.iloc[:, column_index]
    
    # Debugging: print type and first few entries
    print(f"column_data type: {type(column_data)}")
    print(f"First 5 entries in column {column_index + 1}:")
    print(column_data.head())
    
    unique_prefixes = set()
    
    # Use 'items()' instead of 'iteritems()'
    for index, field in column_data.items():
        if pd.isna(field):
            print(f"Row {index + 1}: Field name is missing (NaN). Skipping.")
            continue
        
        field = field.strip()
        
        if '_' in field:
            # Split by the last underscore to separate prefix and suffix
            prefix, _ = field.rsplit('_', 1)
            prefix = prefix.strip()
            unique_prefixes.add(prefix)
        else:
            print(f"Row {index + 1}: Cannot parse prefix from field '{field}'. Skipping.")
    
    return unique_prefixes

def main():
    excel_file = 'OPCtest2.xlsx'  # Replace with your actual Excel file path
    sheet_name = "NS16"  # Replace with your sheet name or index if different
    column_index = 1  # Zero-based index for the second column
    
    unique_prefixes = get_unique_prefixes(excel_file, sheet_name, column_index)
    
    if unique_prefixes:
        
        print("\n=== Unique Prefixes Found ===")
        with open("prefixfile.py", "w") as f:
            f.write("tag_model_mapping = {\n")
            for prefix in sorted(unique_prefixes):
                print(prefix)
                f.write(f'    "{prefix}": ,\n')
    else:
        print("No unique prefixes found.")

if __name__ == "__main__":
    main()
