import pandas as pd
import numpy as np

df = pd.read_csv("company_data.csv")

print(df)

print(df.info())

print(df.describe())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df["Profit"] = (
    df["Revenue_Generated"] -
    df["Salary"]
)

df["Revenue_Per_Hour"] = (
    df["Revenue_Generated"] /
    df["Working_Hours"]
)

df["Productivity_Score"] = (
    df["Projects_Completed"] *
    df["Customer_Rating"]
)

print(df)

department_revenue = (
    df.groupby("Department")
    ["Revenue_Generated"]
    .sum()
)

print(department_revenue)

department_profit = (
    df.groupby("Department")
    ["Profit"]
    .sum()
)

print(department_profit)

department_avg_rating = (
    df.groupby("Department")
    ["Customer_Rating"]
    .mean()
)

print(department_avg_rating)

top_employees = (
    df.nlargest(
        5,
        "Revenue_Generated"
    )
)

print(top_employees)

bottom_employees = (
    df.nsmallest(
        5,
        "Revenue_Generated"
    )
)

print(bottom_employees)
print(
    "Average Revenue:",
    np.mean(
        df["Revenue_Generated"]
    )
)

print(
    "Median Revenue:",
    np.median(
        df["Revenue_Generated"]
    )
)

print(
    "Revenue Variance:",
    np.var(
        df["Revenue_Generated"]
    )
)

print(
    "Revenue Std:",
    np.std(
        df["Revenue_Generated"]
    )
)

conditions = [
    df["Revenue_Generated"] >= 200000,
    (
        df["Revenue_Generated"] >= 150000
    ) &
    (
        df["Revenue_Generated"] < 200000
    ),
    df["Revenue_Generated"] < 150000
]

categories = [
    "Excellent",
    "Good",
    "Needs Improvement"
]

df["Performance_Level"] = (
    np.select(
        conditions,
        categories,
        default="Needs Improvment" 
    )
)

df["Efficiency_Score"] = (
      df["Revenue_Per_Hour"] * 0.4
    + df["Customer_Rating"] * 20
    + df["Projects_Completed"] * 2
)

correlation_matrix = (
    df[
        [
            "Revenue_Generated",
            "Projects_Completed",
            "Working_Hours",
            "Customer_Rating",
            "Salary"
        ]
    ]
    .corr()
)

print(correlation_matrix)


df["Business_Risk"] = np.where(
    df["Efficiency_Score"] < 450,
    "High Risk",
    "Low Risk"
)
final_report = df[
    [
        "Employee_Name",
        "Department",
        "Revenue_Generated",
        "Profit",
        "Efficiency_Score",
        "Business_Risk",
        "Performance_Level"
    ]
]

final_report.to_csv(
    "Company_Analysis_Report.csv",
    index=False
)

print(
    "Report Generated Successfully"
)