# Programs for Parsing

**By David Heath**
*Seattle Times*

If you work with data much, at some point you're going to deal with files that defy easy import.

Knowing a few tricks can sometimes save you lots of work. For example, if a text file is missing carriage returns at the end of each line — a common dilemma — you can open it in Word and save it into a new text file. Voilà. You now have carriage returns.

You can also do a lot with search and replace tools, Excel's import wizard and Monarch, a terrific software package that converts reports back into databases. But there are times when even Monarch falls short. That's especially true if columns don't line up or the structure of each record is not consistent.

When the going gets rough, the tough write a program.

Writing your own program is the only solution I know if you're trying to parse data that's loosely structured. Say that you want to take a collection of Web pages and put all the links into a database. The links aren't hard to find; they always begin with `<a href=`. But otherwise, the pages may lack any consistent format.

There is a way to do this, but you have to learn a smidgen of programming. If you already write simple programs to clean data, you probably already have most of the skills needed. If you are a novice or have never tried programming, the good news is that you don't have to learn that much. You'll be working with a limited set of functions and statements.

I'm going to show you how to deal with problems using Visual Basic. You could do the same type of thing with FoxPro or, for those fearless of its steep learning curve, Perl. The latter is especially powerful at pattern matching, making it an ideal tool for finding HTML tags.

VB's chief advantages are that it's already built in to Access, Excel and Word — so you don't have to buy any new software — and it was especially created to be an easy-to-learn programming language. (Although you've already got a version of VB, if you buy the full version you'll get a lot of debugging tools that can be a life saver.)

To manipulate text in VB, you need to learn five things:

1. How to declare variables, which simply means defining them as either characters or numbers.
2. How to open and close files.
3. How to read from files and write to files.
4. How to use text functions, such as MID, INSTR, LEFT, TRIM and LEN
5. How to create loops.

When you're first learning Visual Basic, it's easy to get distracted making pretty pictures: forms, buttons, labels, etc. But your program doesn't have to look good; it just needs to get the job done. In fact, all the tools you need can be found in the old QBasic, that free program that comes with DOS. A great book for learning Basic programming is "QBasic by Example," written by Greg M. Perry.

There's no way to teach you everything you'll need to start programming in a brief article, so I highly recommend getting a book. However, I can walk you through a fairly simple program that parses data, and that should give you a pretty good idea of what to expect.

Let's take the U.S. Census home page, at *www.census.gov*, and parse all the links into a comma-delimited file that we can easily import into a database. Save the page to your hard drive and note the location, because you'll need it for later. The file is tricky because the page is very loosely structured and the HTML tags are not always consistent. Sometimes they are followed by quotation marks and sometimes they aren't. So we have to include some conditional statements in our programs.

Of course, it's not efficient to write a program to parse a single page, but this program could parse scores of Web pages all at once. You'll find plenty of situations where such a program can do wonders.

To run this, go to Tools | Macro | Visual Basic Editor in Excel and type in the following code. Then simply click on the Run button.

```vb
Private Sub Command1_Click()
```

Start by declaring the data type of all the variables you'll use. I've just made up the variable names on the left, starting some with "str" to signify string, int to signify integer or lng to signify Long Integer.

```vb
Dim strLine As String
Dim intRead, intWrite As Integer
Dim lngFindAHREF, lngEndHere, lngFindAlt As Long
Dim lngStartHere, lngFindEndTag, lngFindName As Long
Dim lngFindGreaterThan, lngFindLessThan As Long
Dim strHref, strAlt, strName As String
Dim strNextLine As String
```

`FreeFile()` is a useful function that assigns an unused number to a file. Basic requires files to be numbered for opening, closing, reading and writing.

```vb
intRead = FreeFile()
```

In this case, intRead is now equal to 1. We can now open our Web page to read from as file No. 1.

```vb
Open "c:\census\www_census_gov.html" For Input As #intRead
```

Next we want to create a second file, No. 2, that we are going to write the data to.

```vb
intWrite = FreeFile()
Open "c:\census\filetoimport.txt" For Output As #intWrite
```

So all we've done is opened the Web page, which was previously saved to your computer. Your path may differ from that above. Then we created a file called "filetoimport.txt" that we will write to.

