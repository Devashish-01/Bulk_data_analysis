import pandas as pd
import streamlit as st

# Function to safely calculate traded quantity
def calculate(quantity_traded):
    try:
        return int(quantity_traded.replace(',', ''))
    except ValueError:
        return 0  # Return 0 if the value cannot be converted

# Function to process the CSV and return a sorted DataFrame
def process_csv(dataframe):
    # Initialize an empty dictionary to store security names and quantities
    name = {}

    # Iterate through the DataFrame rows
    for _, row in dataframe.iterrows():
        # Clean and extract necessary fields
        security_name = row['Security Name '].strip()
        quantity_traded = row['Quantity Traded '].strip()
        buy_sell = row['Buy / Sell '].strip().upper()

        # Use .get() to handle missing names gracefully
        current_quantity = name.get(security_name, 0)

        # Update the quantity based on the 'Buy / Sell' value
        if buy_sell == 'BUY':
            name[security_name] = current_quantity + calculate(quantity_traded)
        elif buy_sell == 'SELL':
            name[security_name] = current_quantity - calculate(quantity_traded)

    # Create a DataFrame from the dictionary and sort it
    result_df = pd.DataFrame(name.items(), columns=['Security Name', 'Quantity Traded'])
    result_df = result_df.sort_values(by='Quantity Traded', ascending=False)

    return result_df

# Streamlit app title
st.title("Bulk Data Processor")

# File uploader widget for the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, process it
if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Check if the required columns are present
        required_columns = ['Security Name ', 'Quantity Traded ', 'Buy / Sell ']
        if not all(col in df.columns for col in required_columns):
            st.error("Uploaded CSV must contain 'Security Name', 'Quantity Traded', and 'Buy / Sell' columns.")
        else:
            # Display the original DataFrame
            st.write("Original DataFrame:")
            st.dataframe(df)

            # Process the CSV
            processed_df = process_csv(df)

            # Display the processed DataFrame
            st.write("Processed DataFrame:")
            st.dataframe(processed_df)

            # Generate CSV for download
            csv = processed_df.to_csv(index=False).encode('utf-8')

            # Provide download button for the processed CSV
            st.download_button(
                label="Download Processed CSV",
                data=csv,
                file_name="bulkdata_revised.csv",
                mime='text/csv'
            )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
