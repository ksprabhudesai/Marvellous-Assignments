import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)



border="-"*30

#---------------------------------------
#  Step 1 : Get Data
#---------------------------------------

print(border)
print("Step 1 : Get Data")
print(border)

Datapath = "WinePredictor.csv"
df =pd.read_csv(Datapath)

print("Dataframe Shape : ",df.shape)
print("Dataframe Head/Initial Entries : ",df.head())
print("Data loaded successfully from ",Datapath)


#---------------------------------------
#  Step 2 : Clean Prepare & Manipulate Data
#---------------------------------------

print(border)
print("Step 2.1 : Clean Data")
print(border)

print("Shape of dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Mising values per column : ")
print(df.isnull().sum())

print("Class distribution (Class count)")
print(df["Class"].value_counts())

print("Statistical report of dataset : ")
print(df.describe())

print("Step 2.2 : Prepare Data")

# X : Independent Varibale / Fetures
# Y : Dependenet VAriable / Labels

feature_cols =['Alcohol',
               'Malic acid',
               'Ash',
               'Alcalinity of ash',
               'Magnesium',
               'Total phenols',
               'Flavanoids',
               'Nonflavanoid phenols',
               'Proanthocyanins',
               'Color intensity',
               'Hue',''
               'OD280/OD315 of diluted wines',
               'Proline']

X=df[feature_cols]  # Features
Y=df['Class']      # Target variable

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)


print(border)
print("Step 2.3 : Split Data")
print(border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

print("X : ",X_train.head())
print("Y : ",Y_train.head())

print("X_train Shape : ",X_train.shape)
print("X_test Shape : ",X_test.shape)

print("Y_train Shape : ",Y_train.shape)
print("Y_test Shape : ",Y_test.shape)

print("Data Split into Train and Test sets successfully")


print(border)
print("Step 2.4 : Build Model")
print(border)

model=DecisionTreeClassifier(max_depth=5)
print("Model gets created succesfully")


#---------------------------------------
#  Step 3 : Train Data
#---------------------------------------

print(border)
print("Step 3.1 : Train Model")
print(border)

model.fit(X_train, Y_train)
print("Model trained successfully")

#---------------------------------------
#  Step 4 : Test Data
#---------------------------------------

print(border)
print("Step 4 : Test Model")
print(border)

Y_pred=model.predict(X_test)
print("Model tested successfully")  

print("Expected Answers : ",list(Y_test))


Y_pred_list = Y_pred.tolist()
print("Predicted Answers : ",Y_pred_list)


#---------------------------------------
#  Step 5 : Evaluating Model
#---------------------------------------

print(border)
print("Step 5 : Evaluate Model")
print(border)

accuracy = accuracy_score(Y_test,Y_pred)
accuracy_result=f"{accuracy*100:.2f}%"
print("Model Accuracy : ",accuracy_result)  


print("Classification Report :",classification_report(Y_test,Y_pred))