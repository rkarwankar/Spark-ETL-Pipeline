# 🚀 Spark Data Processing Pipeline

## 📋 Overview
This project implements an automated data processing pipeline that retrieves CSV files from Amazon S3, validates their schema against required columns, processes them, and loads the data into a MySQL database. The pipeline handles error scenarios by moving invalid files to a designated error directory both locally and in S3.

## ✨ Features
- 📦 S3 file listing and downloading
- 🔍 Schema validation against mandatory columns
- ⚠️ Error handling for files with missing required columns
- ➕ Additional column handling via concatenation into a single field
- 🗄️ MySQL database integration for tracking file processing status
- 📝 Logging of all operations for audit and troubleshooting
- 🔐 Secure AWS credential handling with encryption/decryption

## 🔧 Prerequisites
- 🐍 Python 3.6+
- ☁️ AWS account with S3 access
- 🐬 MySQL database
- 📚 Required Python packages (see Installation section)

## 🔌 Installation

### Clone the repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up configuration
Edit the `resources/dev/config.py` file to include your specific settings:
- AWS credentials (encrypted)
- S3 bucket and directory paths
- Local directories for processing
- MySQL database connection details
- Mandatory columns for data validation

## 📂 Project Structure
```
my_project/
├── docs/
│   └── readme.md
├── resources/
│   ├── __init__.py
│   ├── dev/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── qa/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── prod/
│   │    ├── config.py
│   │    └── requirement.txt
│   ├── sql_scripts/
│   │    └── table_scripts.sql
├── src/
│   ├── main/
│   │    ├── __init__.py
│   │    └── delete/
│   │    │      ├── aws_delete.py
│   │    │      ├── database_delete.py
│   │    │      └── local_file_delete.py
│   │    └── download/
│   │    │      └── aws_file_download.py
│   │    └── move/
│   │    │      └── move_files.py
│   │    └── read/
│   │    │      ├── aws_read.py
│   │    │      └── database_read.py
│   │    └── transformations/
│   │    │      └── jobs/
│   │    │      │     ├── customer_mart_sql_transform_write.py
│   │    │      │     ├── dimension_tables_join.py
│   │    │      │     ├── main.py
│   │    │      │     └──sales_mart_sql_transform_write.py
│   │    └── upload/
│   │    │      └── upload_to_s3.py
│   │    └── utility/
│   │    │      ├── encrypt_decrypt.py
│   │    │      ├── logging_config.py
│   │    │      ├── s3_client_object.py
│   │    │      ├── spark_session.py
│   │    │      └── my_sql_session.py
│   │    └── write/
│   │    │      ├── database_write.py
│   │    │      └── parquet_write.py
│   ├── test/
│   │    ├── scratch_pad.py.py
│   │    └── generate_csv_data.py
```

```

## ⚙️ Configuration
The application is configured through the `resources/dev/config.py` file. Key configuration parameters include:

| Parameter | Description |
|-----------|-------------|
| aws_access_key | Encrypted AWS access key |
| aws_secret_key | Encrypted AWS secret key |
| bucket_name | S3 bucket name |
| s3_source_directory | Source directory path in S3 |
| s3_error_directory | Error directory path in S3 |
| local_directory | Local directory for processing |
| error_folder_path_local | Local directory for error files |
| database_name | MySQL database name |
| table_name | MySQL table for tracking processing |
| product_staging_table | MySQL staging table |
| mandatory_columns | Required columns for CSV validation |

## 🔄 Workflow

1. **🔑 Authentication & Setup**: 
   - Decrypt AWS credentials and establish S3 client connection
   - Verify previous run status by checking MySQL database

2. **📥 File Retrieval**:
   - List files in the S3 source directory
   - Download files to the local directory

3. **🔎 Schema Validation**:
   - Analyze each CSV file using Spark
   - Compare schema against mandatory columns
   - Move files with missing columns to error directories

4. **⚡ Data Processing**:
   - Handle extra columns by concatenating them into a single column
   - Create a unified dataframe with all valid data

5. **💾 Database Integration**:
   - Update MySQL staging table with processing status
   - Track file processing status and timestamps

## 🛡️ Error Handling
The pipeline includes robust error handling:
- Files with missing required columns are moved to an error directory
- Detailed logging of all errors and operations
- Database tracking of file processing status
- Graceful exit with meaningful error messages

## 📊 Logging
Comprehensive logging is implemented throughout the application to facilitate debugging and monitoring:
- File operations
- Schema validation
- Database operations
- Error conditions
- Processing status

## 🔒 Security
- AWS credentials are encrypted in the configuration file
- Decryption happens at runtime

## 🔥 Spark Data Transformation

The pipeline leverages Apache Spark for high-performance data processing, supporting complex transformations on sales and customer data:

### Current Capabilities
- Schema validation of source CSV files
- Handling of missing and extra columns
- Unification of validated data into a single processing dataframe

### Planned Spark Transformations
- **💰 Sales Incentive Calculations**: Computing performance-based incentives for sales personnel based on sales metrics
- **👥 Customer Analytics**: Segmentation and analysis of customer purchasing patterns
- **📈 Dynamic Aggregations**: Period-over-period performance comparisons at various levels (product, store, salesperson)
- **🔄 Data Enrichment**: Joining sales data with additional datasets for enhanced analytics
- **⚡ Performance Optimization**: Utilizing Spark's parallelism for processing large volumes of sales data efficiently

### Implementation Details
The pipeline uses PySpark's DataFrame API to:
- Load and validate CSV data with defined schemas
- Apply complex transformations using SQL and DataFrame operations
- Handle various data types including numeric, string, and date fields
- Support both batch processing and potential future streaming capabilities

These Spark transformations turn raw sales data into actionable business intelligence, enabling data-driven decision making for sales incentive programs and customer relationship management.

## 🔧 Extending the Project
To add new functionality:
1. Extend the schema validation for different file types
2. Add more data transformation steps
3. Implement additional destination options beyond MySQL
4. Create a monitoring dashboard for the pipeline

## 🔍 Troubleshooting
- Check logs for detailed error information
- Verify AWS credentials and permissions
- Ensure MySQL connection details are correct
- Validate that the S3 paths and bucket names are properly configured
