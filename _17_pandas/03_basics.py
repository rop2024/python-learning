import pandas as pd

def main():
    df = pd.read_excel("_17_pandas/marks.xlsx", "Sheet1")
    basics(df)
    maths_basic_stats(df)


def basics(df):   
    # print column headings
    # print(df.head()) # this prints first 5 rows unless specified

    print(df.columns)
    
    # this returns table related stats
    # print(df.describe())


def maths_basic_stats(df):
    # who got the highest marks in class
    # print(f"Max marks in maths is {df['Maths'].max()}")
    # print(f"Max marks in Science is {df['Science'].max()}")
    # print(f"Max marks in English is {df['English'].max()}")

    # # min marks in each subject
    # print(f"Min marks in maths is {df['Maths'].min()}")
    # print(f"Min marks in Science is {df['Science'].min()}")
    # print(f"Min marks in English is {df['English'].min()}")

    # but this does not help, we want to know who scored the highest and lowest
    print(f"Max maths in maths was scored by -")
    print(df["Name"][df['Maths'] == df["Maths"].max()].tolist())

    print("-----")

    print(f"Min marks in maths was scored by -")
    print(df["Name"][df["Maths"] == df["Maths"].min()].tolist())

    print("-----")

    print(f"Mean maths marks of class is - {df["Maths"].mean()}")
    print("-----")


def combined_performace(df):
    # what is the average marks of the class
    return  


def average_student_list(df):
    # find how many students fall between quartile1 and quartile3
    return


if __name__ == "__main__":
    main()