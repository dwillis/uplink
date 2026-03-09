# Letters

Dear Uplink:

I got my April 1992 Uplink today and was intrigued by the reports of problems with XDB software. I have had some of the same problems, and I'll be waiting to hear what solutions arise.

I got XDB 2.30 in May 1991. We have not yet attempted any projects as complicated as those described by Robert Paynter, so I hadn't run into the problems with indexing, but I had noticed two other problems mentioned in the article: the software would give some sorts out of order (the decimal point example cited by Ed Foldessy of the Wall Street Journal is a perfect parallel), and its computations were not always trustworthy.

As an example of the former, I've run a fair number of queries on census data, and I frequently found that when I calculated percentages—say, ranking census tracts by percentages of minority residents— two percentages that were a point or two apart would occasionally appear out of order. I eliminated most of those problems by simply adding another float decimal place (F10 utility menu, then F5 user profile, then F6 format options, then F8 float decimal places), but that didn't get rid of them all, and even with version 2.41 I've had to keep a close on any calculations and oderings in which decimal places were significant. Perhaps I should've been less tolerant.

I ran into the other computational problems in working with a cutdown version of the 1989 Toxic Release Inventory data for North Carolina. I found that XDB 2.30 could rank them accurately statewide—it seemed to ignore any record with a toxics total exceeding seven digits, of which we had at least one. (This wasn't apparent from the data itself; fortunately, we had other TRI reports with which to compare some of our data and could tell right off that there was a problem.) However, version 2.41 totals the larger numbers accurately.

One other problem that 2.41 solved for us was using the PC's random access memory. We bought four megs of RAM with the machine, and in my relative ignorance of computers I'd assumed that if it was in the machine, it was being used. Meanwhile, when I tried to import census data into 400-field tables and kept getting the X10 error message—insufficient RAM— I just figured that four megs wasn't enough and built smaller tables. I didn't learn about basic versus extended memory until stumbling over Jack Warner's computer column from Cox News Service on the on the wire a couple of months ago— it explained what the problem was, although it didn't suggest anything to solve it that worked for us. Dave Stroble, our audiotext product manager and a PC fiend, futzed around with my AUTOEXEC.BAT and CONFIG.SYS files but couldn't solve the problem. Then we got XDB 2.41 and its extended memory manager. I don't know exactly how it works, but since I installed 2.41, I've had no more problems with totaling numbers or importing files with many fields. (I haven't had occasion to try 400, but I have gone as high as 288 with no problem. Not only that, 2.41 appears to import about 20 percent faster that 2.30.)

If XDB has figured out how to fix the ordering bug, I'd like to hear about it. Meanwhile, please keep us posted on other problems, even if it doesn't make for as compelling reading as does the Hartford Courant's serial killer!

Lex Alexander
Investigative/Database Reporter, Hartford Courant
