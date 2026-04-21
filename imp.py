import csv
with open("filebook.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])    # header
    writer.writerow(["sri", 20, "hyderabad"])
    writer.writerow(["ravi", 22, "chennai"])
