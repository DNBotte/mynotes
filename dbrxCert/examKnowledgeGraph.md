# CREATE A KNOWLEDGE GRAPH-LIKE ONJECT STRUCTURE FOR THE GEN AI EXAM INFO

### Explanation:

I asked anthropic for a hands-on tutorial experience. It started off with a list of exam subjects, topics, and subtopics.
I decided it would be easiest to keep track of them and my progress through them if I were to upload the info into a database.
This will work in a Databricks notebook after setting it to SQL

# PART I: SET UP

## Step 1: Create schema for metadata (if one doesn't already exist)

```sql
CREATE schema meta
```
#### This output is normal:

_sqldf:pyspark.sql.connect.dataframe.DataFrame
OK
This result is stored as _sqldf and can be used in other Python and SQL cells.


## Step 2: Create a table for Gen AI Exam Contents:

```sql
%sql
CREATE OR REPLACE TABLE meta.GAIContents (
  SectionID INT,
  Section   STRING,
  Why       STRING,
  CONSTRAINT pk_gaicontents PRIMARY KEY (SectionID)
);

INSERT INTO meta.GAIContents VALUES
  (1, 'Data Preparation',      'Everything feeds from this — no data, no RAG'),
  (2, 'Application Development','Build the chain that uses the prepared data'),
  (3, 'Assemble & Deploy',     'Wire it all together, Vector Search, MLflow, endpoints'),
  (4, 'Design Applications',   'Easier once you have built one'),
  (5, 'Evaluation & Monitoring','Cannot evaluate what you have not deployed'),
  (6, 'Governance',            'Wraps around everything else');

  -- VERIFY UPLOAD:

  SELECT * FROM meta.gaicontents
```

 ## Step 3: Create a table for the topics of those subjects:

```sql
  %sql
CREATE OR REPLACE TABLE meta.GAITopics (
  TopicID   INT,
  Topic     STRING,
  SectionID INT,
  CONSTRAINT pk_gaitopics PRIMARY KEY (TopicID),
  CONSTRAINT fk_gaitopics_section FOREIGN KEY (SectionID) REFERENCES meta.GAIContents(SectionID)
);

INSERT INTO meta.GAITopics VALUES
  (1, 'Chunking strategies — how to split documents', 1),
  (2, 'Embedding pipelines — chunk to vector to Delta table', 1),
  (3, 'Retrieval evaluation — is your retriever actually working?', 1);

  SELECT * FROM meta.gaitopics
```

## Step 4: table for subtopics:

```sql
%sql
CREATE OR REPLACE TABLE meta.GAISubTopics (
  SubTopicID INT,
  SubTopic   STRING,
  Why        STRING,
  TopicID    INT,
  CONSTRAINT pk_gaisubtopics PRIMARY KEY (SubTopicID),
  CONSTRAINT fk_gaisubtopics_topic FOREIGN KEY (TopicID) REFERENCES meta.GAITopics(TopicID)
);

INSERT INTO meta.GAISubTopics VALUES
  (1, 'Chunking strategies',        'Fixed-size vs semantic vs recursive — exam loves this', 1),
  (2, 'Chunk size / overlap tradeoffs', 'Direct exam question type', 1),
  (3, 'Filtering bad content',      'Remove noise before embedding', 1);

SELECT * FROM meta.gaisubtopics
```

## You might have noticed there are two foreign keys in there corresponding to two (out of three) primary keys.
That's because I mean for this to all be related and work as a progress ledger in addition to being a fancy table of contents out in cyberspace

Unfortunately I hadn't thought of adding in the ledger/marking column while creating the table so that gets added in later (an alter table exercise)

## Step 5: Verify joins work:

```sql
%sql
SELECT 
  c.SectionID,
  c.Section,
  t.TopicID,
  t.Topic,
  s.SubTopicID,
  s.SubTopic,
  s.Why
FROM meta.GAIContents c
JOIN meta.GAITopics t ON c.SectionID = t.SectionID
JOIN meta.GAISubTopics s ON t.TopicID = s.TopicID
ORDER BY c.SectionID, t.TopicID, s.SubTopicID
```

## How to add more subtopics:

```sql
%sql
INSERT INTO meta.gaisubtopics VALUES
(4, 'Embedding models', 'Exam asks you to select based on cost/latency/quality', 2)
```

```sql
%sql
INSERT INTO meta.gaisubtopics VALUES
(5, 'Chunk to vector to Delta table', 'The actual pipeline you will build', 2),
(6, 'Writing to Unity Catalog', 'Exam tests UC-specific patterns', 2)
```

# PART II: Glossary

## Step 1: create and populate

```sql
%sql
CREATE OR REPLACE TABLE meta.dbrxGlossary (
  termID INT,
  term STRING,
  defDBrx STRING,
  defS46 STRING,
  SubTopicID INT,
  CONSTRAINT pk_dbrxglossary PRIMARY KEY (termID),
  CONSTRAINT fk_dbrxglossary_subtopic FOREIGN KEY (SubTopicID) REFERENCES meta.GAISubTopics(SubTopicID)
);

INSERT INTO meta.dbrxGlossary VALUES
  (1, 'embedding', 'A vector representation of a piece of text', 'a chunk converted to a numeric vector hat captures semantic meaning', 3)
```

Validate:

```sql
%sql
SELECT * FROM meta.dbrxglossary
```

Populate (continued):

```sql
%sql
INSERT INTO meta.dbrxGlossary VALUES
  (2, 'embedding pipeline', 'A series of steps to convert text into a vector', NULL , NULL),
  (3, 'embedding model', 'A model that converts text into a vector', 'the model that does that conversion (e.g. all-MiniLM-L6-v2', NULL)
```
```sql
%sql
INSERT INTO meta.dbrxGlossary VALUES 
(6, 'fixed-size splitting', 'The splitting of a dataset into a training and a test set, where the test set is a fixed-size subset of the original dataset', 'brute-force split on one separator', NULL),
(7, 'recursive splitting ', 'algo splits dataset into train/test set', 'tries \n\n to \n to . to ____ in order and respecting structure', NULL),
(8, 'vector', 'dbrx: piece of text; me: embedding array', 'list of floats representing meaning in N-D space', NULL),
(9, 'Delta table', 'table in a delta lake', 'DatabriDBrx  native table format (parquet + transaction log); can store chunks and vectors', NULL),
(10, 'Unity Catalog', 'UC is a cloud-native data governance layer that enables you to share data securely across your organization', 'DBrx governance layer (workspace.meta lives here)', NULL);

SELECT * FROM meta.dbrxGlossary
```
