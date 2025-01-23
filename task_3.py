"""Task 2: Python (Polars or Pandas)

1. Load data from the [yellow_tripdata_2024-01.parquet](data/yellow_tripdata_2024-01.parquet) file into a DataFrame and inspect the schema. You can use either Polars or Pandas  
so comment out the one you don't need.
2. Filter all trips that with a trip_distance greater than 5 miles, and tip_amount of 0.
3. Write the results to a csv file temp/no_tip.csv.
"""

import polars as pl
import pandas as pd
import pyarrow.parquet as pa

# polars
taxi_df = pl.read_parquet("data/yellow_tripdata_2024-01.parquet")

# pandas + pyarrow to load parquet file
pa_table = pa.read_table('data/yellow_tripdata_2024-01.parquet') 
taxi_df = pa_table.to_pandas()
