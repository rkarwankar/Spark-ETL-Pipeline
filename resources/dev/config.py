import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

# AWS Access And Secret key
aws_access_key = "OrShFTjCqu7aIhSTA7lhYdZaxaQDnz8d5Y4l4rax4OE="
aws_secret_key = "pnlIZUTMbctYciVtb9q7MJ7cceTXHT9KI3+sI1a1DrjX0mXm+CNBVQ4gAZeE27R9"
bucket_name = "sales-cust-data"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


# Database credential
# MySQL database connection properties
database_name = "sales_project"
url = f"jdbc:mysql://localhost:3306/{database_name}"
properties = {
    "user": "root",
    "password": "password",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

# Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "C:\\Users\\rkarw\\Desktop\\Data Engineering project(Spark and AWS)\\data_files_download\\file_from_s3\\"
customer_data_mart_local_file = "C:\\Users\\rkarw\\Desktop\\Data Engineering project(Spark and AWS)\\data_files_download\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\Users\\rkarw\\Desktop\\Data Engineering project(Spark and AWS)\\data_files_download\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\Users\\rkarw\\Desktop\\Data Engineering project(Spark and AWS)\\data_files_download\\sales_partition_data\\"
error_folder_path_local = "C:\\Users\\rkarw\\Desktop\\Data Engineering project(Spark and AWS)\\data_files_download\\error_files\\"


# SQL server
host = "localhost"
user ="root"
password="toor"
database="sales_project"
table_name="product_staging_table"