We're now ready to look through the Web page for patterns. The statement for that is `Do while NOT EOF(intRead)`, meaning read until you get to the End Of File #1, followed by `Line Input #intRead, strLine`, meaning go to the next line and put it into my variable "strLine."

```vb
Do While Not EOF(intRead)
Line Input #intRead, strLine
```

Time to start looking for the pattern "a href". The function InStr gives the number of the characters from the left that a pattern appears. `vbTextCompare` ignores upper and lower cases.

```vb
lngFindAHREF = InStr(1, strLine, "A HREF", vbTextCompare)
```

If we find "a href" in a line, we want to grab that line eight characters to the right of the start of the tag.

```vb
If lngFindAHREF > 0 Then strLine = Mid(strLine, lngFindAHREF + 8)
```

Some of the lines wrap, so we have to make them one long line using a loop.

```vb
Do While Not InStr(1, strLine, "</A", vbTextCompare) > 0
Line Input #intRead, strNextLine
strLine = LTrim(strLine) + " " + LTrim(strNextLine)
Loop
```

We're looking for the end of the first tag and will put the text in between into a variable called strHref.

```vb
lngEndHere = InStr(1, strLine, ">", vbTextCompare)
strHref = Mid(strLine, 1, lngEndHere - 1)
```

Now we're looking for the ALT tag, which is what shows up if an image can't be displayed on the Web page. If we find it, we'll put the text in that tag into the variable "strAlt." To help find the end of the tag, we're searching for quotation marks. I've used the Chr() function because we can't put quotations within quotations.

```vb
lngFindAlt = InStr(1, strLine, "ALT", vbTextCompare)
If lngFindAlt > 0 Then
lngStartHere = InStr(lngFindAlt, strLine, Chr(34)) + 1
lngEndHere = InStr(lngStartHere, strLine, Chr(34))
strAlt = Mid(strLine, lngStartHere, lngEndHere - lngStartHere)
End If
```

Finally, we're looking for the last tag, which sometimes will include text that you see on the Web page as a hyperlink.

```vb
lngFindEndTag = InStr(1, strLine, "</a", vbTextCompare)
strLine = Mid(strLine, 1, lngFindEndTag - 1)
lngFindGreaterThan = InStr(1, strLine, ">")
lngFindLessThan = InStr(1, strLine, "<")
If lngFindLessThan > 0 Then
strLine = Mid(strLine, lngFindGreaterThan + 1)
End If
lngFindName = InStr(strLine, Chr(62))
strName = Mid(strLine, lngFindName + 1)
```

We have a little bit of clean up work to do. There are extraneous quotation marks to remove and pieces of unwanted text. Also, some of the links begin with "http://" and some don't.

```vb
If Left(strHref, 1) = Chr(34) Then strHref = Mid(strHref, 2)
If InStr(1, strHref, " ") > 0 Then strHref = Mid(strHref, 1, InStr(1, strHref, " ") - 2)
Select Case Left(strHref, 1)
Case "h"
strHref = strHref
Case "/"
strHref = "http://www.census.gov" + strHref
Case Else
strHref = "http://www.census.gov/" + strHref
End Select
If Right(strHref, 1) = Chr(34) Then strHref = Mid(strHref, 1, Len(strHref) - 1)
```

We're combining the ALT tags with the hyperlinks because they do essentially the same thing.

```vb
If strAlt = "" Then strAlt = strName
```

Now we'll write the variables to a comma-delimited file.

```vb
Write #intWrite, strHref, strAlt
```

It's time to clean out the variables and run through the loop again.

```vb
strHref = ""
strAlt = ""
strName = ""
End If
Loop
```

You always have to close files that you've opened. The command for that is simple.

```vb
Close
End
End Sub
```

David Heath can be reached by e-mail at dheath@seattletimes.com

---

**VBasic resources**

Try these Web sites for more on Visual Basic:

- *http://msdn.microsoft.com/vbasic*
- *www.vbexplorer.com*
- *www.programmersheaven.com/zone1/index.htm*
- *www.vb-helper.com*
- *www.vbsquare.com/beginning*
