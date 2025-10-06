# Weekend Project: Streamlit Data Uploader
## Project Overview

Weekend Project — Streamlit Data Uploader is a lightweight web app built using Streamlit that allows you to:

Upload CSV or JSON data files 📂

Automatically preview, explore, and visualize the dataset

Generate summary statistics and detect missing values

Apply filters, view histograms, and download the processed dataset

This project is ideal for beginners to learn how to use Streamlit for quick data visualization and interaction.

## ⚙️ Features

Upload and parse CSV / JSON / TXT files
View data preview with interactive table
Display basic info — rows, columns, memory, missing values
Generate and download sample fitness dataset (heart rate, steps, sleep)
Create histograms for numeric columns using Plotly
Apply quick filters to any column
Download cleaned or filtered data as CSV

## weekend_project/
├── assets/             # Optional folder for logo and CSS
│   ├── logo.png
│   └── style.css
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/          # For data experiments
├── streamlit_app.py    # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

## Run
Create a virtual environment (recommended)
Install dependencies:
pip install -r requirements.txt
Run the Streamlit app:
streamlit run streamlit_app.py

## 📂 Sample Dataset

If you don’t have a dataset, use the “Generate Sample CSV” button in the app.
It will create a mock fitness dataset with:

timestamp

heart_rate

steps

sleep_quality

You can download or use it directly inside the app to test functionality.

## 📊 Example Workflow

Launch the app

Upload your data.csv or generate sample data

View dataset preview and stats

Choose numeric columns for histogram plotting

Filter columns and inspect subsets

Download processed CSV

## 🧠 Learning Goals

This project demonstrates:

Streamlit UI layout and components

Handling file uploads (st.file_uploader)

Reading CSV/JSON using pandas

Displaying tables and metrics

Plotly chart integration

Dynamic filtering and data exploration

Exporting processed files