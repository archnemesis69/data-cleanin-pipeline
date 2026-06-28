import pandas as pd
Class DataLoader:
 def __init__(self,file_path):
     self.data=pd.read_csv(file_path)
 def load(self):
     return self.data
 def showshape():
     return self.data.shape
 def showdata(self):
     return self.data.head()
 def save(self):
     self.data.to_csv('data.csv')
def showcolumns(self):
    return self.data.columns

