# Trial of the century

**By Wendell Cochran**
American University

Nanosecond by nanosecond, the clock ticks toward the millennium and the biggest beta test in computer history – the rollover from 1999 to the year 2000. By some accounts, that first day of the new century is going to bring a silicon meltdown because millions of computers, literally, won't know what day it is.

Stock exchanges, banks, airlines, government agencies and major corporations are spending billions to make their systems compliant. The Information Technology Association of America estimates it will cost more than $50 billion to fix computers in the United States, perhaps $600 billion worldwide. A few economists have predicted that the costs of fixing computer hardware and software are so high that the U.S. economy will be thrown into a recession.

Some companies and governmental bodies, apparently hoping the problem will just go away, have barely begun to figure out what the Y2K issue means to their operations. A member of Congress recently reported that some "mission-critical" Pentagon systems won't be fixed until 2009.

Thankfully, those of us who work in computer-assisted journalism probably don't need to panic. Most of our hardware is relatively new; most of the applications we use regularly have tried to address the Year 2000 problem at least after a fashion; and most of our databases and spreadsheets don't depend on precise date calculations.

That doesn't mean CAR specialists are off the Y2K hook. A program that mishandles a date calculation, query or sort might well produce an error that is published or broadcast.

*InfoWorld*, a leading computer industry publication, cautioned last year against being too complacent. "The year 2000 will affect almost every machine on your network to some degree," the paper said. And nearly every computer expert warns against counting on hardware and software companies to diagnose and fix all the problems.

So you should understand just what Y2K issues you might face in your CAR shop. It would be a good idea to test your computers, to experiment with how your favorite software deals with dates such as 04/15/00, and to review the structure and content of the date fields in your databases. You might also want to contact the folks who regularly supply you with data to see what changes they foresee making.

Bill Loving, computer-assisted reporting editor formerly at the *Minneapolis Star-Tribune*, assessed his newsroom's inventory of software and databases for Y2K risks but wasn't too concerned based on what he found. "My understanding is that all the major commercial apps that we use in CAR will be, or already have been, repaired by the vendors. I don't know yet what the database implications are."

Tom Boyer at the *Seattle Times* also thinks his computers and programs are in good shape for the next millennium. He says the problem will "probably affect some of the databases we acquire. But they're often so dirty anyway – this'll just be one thing more we have to clean up."

## Do your computers recognize the Year 2000?

The first step is to determine whether you have hardware problems. Generally speaking, if you're using a Macintosh, you won't have any problems. Apple claims its operating system can handle dates from 30,081 B.C. to 29,940 A.D.

Most software applications take their time and date formats directly from the system, where time/date is kept at the BIOS level. BIOS stands for Basic Input Output System, a set of instructions automatically loaded into a computer before the operating system. It allows the computer to interact with the keyboard, ports, and other hardware devices. In other words, if the system clock doesn't properly adjust for the new century, your software probably won't either.

In general, the newer the system, the better the chance that your PCs won't choke on Jan. 1, 2000. But even Intel says, "Although, in general, the system BIOS revisions provided with Intel desktop motherboards and server baseboards manufactured since 1992 contain services capable of transitioning to the year 2000, this BIOS capability alone does not ensure that the system will handle the transition without error. The behavior of any given system during the year 2000 rollover is dependent on several factors alone or in combination, including, but not limited to, the system configuration, BIOS, operating system, and application software."

Translation: A lot of stuff could go wrong. What's more, many clones don't use Intel motherboards.

Different computer manufacturers report different levels of Y2K compliance. Dell systems made after October 1996 are fully compliant, the company says, and it has upgrades for older BIOSes. Gateway 2000 says its Pentium-based models work properly. 486 models will be fine until they are rebooted after the new century. Once they're rebooted, the system clock will need to be set again.

If you don't feel comfortable conducting your own test, several vendors are selling Year 2000 test programs. But, in case something goes wrong, don't test the computer with your most important databases until you've backed them up. And you're probably better off disconnecting from the network. Check network software and components later. (Expect problems to show up, especially if you do such things as force periodic password renewals.)

To test your computers, boot in DOS. At the C:\> prompt, type "date" and then "12/31/99". Also at the C:\> prompt, type "time" and set it for 11:48:00 p.m. Turn the computer off and wait long enough for the system to rollover. Reboot and check the system date.

If it says 01/01/2000, you are one step closer to home.

If the computer doesn't seem to know the date – for example, if it displays Jan. 4, 1980 or Jan. 1, 1900 – you've got a problem. Contact the manufacturer of your machine to determine whether an updated BIOS is available. If it's an older model, you might want to scrap the computer.

## Applications: Where the real issues lie

Hardware problems might turn out to be the easiest ones to handle. Software and data are likely to be tougher for many CAR newsrooms. At the least, you'll want to understand how your programs handle dates. Dates are stored as numeric values based on a fixed starting date that varies according to the program. Date fields can be formatted and displayed in a variety of ways, with the most common default being 00/00/00.

Most Year 2000 problems could have been prevented if date fields contained four-digit years. Few do. Two-digit years were designed into most applications and databases as a way to preserve scarce memory and disk space in the 1960s and 1970s, when most computer standards were set.

When did time begin? For personal computers, the short answer is Jan. 1, 1980. You cannot set most PC system clocks to an earlier day. Fortunately, most applications can deal with earlier dates by using a system known as Date Serial. Dates are assigned numeric values based on a fixed starting point: Day 1=1, day 10=10, etc. This system permits date-formatted cells and fields to be used in calculations.

