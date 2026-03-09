# Tech Tips: Eliminating Happy Faces and Other Garbage Characters

**By Brant Houston**
The Hartford Courant

**Subject:** Cleaning up data from a file on diskette so you can run a match in XDB.

**Problem:** You find out that a small state agency has collected information on thousands of businesses and keeps that information on a diskette. You want to merge that information with your own database of a couple of hundred business names.

Before you can worry about spelling differences in the names, you discover that the agency's file is, not surprisingly, fraught with problems, including garbage characters. And your problems aren't over after you import it into database software.

**Solution:** If you are a journalist who is just getting into computer-assisted reporting, you probably don't have programming skills. But that's not a problem if you have a quick text editor and use a little imagination with XDB.

One commercial text editor is XYWrite III Plus. Copy the agency file onto your hard disk as BIZINFO and look at it by calling it up through XYWrite.

There is the file in all its ugliness with ASCII characters (such as the ubiquitous and ironic happy face) popping up here and there. The nice thing about XYWrite III Plus is that it has an ASCII menu from which you can pluck the offending character and put in the header area.

By typing CH /[ @)]// in the header area and hitting enter, XYWrite will race through the file and eliminate the happy faces. You can do whatever search-and-destroy missions you need to on other garbage characters. You can also eliminate unwanted spaces with CH / //, and add a character, if needed, with the same function.

Another nice feature of XYWrite is that it stores a backup of the original file in case you get excited by all the destruction and blast away an innocent character.

When you import BIZINFO as a comma delimited file, the quote marks around the company names also get imported. (This actually happened to me.) That means there are company names with quotes around them in BIZINFO, and there are no quotes around company names in your own file (call it BIZNAME).

Rather than taking awhile to figure out what is going on (which might mean fathoming bits and bytes, hidden characters and tabs, etc.), there is a quick solution.

Export BIZNAME from XDB as a comma delimited file with quotes around characters. Then re-import it as a fixed file, BIZNAME2. That brings those names back into XDB with quotes. Your company names now have a chance of matching because they have quotes around them in both files.

At this point you might want to use XDB's command Xleft to run a join on the first nine characters in name field in each file in order to pick up most of your matches.

For example:

```
Select A.*, B.Name
From BIZINFO A, BIZNAME2 B
Where Xleft (A.Name,9) =
Xleft(B.Name,9)
```

Make sure you index both name fields before running it.

You may have to clean up the data further by using XDB's Update command, but you are well on your way at this point.

I'm sure there are other effective text editors and that a little programming knowledge would go a long way toward solving these problems in a better manner. The bizarre importing of names is just an example to show how to clean and shape data by using the import and export functions in XDB. Nonetheless, these tricks do come in handy when importing data from an optical scanner or an online source such as the Federal Election Commission.
