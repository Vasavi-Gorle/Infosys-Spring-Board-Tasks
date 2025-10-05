import streamlit as st
import pandas as pd
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="Data Explorer Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Sidebar with Project Information (Requirement 3) ---
st.sidebar.title("Weekend Project Info")
st.sidebar.markdown(
    """
    **Project Goal:** Basic Data Exploration Dashboard
    
    This app allows users to upload a CSV or JSON file and view
    its structure and first few rows.
    
    **Libraries Used:**
    - Streamlit
    - Pandas
    """
)
st.sidebar.info("Data Science Setup Mastery Task")
# (Optional Bonus: Interactive Widget)
show_raw_data = st.sidebar.checkbox("Show Raw Data Preview", value=True)

# --- Main Dashboard Title ---
st.title("Data Upload & Exploration Dashboard 📊")
st.markdown("Upload your data file (CSV or JSON) below.")

# --- File Upload Interface (Requirement 1) ---
uploaded_file = st.file_uploader(
    "Choose a CSV or JSON file", 
    type=['csv', 'json']
)

# --- Data Processing and Display ---
if uploaded_file is not None:
    # 1. Read the file
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            # Load JSON, assuming a standard format that converts to a DataFrame
            # For complex JSON, more logic is needed
            data = json.load(uploaded_file)
            df = pd.DataFrame(data)
        
        st.success("File uploaded successfully!")
        
        # 2. Display basic dataset information (Requirement 2)
        st.header("Dataset Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Rows", f"{df.shape[0]:,}")
        col2.metric("Columns", f"{df.shape[1]}")
        col3.metric("Data Types", f"{len(df.dtypes.unique())} Unique")

        with st.expander("Detailed Column Information"):
            # Display non-null count, data type, etc.
            st.dataframe(df.dtypes.reset_index().rename(columns={
                'index': 'Column Name', 0: 'Data Type'
            }))
        
        # 3. Show first 10 rows of uploaded data (Requirement 3)
        if show_raw_data:
            st.header("Data Head (First 10 Rows)")
            st.dataframe(df.head(10))
            
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Awaiting file upload...")

# --- Run the App ---
# Save the file as streamlit_app.py in the weekend_project directory.
# Run from the terminal:
# streamlit run streamlit_app.py