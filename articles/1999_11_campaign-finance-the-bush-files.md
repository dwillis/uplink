# Campaign Finance: The Bush Files

**By Aaron Diamant**
*IRE and NICAR staff*

Amidst a great deal of self-congratulatory hype, George W. Bush has made available on his Web site (*www.georgewbush.com*) a complete list of every single campaign contribution he has ever received. Sounds great, except it's nearly impossible to work with.

The problem is that the data are only available as one giant .pdf file (and I mean a giant 1,750 pages and counting as of this writing and that's only for the 3rd quarter of 1999). So although the data don't cost you a dime, you really can't do anything with them unless you have lots of time and specialized software to convert them into a workable format.

A few of you have written to the NICAR-L listserv in the last few months asking for help converting the monster .pdf file into a format that can be imported into Excel or Access.

And as the 2000 election gets closer, more of you will be asked to take a look at, and produce stories on, the Bush campaign finance data from your area.

The following are some methods others have used:

### MacGyver method

This is the method used by reporters at *The New York Times.*

Step 1. Write two PostScript programs that go automatically to the Bush Web site. One version should read the page and download the .pdf files you need. However, you don't want to download all the files after the first time. A second version of the PostScript goes to the directory and checks for the most recent additions.

Step 2. Load the data into Adobe Exchange with a "Redwing" plug-in designed by Monarch. This extracts text from a .pdf file. Use the "Extract all to Monarch" command that parses the text. You may run into a problem with the multi-line format of the original data (sometimes there is a second line added for comments which can be lost). To solve it, go to step 3.

Step 3. Run a PostScript that checks for spaces at the beginning of lines. If there is a space, write the script such that it will save the comment as a separate field.

Step 4. Export as Tab Delimited.

Step 5. Load into Access.

Degree of difficulty: 9.5. Not recommended for anyone except the most serious programmers.

### Mother Theresa method

For those of you who are fairly patient, this method may be for you. It is much simpler than the previous method, but there are more limitations.

There is an Acrobat Reader plug-in called Aerial, which a number of you may be familiar with. You can use Aerial to convert a .pdf to an .rtf document. This is a good tool for copying a table at once and pasting it into Excel.

It can convert the whole .pdf document at once, but is not infallible. This is where the Mother Theresa part comes in. Once you convert the .pdf to an .rtf document you can use a word processing program such as Microsoft Word to clean the data and convert it to the format of your choice for import into a spreadsheet or database.

You can download a trial version of Aerial from *www.ambia.com/aerial.htm*. For help using Aerial you can refer to an article written by IRE's Training Director Tom McGinty in the July/August edition of *Uplink*.

Degree of difficulty: 5.

### Fed Ex method

If you need to get data from a .pdf file that's posted on the Web, you can send a message to pdf2txt@adobe.com with the URL of the .pdf in the body of the message. The contents of the .pdf should be returned to you as a text message. You should get a response in a few minutes (sometimes a lot longer for larger files like the Bush .pdf). But be warned, you are going to have to clean the data yourself.

Degree of difficulty: 4

### Indiana Jones method

Indy was known for hunting for things that are already out there. Believe it or not there are actually a number of sites that have already done some of the work for you.

**Bush data sources:**

- *www.georgewbush.com* – George W. Bush's Web site, where the public can access his campaign contribution reports in .pdf format.
- *www.ambia.com/aerial.htm* – At this site, you can download a trial version of Aerial, a software program that can help translate .pdf documents.
- *pdf2txt@adobe.com* – An e-mail address to Adobe; send .pdf files here to be returned as a text message.
- *www.tray.com* – Web site of Public Disclosure, Inc., where electronically filed presidential data is easily downloaded.
- *www.foodnews.org/bush.html* – Food News' searchable database of Bush's campaign finance reports; however, data can't be downloaded.
- *http://metalab.unc.edu/javafaq/bush* – Elliotte Harold's Web site includes Bush's original data as tab-delimited documents, available for downloading.
