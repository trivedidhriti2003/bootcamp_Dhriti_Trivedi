## Data Preprocessing and Cleaning Strategy

The raw data was processed to prepare it for analysis and machine learning. The following steps and assumptions were made:

1.  **Handling Missing Values**:
    * **Dropped Columns**: Columns with more than 50% missing values were dropped, as they were considered too sparse to provide reliable information.
    * **Filled Columns**: Missing values in the `Age` and `Salary` columns were filled using the **median** value of each respective column. The median was chosen over the mean to minimize the effect of potential outliers.

2.  **Feature Scaling**:
    * **Normalization**: The `Age` and `Salary` columns were normalized using Min-Max scaling. This transforms their values to a common range of [0, 1], ensuring that they have equal importance in distance-based algorithms (e.g., k-NN, SVM).

The final, cleaned dataset is saved in `/data/processed/cleaned_data.csv`.