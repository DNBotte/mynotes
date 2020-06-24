### Execute a Python script from MS Access AND wait until finished running

```vba
Option Compare Database

Sub helloWorld()

    Dim wsh As Object
    Set wsh = VBA.CreateObject("WScript.Shell")
    Dim waitOnReturn As Boolean: waitOnReturn = True ' WAIT UNTIL PYTHON IS DONE
    Dim windowStyle As Integer: windowStyle = 1

    wsh.Run "C:\Users\user.name\AppData\Local\Programs\Python\Python38\python.exe C:\Users\user.name\Documents\test.py", windowStyle, waitOnReturn

    ' src for above: https://stackoverflow.com/questions/15951837/wait-for-shell-command-to-complete

    'RetVal = Shell("C:\Users\user.name\AppData\Local\Programs\Python\Python38\python.exe" & "C:\Users\user.name\Documents\test.py")
    ' below works, above does not
    'Shell ("C:\Users\user.name\AppData\Local\Programs\Python\Python38\python.exe C:\Users\user.name\Documents\test.py")
    ' src for above: https://old.reddit.com/r/vba/comments/5dvk9w/calling_python_script_from_vba/


    DoCmd.SetWarnings False

    DoCmd.OpenQuery "qryRevByProduct"

    DoCmd.SetWarnings True

    Call tblOverwrite

End Sub
```
