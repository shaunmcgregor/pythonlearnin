import pandas
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Batting/test.csv')
data = pandas.read_csv(filename)

print(data.columns)
#data.items.