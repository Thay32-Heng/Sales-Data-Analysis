import pandas as pd
from pathlib import Path

def clean_data():
    root = Path(__file__).resolve().parents[1]   
    input_path = root / "data" / "raw" / "sales.csv"
    output_dir = root / "data" / "processed"
    output_path = output_dir / "sales_cleaned.csv"

    df = pd.read_csv(input_path)
    df = df.dropna().drop_duplicates()

    output_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print("Saved:", output_path)

if __name__ == "__main__":
    clean_data()
