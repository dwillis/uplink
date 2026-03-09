### Tech tips
## Getting your program to talk back

**By Richard Mullins**

Our last tech tip illustrated something you can do with a simple database program that you can't do with a query: jump through a table at a certain interval, say every 11th or 531st record, and then copy that record to another table. The extracted version would be a small version of the original. And if the records in the parent table were unordered, then the extracted records would be a genuinely random sample.

When I made the program, I just needed a small slice of a large table. I wanted to test my queries on the small table, since they would execute faster, then do them on the larger table when I got them right.

A shorter version of the program was printed in *Uplink* in the September 1993 issue. It worked fine, but you had to edit the variable parts of it — the Skip Interval, the Source Table Name, the Target Table Name — every time you wanted it to slice a different table to a different size and a different name. That can be just a slight inconvenience for a knowledgeable user, but it's a barrier to less experienced users.

So we'll add some code to the program so it will ask the human at the keyboard what database to extract from and where to put the extracted records.

The lines beginning with asterisks are comments. The program ignores them, so you don't need to type them for the program to work, but they're important to you. They help you remember how the program was written, how it works, and anything you'll need to know when you look at the program code a month or a year later.

To create a program file, go to the command window and type: `modify command xtract`

This opens up the Fox text editor. Type in the program as it's printed here. When you're done, pull down the FILE menu, choose CLOSE, and answer YES to the Save Changes Dialog Box.

The program begins with defining the variables to be used. We give them an empty value (zero, or a string of spaces) to start with:

```
* Set up the variables
nExtract = 0
TargetDB = space(30)
SourceDB = space(30)
```

The next part puts up a prompt, a space to accept the answer and then stores that answer. The command to get user input is the "@ ... SAY ... GET ... READ" sequence. This and all other Fox commands can be looked up in the manual or in the on-screen help directory. But here is a brief explanation:

The At-sign (@) sets the screen position (row, column).

The part in quotes is the prompt.

The name after the keyword "get" is where the program stores the answer.

The two answers are plugged into the command to open the databases.

The "alias" lets you give the databases a temporary nickname.

```
* Ask user for input
@ 8,5 say "Source DB? " get SourceDB
read
* Open the Source database
use (SourceDB) in 1 alias source
@10,5 say "Target DB? " get TargetDB
read
* create an empty Target Database
copy structure to (TargetDB)
```

The next part looks complicated, but it helps the user. Before asking how many records to extract, it helps to know how many records there are. Make sure you get all the nested parentheses typed in.

```
* Now put up info for user and get input
@12,5 say "There are " + alltrim( str(reccount ("source"))) + ;
" records in " + SourceDB
```

The program works by skipping over a defined number of records, copying one, skipping the defined number, copying one, and so on to the end. Here the program displays the record count, then asks the user how many records should be extracted. Based on the answer, it figures the Skip Interval to yield that number.

```
@13,5 say "Extract how many records?" get nExtract
read
nSkipInt = int ( reccount("source") / nExtract)
```

Now everything is ready to roll. It helps to let users know that something is really happening, so we'll clear the screen and put up a message.

```
@8,0 clear to 15,70
@12,5 say "Extracting records..."
* Here's where the work is done...
select source
copy to (TargetDB) for mod( recno(), nSkipInt ) = 0
@12,5 say "Done. "
```

The "copy to" line, roughly translated, says: "Copy records to the Target database where the record number is evenly divisible by the Skip Interval the user typed in." Here's how the arithmetic works: The `mod()` function finds the remainder from dividing two numbers; in this case it's the internal record number divided by the Skip Interval. If the remainder is zero, then the record is copied to the Target table.
