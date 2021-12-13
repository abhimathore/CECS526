from pandas import read_csv
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# Loading the Data as Pandas DataFrame
df = read_csv("Salary_Data.csv")

# Preprocessing the Data according to our needs
X = df["YearsExperience"].values.reshape(30,1)
y = df["Salary"]

# Spliting the Data into Training Set(80%) and Test Set(20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initated the Machine Learning Model
mind = LinearRegression()

# Trained the Machine Learning Model using X_train, y_train data 
mind.fit(X_train ,y_train)
# Make predictions using the testing set
y_pred = mind.predict(X_test)


# Plot outputs
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# Saving the Model as pickle file
dump(mind ,"SalaryModel.pkl")