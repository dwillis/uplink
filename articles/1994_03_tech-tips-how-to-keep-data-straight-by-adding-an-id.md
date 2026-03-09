## Tech Tips: How to Keep Data Straight by Adding an ID

**By Richard Mullins, University of Missouri**

Every data table you work with should have rows that are unique. Duplicates can be confusing, for one thing, because you never know if the duplicate row belongs there. (Did Richard Mullins bounce a check twice, or did a data clerk just type it in twice?)

This uniqueness rule is not just a good idea, it's the law, at least according to relational theory. Most often this is a number, in a column called ID, (or Casenum, Case# or CaseNo).

But we all know that there are lots of databases and data creators that overlook this. You may have done it too, in your young and foolish days.

Here's how to right the wrong and be sure every row in a table is uniquely identified. The commands are for FoxPro or dBase.

After you've created a new field to hold the number (make sure it's NUMERIC and big enough to hold the largest number that might be put there), type this command in the Command Window: (The field or column name here is ID)

`REPLACE ALL id WITH RECNO( )`

That's it. This one-line command works because Fox stores internally a number for every row, or record, in the table. The REPLACE...WITH command puts that number (supplied by RECNO( ), a built-in function) in a field where you can see it. The command word ALL makes the replacement on every row.

Here's one more twist on this command, if you want to start the ID numbers with a larger number. You can add another number, say 1000, to the internal record number. Then your ID numbers would start at 1000, instead of one. Here's the command:

`REPLACE ALL id WITH RECNO( ) + 1000`
