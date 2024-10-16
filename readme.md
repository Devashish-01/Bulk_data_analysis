 ## Bulk Data Processor

This is a Streamlit web application designed to process bulk data from CSV files related to trading quantities of securities. The app analyzes the data, calculates the total quantities traded for each security, and allows users to download the processed data.

## Features

- **CSV File Upload**: Users can upload a single CSV file containing trading data.
- **Data Processing**: The app processes the CSV to calculate the total quantities traded for each security based on buying and selling transactions.
- **Download Processed Data**: Users can download the processed data as a CSV file.

## Prerequisites

Make sure you have the following installed:

- Python 3.x

### Required Libraries

You will need to install the following libraries:

- **pandas**: For data manipulation and analysis.
- **streamlit**: For building the web application.

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install required dependencies:**

   Create a `requirements.txt` file with the following content:

   ```
   pandas
   streamlit
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   After installing the required libraries, run the application with the following command:

   ```bash
   streamlit run app.py
   ```

4. **Access the app:**

   Open your browser and go to `http://localhost:8501/`.

## CSV File Requirements

The uploaded CSV file must contain the following columns:

- `Security Name `
- `Quantity Traded `
- `Buy / Sell `

## Usage

1. **Upload CSV File**: Use the file uploader to select a CSV file.
2. **View Original DataFrame**: The app displays the original data from the uploaded file.
3. **Processed Data**: The app displays the processed DataFrame with the total quantities traded for each security.
4. **Download Processed Data**: Click the download button to get the processed data as a CSV file.

## Example CSV Data

| Security Name  | Quantity Traded | Buy / Sell |
|----------------|-----------------|------------|
| ABC Corp       | 1,000           | Buy        |
| XYZ Inc        | 500             | Sell       |
| ABC Corp       | 300             | Sell       |

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to [Streamlit](https://streamlit.io/) for providing an easy framework for building interactive web apps.

### Updates Made:
- **Required Libraries**: Added a section listing the necessary libraries (`pandas` and `streamlit`).
- **How to Run**: Expanded the instructions under the "Installation" section to provide a clear step on running the application after installation.
