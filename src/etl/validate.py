import pandas as pd

def validate_dataframe(df: pd.DataFrame, table_name: str) -> bool:
    """
    Validate the Dataframe before transformation.
    Returns True if validation passes, otherwise False.
    """

    print(f"\n Validating {table_name}...")

    # Check if Dataframe is empty
    if df.empty:
        print("Dataframe is empty.")
        return False
    
    duplicate_count = df.duplicated().sum()

    if duplicate_count  > 0:
        print(f"Duplicate records found: {duplicate_count}")
    else:
        print("No duplicate records found.")
    
    missing_values = df.isnull().sum()

    print("\n Missing values:")
    print(missing_values)

    print("\n Validation completed successfully.")

    return True