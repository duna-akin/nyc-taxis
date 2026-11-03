import pandas as pd

ride_share_df = pd.read_parquet('source-data/fhv_tripdata_2026-01.parquet')
taxi_df = pd.read_parquet('source-data/yellow_tripdata_2026-01.parquet')

taxi_df.info()
print(taxi_df)
