# Building a database for tracking state money

By MaryJo Sylvester, *Center for Public Integrity*

State Secrets, an investigation of contributions and expenditures reported by state political party committees, started with a pile of paper reports that stood more than 15 feet high. That doesn't count thousands of records obtained directly in electronic format.

All told, there were nearly 400,000 records — and no easy way to put them together. The paper forms differed from state to state. Even the content in a single state didn't always remain consistent.

As a result, compressing all of that into one table of contributions and another of expenditures — and cleaning them — provided valuable lessons in how to build an effective database.

The Center for Public Integrity, in conjunction with the Center for Responsive Politics and the National Institute on Money in State Politics, published the findings of the yearlong investigation on June 25. (See the July-Aug. 2002 *Uplink* for more on political reporting.)

Our analysis showed that 46 percent of the money state political parties collected in the 2000 election was soft money from national party coffers. These transfers confirmed a commonly held perception that state parties are used to channel soft money and influence presidential and congressional elections.

## Paper to data

Even the most organized person would be taxed by the collection of hundreds of reports and the data entry. Planning how you're going to tackle the paper pile is crucial no matter the database size. If you don't set it up properly, you'll have bigger problems later.

There were some things that made life easier with State Secrets:

- I created an Access database where our staff members tracked our FOIA requests for each state, including phone numbers, Web sites, and notes. They also had a Word file for each state for more extensive notes and e-mails. I could run a query to quickly see what was missing.

- I pored over the campaign finance forms and listed the various features of each in an Excel worksheet. This showed me which fields were necessary for data entry and where the limitations were.

- We hired a data entry firm. This was, by far, the best move we made.

- We broke the work into manageable chunks. In this case, it was on a state-by-state basis. Once all the data entry, basic cleanup and checking was done on each of the states, we appended the files together. Some of the cleanup (like standardizing names) was better left until after we assembled the full table, however.

- We ran summary queries to compare the total expenditures to the summaries listed on paper reports. We found missing pages, duplicate records and even bad math on the part of the political parties that we would not have found without these queries.

In hindsight, I should have created ID numbers for each of the paper reports. The data entry house could have typed those IDs into the data to indicate which paper report each item came from. And the forms could have been stored in numerical order for easier access.

Instead, we used the name or date of the report (such as "Fourth Quarter report" or "Pre-Primary"), but there was so much inconsistency we had to spend several days standardizing the report names in order to do the summary queries mentioned above.

I also would have assigned a code to each committee to be typed in addition to the name. We applied a code only after the information was typed — a difficult process because the committee names were never consistent.

## The scrubbing phase

Before embarking on data cleanup you should answer two questions: What standards do you want to meet? And how dirty is the data? (See page 16 for details.)

On the expenditure data, we decided it would be an ineffective use of our time to clean up all recipient names, but consultant names should be standardized so we could focus on those. On the contribution data, we scrubbed and scrubbed to make sure the contributor names were as clean as we could get them. We set a very high standard because we wanted to be positive that we identified the true top donors.

Figuring out the dirtiness of the data is the harder part. I'd recommend running queries, and making notes about the variations you find. Are there big chunks with consistent patterns that could be fixed using an update query? If you can pinpoint places to do mass updates first, that will save work later. Eventually, you'll have to do line-by-line cleanup no matter what, so do whatever you can to minimize that.

All of the suggestions I've listed here are beneficial no matter how small or large the database. Consistency and advanced planning will make your job much easier in the long run.

*MaryJo Sylwester, formerly with the Center for Public Integrity and now with* USA Today, *can be contacted by e-mail at msylwester@usatoday.com*
