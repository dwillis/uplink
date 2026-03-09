# Advanced Seminar: Client/Server Solutions

**By George Landau
NewsEngin Inc.**

Take a dozen experienced CAR jockeys from around the nation, lock them in a NICAR computer lab for three days at the mercy of two hard-core data wonks, and what do you get?

For starters, you get a dozen CAR jockeys who can install and maintain a Web-based, client/server data warehouse for their newsrooms. And you get to brag about the successful inaugural run of NICAR's advanced seminar.

The advanced seminar arose from a basic question that our crowd has been wrestling with for quite a while: how can CAR specialists manage their valuable data so that the newsroom can perform basic queries without bugging the specialist, and perform fancier queries without a lot of logistical hassles and network slowdowns?

The answer is a client/server database manager with a Web interface. For this particular seminar, the teachers – myself and Tom Torok of the *Philadelphia Inquirer* – instructed our colleagues in the 100% Microsoft solution that consists of Windows NT as the operating system, SQL Server as the database manager, and Internet Information Server (IIS) as the Web server. This all-Microsoft lineup is certainly not the only way to go, but Torok and I believe it provides a strong combination of low-cost, high-performance and predictable results. Besides, what journalist really wants to learn UNIX?

## Day One

We began with an hour-long discussion of client/server databases and Web technology – why they make sense for sharing data within a newsroom. The idea behind client/server is that the database queries run on a beefy PC (the server), which accepts commands over a network in the form of SQL statements. The server executes the SQL statement and passes only the results back over the network to the user (the client). The client software can be a Web browser or a desktop data tool like Access, Approach, Paradox or Excel. The client software can use a graphical interface, like a Web form or the Access query builder, to generate the SQL statements; your users don't have to know SQL.

Client/server is generally a better solution than simply putting an Access or FoxPro database on a server and letting your users open the database over the network. While this might work for simple queries on indexed fields, for anything more ambitious it means pumping the entire database through the narrow (and typically congested) pipes of your network. This tends to make the network crawl for everyone else in your newsroom, especially the folks in photo who inevitably need to move several large images at the same time your query is scanning a 1-gigabyte table.

So that they could repeat the process in their own newsrooms, we led the participants through the entire drill of installing Windows NT Server, SQL Server, IIS and the numerous bug fixes ("Service Packs") that Microsoft provides subsequent to any product's release. Fortunately, we hit just enough snags in this process to make for an authentic experience, and by day's end each participant was the new administrator of a fully-loaded NT Server.

## Day Two

We spent the morning learning about security, configuration and administration in NT Server, SQL Server and IIS. We sailed through the creation of SQL Server devices, databases, tables, views and indexes. We dabbled with various settings and discussed ways to maximize performance.

Once we had a grip on SQL Server, we used ODBC (Open Data Base Connectivity) to connect from Microsoft Access to SQL Server over the network. We transferred data from Access to SQL Server using ODBC alone and in combination with SQL Server's BCP (Bulk Copy Program).

With some data on the server, it was time to install a Web interface. NewsEngin provided all seminar participants with an application called UniQuery and a license to deploy it in their newsrooms. UniQuery's greatest value lies in its ability to perform global searches of all the databases on your server. A user can enter a name, address, birthdate, etc.; regardless of the database the information is in, UniQuery will find it.

---

*The advanced seminar drew a sellout crowd from the San Jose Mercury News, USA Today, Detroit Free Press, Baltimore Sun, Daily Oklahoman, Lexington Herald-Leader, Associated Press and WCCO-TV in Minneapolis.*

*George Landau and Tom Torok will repeat their seminar on Web applications with NT and SQL Server this summer, August 14-17. For more information or to register, contact Katy Fanning at (573) 882-0684.*
