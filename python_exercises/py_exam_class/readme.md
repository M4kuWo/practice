# Diamond Analysis App

## Overview

This application performs various analyses on a dataset of diamonds. It leverages SQLite for in-memory database operations and Pandas for data manipulation. The app provides insights into diamond characteristics such as price, cut, color, and carat.

## Files
1. py_exam_functions.py: Contains functions for performing different queries and calculations on the diamond dataset.
2. py_exam_app.py: The entry point of the application that calls the functions defined in py_exam_functions.py to execute the analyses.
3. requirements.txt: Lists the Python packages required for the application.

## Setup

### Prerequisites
- Python 3.x

### Installation
1. __Install required Python packages:__

You can use the requirements.txt file to install the necessary packages. Run the following command:

```bash
Copy code
pip install -r requirements.txt
```
The requirements.txt file should include:

- pandas
- numpy

2. __Dataset__

The application requires a CSV file named diamonds.csv in the same directory. The dataset should have the following columns:

- carat
- cut
- color
- clarity
- depth
- table
- price
- x
- y
- z

Ensure that the CSV file is formatted correctly and includes these columns for the application to function properly.

## How to Run

1. Place the diamonds.csv file in the same directory as the py_exam_functions.py, py_exam_app.py, and requirements.txt files.

2. Run the application by executing the py_exam_app.py script:

```bash
python py_exam_app.py
This will call all the functions defined in py_exam_functions.py and print the results to the console.
```

## Functions

1. __tallestDiamondPriceFunc()__
__Description:__ Retrieves and prints the price of the tallest diamond (diamond with the maximum height y).
__Output:__ Price of the tallest diamond rounded to two decimal places.
2. __avgDiamondPriceFunc()__
__Description:__ Calculates and prints the average price of all diamonds.
__Output:__ Average price of diamonds rounded to two decimal places.
3. __numDiamondsIdealCut()__
__Description:__ Counts and prints the number of diamonds with the cut type 'Ideal'.
__Output:__ Number of 'Ideal' cut diamonds.
4. __numDiamondColors()__
__Description:__ Counts and lists all unique diamond colors in the dataset.
__Output:__ Number of unique diamond colors and a comma-separated list of these colors.
5. __medianCaratPremiumDiamond()__
__Description:__ Calculates and prints the median carat weight of diamonds with the cut type 'Premium'.
__Output:__ Median carat weight of 'Premium' cut diamonds rounded to two decimal places.
6. __avgCaratPerCut()__
__Description:__ Calculates and prints the average carat weight for each diamond cut type.
__Output:__ Average carat weight for each cut type, rounded to two decimal places.
7. __avgPricePerColor()__
__Description:__ Calculates and prints the average price of diamonds for each color type.
__Output:__ Average price for each color, rounded to two decimal places.

## Example Output
```yaml
1 . The tallest diamond's price is: 18000.00
2 . The average price of a diamond is: 3950.00
3 . The number of diamonds of Ideal cut is: 21551
4 . The number of diamond colors is: 7
    The colors are the following: D, E, F, G, H, I, J
5 . The median Carat Premium is: 1.10
6. The average carat for each cut type is:
    Cut type: Fair, Average carat: 1.05
    Cut type: Good, Average carat: 1.02
    Cut type: Ideal, Average carat: 0.70
    Cut type: Premium, Average carat: 1.10
7. The average price for each color is:
    color: D, Average Price: 3261.00
    color: E, Average Price: 2887.00
    color: F, Average Price: 2755.00
    color: G, Average Price: 2636.00
    color: H, Average Price: 2633.00
    color: I, Average Price: 2520.00
    color: J, Average Price: 2170.00
```

## Troubleshooting

- __FileNotFoundError:__ Ensure that diamonds.csv is located in the same directory as the Python scripts.
- __KeyError:__ Verify that the CSV file contains all the required columns (carat, cut, color, clarity, depth, table, price, x, y, z).