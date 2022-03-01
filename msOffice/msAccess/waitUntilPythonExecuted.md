### Execute a Python script from MS Access AND wait until finished running

```vba
Option Compare Database

Sub helloWorld()

    Dim wsh As Object
    Set wsh = VBA.CreateObject("WScript.Shell")
    Dim waitOnReturn As Boolean: waitOnReturn = True ' WAIT UNTIL PYTHON IS DONE
    Dim windowStyle As Integer: windowStyle = 1

    wsh.Run "C:\Users\user.name\AppData\Local\Programs\Python\Python38\python.exe C:\Users\user.name\Documents\test.py", windowStyle, waitOnReturn




    DoCmd.SetWarnings False

    DoCmd.OpenQuery "qryRevByProduct"

    DoCmd.SetWarnings True

    Call tblOverwrite

End Sub
```
