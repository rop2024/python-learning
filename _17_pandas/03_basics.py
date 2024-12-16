import pandas as pd

def main():
    df = pd.read_excel("_17_pandas/marks.xlsx", "Sheet1")
    basics(df)
    maths_basic_stats(df)
    combined_performace(df)
    average_student_list(df)

    # saving back to excel
    df.to_excel("_17_pandas/new_marks.xlsx", index=False)

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
    df['TotalMarks'] = (df['Maths'] + df['Science']+ df['English'])/3.0

    # printing name and average marks
    
    # student with maximum and minimum performance
    maximum = df["Name"][df["TotalMarks"]== df['TotalMarks'].max()].tolist()
    print(f"Maximum percentage attended by {maximum}")

    minimum = df["Name"][df["TotalMarks"] == df['TotalMarks'].min()].tolist()
    print(f"Miminum percentage was attended by {minimum}")


def average_student_list(df):
    # find how many students fall between quartile1 and quartile3
    
    # values of quartile 1 and quartile 3
    quar3 = df['TotalMarks'].quantile(0.75)
    quar1 = df['TotalMarks'].quantile(0.25)

    list = df['Name'][(df['TotalMarks'] >= quar1) & (df['TotalMarks'] <= quar3)].tolist()
    
    print("-----")
    print("Names -")
    for name in list:
        print(f"{name}")
    
    print("-----")


if __name__ == "__main__":
    main()