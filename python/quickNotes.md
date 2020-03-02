# Notes as going along
Mostly things frequently looked up but never remembered precisely

# Frequently used/forgotten stuff

## PIP WITH MULTIPLE VERSIONS OF PYTHON

eg. Py 2.7 & 3.8 or 3.8x64 & 3.8x32

```CMD
cd C:\Users\user.name\AppData\Local\Programs\Python\Python38-32 pip.exe install pkgName
```

```python
import os
os.system('cmd /k "cd C:\Users\user.name\AppData\Local\Programs\Python\Python38-32"')
# then add pip.exe install pkgName
```

## LOOP BACKWARDS:

```python
>>>for item in L[::-1]:
   ....print item
```

### Notice it uses item and not L[item]
Another example:

```python
>>>x = ['a', 'b', 'c']
>>>for i in x[::-1]:
   ....print i
c
b
a
```
