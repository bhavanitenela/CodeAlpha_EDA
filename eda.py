import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_data.csv")

# 1. Display first 5 rows
print("===== FIRST 5 ROWS =====")
print(data.head())

# 2. Dataset shape
print("\n===== DATASET SHAPE =====")
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

# 3. Dataset information
print("\n===== DATASET INFORMATION =====")
data.info()

# 4. Statistical summary
print("\n===== STATISTICAL SUMMARY =====")
print(data.describe())

# 5. Check missing values
print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

# 6. Average marks
print("\n===== AVERAGE MARKS =====")
print(data["Marks"].mean())

# 7. Highest marks
print("\n===== HIGHEST MARKS =====")
print(data["Marks"].max())

# 8. Lowest marks
print("\n===== LOWEST MARKS =====")
print(data["Marks"].min())

# 9. Average study hours
print("\n===== AVERAGE STUDY HOURS =====")
print(data["StudyHours"].mean())

# 10. Average attendance
print("\n===== AVERAGE ATTENDANCE =====")
print(data["Attendance"].mean())

# 11. Student with highest marks
print("\n===== TOP STUDENT =====")
top_student = data.loc[data["Marks"].idxmax()]
print(top_student["Name"], "-", top_student["Marks"], "marks")

# 12. Student marks visualization
plt.figure(figsize=(8, 5))
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== EDA COMPLETED SUCCESSFULLY =====")