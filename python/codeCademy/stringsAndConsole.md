# II. Strings and Console Output

[1. Strings](#1-strings)  
[3. Escaping Characters](#3-escaping-characters)  
[4. Access By Index](#4-access-by-index)  
[5. String Methods](#5-string-methods)  
[9. Dot Notation](#9-dot-notation)
[14. String Formatting with % Part 1](#14-string-formatting-with-percent-part-1)


## 1 Strings

[This conversation on Stack Exchange](https://softwareengineering.stackexchange.com/questions/155176/single-quotes-vs-double-quotes) suggests the following on single- vs double-quotes:

The other answers are correct in that it makes no technical difference, but I have seen one informal style rule on a couple of open-source projects: double quotes are used for strings that might eventually be visible to the user (whether or not they need translation), and single quotes are for strings that relate to the functionality of the code itself (eg. dict keys, regular expressions, SQL).

## 3 Escaping Characters

Use the backslash

```python
>>>print "David\'s notes"
David's notes
```

## 4 Access By Index

Everything is indexed at 0 meaning the 1st character is string[0]

```python
>>>print 'cats'[2]
t
```

## 5 String Methods

len()
lower()
upper()
str()

```python
>>>len('cats')
4

>>>x = 'CATS'
>>>print x.lower()
cats

>>>'cats'.upper()
CATS

>>>str(1)
'1'
```

# 9 Dot Notation

Dot notation methods only work with strings

Other methods can work with other data types
	eg len() and str()
	
# 14 String Formatting with Percent Part 1

```python
>>>myVar = "pizza"
>>>print = "I want %s" % (myVar)
I want pizza
```

Can also put characters right next to it:

```python
>>>print = "I want %s." % (myVar)
I want pizza.
#notice the decimal after %s and pizza
```