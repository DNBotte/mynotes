Python
Pandas
CodeCademy

1 Creating, Loading, and Selecting Data with Pandas

1.2 How to Create a Dataframe Using a Dictionary

(think of a transposed version of query design mode)

import pandas as pd

df1 = pd.DataFrame({
    'col1' : [fld1.1, fld1.2, ... , fld1.n],
	'col2' : [fld2.1, fld2.1, ... , fld2.n],
	.
	.
	.
	'colm' : [fldm.1, 'fldm.2, ... , fldm.n]
})

# Notes

# Columns require same number of fields

Ex 1:

``` Python
```

Ex 2:

``` Python
```

1.3 How to Create a Datframe Using a List

df2 = pd.DataFrame([
    [fld1.1, fld2.1, ... , fldn.1],
	[fld1.2, fld2.2, ... , fldn.2],
	.
	.
	.
	, [fld1.m, fld2.m, ... , fldm.n]
	],
	
	columns = [
	'col1', 'col2', ... , 'colm'
	]
)

1.5 Reading & writing to csv

dataframeVarName = pd.read_csv('my-csv-file.csv')

df.to_csv('new-csv-file.csv')

1.6 Inspect a DataFrame

print(df) -> prints entire dataframe

df.head() -> 1st 5 rows
df.head(n) -> n rows
df.info() -> stats on df

1.7 Select Columns

colNameVar = df['colName']

series - one dimensional (like a vector?)
dataframe - 2 dimensional (like a SQL table)

1.8 Select Multiple Columns

multiCols = df.[['colA', 'colB']]

NOTE the double square brackets

1.9 Select Rows

dfName.iloc[row#-1]

(rows are zero indexed)

1.10 Select multiple rows

dfName.iloc[startRow-1:stopRow+1]

ex.

happyDF = df.iloc[3:7]

start with 4th row

stop with 6th row

1.11 Row Selection Logic

rowVar = df[df.colName == 'value']

1.12 Row Selection Complex Logic

df[(df.colA <= 'value1') |
    (df.colB != 'value2')]
	
| = or

& = and

1.13 Multi Row Logical Selection

rowVar =  = df[df.month.isin(['tow1',
    'row2',
	'row3'])]
	
1.14 Setting Indeces

df2 = df.reset_index()

creates new & reindex dataframe with an additional column including original index values

df.reset_index(drop=True, inplace=True)

drop=True -> drops the old index vals column

inplace=True -> modifies original dataframe as opposed to requiring a new one in a new variable

2.2 Add Colmumn

df['Column Name'] = [val1, val2, ... , valn]

2.3 Add Column of equal values

df['Column Name'] = value

2.4  Add Column with Operands

df['colName'] = df.colA*2
df['colName'] = df.colB + 10
df['colName'] = df.colA - df['spacey column name']

2.5 Column Operations


df['newCol'] = df.colName.apply(functionOrMethodExcludingItsParenAndParam)
^that works
Does not seem to be working in py3

Up to date documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html

2.6 Lambda Review

myLambda = lambda x, y: x * 2 + y
lamb = lambda x: x.lower()
lastAndFirst = lambda n: n[len(n)-1] + n[0]

>>>lambo = df.Email.apply( lambda x: x.split('@')[-1] )
>>>lambo(first.last@email.com)
'email.com'


>>> lamb("BAHHHHHHHH")
"bahhhhhhh"

2.7 iffy lambs

temp = lambda x, s: (x - 32) * 5 / 9 if s.lower() == 'f' else x * 9 / 5 + 32

2.8

should practice this more

get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)