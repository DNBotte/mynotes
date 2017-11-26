# Sets Data Fields of Pivot Tables to Average
(set as sum by default)

1. Click on cell in table
2. Open VBE with Ctrl + F11 or Developer > Visual Basic (icon on far left of ribbon)
3. Click Insert Module
4. Paste the following into editor:

```vba
Public Sub SetDataFieldsToAverage()
'Update 20141127
Dim xPF As PivotField
Dim WorkRng As Range
Set WorkRng = Application.Selection
With WorkRng.PivotTable
   .ManualUpdate = True
   For Each xPF In .DataFields
      With xPF
         .Function = xlAverage
         .NumberFormat = "#,##0"
      End With
   Next
   .ManualUpdate = False
End With
End Sub
```

### Changing Average to other functions:

Replace any instance of "Average" with the necessary function.
