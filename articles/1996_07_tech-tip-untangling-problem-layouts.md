# Tech Tip
## Untangling problem layouts ... Several programs help

**By Richard Mullins**
NICAR staff

Getting new data is like getting a present. You want to get the data loaded into your PC database program as quickly as possible so you can start playing with it.

But this unwrapping process can be delayed by simple typing mistakes on our part, or, what's worse, there can be small or frustratingly substantial differences between the record layout we have on paper and the data we were given on tape.

Just like alarm clocks going off at 6:15 a.m., this kind of thing happens more often than we'd like. Here are some of the procedures I've come up with to deal with the problems that sometimes hold us up from the fun part: getting to interview data.

For the tape processing, I'm using Nine Track Express and assuming familiarity with its Create File Parameters and Create Field Descriptions steps. Additionally, these tips take advantage of Microsoft Excel's marvelous Text Import Wizard; a graphical word processor such as Microsoft Word; and a file viewer called List, a shareware program I find indispensable.

### Testing format

Use .csv as the output format while testing. The Preview feature in Nine Track Express can save you a lot of time. I never process any tape without using it. While the Transfer File procedure is counting off the records moved from the tape to the PC, pressing the "P" key pauses the process and shows you exactly what Nine Track is reading as a single record. If the data at the beginning and at the end looks OK, then you know the record length you are using is correct. I always use the Preview several times to make sure the one record I saw wasn't coincidentally correct and most of the others were wrong.

Mistakes in field lengths are more frustrating. If you are outputting the data to the FoxPro or Paradox format, the preview will not show you how the data is being split into fields. To find out if it's right, you have to quit Nine Track and look at the results in the database program. If it's wrong, that means quitting FoxPro or Paradox and going back to Nine Track. And if you're using the Windows version of these database managers, then you have the extra step of loading and unloading Windows.

### Time saver

Save yourself some time and use .csv as the output format until you know that the data fields are being split in the right places. Then, when the field description is right, change the output format to the database format you want.

The commas and quotes will reveal simple field length problems such as: every ZIP code field beginning with a letter (some column before the ZIP is one byte too long). Of course, this example is too easy. Finding mistakes in data layouts when most of the information is readily recognizable stuff such as names, addresses, amounts and dates is easy compared to data sets that are hundreds of bytes long, with nothing but key fields, and lots of small fields with codes like "EA" and "J1."

When scanning the preview output, go to the end of the line, and work back to the beginning.

Load a small sample of the file (1,000 records or less) in fixed-position format.

### Saving samples

I often do this step first with a dataset I haven't processed before. I save the sample file on the floppy I keep for every data project. All finished and tested Nine Track profile (PR2) files go here too. (I know I wouldn't want to have to do all that typing and testing all over again.) I also save small .dbf samples of all the tables in the data set.

I often print a small portion of this file, especially if it's obvious that some record layout debugging is going to be needed. Most data records are longer than 80 characters, so this is where a graphical word processor comes in handy. First, for the printout to be useful, you have to set the text to a monospace font such as Courier, then set the margins as wide as possible to get as many characters on a line as you can.

> Drew Sullivan of the Associated Press recommends a research tool called NameBase, available for free at http://www.pir.org. Namebase, run by Public Information Research, "is an index of names pulled from books, magazines, newsletters and all sorts of strange and rare sources dealing with the CIA, intelligence, corporate fraud, drug-dealing, the mob and more than a few conspiracy theories," Sullivan says. "If you can't remember what Thomas Clines or Richard Secord was involved in, this is your place." Drew Sullivan can be reached by e-mail at drew@ap.org
