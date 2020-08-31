import pandas as pd
pd.set_option('display.max_colwidth', None)


jeopardy = pd.read_csv('jeopardy.csv')

jeopardy.rename(columns={
 ' Show Number' : 'Show Number',
 ' Air Date' : 'Air Date',
 ' Round' : 'Round',
 ' Category' : 'Category',
 ' Value' : 'Value',
 ' Question' : 'Question',
 ' Answer' : 'Answer'
})

print(jeopardy.head(10))
