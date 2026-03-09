# Simplifying Database Full-Text Searches

*Open Source*

By Brad Heath, *The Detroit News*

One of the most important things you can do in your newsroom is spread the wealth of information. But finding a way to let other reporters and editors get the data they need, whenever they need it, is a challenge. The easiest way to do it is on your company's intranet — but most of the tools are cumbersome or expensive.

Here is my solution.

OpenInfo is a collection of intranet scripts you can use to run simple, full-text searches across dozens of newsroom databases simultaneously. You can add data to the site with a few minutes of work, instead of spending hours writing new search forms. You can customize it to help people in your newsroom find information most relevant to them, with easy searches and automatic cross-referencing of records. Users who want to go deeper will find forms they can use to run advanced searches or write data queries (without having to know Structured Query Language).

Best of all, it runs entirely on open-source platforms (an Apache Web server, a MySQL database server and the PHP scripting language). If you already have the hardware, you can get the whole package set up in an afternoon, at no cost. And because it relies on MySQL to do the heavy lifting, it can easily accommodate searches of millions of records. (I have used it on one server with almost 70 million records spread across 60 tables.)

Download the OpenInfo file from *www.nicar.org/downloads.*

Once you provide OpenInfo with basic information about what kinds of data are stored in your table, it does the rest: building search forms, a query wizard and integrating the records into a global full-text search.

Once you have the scripts set up (more on that in a minute), searching is very straightforward. The home page offers a single form that will search across every database that you incorporate into OpenInfo, using syntax similar to what you are accustomed to using for searching the Web or your electronic archives. Because the search runs against a full-text index, you don't need to know the order in which your search words appear, or whether they're in the same field in the database.

In addition to simple searches, OpenInfo gives you an almost unlimited ability to drill into and cross-reference your data. Take, for example, my own voter registration information. To find it, I'd start by searching for Heath, Brad* (yes, OpenInfo supports wildcards), then click on the matching results to see the full record. OpenInfo shows all the fields incorporated into the database (unless you have chosen to hide a few), and makes the contents of each field clickable. Clicking any of the links will take you to a pop-up guide that will help you cross-reference that information against other OpenInfo records, Google, or any other online database with an accessible URL syntax (Yahoo! News, your archives, your photo assignments, etc.).

If you want, OpenInfo can also do some of this work for you. For example, you can teach OpenInfo how to assemble the fields in your database to make a complete address. If you do, the script displays an embedded map for each record (as well as linking to Google Maps), and gives you tools for cross-referencing the address against other records. It will also automatically check for other records in that table with a matching address and show you a list. That means when you look at my voter registration record, OpenInfo automatically finds my wife's registration, too. You also can have OpenInfo mash together other fields from the record that you think might be helpful for users looking to find related information. For example, it might be helpful to have one link that will search based on a person's first name, last name, city and state.

For users who want more power, OpenInfo has more advanced search functions. You can search individual fields in a database, or use a built-in query grid to search through or summarize your data and export the results to Microsoft Excel (users who want to do even more can download full data tables as dBASE files). Users can create custom groups of sources, or search based on the type of information associated with a field, such as names and addresses. If you want, you can allow users to create their own databases on the fly, for their own use or to add to the public collection of sources. OpenInfo tracks searches and record views so you can find out quickly what is most popular with your newsroom.

Setup is easy and inexpensive. To start, you need a MySQL database server, an Apache Web server and the PHP scripting language, all of which are open source. If you don't already have these, you can add them fairly easily by downloading XAMPP, which installs all three at once, from *http://sourceforge.net/projects/xampp.* After that, unpack the script files into one of the folders on your server. Then sign on to your database server as a root user and run the setup.sql file included with the scripts. (You might need to make a few other adjustments to your server, depending on how it's configured. A complete readme file is included with the scripts.)

Once the scripts are configured, you need to load your data tables into MySQL. (Because it's open source, you can find a variety of free tools to help with this...)
