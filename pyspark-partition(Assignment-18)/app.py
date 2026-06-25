from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("PartitionOperations") \
    .getOrCreate()

# Generate DataFrame with 5 million records
df = spark.range(5000000)

# Display initial number of partitions
print("=" * 50)
print("Initial Number of Partitions:", df.rdd.getNumPartitions())

# Increase partitions to 12 using repartition()
df_repartition = df.repartition(12)

print("Partitions After repartition(12):",
      df_repartition.rdd.getNumPartitions())

# Reduce partitions to 3 using coalesce()
df_coalesce = df_repartition.coalesce(3)

print("Partitions After coalesce(3):",
      df_coalesce.rdd.getNumPartitions())

print("=" * 50)

# Show a few records
df_coalesce.show(10)

# Stop Spark
spark.stop()