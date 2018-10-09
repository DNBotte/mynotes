### Intro to Loops

They work kinda like loops in any other language, resembling python the most

**Index**

### 1. [Basic Loop](#Basic-Loop)

### 2.  [Nested Loop](#Nested-Loop)

1. [Basic Loop](#1-Basic-Loop)

```VBA

Dim i As Integer

For i = 1 To 10
    Cells(i,10).Value = i
Next i

```

Result: cells count 1 to 10 top to bottom

```VBA

Dim  j As Integer

For j = 1 To 10
    Cells(1,j).Value = j
Next j

```
Result: cells count 1 to 10 left to right

2. #Nested-Loop

```VBA

Dim i As Integer, j As Integer

For i = 1 To 10
    For j = 1 To 10
        Cells(i, j).Value = i * 10 + j -10
    Next j
Next i

```

Result: Count top to bottom by column 1 to 100 left to right
