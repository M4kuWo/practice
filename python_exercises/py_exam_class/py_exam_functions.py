import pandas as pd
import sqlite3
import numpy as np

csvFile = 'diamonds.csv'
df = pd.read_csv(csvFile)

conn = sqlite3.connect(':memory:')  # This stores the db in the memory instead of an actual file

df.to_sql('diamonds', conn, if_exists='replace', index=False)

## Assignments:

# 1 . What's the price of the tallest diamond?
def tallestDiamondPriceFunc():
    query1 = "SELECT price, y FROM diamonds ORDER BY y DESC LIMIT 1"
    tallestDiamondPrice = pd.read_sql_query(query1, conn)
    tallestDiamondPriceValue = tallestDiamondPrice['price'].values[0]  # Access the price value from the DataFrame
    print(f"1 . The tallest diamond's price is: {tallestDiamondPriceValue:.2f}")

# 2 . What's the average price of a diamond?
def avgDiamondPriceFunc():
    query2 = "SELECT AVG(price) avgPrice FROM diamonds"
    avgDiamondPrice = pd.read_sql_query(query2, conn)
    avgDiamondPriceValue = avgDiamondPrice['avgPrice'].values[0]  
    print(f"2 . The average price of a diamond is: {avgDiamondPriceValue:.2f}")

# 3 . How many diamonds of type Ideal are there in the data?
def numDiamondsIdealCut():
    query3 = "SELECT COUNT(*) numDiamonds FROM diamonds WHERE cut = 'Ideal'"
    howManyIdealDiamonds = pd.read_sql_query(query3, conn)
    howManyIdealDiamondsValue = howManyIdealDiamonds['numDiamonds'].values[0]  
    print(f"3 . The number of diamonds of Ideal cut is: {howManyIdealDiamondsValue}")

# 4 . How many different colors of diamonds are there? What are the colors?
def numDiamondColors():
    query4 = "SELECT COUNT(DISTINCT color) numberOfColors FROM diamonds"
    query5 = "SELECT DISTINCT color FROM diamonds"
    numberOfColors = pd.read_sql_query(query4, conn)
    numberOfColorsValue = numberOfColors['numberOfColors'].values[0]  
    colors = pd.read_sql_query(query5, conn)
    colorsList = colors['color'].tolist()  # Convert the 'color' column to a list
    print(f"4 . The number of diamond colors is: {numberOfColorsValue}")
    colorsString = ', '.join(colorsList)
    print(f"    The colors are the following: {colorsString}")

# 5 . What's the median carat of diamonds of type Premium?
def medianCaratPremiumDiamond():
    query6 = "SELECT carat FROM diamonds WHERE cut = 'Premium'"
    caratData = pd.read_sql_query(query6, conn)
    caratValues = caratData['carat']

    # Calculate the median using numpy
    medianCaratPremium = np.median(caratValues)

    print(f"5 . The median Carat Premium is: {medianCaratPremium:.2f}")

# 6 . Give an average carat of each type of cut.
def avgCaratPerCut():
    query7 = "SELECT cut,AVG(carat) avgCarat FROM diamonds GROUP BY cut"
    avgCaratPerCutType = pd.read_sql_query(query7, conn)
    print("6. The average carat for each cut type is:")
    for index, row in avgCaratPerCutType.iterrows():
        cutType = row['cut']
        avgCarat = row['avgCarat']
        print(f"    Cut type: {cutType}, Average carat: {avgCarat:.2f}")

# 7 . Give an average price of each type of color.
def avgPricePerColor():
    query7 = "SELECT color,AVG(price) avgPrice FROM diamonds GROUP BY color"
    avgPricePerColor = pd.read_sql_query(query7, conn)
    print("7. The average price for each color is:")
    for index, row in avgPricePerColor.iterrows():
        colorType = row['color']
        avgPrice = row['avgPrice']
        print(f"    color: {colorType}, Average Price: {avgPrice:.2f}")
