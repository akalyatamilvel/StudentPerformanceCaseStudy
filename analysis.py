import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_data.csv")

# Show data
print("First 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nStatistics:")
print(df.describe())

# Create Performance Category
def categorize(marks):
    if marks >= 85:
        return "High"
    elif marks >= 65:
        return "Medium"
    else:
        return "Low"

df["Performance_Level"] = df["Final_Exam_Marks"].apply(categorize)

print("\nPerformance Levels:")
print(df[["Student_ID", "Final_Exam_Marks", "Performance_Level"]])

# Scatter plot 1
plt.scatter(df["Study_Hours"], df["Final_Exam_Marks"], color="blue")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("output_screenshots/scatter_study.png")
plt.show()

# Scatter plot 2
plt.scatter(df["Mobile_Usage"], df["Final_Exam_Marks"], color="red")
plt.title("Mobile Usage vs Marks")
plt.xlabel("Mobile Usage")
plt.ylabel("Marks")
plt.savefig("output_screenshots/scatter_mobile.png")
plt.show()

# Bar chart
sns.barplot(x="Performance_Level", y="Final_Exam_Marks", data=df)
plt.title("Performance Category Analysis")
plt.savefig("output_screenshots/bar_chart.png")
plt.show()

# Heatmap
plt.figure(figsize=(10,7))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("output_screenshots/heatmap.png")
plt.show() 

print("\nAll charts saved to output_screenshots folder!")
