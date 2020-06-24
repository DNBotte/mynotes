### Call An Access Mod's SubRoutine from Excel VBA

```vba
Sub RunAccdbMod()

Dim acObj As Object
Set acObj = CreateObject("Access.Application")
acObj.Application.Visible = True

' 1st String: location and name of db
' 2nd String: name of module
acObj.OpenCurrentDatabase "C:\Users\user.name\filePath\fileName.accdb", , "mod_Name"

' name of SubRoutine to be called
acObj.Application.Run "SubName"

End Sub
```
