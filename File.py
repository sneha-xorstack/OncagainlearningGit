import pandas as pd


df = pd.read_csv('policy issue must fix.csv')

print(df)

Particular_col = df['Issue location']
print(Particular_col)


def splitfunction(text):
    last_part = text.split('-')
    number_value = last_part[-1]
    print(number_value)
    return number_value
    

output_file = Particular_col.apply(splitfunction)
output_file.to_csv('Op.csv', index= False)









