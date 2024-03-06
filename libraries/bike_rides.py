def read_bike_rides(spark):
  return spark.read.csv("/databricks-datasets/bikeSharing/data-001/day.csv", header=True, inferSchema=True)
