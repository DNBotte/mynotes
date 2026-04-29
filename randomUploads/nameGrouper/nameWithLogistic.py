# Not sure if this is the version that worked

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sparse_dot_topn import awesome_cossim_topn

dfNames = pd.read_csv('./nameData.csv')
allNames = {}


def analyzeNGrams(acctName):
    acctName = re.sub(r'[,-./]', r'', acctName)
    ngrams = zip(*[acctName[i:] for i in range(5)])  # N-Gram length is 5
    return [''.join(ngram) for ngram in ngrams]


def normalizeName(name):
    name = str(name).lower()
    name = re.sub(r'[,-./]', r'', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def calcTokenOverlap(record, field):
    recordTokens = set(normalizeName(record).split())
    fieldTokens = set(normalizeName(field).split())

    if len(recordTokens) == 0 or len(fieldTokens) == 0:
        return 0

    return len(recordTokens.intersection(fieldTokens)) / len(recordTokens.union(fieldTokens))


def calcLengthDifference(record, field):
    return abs(len(normalizeName(record)) - len(normalizeName(field)))


def calcExactNormalizedMatch(record, field):
    if normalizeName(record) == normalizeName(field):
        return 1
    else:
        return 0


def buildMatchFeatures(record, field, cosineScore):
    return [
        cosineScore,
        calcTokenOverlap(record, field),
        calcLengthDifference(record, field),
        calcExactNormalizedMatch(record, field)
    ]


def getCosineScore(record, field, vectorizer):
    pairMatrix = vectorizer.transform([record, field])
    cosineScore = pairMatrix[0].dot(pairMatrix[1].transpose())[0, 0]
    return cosineScore


def trainNameMatchModel(trainingFilePath, vectorizer):
    dfTraining = pd.read_csv(trainingFilePath)

    xTrain = []

    for row in dfTraining.itertuples(index=False):
        cosineScore = getCosineScore(row.record, row.field, vectorizer)
        features = buildMatchFeatures(row.record, row.field, cosineScore)
        xTrain.append(features)

    yTrain = dfTraining['is_match']

    model = LogisticRegression()
    model.fit(xTrain, yTrain)

    return model


def isLikelyNameMatch(model, record, field, cosineScore, probabilityThreshold=0.70):
    if model is None:
        return True

    features = [buildMatchFeatures(record, field, cosineScore)]
    matchProbability = model.predict_proba(features)[0][1]

    return matchProbability >= probabilityThreshold


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

nameMatchModel = None

try:
    nameMatchModel = trainNameMatchModel('./nameMatchTraining.csv', vectorizer)
except FileNotFoundError:
    nameMatchModel = None

matrixCosine = awesome_cossim_topn(matrixTFIDF, matrixTFIDF.transpose(), vals.size, 0.8)
matrixCoordinates = matrixCosine.tocoo()

for row, col, score in zip(matrixCoordinates.row, matrixCoordinates.col, matrixCoordinates.data):
    if row != col:
        if isLikelyNameMatch(nameMatchModel, vals[row], vals[col], score):
            appendLookupMatch(vals[row], vals[col])

dfNames['entityName'] = dfNames['Entity_Name'].map(allNames).fillna(dfNames['Entity_Name'])
dfNames.to_csv('./NameExport.csv', index=False)
