from app.db.connection import get_connection
import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

TABLE_NAMES = [
    "tbl_vw_Last_10_Withdrawals_Tumbet",
    "tbl_vw_Top_Profitable_Players_1Day_Sum_Tumbet",
    "tbl_vw_Top_Profitable_Players_1Week_Sum_Tumbet",
    "tbl_vw_Top_Profitable_Players_1Month_Sum_Tumbet",
    "tbl_vw_Top_Paying_Players_1Day_Sum_Tumbet",
    "tbl_vw_Top_Paying_Players_1Week_Sum_Tumbet",
    "tbl_vw_Top_Paying_Players_1Month_Sum_Tumbet",
    "tbl_vw_Top_Players_Who_Made_Most_of_The_Money_1Day_Sum_Tumbet",
    "tbl_vw_Top_Players_Who_Made_Most_of_The_Money_1Week_Sum_Tumbet",
    "tbl_vw_Top_Players_Who_Made_Most_of_The_Money_1Month_Sum_Tumbet",
    "tbl_vw_Latest_10_Winners_Slots_Tumbet",
    "tbl_vw_Highest_10_Earners_Slots_Tumbet",
    "tbl_vw_Top_Payer_Providers_Slots_1Week_Sum_Tumbet",
    "tbl_vw_Top_Paying_Slots_1Week_Sum_Tumbet",
]

def fetch_table(table_name):
    with get_connection() as conn:
        query = f"SELECT * FROM ReportDB.BIDS.{table_name} (nolock)"
        df = pd.read_sql(query, conn)
        print(table_name, "   done")
        return table_name[7:-7], df.to_dict(orient="records")

def fetch_all_tables():
    start_time = time.time()
    response = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_table, table) for table in TABLE_NAMES]
        for future in as_completed(futures):
            table_key, table_data = future.result()
            response[table_key] = table_data
    print(time.time() - start_time)
    return response
