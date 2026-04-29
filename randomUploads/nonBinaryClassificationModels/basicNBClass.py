# Backing up scripts found on an old pc
# I think this is one of the earlier prototypes of a
# Non-Binary Classification Model
# Intended for 185 different classes

# Part I:       Load Train & Test Data

import pandas as pd

filepath_dict = {'first':   'data/subbed/first.csv',
                 'second': 'data/subbed/second.csv',
                 'third':   'data/subbed/third.csv'}

df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep=',')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
print(df.iloc[0])

# PART II:      Build Vocabulary

from sklearn.model_selection import train_test_split

df_yelp = df[df['source'] == 'first']

sentences = df_yelp['sentence'].values
y = df_yelp['label'].values

sentences_train, sentences_test, y_train, y_test =
train_test_split(sentences, y, test_size=0.25, random_state=1000)

#

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
X_train

#

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)

print("Accuracy:", score)

#

for source in df['source'].unique():
    df_source = df[df['source'] == source]
    sentences = df_source['sentence'].values
    y = df_source['label'].values

    sentences_train, sentences_test, y_train, y_test =
train_test_split(sentences, y, test_size=0.25, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(sentences_train)
    X_train = vectorizer.transform(sentences_train)
    X_test  = vectorizer.transform(sentences_test)

    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    score = classifier.score(X_test, y_test)
    print('Accuracy for {} data: {:.4f}'.format(source, score))


#############
# Application
#############

# save trainTest dataframe

df0 = df

# import application dataset

filepath_dict = {'noSubs':   'data/notSubbed/noSubs.csv'}

df_noSub = []

for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence'])
    df['source'] = source  # Add another column filled with the source name
    df_noSub.append(df)

df = pd.concat(df_noSub)
print(df.iloc[0])

#

print('executed')
