# Tech Tip: Switching from FoxPro to Access

### By Richard Mullins
### University of Missouri/NICAR

Some journalists love FoxPro; others just use it. But no one believes it's pretty or the easiest to learn. And when some former FoxPro users discover Microsoft's Access, they begin harboring thoughts of revenge against those who told them FoxPro was the way to go.

It's the nature of computer-industry progress that we eventually have to switch, grudgingly, from our favorite, trusted, workhorse software to something newer. The reasons and timing vary. In FoxPro and Access, one contributing factor is that version FoxPro 2.6 is no longer being sold. Its successor, Visual FoxPro 3, has taken great steps in the Access direction.

If you're making the switch, or better yet, starting to use Access for much of your work, but still using FoxPro for larger tasks, here's a guide to the conversion. I'll deal with important differences, syntax and SQL differences, and features to take advantage of. When I use the name FoxPro, I'm referring to version 2.6, or all versions up to that one. For Access, I'm talking about version 2.0.

### Important differences

**Terms: Databases, Tables and Objects:** In FoxPro, the words **table** and **database** are used interchangeably. Access conforms to the relational terminology: A **database** is a collection of **related tables**. Actually, it goes further than that: An Access database is a collection of related **objects**.

Not knowing this can create some confusion when you start creating or importing tables in Access. In FoxPro, every table, every query, every index is a separate file on the computer hard disk. Access, on the other hand, uses one Database file (*.mdb) to hold things it calls objects: tables, queries, forms, reports, macros, modules. It presents these objects to the user with a file cabinet metaphor.

For a database called **housing**, your directory listing shows a file called **housing.mdb**. On the inside, when Access opens this database file, there may be five tables, 12 stored queries and three data entry forms.

**Character field length storage:** The width of a text or character field in Access only defines the limit of what it will hold; long field lengths do not waste space in Access. This is the opposite of FoxPro, which consumes the same amount of disk space for an empty 50-character field as for a full one.

**MDB file sizes:** The file size of an Access database increases as you add to it, but does not contract if you delete tables and rows. Use the **Compact Database...** command, under the File menu when no database is open to reclaim disk space after making substantial deletions.

**Making Queries:** The best part is that you can type SQL to make queries in Access.
