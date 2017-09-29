# Notes as going along
Mostly things frequently looked up but never remembered precisely

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
