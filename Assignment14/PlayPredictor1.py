import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def MarvellousKNeighborsCassifier(data_path):
    Dataset=pd.read_csv(data_path,index_col=0)     #1 load the data


    #2.clean,manipulate data
    feature_names=['whether','Temperature']

    whether=Dataset.Whether
    Temperature=Dataset.Temperature
    play=Dataset.Play


    #3.create object of labelencoder
    le=LabelEncoder()

    #.convert the string data into numeric
    wheather_encoded=le.fit_transform(whether)

    
    temp_encoded=le.fit_transform(Temperature)

    label=le.fit_transform(play)


    #jion the two list
    features=list(zip(wheather_encoded,temp_encoded))

    #create object of KNN
    Classifier=KNeighborsClassifier(n_neighbors=3)

    #3:Bulid the model
    Classifier.fit(features,label)

    #4:test the model
    predictions=Classifier.predict([[1,0]])

    print(predictions)

    if predictions:
        print("you can play")
    else:
        print("No play")

   
    

def main():
   Ret= MarvellousKNeighborsCassifier(r"C:\Users\Onkar Ople\Desktop\PlayPredictor.csv")

   
   

if __name__ =="__main__":
    main()