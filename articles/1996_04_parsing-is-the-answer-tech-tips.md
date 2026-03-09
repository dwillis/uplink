# Tech tips: It may look like a table — but it's not
## Parsing is the answer

### By Natalya Shulyakovskaya
#### NICAR Staff

Parsing comes into play when you need to turn a text file into a table with rows and columns. There are plenty of those text files scattered all over the Web with numbers and other information organized into columns, or, once in a while, you get a disk from a bureaucrat with data in report format: The files look like tables because the information is organized into separate columns, but they are flat text files. They may have a .txt extension, the extension .dat or some other creative three-letter extension — or no extension at all.

You can open these files with a text editor, but no database manager or a spreadsheet will recognize them as tables. At this moment, you know it's time to parse.

One word about downloading files using Netscape: If you are saving a table-looking file from the Web, make sure to save it as a text file and not as an html file. You don't want to waste time fishing out html coding from the document; let the browser do it for you. If you are not using Netscape, you may have to strip out the html coding using an html browser or text editor before proceeding.

### Straight to the business

Let's download and parse one of the tables from the Census Bureau Web site (http://www.census.gov/)

The easiest tool to use for parsing is Excel, but remember: Excel can only handle up to 16,000 records in one table.

Table 1. Projections of the Population of Voting Age, for States, by Sex, Race, and Selected Ages: November 1996: http://www.census.gov/ftp/pub/population/socdemo/voting/proj/votepg1.asc

Go to the File pull-down menu, pick Save As and for File Type, specify All files. Save the file, and go to Excel.

In Excel, under the File pull-down menu, choose Open. Find your file, making sure to look for All Files in the file type box, or the file won't show up.
