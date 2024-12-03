"""Task 2: SQL

2. In the following cell, calculate the ordinal number of each bank failure per State based on the chronological order of failure.  
The result should show the Bank, city, State and the order in which it failed compared to its peers.  
Sort the results according to the State, Bank and Date.
 Hint: Window functions
"""

import duckdb

bank_failures_data = duckdb.read_parquet("bank_failures.parquet").show()

# duckdb.sql("""
# Write your code here!
# """).show()