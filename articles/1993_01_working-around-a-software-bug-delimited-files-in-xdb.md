# Working around a software bug

## Solving some problems with delimited files in XDB

**By Elliot Jaspin
Cox Newspapers**

Anyone who has worked with software for any length of time will soon encounter a bug. It may be large or small, but once you hit the enter key and watch a program sail off into cyberspace, it can be awfully irritating.

My personal favorite involved software for aircraft navigation. The software worked perfectly until the plane flew across the equator. Then the onboard computer commanded the plane to fly upside down. Hmmmmm.

While every programmer will try to produce software with as few bugs as possible, the chances of producing a perfect piece of code seems remote. The trick for the user is to find an acceptable "workaround" when a problem is encountered.

A particularly irritating bug in some versions of XDB involves importing delimited files. Each field in a delimited file is separated by a character, usually a comma, and text fields are enclosed within quotation marks. Thus, a record might appear as:

**"Doe, John", "123 Maple St.", "Bristow, VT"**

Although there are four commas in our example, software should be able to see this as a record with only three fields, because two commas are within quotation marks. When the software encounters the first set of quotation marks, it should know that anything that follows is data. If it encounters a comma it should not treat it as a delimiter. Once it reaches the terminating set of quotation marks, the software should consider the comma that follows as the end of one field and the beginning of another.

Alas, versions of XDB prior to release 2.41 see the quotation marks but keep on looking for the comma as a delimiter. The results are usually commastrophic (**ouch**).

While the problem is potentially fatal, the workaround is simple. XDB allows the user to specify what the field delimiter is when importing a delimited file. By the same token NineTrack Express allows the user to pick any character that can be entered at a keyboard as a delimiter. Instead of using a comma, transfer a file in NineTrack Express using a "^" or a "|", both characters rarely or ever are found in a file. Once you have transferred the file from tape, specify the character in XDB, and the file should import perfectly.

A few closing notes, this particular bug in XDB was corrected in version 2.41. But a similar bug has popped up in the database program from Microsoft: Access. The software gets confused when it encounters a record such as:

**"Bartowski, "Buddy"", "123 Maple St.", "Bristow, VT"**

As I said at the start, software bugs are everywhere, like. . .
