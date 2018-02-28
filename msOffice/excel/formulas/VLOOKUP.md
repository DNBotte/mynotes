# VLOOKUP

*Used to find one value that's paired with another elsewhere in another range*

### Pre-Requisites:

* Data must be in a named ranged
* A column of values. These are paired with other values in the named range.

Formula: =VLOOKUP

Expanded: =VLOOKUP(lookup value, table array, column index number, boolean)

* *lookup value:* the known value (basically the column to the left)
* *table array:* basically the named range where all the data is (yes, type in the actual name)
* *column index number:* the column with the values trying to get
* *boolean*: use *FALSE* for an exact match