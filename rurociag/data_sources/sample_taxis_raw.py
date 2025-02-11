"""
The 'data_sources' folder contains definitions for all data sources
used by the pipeline. Keeping them separate provides a clear overview
of the data used and allows for easy swapping of sources during development.
"""

import dlt


@dlt.view
def taxis_raw_2025_02_11_11_28_33():
    return spark.sql("SELECT * FROM samples.nyctaxi.trips LIMIT 10")
