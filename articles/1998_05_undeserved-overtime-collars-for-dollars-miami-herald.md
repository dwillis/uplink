# Undeserved Overtime

**By Dan Keating**
*The Miami Herald*

In late April, Metro Dade Police – the largest agency in south Florida – punished 36 officers, the largest disciplinary effort in its history. Supervisors were demoted and officers were suspended without pay for a widespread scam in which officers, even if they had not performed any police work, added their names to arrest reports in order to collect court overtime.

The department's nine-month internal investigation was prompted by *The Miami Herald*'s 1997 investigation, "Collars for Dollars." In April, the project was named a Pulitzer finalist in the investigative category.

The story pulsed with rich anecdotes produced by the shoe-leather effort of three reporters on *The Herald*'s investigative team. Its foundation lay in ironclad assertions drawn from data analysis, which involved nine different criminal justice datasets from a variety of sources.

The key ingredient was the court's electronic docket that lists officers subpoenaed to court. We obtained records of 704,077 officers subpoenaed in 143,055 felony, misdemeanor, juvenile and traffic cases in Dade County from 1994 through 1996. Our main goal was to tally how many officers were coming to court and then calculate by case, agency, officer and charge.

The hard work wasn't analyzing the data – it was organizing it.

Unfortunately, the raw data was structured in a format that couldn't be used for effective analysis. The database arrived in two tables. One table listed the case number, charge and disposition. With separate records for every charge, each case could have a dozen records or more. The second table had one record for each subpoena, listing the case number, agency, officer and hearing date. It, too, could have a dozen records per case.

Although the tables were related by case number, any attempt to join them produced a mishmash of up to 100 records for an individual case.

### The Multiplicity Challenge

Before we could do anything, we had the tricky chore of reshaping the data. We needed a single record to summarize each case, but we couldn't lose the ability to pinpoint specific officers or charges.

For the charges, we made a single summary record for each case. The record included the first eight charges (if that many were included), a count of the total number of charges, and dispositions.

To be able to quickly find particular kinds of cases, we created yes/no flags for several types of charges: from murder and robbery to prostitution and drunk driving. If a case involved any of those charges, its flag was set to "yes." Since the project concentrated on misdemeanors, the flags let us quickly run statistics on those cases.

We also created a single record for each case in the subpoena database. It included the total number of officers subpoenaed, the names of up to three departments and how many officers were subpoenaed from each. It also noted the officer and department that initiated the case. That showed us how groups of officers piled onto cases.

It's usually hard to turn multiple records into individual summaries with such a wide variety of information. We used SAS because it can manipulate a group of records to produce a single summary record.

To be able to find specific officers, we kept a dataset listing one subpoena per record. A name search would draw up all the case numbers for a given officer. The case numbers could then be linked to the charge summary or subpoena summary to pull statistics for that officer.

Once we had the SAS program to reshape the felony/misdemeanor data, we could change file names to run the same operation on the juvenile data and then the traffic data. The ability to recycle SAS code and repeat a lengthy series of steps came in handy since we ended up getting four sets of the traffic data before the court folks finally produced a database including all police witnesses on a case.

### Gone Fishin'

With the data reshaped, it was time to actually analyze it. First, we cast a sweeping net through the data to catch tips (cases and officers) for the reporters to track down.

We specified a kind of case using the yes/no flags and then grabbed the cases with the most witnesses. We also pulled the officers whose cases averaged the highest number of witnesses.

To see who was in the habit of joining with a friend, we checked how many times any two officers appeared together on a case. To do that, we made a temporary duplicate of the subpoena dataset in order to compare it with itself.

With help from my predecessor and mentor, Professor Steve Doig of the Cronkite School of Journalism at Arizona State University, we used the following code. It's SQL code, but for this story run under SAS. You might find it useful anytime you're trying to match a dataset against itself to pull out pairs.

The original dataset was named subp1 and the duplicate subp2. In the duplicate, the officer identification was renamed copid2 and the case number was renamed casenum2.

The code uses a "less than" on the officer identification number so that each pair can be listed only one way (you won't have both "Keating-Doig" and "Doig-Keating"):

```sql
create table witness.subp3 as
  select subp1.copid,subp1.casenum,
         subp2.copid2,subp2.casenum2
  from subp1, subp2
  where subp1.casenum =
        subp2.casenum2
  and copid lt copid2
  order by 1, 2;
```

The code produced a table of matched pairs with case numbers. We then grouped by the pairs and counted to find which officers appeared together the most. We could also see all the cases of any given pair.

Using those techniques, we found plenty of cases worth checking out. At least six police witnesses appeared in 128 misdemeanor prostitution cases. Two officers (close friends) were listed 238 times as witnesses in each other's drunken-driving cases, even though they worked for different departments in different jurisdictions.

### Publication Precision

To produce statistics for publication, our analysis had to be more precise. We considered other complicating factors, such as officers subpoenaed only to testify about the calibration of the breathalyzer, the tiny proportion of cases with guilty pleas at arraignment, or cases with multiple defendants.

In any analysis, a baseline for comparison is the most important part: What can we use to define what's normal or abnormal? In our case, we had four major police departments, three that pay for court overtime and one that does not.

That made it easy to draw comparisons. For instance, the department that doesn't pay for overtime was 100 times less likely to have at least five officers on a DUI case. The three departments that paid overtime had 6,445 routine DUI cases with at least five officers in three years. Experts said three officers would be the maximum needed to prosecute a case.

One piece of telling evidence: the conviction rate for cases with many witnesses was actually lower than cases with fewer witnesses, suggesting that the extra officers weren't improving case outcomes — they were just collecting overtime.

*Dan Keating can be reached at The Miami Herald.*

---

*The "Collars for Dollars" series, which was a Pulitzer finalist, can be accessed online at www.herald.com/archive/collar*

*Most of the analysis for the story was done on a Pentium 166 with 64 megs of RAM running OS/2 Warp 4.0, SAS for OS/2, Access 2.0 and Excel 5.0. The data files occupied about 325 megabytes.*
