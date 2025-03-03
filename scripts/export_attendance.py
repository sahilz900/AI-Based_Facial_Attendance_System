import pandas as pd

attendance_file = "attendance.xlsx"
df = pd.read_excel(attendance_file)

df.to_csv("attendance_report.csv", index=False)
print("✅ Attendance exported successfully to 'attendance_report.csv'!")
