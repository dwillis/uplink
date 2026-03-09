# Tech tips
# Programming? As easy as SQL

**by Richard Mullins**
**National Library on Money & Politics**

OK, this one's about programming, a word that may clash with the usual job description of a reporter. Just like the ideas of data and computers and SQL once did.

Assimilating SQL required something of an attitude adjustment from reporters about their life's calling and how they were to go about fulfilling their mission. This, in spite of the fact that SQL is all about Queries, the Prime Mover of Reporting.

Well, scribblers, while you were cultivating the intellectual traits necessary for writing sharp, database-piercing queries, fertile ground was prepared for programming. Yes, programming. It's been growing up there, inside your skull, though you probably weren't aware of it.

Since you already know so much about programming, this article would be as easy as SELECT * FROM BidRiggers.

I'm going to use the FoxPro environment to talk about programming since it integrates (with a few compromises) SQL and a Fox's version of a standard database programming language called XBase.

You may have also used some FoxPro commands by typing them in the command window: LOCATE, GOTO BOTTOM, INDEX ON, etc. If so, then you know all you need to know to de-mystify Fox Programming. A Fox program is just an ordinary text file with several commands that execute in order when you run the program.

One of the benefits of SQL is that it is a Query Language, not a programming language. That means you use SQL to specify what information you want extracted from the database; you don't have to tell the computer how to do the fetching. But there are things that you may need to do with your data that can't be done with a query language. That's when it's time for programming. Many repetitive data cleanup tasks can be programmed, for example.

The program can take user input, and then proceed based on the answers. A program can save the frustration of remembering the commands and the syntax and typing them correctly. Look them up and type them once, then run the program over and over.

I'll end this part with a very shortened version of a program you can use to cut down, for example, a 500,000 record database to a copy with only 1,000 records. The program extracts or samples every 500th record (500,000 divided by 1,000).

In this shortened form, the program is a slight improvement over typing a few lines in the command window. It would be more useful if you didn't have to go into the program to change the three variables. I'll add this next level -- getting the variables from the user -- in a second part. It would also be more useful if it figured out the skip interval for you, based on your input of how many records you wanted extracted.

The last line needs some explaining. The program language lets you copy ALL records or records satisfying a certain condition. The condition is introduced by the keyword "FOR". Fox and Dbase files keep a record number for every record in a database.

To satisfy the condition for getting copied to the target database, the number that we set as the skip interval (that's 'SkipInt' in the program) should divide evenly into the record number ('recno()' in the program). The 'MOD' function does the division and reports what the remainder is; if it's ZERO, that record is extracted to the target database. (This method is not the only way this could be done. It's the one I thought of when I wrote the program, ad hoc, two years ago.)

Use the built-in text editor in Fox to type in this program. To create or edit a program file: In the command window, type 'modify command xtract'. If the file 'XTRACT.PRG' doesn't already exist, it is created.

To run the program, type 'DO xtract' in the command window.

### Program Listing: XTRACT.PRG

In this simple version, you have to fill in these three variables each time you use the program:

```
SkipInt = 500  && This number sets the extraction interval
SourceDB = " "  && Name of DB to extract from
TargetDB = " "  && Name of DB to copy extracted records

use (SourceDB) in 1 alias source

* make an empty copy of the source DB
copy structure to trim (TargetDB)
* now put the extracted records in it
copy to (TargetDB) for mod( recno(), SkipInt ) = 0
```
