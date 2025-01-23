"""Task 4: Python (Polars or Pandas)

1. Using the same taxi tripdata from the previous task union it with the data from in [yellow_tripdata_2024-02.parquet](data/yellow_tripdata_2024-02.parquet)
2. Group by **tpep_pickup_datetime** but only based on **YYYY-MM-DD**. Count the number of passengers per group, the sum of all payments, the average congestion surcharge.
3. Write the results to a parquet file at `temp/daily_trip_stats.parquet`
"""

import polars as pl
import pandas as pd
import pyarrow.parquet as pa

# polars
taxi_df = pl.read_parquet("data/yellow_tripdata_2024-01.parquet")

# pandas + pyarrow to load parquet file
pa_table = pa.read_table('data/yellow_tripdata_2024-01.parquet') 
taxi_df = pa_table.to_pandas()
