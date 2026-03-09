# Tech Tips: Getting rid of those pesky duplicate records

**By Elliot Jaspin
Cox Newspapers**

One of life's more vexing problems — along with faulty plumbing and telephone solicitations — is getting rid of duplicate records. You can, of course, use the **DISTINCT** command, but it has its limitations. If you want to eliminate the second record with a duplicate field in a list, **DISTINCT** has no way of distinguishing between which record came first and which came second.

The only alternative, short of manually deleting each record, is to use the programming language that is part of any database software. While the following example is done using the procedural language in XDB, the same approach can be modified to work with PAL in Paradox or any of the xbase products.

Before writing any code to accomplish this task, imagine how you might do this if you were working with a stack of papers instead of electronic records.

You would first sort the records to make sure that the first record you wanted of any duplicates would always appear first. Next you would take the first record off the stack, and compare a key field with the second record. If the two fields matched you would throw away the second record. But if they didn't match, you would save the second record and use it to match against the next record. You would then repeat the process until you had gone through all the records.

While the instructions to the computer will appear different from the way it is described above, the method is the same.

Let us assume our list of records looks like the following table, called Doubles:

| Key | Company | Last | First |
|-----|---------|------|-------|
| 57 | Ajax | Smith | John |
| 44 | Widget | Clinton | Bill |
| 44 | Widget | Roebuck | Bubba |
| 32 | Widget | Wheedle | Skeeter |
| 88 | Rebar | Lybdenum | Molly |
| 88 | Rebar | Stang | Arnold |

The first step is to select a stack of records and sort them according to our criteria. In XDB this means running a select statement and assigning the result to a label.

```
Q1: SELECT * FROM DOUBLES ORDER BY KEY, COMPANY, LAST
```

Just as with our hypothetical stack, you then select the first record and load the comparison value into a variable.

```
FIRST Q1       < This selects the first record, and
COMPVAL = Q1.KEY    < the value in the key field is loaded into compval.
```

Our next step is to select the second record from the list before we begin repeating the process.

```
NEXT Q1
```

To loop through the entire list we can use a **WHILE** statement. In this case the **WHILE** statement is constantly checking to see if the next record grabbed from the list is the last record in the list. In XDB, determining the last record is done by checking the "stat" value. If **STATUS** is "1" then there are still more records. But if the status value changes to "0" we know we have reached the end of the list. What we are saying in the next statement is to keep taking records from the list until there are no more records – until the value of status is "0."

```
WHILE (STATUS[Q1])>0
```

We're now ready to make the actual comparison, using an "if-then-else" statement.

If the two values match then delete the second record, grab another record, make it the comparison value and repeat the process. **ELSE** makes the second record the comparison value.

```
IF COMPVAL = Q1.KEY    < If they match,
DELETE Q1          < delete the second record,
NEXT Q1            < get another record
COMPVAL = Q1 KEY       < make it the comparison value.
ELSE
COMPVAL = Q1 KEY       < Otherwise make the second record the comparison value.
ENDIF
```

Whether we decide to delete a record, the last thing we need to do is get another record.

```
NEXT Q1
```

To repeat the whole process we end this short routine with an **ENDWHILE**. That forces our program to loop back to the **WHILE** statement and repeat the process until, of course, we run out of records.

Note that this method only deletes the first duplicate record. If more than one duplicate exists, another approach must be used.

Now if we could just write a program to prevent salesmen from hawking life insurance by phone. . .

**The only way, short of manually deleting each record, is to use the programming language that is part of any database software.**
