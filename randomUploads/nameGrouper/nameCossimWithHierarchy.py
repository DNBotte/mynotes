import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sparse_dot_topn import awesome_cossim_topn


def analyze_ngrams(name: str, n: int = 5) -> list[str]:
    name = re.sub(r"[,-./]", "", str(name).lower())
    return ["".join(ngram) for ngram in zip(*[name[i:] for i in range(n)])]


class UnionFind:
    def __init__(self, values):
        self.parent = {value: value for value in values}

    def find(self, value):
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a


df_names = pd.read_csv("./nameData.csv")

names = df_names["Entity_Name"].dropna().unique().astype("U")

vectorizer = TfidfVectorizer(analyzer=analyze_ngrams)
tfidf_matrix = vectorizer.fit_transform(names)

cosine_matrix = awesome_cossim_topn(
    tfidf_matrix,
    tfidf_matrix.transpose(),
    ntop=10,
    lower_bound=0.8
)

coordinates = cosine_matrix.tocoo()
uf = UnionFind(names)

for row, col, score in zip(coordinates.row, coordinates.col, coordinates.data):
    if row != col:
        uf.union(names[row], names[col])

entity_lookup = {name: uf.find(name) for name in names}

df_names["entityName"] = (
    df_names["Entity_Name"]
    .map(entity_lookup)
    .fillna(df_names["Entity_Name"])
)

df_names.to_csv("./NameExport.csv", index=False)
