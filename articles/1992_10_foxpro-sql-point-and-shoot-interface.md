# Tech Tips: FoxPro adds a new dimension to SQL

*FoxPro's Point and Shoot SQL Interface can smooth the way for beginners.*

The great thing about Structured Query Language is that it is simple, powerful and for the most part, easy. Beginners can get started quickly, and pros can go as fast as they need to. It's no surprise that SQL has been adopted by reporters enthusiastically.

For the first stage of a program of computer-assisted reporting, SQL releases the power of the highly-motivated individuals who are driving the effort. But after a small cadre of reporters has hit a few home runs, knowledge must spread throughout the newsroom in order to avoid a bottleneck. That's why training eventually becomes one of the top, if not the top priority to ensure the success of a program of computer-assisted reporting.

For those news organizations using FoxPro Version 2.0, the Relational Query By Example interface provides a tremendous tool for teaching SQL to beginners. No matter how easy SQL may seem to the initiated, beginners need, and should have, as much help as possible.

What the Relational Query By Example interface does is provide a point and shoot menu interface for SQL. For each portion of the SQL statement, the user chooses from a menu instead of typing the command. For the seasoned SQL programmer, this may seem awkward at first. I know it did for me, but now I write almost all of my SQL statements using RQBE.

The benefit for beginners is that they don't have to sit there facing a SELECT statement, wondering what to type next. With the RQBE interface, they can play around and use menus to build the statement they want as follows.

To enter the RQBE interface, a FoxPro user creates a new query file by choosing New from the file menu and specifying the file type as Query. This displays the interface screen depicted in the diagram.

When FoxPro creates the query, it assumes that whichever database is open will be the subject of the query. If this isn't the correct database, then it can be cleared from the screen, and another database can be added from a menu of all available databases. If a database named "DB1" were open, then that database would be used for the query and its fields would be displayed in the Select Fields window.

The user can change which fields appear in the query, or to choose various functions, such as SUM, AVG, COUNT, etc.

When a user adds a second database to the query, say "DB2" FoxPro pops up a menu-driven interface to the WHERE clause. Instead of typing in WHERE DB2.IDNUM = DB1.IDNUM, the WHERE interface allows a user to point and shoot. First a menu of all the fields in the DB2 database is presented so the user can select the appropriate field to join the databases together. Then the user selects the comparison operator, (LIKE or =, EXACTLY LIKE or ==, etc.), and finally a menu of fields from the DB1 database appears.

After the WHERE menu has been filled out, the where clause will appear in the large box at the bottom left of the screen. Also, all of the fields in the DB2 database will appear when the Select Fields menu is chosen. The same style interface is available for the ORDER BY, GROUP BY and HAVING clauses.

The menus are nice for queries that use several databases, because the job of placing the alias tags that identify which field belongs to which database is handled automatically.

When I first started to use this interface, I balked because I thought that it was a replacement for SQL, not a way to learn it. As soon as I clicked on the See SQL box, I realized I was wrong. Clicking on this box displays the SQL query built by the interface. A beginner can point and shoot for a while, then look at the SQL that he or she has created.

Once the query has been completed, then it can be executed. The output can be directed to a temporary database for browsing, a permanent database for later use, or a report for printing.

*The mouse-driven interface of FoxPro's Point and Shoot makes using SQL easy, even for beginners.*

*DAN WOODS is a reporter at The Raleigh, (N.C.) News & Observer.*
