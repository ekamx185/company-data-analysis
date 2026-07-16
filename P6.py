import pandas as pd 
data = {
    'Name': ['Ekam', 'Jaspinder' ,'Paggu' ,'Manshi'],
    'Age' : [16,17,18],
    'Salary' : [90000,70000,50000]
}
df = pd.DataFrame(data)
print(df)