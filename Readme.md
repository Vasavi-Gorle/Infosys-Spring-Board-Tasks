# Data Format Mastery
## 🎯 Objective

Learn to analyze multiple data formats, build robust multi-format loaders, and handle file errors gracefully for fitness data.
This task demonstrates how to manage real-world data pipelines where data may arrive as CSV, nested JSON, or Excel files — sometimes even corrupted or inconsistent.

## 🧠 Learning Goals

Understand various fitness data formats (CSV, JSON, Excel)

Build a universal data loading function

Compare file size, load time, and usability

Handle corrupted/malformed files gracefully

(Bonus) Add XML/Parquet support, validation, and format conversion

## 📂 Project Structure
task2_data_format_mastery/
│
├── data/
│   ├── fitness_sample.csv
│   ├── fitness_sample_nested.json
│   ├── fitness_sample.xlsx
│   ├── fitness_sample_corrupted.csv
│
├── src/
│   ├── loader.py               # Universal data loader
│   ├── demo.py                 # Comparison & visualization script
│   ├── converter.py            # Format converter 
│   ├── validation.py           # Basic schema validation 
│
├── output/
│   ├── format_load_time.png    # Load time comparison chart
│   ├── format_comparison_report.txt
│
├── tests/
│   └── test_loader.py          # Loader test cases
│
└── README.md                   # Documentation (this file)