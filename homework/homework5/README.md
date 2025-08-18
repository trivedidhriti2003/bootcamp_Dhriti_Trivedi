# Project Title

... (other project details)

## Data Storage

This project follows a structured approach to data storage, utilizing two key directories and different file formats for efficiency and clarity.

### Folder Structure
- `data/raw/`: This directory stores **raw, unprocessed data**. Files here are typically in formats like CSV, which is human-readable and easy to ingest.
- `data/processed/`: This directory contains **cleaned and processed data**. Data is stored here in more efficient formats like Parquet.

### File Formats
- **CSV (Comma-Separated Values):** A simple, text-based format ideal for raw data. It's universally compatible but can be inefficient for large datasets and does not preserve data types well.
- **Parquet:** A columnar storage format  optimized for analytical queries. It is significantly more efficient in terms of storage and read performance and correctly preserves data types, which is crucial for data integrity.

### Workflow and Code
Our code uses environment variables (`DATA_DIR_RAW`, `DATA_DIR_PROCESSED`) defined in the `.env` file to manage file paths. This makes the code portable and easy to configure. Reusable utility functions (`read_df` and `write_df`) handle saving and loading data, automatically choosing the correct pandas method based on the file extension (`.csv` or `.parquet`). This abstraction simplifies data I/O throughout the project.