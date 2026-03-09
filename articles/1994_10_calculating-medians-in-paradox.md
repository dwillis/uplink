# Tech Tips: Calculating medians in Paradox

**By Ray Robinson**
*The Press of Atlantic City*

Any database software can easily calculate the average of a numeric field. But sometimes a few extremely high values skew the average.

We ran into that with the income field of the Home Mortgage Disclosure Act data for New Jersey. Our MSA, due to some extremely high incomes, was showing the average loan applicant with an income of more than $84,000 per year.

When the average is skewed, you can often get a more representative number by calculating the median. That's a little more difficult than calculating an average. Here's how it's done in Paradox 4.0:

1. Query your table, marking the following fields: the field you want to group by; the field you want to calculate as a median (be sure to mark this field with Alt-F6, rather than just F6, so it will include duplicate values in the answer). Rename the answer table to save it.

2. Sort the table in ascending order, making the median field the last sort field.

3. Restructure the table, adding a numeric field called RECNO.

4. Insert the record number Paradox has assigned to each record into the new field. Here's the code:

```
EDIT "Tablename"
MOVETO [RECNO]
SCAN
[] = RECNO()
ENDSCAN
DO_IT!
```

5. Query the resulting table to mark the grouping field and do a CALC AVERAGE on the RECNO field. Rename the answer table to save it.

6. The resulting table will have each value in the grouping field with an average in the RECNO field. Now you need to strip the decimal places off the averages in RECNO. Here's the code:

```
EDIT "Tablename"
SCAN
IF ([Average of Recno] - Int([Average of Recno])) > 0
THEN [Average of Recno] = Int([Average of Recno])
COPYTOARRAY arecord
DOWN
INS
COPYFROMARRAY arecord
[Average of Recno] = [Average of Recno] + 1
ENDIF
ENDSCAN
DO_IT!
```

7. Now set up a multi-line query as follows: In the new table, put an example element in the Average of Recno field. In the earlier table, put the same example element in the Recno field. Mark the grouping field in that table.

And in the field you want to calculate as a median, type CALC AVERAGE AS MEDIAN.

The resulting table should display each value in the grouping field with a median value.

Yes, it's a headache. And if you only have one median to figure, it's obviously easier to sort the original table and scroll down to the record number that falls in the middle. But if you want to calculate the median for a number of different groups, it's worth it.

*— Ray Robinson, (609) 272-7273; Primary: 73203.3644@compuserve.com; Secondary: acpress@acy.digex.net*
