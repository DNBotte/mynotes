# MISCELLANEOUS FORMULAE

### Display Date Values

=DATEVALUE("DD/MM/YYYY")

### Display Date if Cell Not Empty

=IF(B2<>"",DATEVALUE("DD/MM/YYYY"),"")

### Value Entered Prior to Present Day:

=IF(R2<TODAY(),1,0)

### Custom Duplicate

=IF(J8=J7,1,0)

### Look Up Functions

### VLOOKUP

see [formulas/VLOOKUP](https://github.com/DNBotte/mynotes/edit/master/msOffice/excel/formulas/VLOOKUP.md)

### HLOOKUP

### Is it not a number?

=ISERROR(VALUE(D2))

If D2 = 123 --> FALSE
elseIf D2 = 123ABC --> TRUE

LOOKUP

Alternatively: INDEX MATCH

### HYPERLINK

=HYPERLINK(A1)
=HYPERLINK(A1,B1) where B1 is the name to be displayed

### Segmented Hyperlink

=HYPERLINK(CONCATENATE(A1,C1),B1)
=HYPERLINK(CONCATENATE("http://davidnbotte.space",C1),B1)

### Split String of "firstName lastName [additional text]" into usable Outlook format of "lastName, firstName; "

=CONCATENATE(MID(E2,FIND(" ",E2)+1,FIND(" ",E2,FIND(" ",E2)+1)-FIND(" ",E2)),", ",LEFT(E2,(FIND(" ",E2,1)-1)),"; ")

BreakDown:

Original string in cell E2
Grab lastName with:

=MID(E2,FIND(" ",E2)+1,FIND(" ",E2,FIND(" ",E2)+1)-FIND(" ",E2)

Grab firstName with:

=LEFT(E2,(FIND(" ",E2,1)-1)

Concatenate commas and semicolon for Outlook format


=LEFT(E2,(FIND(" ",E2,1)-1))
