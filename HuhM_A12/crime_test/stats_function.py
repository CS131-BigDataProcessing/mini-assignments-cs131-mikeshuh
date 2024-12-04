import pandas as pd

def age_mean(df):
    return df["Vict Age"].mean()

def age_median(df):
    return df["Vict Age"].median()

def main():
    print("Reading Crime Data...")
    df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

    print("Calculating Age Mean and Median...")
    print("Mean:", age_mean(df))
    print("Median:", age_median(df))

if __name__ == "__main__":
    main()