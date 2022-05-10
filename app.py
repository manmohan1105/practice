print("hello")
print("this is a change 1")
print("this is some change")
import pandas as pd

class File_Outer_Join():
    
    def __init__(self):
          self.file_name1='emp_contact.csv'
          self.file_name2='emp_core.csv'

    def joiner(self):
        # reading csv files
        data1 = pd.read_csv(self.file_name1)
        data2 = pd.read_csv(self.file_name2)
  
        # using merge function by setting how='outer'
        output_file_data = pd.merge(data1, data2,on='EMPLOYEE_ID',how='outer')
        output_file_data.to_csv (r'./export_dataframe.csv')

if __name__=="__main__":
   obj=File_Outer_Join()
   obj.joiner()
