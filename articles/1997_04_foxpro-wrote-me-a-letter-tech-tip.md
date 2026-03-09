# Lonely Days are Gone
## FoxPro wrote me a letter

*For our recent conference in Nashville, NICAR gathered the country's top journalists in computer-assisted reporting and asked them to jot down their ideas, tips, and practical anecdotes. The result is a binder full of handouts and tipsheets that among other things cover math and stats, suggest CAR stories for sports reporters, describe how to diagnose hospitals, and detail how to investigate immigration issues. The sheets are currently available through the IRE Resource Center. They can be ordered individually, or you can purchase the entire set for $75. Eventually, this resource will be available electronically.*

**By Jo Craven**
NICAR staff

Why work if you can get a computer to do the job for you?

Recently, when I needed to send a form letter to 133 different businesses, I thought of NICAR data guru Richard Mullins, who teaches this ethic. I could sit and type 133 different addresses on top of 133 different copies of the same form letter — or I could get a computer to do it for me. I decided to let the computer do the job.

Here's what I had available: a FoxPro database that included, among other things, the names and addresses of the businesses that I wanted to contact.

I knew I could write a scanloop in FoxPro to pull out the addresses. And I found out that I could use the TEXT/ENDTEXT function to insert a text block — in this case, my form letter — after each scanned address. Later, I found I could get FoxPro to use the same database to print out mailing labels. What would have taken me a couple of hours, FoxPro did in minutes. (Incidentally, you could accomplish this same task with Microsoft Word's Mail Merge without writing a FoxPro program).

To create the FoxPro program, which I called "letters," in the command window, I typed:

`modify command letters`

In the .prg, or program, window that appeared, I wrote the following program (an explanation follows):

```
CLEAR
CLEAR ALL
CLOSE ALL

SET CENTURY ON
SET TALK OFF
SET STATUS BAR OFF

USE c:\business.dbf

files = " "

SCAN

files = alltrim(str(business.id))

SET ALTERNATE TO "c:\" + files
SET ALTERNATE ON

?alltrim(cmonth(date())) + " " +
alltrim(str(day(date())))
```
