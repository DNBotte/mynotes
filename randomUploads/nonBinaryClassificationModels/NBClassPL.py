# Same model but beefed up
# NLP text classification pipeline for messy business/vendor descriptions

import os
import re
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ----------------------------
# Part I: Load Training Data
# ----------------------------

filepath_dict = {
    'first':  'data/subbed/first.csv',
    'second': 'data/subbed/second.csv',
    'third':  'data/subbed/third.csv'
}

df_list = []

for source, filepath in filepath_dict.items():
    df_temp = pd.read_csv(filepath, names=['sentence', 'label'], sep=',')
    df_temp['source'] = source
    df_list.append(df_temp)

df = pd.concat(df_list, ignore_index=True)

df['sentence'] = df['sentence'].fillna('')
df['label'] = df['label'].astype(str)

print("Training rows:", len(df))
print("Labels:", df['label'].nunique())
print(df.head())


# ----------------------------
# Part II: Text Normalization
# ----------------------------

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'&', ' and ', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


df['clean_sentence'] = df['sentence'].apply(clean_text)


# ----------------------------
# Part III: Train/Test Split
# ----------------------------

sentences = df['clean_sentence'].values
labels = df['label'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(
    sentences,
    labels,
    test_size=0.25,
    random_state=1000,
    stratify=labels
)


# ----------------------------
# Part IV: NLP + ML Pipeline
# ----------------------------

model = Pipeline([
    ('features', FeatureUnion([
        ('word_tfidf', TfidfVectorizer(
            analyzer='word',
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95,
            sublinear_tf=True
        )),
        ('char_tfidf', TfidfVectorizer(
            analyzer='char_wb',
            ngram_range=(3, 5),
            min_df=2,
            sublinear_tf=True
        ))
    ])),
    ('classifier', LogisticRegression(
        max_iter=1000,
        class_weight='balanced',
        solver='liblinear'
    ))
])

model.fit(sentences_train, y_train)


# ----------------------------
# Part V: Evaluation
# ----------------------------

predictions = model.predict(sentences_test)

accuracy = accuracy_score(y_test, predictions)

print("\nOverall Accuracy:", round(accuracy, 4))
print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


# ----------------------------
# Part VI: Source-Level Testing
# ----------------------------

print("\nAccuracy by source:")

for source in df['source'].unique():
    df_source = df[df['source'] == source].copy()

    if len(df_source) < 5:
        continue

    source_sentences = df_source['clean_sentence'].values
    source_labels = df_source['label'].values

    source_predictions = model.predict(source_sentences)
    source_accuracy = accuracy_score(source_labels, source_predictions)

    print('{} accuracy: {:.4f}'.format(source, source_accuracy))


# ----------------------------
# Part VII: Save Model
# ----------------------------

os.makedirs('models', exist_ok=True)

model_path = 'models/business_category_classifier.joblib'
joblib.dump(model, model_path)

print("\nModel saved to:", model_path)


# ----------------------------
# Part VIII: Application Dataset
# ----------------------------

filepath_dict = {
    'noSubs': 'data/notSubbed/noSubs.csv'
}

df_no_sub_list = []

for source, filepath in filepath_dict.items():
    df_temp = pd.read_csv(filepath, names=['sentence'])
    df_temp['source'] = source
    df_no_sub_list.append(df_temp)

df_no_sub = pd.concat(df_no_sub_list, ignore_index=True)

df_no_sub['sentence'] = df_no_sub['sentence'].fillna('')
df_no_sub['clean_sentence'] = df_no_sub['sentence'].apply(clean_text)


# ----------------------------
# Part IX: Predict Categories
# ----------------------------

df_no_sub['predicted_label'] = model.predict(df_no_sub['clean_sentence'])

prediction_probabilities = model.predict_proba(df_no_sub['clean_sentence'])
df_no_sub['prediction_confidence'] = prediction_probabilities.max(axis=1)

df_no_sub = df_no_sub.sort_values(
    by='prediction_confidence',
    ascending=False
)


# ----------------------------
# Part X: Export Results
# ----------------------------

os.makedirs('data/output', exist_ok=True)

output_path = 'data/output/noSubs_classified.csv'

df_no_sub[[
    'sentence',
    'predicted_label',
    'prediction_confidence',
    'source'
]].to_csv(output_path, index=False)

print("\nPredictions exported to:", output_path)
print("\nSample predictions:")
print(df_no_sub.head(10))

print("\nExecuted")
