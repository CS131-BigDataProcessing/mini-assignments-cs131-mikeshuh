import pandas as pd

def validate_victim_sex(df):
    sex = df['Vict Sex'].isin(['M', 'F']) & df['Vict Sex'].notnull()

    if(sex.all()):
        return True
    return False

def validate_victim_age(df):
    age = df['Vict Age'].between(1, 100) & df['Vict Age'].notnull()

    if(age.all()):
        return True
    return False

def main():
    print("Reading Crime Data...")
    df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

    print("Validating Victim Sex and Age Columns...")
    print("Pass Sex Validation?:", validate_victim_sex(df))
    print("Pass Age Validation?:", validate_victim_age(df))
    
if __name__ == "__main__":
    main()