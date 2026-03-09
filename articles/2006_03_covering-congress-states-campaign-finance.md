# Covering Congress, States Getting Trickier

By Derek Willis, *The Washington Post*

Using computer-assisted reporting to cover congressional elections used to be so much simpler.

The Federal Election Commission's FTP site was the first stop, where pretty much all of the campaign finance data you would ever need resided.

Now, thanks to 527 political committees, state PACs and the 2002 McCain-Feingold campaign finance law, things are more complicated.

It is no longer enough to limit your data gathering and analysis to the two or more candidates in a given congressional or statewide race. Do that in 2006 and you could miss the big story, or at least trail the rest of the pack on it.

While the FEC is still the starting point for federal races, it is not the finish line. Those using CAR for elections should assess the contests they will be covering to see whether the old boundaries between federal and state races still apply. If your state has a hot race, then you will need to know how to gather data from multiple sources and integrate it into a single system.

Consider the election for Virginia's attorney general in 2005 (Virginia is one of a few states that have significant off-year elections). While Republican and Democratic candidates raised millions for this statewide post, the GOP candidate got more than a third of his money from a single source: the Republican State Leadership Committee. Because the RSLC is a 527 organization reporting to the Internal Revenue Service, Virginia regulators and journalists knew only that it had given a bunch of money to a state candidate. They did not know where that money came from and, thanks to the IRS reporting schedule, they would not find out until after the election.

Elections in 2006 will see more frequent disclosure from 527s, which follow a reporting schedule roughly equivalent to the FEC in even-numbered years. And like the FEC, the IRS releases its data in bulk — meaning that CAR folks will have to download the entire set of 527 electronic filings and then find the committees they are after. If you have never done this before, a little practice wouldn't hurt. Unlike the FEC, dealing with the IRS data doesn't require any reformatting of fields (something you can avoid by purchasing FEC data from the IRE and NICAR Database Library), but it does lump original and amended filings in the same compressed file.

Updates are available every Sunday at *http://eforms.irs.gov,* and The Center for Public Integrity also has a regularly updated site that provides downloadable contributions and expenditures for 527 committees *(www.publicintegrity.org/527).*

In federal races, some advertising activity by 527 committees must be reported to the FEC, thanks to the McCain-Feingold law. These expenditures, known as "electioneering communications," occur when an organization not registered with the FEC airs a television or radio ad that mentions or identifies a federal candidate within 30 days of a primary election or 60 days of the general election. Such ads fall under the scope of the law only if they are targeted to a candidate's constituency; if the Sierra Club runs an ad about a New Jersey candidate in Arizona, it would not meet the criteria.

The good news about electioneering communication reports is that they include very specific information about ad buys, including the stations and amounts involved, and reports are due within 24 hours of the ad's initial appearance. The bad news is that those reports are filed by fax only. For journalists outside Washington, D.C., that means waiting on the FEC to scan and post images of those faxes, which sometimes are difficult to read. It also means that there is no database of such activity, unless you decide to build one (The Center for Public Integrity did so for the 2004 elections).

This year, state political parties will face their first real test since McCain-Feingold, since many of them received an artificial boost during the 2004 presidential campaign. State parties now find themselves having to raise and spend mostly federal or "hard" money, since even the most generic party activity is presumed to have some benefit to House and Senate candidates on the ballot. So if your state has a looser reporting schedule, you may find that the state parties' federal accounts file more often and contain the bulk of the money raised and spent. In some cases, journalists will find more details in the federal data than is required on the state level. Beware of duplicative reports — reconciling state and federal data can be a tricky proposition. When in doubt, call the treasurer or the party official in charge of filing the reports for an explanation.

In most respects, the FEC hasn't changed its data-handling process much; the data it makes available via FTP is updated every Monday morning (usually before 5 a.m., for those interested in running Scheduled Tasks in Windows or cron jobs on other operating systems). These files contain all of the contributions associated with a two-year election cycle (the current cycle began the day after the 2004 election).

There are ways, however, to avoid working with the entire set if you are only focusing on a handful of committees. All FEC committees, except for Senate candidates and the two parties' senatorial fundraising arms, file electronic reports to the FEC, and those filings can be downloaded and used to create databases. The advantages of doing so are two: timeliness (you can access a filing as soon as it appears in the FEC's system) and the presence of expenditures, which the FEC does not keypunch or release in bulk form but are available on a filing-by-filing basis.

Expenditures are easily the least-covered aspect of campaign finance, and sometimes the most important. They can show the tactics used by campaigns (direct-mail fundraising or big, flashy events?) or provide home addresses for campaign workers. Particularly interesting are the expenditures of candidates who face little or no opposition — what do they spend their money on?

Such reporting can yield great stories, but if you go this route, remember that you'll need to keep track of the filings, because amendments appear often. I've found that it's useful to track filings themselves, and you'll probably want to do the same if you plan to maintain the latest and greatest version of a committee's data.

The electronic filings end with the file extension ".fec", but they are delimited text files that can be imported into Microsoft Excel or other programs. But you'll want to be familiar with the layouts and keep in mind that each filing contains all of the transactions associated with that report: contributions, expenditures and summary figures, all stacked on top of each other.

A campaign finance junkie would do well to keep checking the FEC's FTP site regularly, however; the agency often will place custom collections of data there that might prove useful.

One last tip, which has been a personal interest of mine: don't forget the metadata. In campaign finance, the metadata means things like when a committee reports, how many amendments it files or even the length of the reports. Such details are worth tracking because they can provide insight into the operations of the campaign. Multiple amendments filed on the same day are a sure sign that either the campaign's accountant found a mistake or the FEC's auditors did. Either circumstance is worth a look, and may yield a good story.

Contact Derek Willis by e-mail at willisd@washpost.com.
