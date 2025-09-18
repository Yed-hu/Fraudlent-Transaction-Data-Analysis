# Fraud Detection System for Credit Card Transactions

A modular Python-based fraud detection system built to analyze and detect potentially fraudulent credit card transactions using statistical methods and distance-based heuristics.

## Project Overview

With the increasing prevalence of electronic payments, financial institutions must proactively detect and prevent fraudulent activities. This project simulates a real-world system for a bank to identify and flag suspicious transactions using a dataset of user activities.

The system is divided into four main modules:
- **Dataset Module**: Parses and structures transaction data.
- **Distance Module**: Calculates Euclidean distance between transactions.
- **Statistics Module**: Provides analytical insights through 12 statistical functions.
- **Main Module**: Acts as a command-line interface for user interaction with the system.

## Project Structure

```
fraud_detection_project/
│
├── dataset_module.py        # Handles data loading and structuring
├── distance_module.py       # Calculates distances between transactions
├── statistics_module.py     # Statistical analysis functions
├── main_module.py           # User interface and program execution
├── Transaction.txt          # Main dataset (1100 transactions, 10 users)
├── description.txt          # Description of all transactions
├── fraud-description.txt    # Description of fraudulent transactions
└── README.md                # Project documentation
```

## Features

- Calculates:
  - Mean, Mode, Median
  - Interquartile Range (IQR)
  - Standard Deviation
  - Z-Scores and Percentiles
- Location-based analysis:
  - Centroid of transactions
  - Transaction frequency by coordinates
  - Outlier detection based on transaction distances
- Fraud Detection:
  - Identifies fraudulent transactions using boolean labels
  - Detects abnormal transactions exceeding statistical thresholds
  - Displays details of flagged activities

## Technologies Used

- Python 3.x
- File I/O operations
- Dictionary-based data structures
- Modular programming
- Descriptive statistics
- Basic linear algebra (Euclidean distance)

## How to Run

1. Clone the repository:
```
git clone https://github.com/yourusername/fraud-detection-system.git
cd fraud-detection-system
```

2. Ensure all required files are in the project directory:
   - Transaction.txt
   - description.txt
   - fraud-description.txt

3. Run the main module:
```
python main_module.py
```

4. Use the menu-driven interface to select analysis options.

## Sample Output

```
Select an option:
1. Check if a transaction is fraudulent
2. Calculate average transaction value
3. Find abnormal transactions
4. Compute Z-scores
5. Calculate distance between transactions
...
```

## Example Use Cases

- Identify transactions that deviate significantly from user behavior.
- Analyze transaction frequency at specific geographic coordinates.
- Detect clusters of potentially fraudulent activities based on spatial distance.



This project is licensed under the MIT License. See the LICENSE file for details.
