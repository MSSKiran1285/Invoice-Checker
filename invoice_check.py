import pandas as pd

# Step 1: Load the Excel files
invoice1 = pd.read_excel('invoice1.xlsx')
invoice2 = pd.read_excel('invoice2.xlsx')
master = pd.read_excel('master_data.xlsx')

# Step 2: Concatenate the two invoice dataframes for a combined comparison
invoices = pd.concat([invoice1, invoice2], ignore_index=True)

# Step 3: Set the key column that is common to all files
key_column = 'Item'

# Step 4: Merge the invoices with the master data on the common key.
merged = pd.merge(invoices, master, on=key_column, suffixes=('_invoice', '_master'), how='left')

# Step 5: Identify discrepancies

# a) Find records missing in master data (NaN in any master columns)
missing_master = merged[merged.filter(like='_master').isna().any(axis=1)]

# b) Compare all common columns (except the key column)
# Identify columns present in both invoice and master (without suffix)
invoice_columns = set(invoices.columns) - {key_column}
master_columns = set(master.columns) - {key_column}
common_columns = invoice_columns.intersection(master_columns)

# Initialize a DataFrame to store all discrepancies
discrepancies = pd.DataFrame()

# Iterate over each common column to check for mismatches
for col in common_columns:
    invoice_col = col + '_invoice'
    master_col = col + '_master'
    
    if invoice_col in merged.columns and master_col in merged.columns:
        mismatch = merged[merged[invoice_col] != merged[master_col]]
        if not mismatch.empty:
            # Add a column to indicate which column has a mismatch
            mismatch = mismatch.copy()
            mismatch['Mismatch Column'] = col
            discrepancies = pd.concat([discrepancies, mismatch], ignore_index=True)

# Combine the missing master records and any column mismatches
all_discrepancies = pd.concat([missing_master, discrepancies]).drop_duplicates()

# Step 6: Write the discrepancies to an Excel file.
output_filename = 'discrepancies_all_columns.xlsx'
all_discrepancies.to_excel(output_filename, index=False)

print(f"Discrepancy check completed. Results saved to {output_filename}")