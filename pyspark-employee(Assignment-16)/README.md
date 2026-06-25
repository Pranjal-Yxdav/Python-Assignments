## Assignment 16

This project demonstrates PySpark RDD operations using Docker.

## Dataset

employees.csv

Operations performed:

1. Read CSV using RDD
2. Sort employees by salary (descending)
3. Calculate total salary of each department
4. Save top 3 highest-paid employees to output file

---

## Build Docker Image

```bash
docker build -t pyspark-employee .
```

## Run Docker Container

```bash
docker run --rm pyspark-employee
```

---

## Expected Console Output

```
===== Employees Sorted by Salary (Descending) =====

(4, 'Priya', 'Finance', 70000)
(3, 'Neha', 'IT', 65000)
(7, 'Rohit', 'Finance', 60000)
(1, 'Amit', 'IT', 55000)
(5, 'Karan', 'IT', 50000)
(6, 'Simran', 'HR', 45000)
(2, 'Rahul', 'HR', 40000)

===== Total Salary by Department =====

('IT', 170000)
('HR', 85000)
('Finance', 130000)

Top 3 highest-paid employees saved in output/top3_employees
```

---



