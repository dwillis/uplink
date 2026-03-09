# Funny CAR
## Computers get comical

**By Victor Greto**
*The Colorado Springs Gazette*

*To get a copy of IRE's "100 Computer-Assisted Stories," which includes ideas for both features and hard-hitting investigations, call NICAR at (573) 882-0684.*

They're inane, funny, silly, idiosyncratic — and humbling because they're one of the most popular features of the daily newspaper.

They're the comics.

Recently, *The Gazette in Colorado Springs* conducted a survey of its readers to discover what its most-read and most-hated comics were. Readers could cut out a form and send it back to us within two weeks. Sure enough, we received over 4,000 replies, better than any other cut-out-a-form-and-send-it-in-on-your-own-nickel survey we've done.

Readers chose what they thought were our best and worst comics, and then rated each comic with one of the three choices: ALWAYS READ, SOMETIMES READ or HATE IT.

*The Gazette's* Research Center volunteered to tabulate the results into Microsoft Access and run queries that dealt with ages and gender of respondents, and how a mix of each of these categories judged the comics.

To facilitate inputting, I converted genders into the numerals 1 and 2. I converted age variables into the numerals 1 (17-younger), 2 (18-34), 3 (35-54), and 4 (55-older). The three ratings from which they chose were also converted into numerals.

We hired temps to input the data. It took about three days.

### For best and worst

First of all, after all the data was inputted, we wanted to find out the overall tally: what was considered the BEST COMIC?

When you choose peculiar queries, you don't want to run the Query Wizard Access 95 provides. So pick QUERY, then DESIGN VIEW. Choose the table (which in my case I called, simply, COMICS). This query entailed two steps: I chose BEST COMIC within the FIELD slot; in the box beneath entitled TOTAL, I chose GROUP BY. In the next column over, I chose BEST COMIC as the Field name, COUNT in the TOTAL field, then DESCENDING in the Sort field.

I got my answer: the winning comic was "For Better or Worse." Running a similar query, and using the same terms — except using the WORST COMIC field instead of the BEST COMIC - I calculated what people had voted as the most-hated comic: "Where's Waldo" and "Judge Parker" came out on top — or bottom, actually.

To ascertain the top 5 ALWAYS READs and HATE ITs by age and sex was a little more time-consuming. I had to use Access in tandem with Excel to do it as expeditiously as I could. If you have a better way, let me know.

I discovered I could not run a single query (like I had hoped) by grouping age and sex, then asking Access to count the individual comics' 1-2-3 variables. Access evidently needs to group, then count what it has grouped, one-by-one. That would mean I would have had to done 42 queries on one category of age and sex. Because I wanted to do 8 categories, that would be a total of 336 queries. Excel came to my rescue.

I exported my original table into Excel. Selecting all the responses to the ALWAYS READ, SOMETIMES READ or HATE IT (i.e., 1,2,3), I eliminated the 2s and 3s, saved the table under COMICS1 (i.e., a different name), then imported it back to Access.

Within Access and with the new table, I ran this query:

Choose QUERY, then DESIGN VIEW; in the first column, I picked my COMICS1 table, the AGE field, the GROUP BY "1" (17-younger); in the next column, I chose the SEX field, GROUP BY "1" (male); in the next column, I chose our first comic, B.C., then COUNT; in the next column, I chose the next comic with the same COUNT, and continued until all the comics were done.

It worked fine. But the results were not sorted in descending order.

To sort the query, I hit the "Analyze it in Excel" button. From there, I selected the results, went to DATA, chose SORT, asked it to sort by ROW 2, which contained the numeric results of the Query, clicked on OPTIONS, asked it to sort from left to right, and hit OK. Finally! The top comics in descending order.

This first query counted all the "1" numerals for each comic as grouped by males 17-younger. I did the same for all the other combinations of male/female and the four different age-groups, analyzing or sorting each in Excel. After the initial set-up query, it didn't take long.

To get the 5 worst for each group, I exported the original COMICS table into Excel again. In Excel, I selected and then eliminated all the "1" and "2" responses for each comic. Preserving the 3s, I saved the new table as COMICS2, then re-imported it into Access.

I built these queries in the same manner as the other ones, but this time the "top" comic was actually the worst.

The story, published on April 12, 1997, on the cover of *The Gazette Lifestyle* section, was a success. The tallying, graphics and tongue-in-cheek approach of reporter Rick Ansorge added to the popularity of the feature.

We found, perhaps naturally enough, that it was dominated by elderly people, but all the categories gave interesting results: for instance, young girls preferred "Luann," while young boys loved "Garfield." Men 18-34 loved "Dilbert," while women 18-34 preferred "For Better or Worse."

More importantly, it was enlightening for our Features Editor, who took the results and the ensuing comments to reshape the comics page.

*Victor Greto can be reached at (719) 636-0182, or by e-mail at dorazio@gazette.com*
