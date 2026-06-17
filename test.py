import pandas as pd

SHEET_ID = "1yB9-jogpwo5XxNdduNAGl__02RnHb8KHedpZW2dvfwk"
CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/"
    f"{SHEET_ID}/export?format=csv"
)


def load_google_sheet(url: str) -> pd.DataFrame:
    """
    Load data from a public Google Sheet into a DataFrame.

    Args:
        url: Google Sheet CSV export URL.

    Returns:
        pandas.DataFrame
    """
    return pd.read_csv(url)


def main() -> None:
    """Read and display Google Sheet data."""
    dataframe = load_google_sheet(CSV_URL)

    print("First 5 Rows:")
    print(dataframe.head())

    print("\nColumns:")
    print(dataframe.columns.tolist())


if __name__ == "__main__":
    main()