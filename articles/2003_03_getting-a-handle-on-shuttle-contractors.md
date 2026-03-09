# Getting a handle on shuttle contractors

By Jeff Porter
*IRE and NICAR*

Space shuttle Columbia crashed in pieces Feb. 1, and all the NASA shuttle program money going to contractors quickly became part of the story.

Journalists covering that angle of the story found that a database of federal contracts of $25,000 or more – called the Federal Procurement Data System – is a great source of information for looking at program spending.

The IRE and NICAR Database Library maintains copies of the data from the General Services Administration back to 1992, covering about a half-million federal contracts each fiscal year. The day of the shuttle disaster, the Database Library culled all of the NASA contracts for each of those years, then posted the data and documentation on its FTP server for a quick download.

Two dozen news organizations obtained the data. In some instances, it allowed journalists to show a local connection to the space program, because the data could show exactly how much money NASA gave to specific contractors in a given state, city or county.

The database is fairly straightforward with a few wrinkles.

There's just one data table, although IRE and NICAR provide a few lookup tables with geographic information and details about the contractors. The primary data table includes the agency, name and address of the company, the amount of the contract, the type of work and where the work was performed.

The type of work listed is not specific enough for certain news reporting. For example, it doesn't say the company worked on the left wing of the space shuttle Columbia. Instead, it might say the company's product or service involved "space vehicles" or "space vehicle components."

Next, contracts can be modified over time, and it's important to understand how the changes are reflected in the data. The GSA data system has a separate record for each of these modifications with each record bearing the same contract number. Take, for instance, contract NAS850000 (with the Boeing Co. for space vehicles), modified 104 times from fiscal year 1992 through 2001.

The records show modification No. 135 in 2001 and an additional obligation of $16.7 million. The next modification resulted in a reduction of the obligation by $1.2 million. So if you add all the numbers together (sometimes over several fiscal years), you can find the total.

Complicating matters further, the GSA has added some fields over time. For fiscal year 2001, the IRE and NICAR Database Library created a program that processes the data, which will smooth some consistency with field names and how dollar amounts are handled over the long run. All those are reflected in the documentation the Database Library provides. Those documents should be examined carefully to account for any of those changes.

It's possible to turn the 10 yearly data files into one. The Database Library kept them separate so it could deliver the data more quickly to journalists the day of the shuttle disaster.

Now, let's turn to the data. We'll go over a basic series of Visual FoxPro commands to choose the fields we're interested in and string the years together, then make some basic queries of the data. Any number of other database managers – Access, SQL Server, for example – could do the trick, too.

First, we studied the documentation and, for our purposes, decided to go with 18 fields, chosen because of their consistency year to year and their importance. They include the contracting agency, the number identifying the contract and any modification, the amount of money, the four fields describing the type of work, the three different fields that could list the company name, plus the locating information on where the company is based and where the work was performed. (See the record layout at *www.ire.org/datalibrary/databases/fedcontacts/layout.txt*).

The complete Visual FoxPro program can be found at *www.nicar.org/techtips.html.* Here are some key parts of the program.

```
use nasa01

select contractor,;
connum,;
modnum,;
entrytype,;
contaction,;
dollaramt,;
prodcd,;
prodnomen,;
naicscd,;
naics,;
contnmicar,;
contnmcif1,;
contnmcif2,;
contcity,;
contstcd,;
contzip,;
stateperf,;
perfcity from nasa01;
into table m:\dataprob\nasa
```

We continued to make separate tables of each year. If a field was named differently in a previous year, we told the program to change the name, simply like this:

```
… siccd naicscd,;
sicnomen naics,;…
```

The GSA had changed its reference from the SIC (Standard Industrial Classification) to NAICS (North American Industry Classification System) from one year to the next. The language simply tells Fox to select the fields refer to SIC and call them the same field names as the 2001 data calls them.

Before 2001, the data implies three zeroes after the dollar amount. So to make it consistent, we multiplied all the dollar amount fields by 1,000 like this:

```
…dollars*1000 dollaramt,;…
```

That line simply does the math and names the field the same as the 2001 data. The 1999 data had a slight variation for the dollar amounts. Instead of indicating a negative number, the data included a field, called NEGATIVE, showing whether the number is negative or positive. So for the 1999 data file, before we ran our main program (although we could have incorporated it into that program), we created a new dollar amount field, then ran a couple of replacements:

```
Replace all dollar2 with dollar
Replace all dollar2 with 0-dollar for negative = '-'
```

Before we stitched all those years together, we needed a way to tell which year is which, so we added a field to each table and told Fox to fill that in with the appropriate year:

```
use nasa98
alter table nasa98;
add column year c(4)
replace all year with '1998'
close databases
```

Finally, we reopened the 2001 table we simply called NASA, then appended all the years together.

There are other ways around this. For example, one could have added the years, then run a UNION ALL query to string the tables together.

With the data file covering 1992-2001, containing 114,126 records, a few queries could trigger some potential thoughts. Here's a very simple one:

```
select year, sum(dollaramt) total;
from nasa;
where prodcd like '18%';
group by 1;
order by 1
```

It shows a 10-year timeline of the money related to space vehicles. Interested in a particular state?

```
select year, sum(dollaramt) total;
from nasa;
where prodcd like '18%' and
(contstcd = 'TX' or stateperf
= 'TX');
group by 1;
order by 1
```

That includes the same timeline, but limiting it to contracts where the company is located in Texas or the work was performed in Texas. Locate the biggest contractors for Texas, on space vehicles work?

```
select contestcd, contnmicar,
contnmcif1, sum(dollaramt)
total;
from nasa;
where prodcd like '18%' and
(contstcd = 'TX' or stateperf
= 'TX');
group by 1;
order by 4 desc
```

This query groups by the Dun and Bradstreet number for the company, the field called CONTESTCD. That's often useful because the data is somewhat inconsistent in how the company is named. It's important to note, though, that some companies have multiple Dun and Bradstreet numbers, so you might need to do a little data checking and cleaning for accuracy and consistency.

Nancy Amons of WSMV-Nashville, was able to localize the shuttle disaster with federal contract data from IRE and NICAR, reporting "NASA pumps millions into our local economy," identifying companies and finding people to interview, guided by the data.

"In all," Amons reported, "NASA awarded nearly $21 million in contracts to Tennessee companies in 2001. Saturday's disaster could mean even more."

Contact Jeff Porter by e-mail at jeff@nicar.org

---

For more information about the Federal Procurement Data System or to purchase it from the Database Library, contact NICAR at 573-884-7711 or go to *www.ire.org/datalibrary/databases/fedcontacts.* The Database Library can provide the data from 1992 through 2001.
