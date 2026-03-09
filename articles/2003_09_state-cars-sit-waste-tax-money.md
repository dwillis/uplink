# State cars sit, waste tax money

By Morgan Loew, *KPHO-Phoenix*

Heading into the 2003 legislative session, the state of Arizona was facing a $1 billion budget shortfall. As in nearly every other state in the country, revenues had fallen, programs were getting slashed and lawmakers were desperately looking for ways to cut expenses.

Journalists were also under the gun to find wasteful spending and report it in print or on the air as fast as possible. We found it in an unusual place: state vehicles that were used so little, the state's own guidelines said they weren't worth the cost of owning them.

Compared to hard-core computer-assisted reporting projects that can take months of spreadsheet and database analysis, this story was pretty simple to do using the skills I learned in a NICAR Boot Camp in January.

### Looking for efficiency

We found a recent audit of one state agency that referred to an "efficient use guideline" for state vehicles. It concluded state vehicles needed to be driven at least 10,000 miles per year to justify the cost of acquiring and maintaining the vehicles.

With that minimum mileage standard in mind, we sent a public records request to the Arizona Department of Administration asking for the entire state vehicle database. The department buys most state vehicles and leases them to individual agencies.

We specifically asked for the following: license plate numbers; agency the vehicles are leased to; year, make and model of the vehicle; mileage at the beginning of the last fiscal year; and mileage at the end of the last fiscal year.

As is the case with most requests, the data I had asked for had shortcomings. Some vehicles were bought in the middle of the year and some were retired in mid-year. The result would not have given me a clear picture of how many miles were driven over a full year. Fortunately, the public information officer I was dealing with helped me and we came up with a better request.

### Querying the data

The department provided an Excel file at no cost that had more than 2,000 rows and included a column that showed the average miles driven per month. It appeared the state had done most of the work for me. All I had to do was import the data into Microsoft Access and write a query that isolated vehicles driven fewer than 10,000 miles per year (834 miles per month.) It looked something like this in Structured Query Language:

```sql
SELECT *
FROM [veh list]
WHERE [FY03 YTD Average miles driven per month] <= 834
```

The result was that nearly half the vehicles were underused, according to the state's own guidelines.

We listed the agencies with the most underused vehicles by using the following query:

```sql
SELECT Agency, count(*)
FROM [veh list]
WHERE [FY03 YTD Average Miles Driven per Month]<= 834
GROUP BY Agency
ORDER BY count(*) DESC
```

So we had a story, but we needed a good way to tell it. I spent a couple of days driving around the state Capitol, studying parking lots that held state vehicles. My photographer and I performed surveillance next to one of the lots, and watched as several state vehicles just sat there day after day. We now had one good visual element to illustrate the issue.

### Adding perspective

Next, I contacted the state Department of Education and got a list of relatively inexpensive state programs that were facing the budget axe. We ended up profiling a program for underprivileged preschoolers and another that helped adults get their high school diplomas.

The story boiled down to this: "State leaders say there is no money lying around to fund programs like preschool and adult education, but we found lots of extra tax dollars – literally 'parked' all over the state Capitol."

The day the story aired, the governor held a news conference to announce an "efficiency review." Part of that review dealt with state vehicles. The governor pledged to get rid of the vehicles that did not meet the minimum mileage standards. She said one of the beneficiaries of the savings would be education spending.

In the end, the database work made up only a small part of the story, but it provided the real meat. Without my limited background in CAR, I would have never thought to look for wasted tax dollars in a parking lot.

Contact Morgan Loew by e-mail at Morgan.Loew@meredith.com.
