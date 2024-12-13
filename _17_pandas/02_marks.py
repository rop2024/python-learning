import pandas as pd

def main():
    df = pd.read_excel("_17_pandas/marks.xlsx", "Sheet1")
    print(df)
if __name__ == "__main__":
    main()