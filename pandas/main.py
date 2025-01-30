import pandas as pd
students = {
    "Name": [
        "Alice", None, "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kelly", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tara",
        "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zack", "Adam", "Beth", "Carl", "Diana",
        "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin", "Luna", "Mason", "Nora",
        "Oscar", "Penny", "Quincy", "Rose", "Steve", "Tracy", "Uri", "Violet", "Will", "Xena",
        "Yuki", "Zara", "Alex", "Bella", "Chris", "Dora", "Eric", "Flora", "Gary", "Hope",
        "Isaac", "Jane", "Kyle", "Lisa", "Mark", "Nina", "Owen", "Piper", "Quest", "Ryan",
        "Sarah", "Tom", "Uma", "Vince", "Wade", "Xander", "Yves", "Zoe", "Aaron", "Bonnie",
        "Cody", "Dale", "Eva", "Felix", "Gina", "Hugo", "Iris", "James", "Kate", "Leo",
        "Maya", "Nick", "Olive", "Paul", "Queen", "Rick", "Sky", "Ted", "Ursa", "Vera",
        "Walt", "Xena", "Yuri", "Zeke"
    ],
    "Age": [
        19, 25, 18, 22, 24, 21, 19, 23, 20, 25,
        18, 22, 24, 21, 19, 23, 20, 25, 18, 22,
        24, 21, 19, 23, 20, 25, 18, 22, 24, 21,
        19, 23, 20, 25, 18, 22, 24, 21, 19, 23,
        20, 25, 18, 22, 24, 21, 19, 23, 20, 25,
        18, 22, 24, 21, 19, 23, 20, 25, 18, 22,
        24, 21, 19, 23, 20, 25, 18, 22, 24, 21,
        19, 23, 20, 25, 18, 22, 24, 21, 19, 23,
        20, 25, 18, 22, 24, 21, 19, 23, 20, 25,
        18, 22, 24, 21, 19, 23, 20, 25, 18, 22, None, None, None, None
    ],
    "Marks": [
        95, 45, 88, 72, 100, 65, 92, 33, 78, 85,
        67, 91, 55, 82, 94, 23, 76, 89, 41, 97,
        58, 83, 90, 12, 75, 88, 49, 93, 71, 84,
        96, 37, 79, 87, 52, 94, 68, 86, 28, 98,
        63, 85, 91, 44, 77, 89, 15, 95, 70, 83,
        92, 56, 81, 88, 39, 97, 64, 86, 93, 25,
        74, 87, 50, 96, 69, 84, 90, 31, 78, 85,
        98, 42, 80, 89, 57, 94, 73, 86, 19, 99,
        62, 85, 91, 48, 76, 88, 35, 95, 67, 83,
        92, 54, 79, 87, 43, 96, 71, 84, 8, 100, None, None, None, None
    ]
}

# print(len(students["Name"]))
# print(len(students["Age"]))
# print(len(students["Marks"]))

# Series
obj = pd.Series([{
    "Name": "Alice",
    "Age": 19,
    "Marks": 95
},
    {
    "Name": "Bob",
    "Age": 19,
    "Marks": 95
}
])
# print(obj)

# DataFrame
students_df = pd.DataFrame(
    students, index=[i for i in range(1, len(students["Marks"]) + 1)])
# print(students_df.head(5))

students_df.dropna(inplace=True)
# print(students_df.tail(5))


# loc
# iloc

MARKS_TRESHOLD = 80

marks_mask = students_df["Marks"] > MARKS_TRESHOLD

string_mask = students_df["Name"].str.startswith('Z')


students_df_greater_than_treshold = students_df[string_mask][marks_mask]

students_df_greater_than_treshold.to_csv("data.csv", index=False)


# print(students_df_greater_than_treshold)


df = pd.read_csv("cleaned_datset.csv")

print(df)
