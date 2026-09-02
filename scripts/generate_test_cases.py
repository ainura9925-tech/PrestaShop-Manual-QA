import pandas as pd
from pathlib import Path


# Excel file
file_path = "data/qase_test_cases.xlsx"

# Read Excel
df = pd.read_excel(file_path)


# Fill empty Suite Title cells with the value above
df["Suite Title"] = df["Suite Title"].ffill()


# Select Homepage & Navigation suite
Accessibility = df[df["Suite Title"] == "Accessibility"]


# Create output folder
output_folder = Path("Test-Cases")
output_folder.mkdir(exist_ok=True)


# Start Markdown file
markdown = "# Accessibility — Test Cases\n\n"


# Go through every row
for index, row in Accessibility.iterrows():

    # New test case starts when ID is present
    if pd.notna(row["ID"]):

        test_id = row["ID"]
        title = row["Title"]
        priority = row["Priority"]
        behavior = row["Behavior"]
        test_type = row["Type"]
        preconditions = row["Preconditions"]

        markdown += f"## {test_id} — {title}\n\n"

        markdown += f"**Priority:** {priority}  \n"
        markdown += f"**Behavior:** {behavior}  \n"
        markdown += f"**Type:** {test_type}  \n"
        markdown += "**Layer:** UI  \n"
        markdown += "**Automation:** Manual\n\n"

        markdown += "### Preconditions\n\n"

        if pd.notna(preconditions):
            markdown += f"{preconditions}\n\n"
        else:
            markdown += "None specified.\n\n"

        markdown += "### Test Steps\n\n"

        markdown += "| # | Action | Expected Result |\n"
        markdown += "|---|---|---|\n"

    # Add test step
    if pd.notna(row["Step"]):

        step = int(row["Step"])
        action = row["Action"]
        expected = row["Expected result"]

        markdown += f"| {step} | {action} | {expected} |\n"


# Save file
output_file = output_folder / "Accessibility.md"

output_file.write_text(markdown, encoding="utf-8")


print(f"Created: {output_file}")