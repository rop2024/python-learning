import pandas as pd

def main():
    return

if __name__ == "__main__":
    main()


import pandas as pd

# Generate the data
data = {
    "Name": [
        "Alex Carter", "Olivia Bennett", "Ethan Davis", "Mia Johnson", "Noah Miller", 
        "Sophia Brown", "Liam Wilson", "Emma Anderson", "Mason Taylor", "Isabella Moore", 
        "Lucas Thomas", "Ava White", "Benjamin Harris", "Charlotte Martin", "Elijah Clark", 
        "Amelia Robinson", "James Walker", "Harper Wright", "Alexander Young", "Evelyn King", 
        "William Scott", "Abigail Adams", "Michael Evans", "Ella Hill", "Samuel Green", 
        "Lily Baker", "Henry Hall", "Chloe Turner", "Jackson Carter", "Grace Morgan", 
        "Sebastian Reed", "Scarlett Bailey", "Aiden Brooks", "Victoria Cooper", "Daniel Hayes", 
        "Aurora Sanders", "Matthew Morris", "Zoe Mitchell", "Christopher Rogers", "Stella Ward", 
        "Jonathan Hughes", "Ellie Foster", "Nathan Kelly", "Hannah Bell", "Ryan Powell", 
        "Natalie Peterson", "Connor Wood", "Aria James", "Caleb Flores", "Layla Parker"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", 
        "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", 
        "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", 
        "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", 
        "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"
    ],
    "Maths": [87, 92, 76, 88, 91, 95, 78, 89, 83, 97, 85, 90, 88, 91, 82, 96, 84, 87, 79, 93, 
              81, 89, 77, 85, 86, 91, 80, 94, 78, 92, 83, 97, 85, 89, 84, 93, 80, 88, 77, 94, 
              79, 90, 76, 89, 82, 96, 78, 92, 84, 95],
    "Science": [88, 91, 77, 86, 90, 94, 80, 87, 81, 96, 86, 88, 87, 90, 84, 94, 85, 86, 82, 92, 
                83, 88, 78, 86, 87, 89, 81, 93, 79, 91, 84, 95, 83, 90, 86, 92, 82, 89, 80, 93, 
                78, 87, 77, 88, 83, 94, 79, 91, 85, 96],
    "English": [89, 93, 78, 85, 92, 96, 81, 88, 84, 98, 87, 91, 89, 92, 85, 95, 86, 88, 83, 94, 
                84, 90, 79, 87, 88, 92, 82, 95, 80, 93, 85, 97, 84, 91, 87, 93, 83, 90, 81, 94, 
                79, 89, 78, 86, 84, 95, 80, 92, 86, 97]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to an Excel file

df.to_excel("", index=False)


