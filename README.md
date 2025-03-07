Below is a step-by-step summary of what I did so that other users can follow along:

Developed the Python Script:

I imported the necessary libraries (pandas and openpyxl).
I loaded the two invoice Excel files and the master data file using pd.read_excel().
I concatenated the invoice files into one DataFrame to simplify the comparison.
I merged the combined invoice data with the master data using a common key (e.g., "Item ID") via a left join.
I wrote logic to detect discrepancies:
Missing Records: Identified rows where master data was missing (NaN values).
Mismatches: Compared common columns (like Price, Quantity, etc.) between the invoices and the master data.
I combined all discrepancy results and exported them to a new Excel file using to_excel().
Set Up a GitHub Account and Repository:

I visited GitHub and created a new account.
I created a new repository (named, for example, invoice-discrepancy-check) on GitHub.
I cloned the repository to my local machine using the repository URL.
Installed Python and Set Up the Local Environment:

I downloaded and installed Python from the official Python website, making sure to add Python to my system's PATH.
I verified the installation by running python --version in my command prompt or terminal.
I navigated to my cloned repository folder.
I set up a virtual environment (using python -m venv env) and activated it.
I installed the required libraries (pandas and openpyxl) via pip.
Integrated and Ran the Code:

I created a Python file (e.g., invoice_check.py) within the repository and pasted the code into it.
I placed the necessary Excel files (invoice1.xlsx, invoice2.xlsx, master_data.xlsx) in the appropriate folder or updated the file paths accordingly in the script.
I ran the script locally to ensure that it executed correctly and generated the discrepancies Excel file.
Committed and Pushed the Code to GitHub:

I used Git commands (git add ., git commit -m "message", and git push) to stage, commit, and push my changes to the GitHub repository.
I verified the updates on GitHub to ensure that my code was version-controlled and available online.
