"""Task 1: SQL

1. Load data from the [bank_failures.parquet](bank_failures.parquet) file into a DuckDBPyRelation and inspect the schema.
2. In the following cell, calculate the number of banks in the state of New York that have failed after 2010-01-01. The result only needs to show the number of banks.

Look up [DuckDb Python API](https://duckdb.org/docs/api/python/overview.html)"""

import duckdb

bank_failures_data = duckdb.read_parquet("bank_failures.parquet").show()

# duckdb.sql("""
# Write your code here!
# """).show()
