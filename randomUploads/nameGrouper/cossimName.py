# Not Sure Which Version this Prototype Is

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sparse_dot_topn import awesome_cossim_topn

dfNames = pd.read_csv('./nameData.csv')
allNames = {}


def analyzeNGrams(acctName):
    acctName = re.sub(r'[,-./]', r'', acctName)
    ngrams = zip(*[acctName[i:] for i in range(5)])  # N-Gram length is 5
    return [''.join(ngram) for ngram in ngrams]

def lookupName(record, field):
    if record in allNames:
        return allNames[record]
    elif field in allNames:
        return allNames[field]
    else:
        return None


def appendLookupVals(entityName, record, field):
    allNames[record] = entityName
    allNames[field] = entityName


def appendLookupMatch(record, field):
    entityName = lookupName(record, field)
    if entityName is not None:
        appendLookupVals(entityName, record, field)
    else:
        appendLookupVals(record, record, field)


vectorizer = TfidfVectorizer(analyzer=analyzeNGrams)
vals = dfNames['Entity_Name'].unique().astype('U')
matrixTFIDF = vectorizer.fit_transform(vals)
matrixCosine = awesome_cossim_topn(matrixTFIDF, matrixTFIDF.transpose(), vals.size, 0.8)
matrixCoordinates = matrixCosine.tocoo()

for row, col in zip(matrixCoordinates.row, matrixCoordinates.col):
    if row != col:
        appendLookupMatch(vals[row], vals[col])

dfNames['entityName'] = dfNames['Entity_Name'].map(allNames).fillna(dfNames['Entity_Name'])
dfNames.to_csv('./NameExport.csv')
