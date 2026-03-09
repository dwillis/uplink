# Editing Data for Consistency

## Tech Tips

**By George Landau**
*St. Louis Post-Dispatch*

A lot of data analysis involves grouping and sorting — summing the expense reimbursements to a bunch of employees when you have the employees' names and addresses but not Social Security numbers, for example. Unless you're sure that Joseph Schmo's name is entered the same way for each reimbursement, and that his address is consistently spelled, you won't be able to get reliable totals.

One dependable but very painful way to edit this stuff is to list the various values in a field — names, for example — and manually do search-and-replace on the database until everything's consistent. In FoxPro or another SQL database, you could start like this:

```
select fullname, count(*) ;
from expenses ;
group by 1 ;
order by 1
```

The query would return an alphabetized list of every way that a name is spelled in the entire database, along with the number of times each variation occurs. For example:

| FULLNAME | CNT |
|---|---|
| Landau, George | 7 |
| Landau, George T | 3 |
| Landau, George T. | 2 |
| Landau, George Thomas | 2 |

Let's say you're certain these are all the same George Landau (remember, we can check addresses, also). You want to standardize on the variation with the most info: "George Thomas Landau." To edit these the hard way, you could start typing commands like this:

```
replace all fullname with "Landau, George Thomas" for fullname = "Landau, George"

replace all fullname with "Landau, George Thomas" for fullname = "Landau, George T"

replace all fullname with "Landau, George Thomas" for fullname = "Landau, George T."
```

Fine, but there are 10,000 records in this database. You might not be done for another month. The absolute fastest way out of this mess involves some moderately complex FoxPro programming; if you really want to know, give me a call and I'll tell you how to do it. But without any fancy programming — with only two keyboard macros, really — you can get the job done with a minimum of pain.

**Without any fancy programming — with only two keyboard macros, really — you can get the job done with a minimum of pain.**

Here's how:

1. For reasons that will become clear as you read on, we need to get a list of every unique name into a FoxPro program file (*.prg), which is just a text file that contains a list of commands that will be executed in bulk, as if you had typed them all at once in FoxPro's command box. A query like this will do the job:

```
select fullname ;
from expenses ;
group by 1 ;
order by 1 ;
to file CLEAN1.PRG nowait
```

The last line of this query puts the results into the specified text file, as ordinary ASCII text. The 'nowait' clause prevents the process from halting at every screenful and forcing you to press a key to continue.

2. Now let's edit the "program" you just created by typing in the Command box: `modify command clean1`

3. Delete the first few lines, down to and including the line that contains the field name heading. You'll also notice that each line starts with two spaces of padding, and ends with a lot of padding. We want to get rid of those extra spaces, which we can do by using the Find function off the Edit menu.

First, get rid of all the leading spaces by searching for `\r\n__` (these blanks represent two spaces) and replacing with `\r\n` (`\r\n` is how you specify CarriageReturn-LineFeed in FoxPro's Find dialog box). Then get rid of the trailing spaces by replacing `______\r\n` with `\r\n` a few times; each time you get no matches, specify fewer trailing spaces until all are gone.

This search-and-replace step can be tricky, so don't panic if you don't get it right the first time. Call me if you get stuck.

4. Now we've got a list of every name variation in the database, free of unwanted spaces. Our goal is to record two keyboard macros that will generate a REPLACE command for the names we want to change. Let's say you're looking at these entries again:

```
Landau, George
Landau, George T
Landau, George T.
Landau, George Thomas
```

If you wanted to make the last one (Landau, George Thomas) the standard entry, click the cursor anywhere on that line. Here's where we'll record our first macro. First press shift-F10 to start the macro recorder. Specify a keystroke to assign the macro (I like Ctrl-Z, 'cause I don't use it for anything else). Then click OK. Every key you press from now until you press shift-F10 again will be recorded — mouse movements and clicks will be ignored. Press these keys (things in curly braces represent special keys; don't actually type the braces or the word, just press the key or key-combo):

```
{Home} {Shift+End} {Ctrl+C}
```

Now click shift-F10 again and click OK to stop recording the macro. Now whenever you press Ctrl-Z (or whatever keystroke you specified for the macro), FoxPro will define whatever line the cursor's on and copy all of it to the clipboard.

Now click the cursor on the first line you want to change, "Landau, George." Here's where we'll record our second macro. First press shift-F10 to start the macro recorder. Specify a keystroke to assign the macro (try something physically close to Ctrl-Z or whatever you chose, like Ctrl-A). Then click OK. Once again, every key you press from now until you press shift-F10 again will be recorded — mouse movements and clicks will be ignored. Type these keys and characters (again, things in curly braces are special keys; don't actually type the braces or the word, just press the key or key-combo):

```
{Home}replace all fullname with "{Ctrl+V}" for fullname = "{End}"
```

Then press Shift-F10 again and click OK to stop recording the macro. Now whenever you press Ctrl-A (or whatever keystroke you specified for the second macro), FoxPro will create a command to replace that line's contents with whatever's in the clipboard.

5. Before you get down to business, you should save the macros so that you won't have to re-record them next time you run FoxPro. Pull down the Program menu and choose Macros. You can either save these as part of the default macros, which are loaded whenever FoxPro is run, or under a new name that you can restore manually when you need to.

6. Now for the truly thrilling part. To begin standardizing all those spellings, just position the cursor on an entry that you want to become the standard and click Ctrl-Z (the first macro you recorded). This copies the line to the clipboard. Then click on one of the lines you want changed to the standard, and click Ctrl-A (or the key for the second macro) to create a "replace" command. Do this until you've made it all the way through the file. Then go through and delete any entries that weren't made into a "replace..." command. (Hint: if you're comfortable going back and forth between text files and tables, as I described in the earlier part of this handout dealing with print images, you can append this program into a table and delete all the records that don't start with "replace", then copy it back to a text file).

7. Before you go any further, make a backup copy of the table you're intending to edit.

8. Then open up either the backup or the original and do the program you just created. If you called the file "clean1.prg," you just need to type "do clean1" in the Command box. This program may take a while to run if the database is large, because each "replace" command forces FoxPro to scan through all of the data. At least you're free to do something else, though.

9. When it's done, your data will be standardized. You can now do accurate grouping, summing and sorting.