For spreadsheets, Jan. 1, 1900 seems to be the most common starting point for time. Lotus1-2-3 set this standard, and Excel uses it. An earlier date is not recognized as a date, will not be formatted as a date and cannot be used in a date calculation. QuattroPro, on the other hand, can handle dates back to Jan. 1, 1600, but day 1 is Dec. 31, 1899. And for Mac Excel users, time begins Jan. 2, 1904.

Steve Doig of Arizona State University points out that the Mac-PC difference means dates can be wrong by four years if you swap data between the platforms. If you move data containing dates between spreadsheet types, different versions of the same program or platforms, you might want to reconstruct your calculation formulas rather than importing them.

The concept of having a beginning for time also means you need to have an end. For you doomsday types, time ends on Dec. 31, 9999, according to Excel 97 and Mac Excel 98, but in 2078 for earlier versions of Excel. If you're using two-digit years in QuattroPro, the latest you can enter is Dec. 31, 2050. The latest four-digit year is 3199.

Database managers are a little more flexible. Access 97 can store and calculate dates in the range of Jan. 1, 1100, to Dec. 31, 9999. Paradox 8 can handle four-digit years from 9999 B.C. to 9999 A.D.; its two-digit range is Jan. 1, 1951 to Dec. 31, 2050.

## Digit difficulty

The real test for date compatibility, however, comes in databases that have dates from multiple centuries, with years formatted as two digits. For example, the Federal Election Commission candidate table now lists some politicians running in 2000 and later, but it only uses two-digit years. The next election cycle covers 1999-2000, so the dates on contributions will be mixed between the 20th and 21st centuries.

For now, this doesn't cause great problems. As the table illustrates, most programs we use in CAR assume that two-digit years early in the century should be interpreted as coming after 2000. For example, in Excel and Access, all two-digit years less than 30 are assumed to be in the 21st century.

Says Tom Torok of the *Philadelphia Inquirer*: "More of a pain are the different defaults some database programs use. For example, Access 7.0 and Access 97 assume any two-digit year that is less than or equal to 29 is in the 21st century … Something that was converted from Access 2.0 to Access 7.0 to SQL might give you any two-digit year between 29 and 48 in the 21st century."

Knowing how your programs handle two-digit years might solve some data problems, but it would be better to create and display true four-digit years. Depending on the structure of your tables and the nature of your data, that can be fairly easy or somewhat complex. In any case, it will be easier in a database manager than in a spreadsheet.

Creating a four-digit year involving only one century is simple. Reformat your table to make the year field a four-character text field and add a date field formatted mm/dd/yyyy.

In Access, use an update query to add the desired century string to the existing year string. Then use another update query to put the combined contents of the month, day, and year fields, formatted as a date, into a true date field that displays all four digits.

In FoxPro, this would be a Replace query; in Paradox, use a Changeto query. In some cases, though, it might be safer to write a script or function to explicitly add the century to the year string. The key is to develop a reliable way to identify which date range belongs in which century.

Doig cautions that CAR specialists will need to be especially diligent when they get data from older systems. Stress the need to be vigilant about data coming from "legacy" systems. "Even if your machine is Y2K compliant, it doesn't mean that the data you're getting will be. The 'does-this-answer-make-sense?' test will be especially important to apply during the next couple of years."

The real solution to date-handling problems is to scrap the notion of formatting dates with two-digit years and create a date data type that only permits four-digit years. That will require changes in operating systems and in almost all applications.

Wendell Cochran can be reached at wcochran@ibm.net

---

### Date handling in popular CAR applications

| PROGRAM | START DATE | END DATE | TWO-DIGIT YEAR DEFAULTS |
|---------|------------|----------|------------------------|
| Excel 97 | Jan. 1, 1900 | Dec. 31, 9999 | 00-29=2000 30-99=1900 |
| Excel 98 for Macintosh | Jan. 2, 1904 | Dec. 31, 9999 | |
| Access for Windows 97 | | Dec. 31, 9999 | Same as Excel |
| FoxPro | | Dec. 31, 9999 | |
| Quattro Pro 8 | Jan. 1, 1600 | Dec. 31, 9999 | 00-50=2000 51-99=1900 |
| Paradox 8 | 9999 BC | Dec. 31, 9999 | 00-50=2000 51-99=1900 |
| Lotus 123 | Jan. 1, 1900 | | |
| Lotus Approach | | | |

*Sources: Microsoft, Corel, Lotus. Note: Earlier versions of these programs handle dates differently. For example, some earlier versions of Excel won't accept dates past 2078. Check your documentation.*

---

**Two web sites to check out for Year 2000 computer issues include:**
- www.y2k.com
- www.year2000.com

**These issues have fostered lengthy discussions on the IRE and NICAR mailing lists. To search the archives of these mailing lists by author, subject or date, point your browser to the following web addresses:**
- IRE-L: www.ire.org/resources/ire-l/index.html
- NICAR-L: www.ire.org/resources/nicar/nicarl.html

**Wendell Cochran provides the following web sites of computer companies addressing Year 2000 computer issues:**
- Microsoft: www.microsoft.com/cio/articles/year2000faq.htm
- Corel: www.corel.com/2000.htm
- Lotus: www.lotus.com
- Intel: http://support.intel.com/year2000/paper.htm
- IBM: www.ibm.com/ibm/year2000
- Apple: www.apple.com/macos/info/2000.html
- Compaq: www.compaq.com/year2000
- Hewlett-Packard: www.hp.com/year2000/index.html
- Dell: www.dell.com/year2000
- Gateway2000: www.gateway.com/home/support/c%5Ftechdocs/y2k/default.htm
- Novell: www.novell.com
