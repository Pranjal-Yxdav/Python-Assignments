from pyspark import SparkContext
import os
import shutil

# Create Spark Context
sc = SparkContext("local[*]", "EmployeeRDD")

# Read CSV file
rdd = sc.textFile("employees.csv")

# Remove header
header = rdd.first()
data = rdd.filter(lambda line: line != header)

# Convert each row into a tuple
employees = data.map(lambda line: line.split(",")) \
                .map(lambda x: (int(x[0]), x[1], x[2], int(x[3])))

# -------------------------------------------------
# Sort employees by salary (descending)
# -------------------------------------------------
print("\n===== Employees Sorted by Salary (Descending) =====")

sorted_salary = employees.sortBy(lambda x: x[3], ascending=False)

for emp in sorted_salary.collect():
    print(emp)

# -------------------------------------------------
# Total salary by department
# -------------------------------------------------
print("\n===== Total Salary by Department =====")

department_salary = employees.map(lambda x: (x[2], x[3])) \
                             .reduceByKey(lambda a, b: a + b)

for dept, total in department_salary.collect():
    print(f"{dept}: {total}")

# -------------------------------------------------
# Top 3 highest-paid employees
# -------------------------------------------------

top3 = sorted_salary.take(3)

print("\n===== Top 3 Highest-Paid Employees =====")
for emp in top3:
    print(emp)

# Output path
output_path = "output/top3_employees"

# Delete existing output folder if it exists
if os.path.exists(output_path):
    shutil.rmtree(output_path)

# Create parent output folder
os.makedirs("output", exist_ok=True)

# Save output
output_data = [
    f"{emp[0]},{emp[1]},{emp[2]},{emp[3]}"
    for emp in top3
]

# Create RDD with only one partition
output_rdd = sc.parallelize(output_data, 1)

output_rdd.saveAsTextFile(output_path)

print(f"\nTop 3 highest-paid employees saved in {output_path}")

# Stop Spark
sc.stop()