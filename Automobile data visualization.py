# Load necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

# Set the style for all plots
plt.style.use('seaborn')

# Define column names based on the dataset's information
columns = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration", "num_doors", "body_style", 
           "drive_wheels", "engine_location", "wheel_base", "length", "width", "height", "curb_weight", 
           "engine_type", "num_cylinders", "engine_size", "fuel_system", "bore", "stroke", "compression_ratio", 
           "horsepower", "peak_rpm", "city_mpg", "highway_mpg", "price"]

# Load the dataset
data_path = os.path.join(extract_path, 'imports-85.data')
df = pd.read_csv(data_path, names=columns, na_values="?")

# Show a preview of the data
df.head()


# 1. Histogram of car prices

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=30, kde=True,  color='skyblue')
plt.title('Distribution of Car Prices', fontsize=15)
plt.xlabel(''Price (USD)', fontsize=12)
plt.ylabel('Count', fontsize=12))
plt.grid(True)
plt.show()


# 2. Scatter plot of horsepower vs. price

plt.figure(figsize=(10, 6))
sns.scatterplot(x='horsepower', y='price', data=df, hue='fuel-type' color='darkorange')
plt.title('Horsepower vs. Price', fontsize=15)
plt.xlabel('Horsepower',fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.grid(True)
plt.show()


# 3. Box plot of price by body-style

plt.figure(figsize=(12, 6))
sns.boxplot(x='body-style', y='price', data=df, palette='Set3')
plt.title('Price Distribution by Body Style', fontsize=15)
plt.xlabel('Body Style', fontsize=12)
plt.ylabel(''Price (USD)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



# 4. Highway MPG vs. City MPG
plt.figure(figsize=(10, 6))
sns.scatterplot(x='city_mpg', y='highway_mpg', data=df, color='green')
plt.title('City MPG vs. Highway MPG', fontsize=15)
plt.xlabel('City MPG', fontsize=12)
plt.ylabel('Highway MPG', fontsize=12)
plt.grid(True)
plt.show()


# 5. Bar plot of average price by make
plt.figure(figsize=(14, 6))
average_price_by_make = df.groupby('make')['price'].mean().sort_values(ascending=False)
sns.barplot(x=average_price_by_make.index, y=average_price_by_make.values)
plt.title('Average Price by Make', fontsize=12)
plt.xlabel('Make', fontsize=12)
plt.ylabel('Average Price', fontsize=12)
plt.xticks(rotation=90)
plt.grid(True)
plt.show()
