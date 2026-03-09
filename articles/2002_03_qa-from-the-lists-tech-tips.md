# Q&A From the Lists

*Listserv messages you may have missed between members of NICAR-L, Census-L and IREplus-L. To learn about joining these mailing lists and searching their archives visit www.ire.org/membership/listserv.html.*

## Downloading with FTP

**Q:** What does using FTP software do for you in downloading that simply right-clicking and saving doesn't?

**A:** I had some problems downloading files through Netscape; when I started using the FTP client, not only did those problems disappear, but I also started seeing about 30 percent faster download times. It also allows you to select an entire set of files to download, rather than right-clicking on them one at a time. If it's just one file, I'd probably right-click on it, too. If it's a set like the 40 per-state SF-1 census files from last summer, right-clicking gets a little tiresome.

## SPSS and Excel

**Q:** I don't use SPSS and know nothing about it. But I want to tell someone who has some data in SPSS how to give it to me in Excel (I'm not sure they know for sure how).

**A:** File/Save As/Excel ought to do it, as long as the SPSS table doesn't have more variables or cases (i.e., columns or rows) than Excel can handle.

## Copying import specs

**Q:** I was under the impression that you could export or somehow copy import specifications between Access databases, but I can't remember how to do it nor find any way to do it in the help file. Can someone explain how to do it or point me to the relevant help entry?

**A:** Open the database to which you want to add the import specs. Go to File, Get External Data, Import. Then select the database that contains the import specs you want. On the import dialogue window, click the button labeled Options. Check the box labeled Import/Export Specs. Then click OK. It won't seem like anything happened, but the specs should be in the new database.

## Summarizing with maps

**Q:** I need help creating a dot-density map. I have a point (dot) theme. Let's say each dot represents a single crime in the county. And I have a census tract theme. How do I assign the dots to their respective tracts and then tell ArcView to show me one dot for, say, every 50 in each tract?

**A:** If I understand, you already have a dot density map with one dot per crime, but want to aggregate it by tract and restate it as 1 dot per 50 crimes. If this is the case, you want to make sure you're joined table and click on the summarize button, which is a Sigma... this will start a dialog box, through which you want to select your TractId field and Summarize by Count. What you'll end up with is a .dbf that has:

```
tract 1  504
tract 2  444
```

Then you can add this new .dbf table and join it to your original tract theme and make a dot density map (double-click on the theme and pick dot density instead of graduated value).

## Splitting those names

**Q:** I have a "name" field in an Access table I need to separate. The names appear like: SMITH, JOHN DAVID. I need to get the individual names in to different columns via update query... simply tell Access to put all characters before the comma in the first new field (lastname), and all remaining characters after the comma into a second new field (restname).

**A:** Use instr() to find the commas. Something like this:

`Left(name,instr(",")-1)` for the last name.
`Mid(name, instr(",")+1)` for the rest.

## Looking at test scores

**Q:** I'm currently helping the education reporter with the state school scores released to the media yesterday. I would like to know what would be the best approach to calculate every district's score on each category, English, language and arts. The same with science. The education reporter received the results on an Excel table. I was thinking about basic math: adding all the percentages and then dividing them by the number of schools on each district.

**A:** A better approach might be to calculate a WEIGHTED average. To do that, multiply the average for each school by the number of kids who took the test, add those numbers together, then divide by the total number of kids.
