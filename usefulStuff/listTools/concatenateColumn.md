How to Concatenate An Excel Column Without A Macro

Plus: Converting it into a JavaScript array

1. =TRANSPOSE(TableName[ColumnName])&", "
2. Ctrl + a
3. F9
4. Ctrl + Home
5. Replace '{' with: =CONCATENATE("var local = [",
6. Ctrl + End
7. Replace ' }' with '"];")'
