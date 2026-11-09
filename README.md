# Inventory Data Analyzer

## About the Project

Inventory Data Analyzer is a Python project that I created to practice working with inventory data using Pandas and NumPy.

The project analyzes product information such as product names, categories, prices, and available quantities. It calculates useful inventory information and generates CSV reports.

The dataset is manually created using Python dictionaries.

## Features

- Create and display inventory dataset
- Calculate total number of products
- Calculate total available stock
- Calculate total inventory value
- Find the most expensive product
- Find the cheapest product
- Identify low-stock products
- Calculate average product price
- Analyze products by category
- Sort products by price
- Sort products by available quantity
- Generate inventory summary
- Export reports to CSV files
- Perform basic data validation

## Technologies Used

- Python
- Pandas
- NumPy
- CSV File Handling

## Project Structure

```text
Inventory-Data-Analyzer/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── output/
    ├── inventory_summary.csv
    ├── low_stock_products.csv
    └── category_summary.csv
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Inventory-Data-Analyzer.git
```

### 2. Open the Project Folder

```bash
cd Inventory-Data-Analyzer
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

## Reports

The project generates three CSV reports inside the output folder:

- **inventory_summary.csv:** Contains the main inventory information, including total products, total stock, and inventory value.
- **low_stock_products.csv:** Contains products with a quantity of 10 or less.
- **category_summary.csv:** Shows product counts, total stock, and total inventory value for each category.

## Data Validation

The project also performs four basic validation checks:

- Checks whether product IDs are unique.
- Checks for negative product prices.
- Checks for negative product quantities.
- Checks for missing values.

## What I Learned

While making this project, I practiced:

- Creating and working with Pandas DataFrames
- Performing calculations on inventory data
- Using NumPy for numerical calculations
- Filtering and sorting data
- Grouping data by categories
- Working with CSV files
- Performing basic data validation

## Future Improvements

- Add new products to the inventory.
- Update existing product information.
- Remove products from the inventory.
- Save inventory changes permanently.
- Create visual reports using Matplotlib and Seaborn.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)