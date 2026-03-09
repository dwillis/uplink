# Tech tips
## Turning print-image files into databases

**By Brant Houston
The Hartford Courant**

In the land of data garbage one of the most painful files to get from a government agency is a print file.

This file looks just like the information you get on a printout and contains header information that looks like "page one, judicial files of america, section 203AB, the office of Eddie Haskell, 10/20/92" and so forth for each "page" of information.

If you can't convince the agency to give you a nice, flat file then it's laundry time.

You can clean these files, if they are small, by throwing them into a word processing program like XYWrite III Plus and manually defining the offending headers and deleting them.

This won't work very effectively for a 10 megabyte file, however, and that is where, whether you are a programmer or not, you should head for a program.

At *The Courant*, I discovered that a good person in our publishing systems had a handy XYWrite III Plus program that with a little modification would go in and destroy headers until it reached the bottom of the file.

All you have to do is identify a mark or string of characters that establishes the beginning of the header — "page" for example — and the end of the header — "92" perhaps — and run it through its loops. Sometimes you might have to make another pass through the data, but the job gets done.

I know the same kind of program can be written more gracefully in other word-processing programs or database programs, but the message of this tip is not to waste time on manual deletion when a little programming can help.

Also, I have been told that a database program — Monarch — takes care of this problem during importing and look forward to reading about it while trying to find money to buy it.

*(Editor's note: We knew Tom Boyer in Virginia has some experience with Monarch. Here's what he has to say.)*

---

**By Tom Boyer
The Virginian-Pilot and Ledger-Star**

Somebody in our data-processing department recently tipped me off to a piece of software that can digest a report print-image file and turn it into a live database. It's called Monarch, and I think its a gem.

Monarch is like a database report writer in reverse. It takes fixed-format reports — even very complex ones — and slices them into data fields. You can export to a bunch of formats, including .wks spreadsheet, .dbf database, or delimited ASCII.

For reporters, it helps with those agencies who aren't set up to output fixed or delimited files to tape, but who send their key data out in long printed reports. If you have a good FOIA, you can pay them to produce a tape file for you, or you can FOIA their print file if it's what you need. It's usually a minor programming change for them to filch a print file — such as a payroll list — from the mainframe's print queue and output it to 9-track tape or floppy disk.

Monarch requires no programming, and you can figure it out in a morning. The new version handles report files up to 30,000 pages. It is very fast on a 486. (No, I'm not getting a commission.)

There are three catches: 1) It must be a fixed-format report with fields of information appearing at the same spot within a line. 2) If it's outputted to tape, you'll need a utility to move the entire file en masse to your PC hard drive. 3) When you get the file in your PC, you may have to clean out weird print characters, extra line feed commands, etc. (More on that below.)

Monarch works by recognizing the various lines of a report by their contents. Say you have a print-image of a report on criminal incidents (this is a report we get weekly). Each page contains headers and footer, and within the headers are three "detail lines" of information describing each crime.

```
CRIME DATE TIME ADDRESS PROPERTY TAKEN
OWNER BUILDING TYPE ENTRY METHOD
SUSPECT SUSPECT OCCUPATION
```

The information, in a fixed format, looks like this:

```
BURGLARY 042193 1330 421 APPLE LANE STEREO
HOUSTON BRANT CONDO REAR DOOR KICKED IN
SCHMID JON GRADUATE STUDENT
```

Working with this file in Monarch, you first teach it to recognize, or "trap" the first detail line by the pattern of characters, spaces and numbers. Once it knows the first detail line, it can pick the two lines immediately below it. Then you "paint" each bit of information with the cursor and give it a name. Monarch then chops up the report into fields according to your instructions. It can even include header and footer information as fields. Monarch has some analysis features of its own, but I generally have it export to .dbf files and do the analysis in FoxPro.

Now for the hairy part. Sometimes the print-image files contain mainframe junk: weird IBM printer instructions, extra line feeds and such. If Monarch chokes on these — you'll know because the report won't look right on your screen — you need to remove the offending characters.

I won't go into detail, but you can use the hex dump feature of NineTrack Express to diagnose the characters that are giving you problems and write a routine to remove them or replace them with spaces. A word processor like XYWrite can clean up a print file with its search-and-replace capability, but its very slow with big files (editor's note: Brant Houston says the newest version of XYWrite is fast even with files up to 20 meg). I use the text editor that comes with FoxPro 2.0, which can search and replace the entire ASCII character set and is blazing fast with big files.

All this sounds complicated, but once you have it figured out, it need not take long. You can run a complete Monarch translation from a DOS batch file, and it can spit out thousands of records in a couple of minutes. In one case I've gotten the whole routine — from tape, through Monarch, to FoxPro's report writer, to an ASCII report that runs in the paper — down to 10 minutes.

Monarch is put out by Personics of Wilmington, Mass. Call them at (800) 445-3311 and they'll send you a demo disk free. The price is currently $395, and you may be able to get it cheaper from discount software houses.
