import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
csv_files = DATA_DIR.glob("*.csv")

dataframes = []

for file in csv_files:
    df = pd.read_csv(
        file,
        names=["product", "price", "quantity", "date", "region"],
        header=0
    )

    # Normalize product names
    df["product"] = df["product"].str.lower().str.strip()

    # Filter ONLY pink morsel (singular)
    df = df[df["product"] == "pink morsel"]

    # Clean price column: "$3.00" -> 3.00
    df["price"] = (
        df["price"]
        .str.replace("$", "", regex=False)
        .astype(float)
    )

    # Ensure quantity is numeric
    df["quantity"] = df["quantity"].astype(int)

    # Create sales column
    df["sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["sales", "date", "region"]]

    dataframes.append(df)

# Combine all files
final_df = pd.concat(dataframes, ignore_index=True)

# Save output
final_df.to_csv("pink_morsels_sales.csv", index=False)

print("pink_morsels_sales.csv regenerated successfully")
