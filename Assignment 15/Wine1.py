from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd


def MarvellousKNeighborsCassifier():
    Dataset=pd.read_csv(r"WinePredictor.csv")     #1 load the data
    df=pd.DataFrame(Dataset,columns=['Class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline'])
    data=df[['Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']]
    target=df[["Class"]]




    #2:manipulate the data
    Data_train,Data_test, Target_train,Target_test=train_test_split(data,target,test_size=0.7)   #divide the data in four set

    Classifier=KNeighborsClassifier(n_neighbors=3)

    #3:Bulid the model
    Classifier.fit(Data_train,Target_train)

    #4:test the model
    predictions=Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,predictions)

    #5:Improve---Missing

    return Accuracy

    

def main():
   Ret= MarvellousKNeighborsCassifier()

   print("Accuracy of Wine dataset with KNN is:",Ret*100)
   

if __name__ =="__main__":
    main()