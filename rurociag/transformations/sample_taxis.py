"""
The 'transformations' folder contains all transformations
applied in this pipeline.
Documentation: https://docs.databricks.com/delta-live-tables/python-ref.html
"""

import dlt
from pyspark.sql.functions import to_date, count


@dlt.table(name="sample_taxis_2025_02_11_11_28_33")
def taxis():
    return (
        dlt.read("taxis_raw_2025_02_11_11_28_33")
        .withColumn("pickup_date", to_date("tpep_pickup_datetime"))
        .groupBy("pickup_date")
        .agg(count("*").alias("number_of_trips"))
    )
