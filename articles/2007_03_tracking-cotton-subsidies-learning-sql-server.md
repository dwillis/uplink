# Tracking Cotton Subsidies and Learning SQL Server on the Fly

**By Megan Clarke, *The Atlanta Journal-Constitution***

Cotton is still king in Georgia. In 2005, the federal government pumped $317 million in subsidies into the state for cotton alone, making it Georgia's top subsidized crop.

Georgia's take was a piece of $23 billion in subsidies paid nationwide that year. American farm subsidies are criticized around the world for artificially depressing crop prices, and *The Atlanta Journal-Constitution* decided to see how those payments help or harm farmers in the United States.

To tell the story, we chose cotton subsidies because of the amount of money involved and the crop's historical importance in Georgia. My collaborators were reporters Ken Foskett and Dan Chapman, and projects editor Jim Walls.

The U.S. Department of Agriculture's Farm Service Agency is responsible for distributing subsidy money. I requested payment data for the entire country dating back to 1994. FSA initially assured me the data included all subsidy payments. But after some research and checking with a fellow CAR person, I discovered I needed databases for three more programs with nearly $4 billion a year in subsidies: tobacco transition payments, commodity certificate payments and cotton cooperative certificate payments.

By requesting a fee waiver because the information was of "public interest," I avoided paying for any of the data. The payment database took about a month to receive, but the others, which are not requested as often, took a little longer. I would recommend requesting expedited action in your FOIA request. Most federal agencies do not recognize such a request, but FSA did.

Once I received 70 GB of data – 180 million records – it was clear that my usual software, Microsoft Access and FoxPro, were not going to cut it.

With trouble-shooting help from our then-CAR editor David Milliron and the book "Sams Teach Yourself Microsoft SQL Server 2000 in 21 Days" by Richard Waymire and Rick Sawtell, I took a crash course in SQL Server.

The capabilities of SQL Server were overwhelming at first. It can handle 1 million terabytes of data, versus 2 gigabytes in Access. (The drawback to SQL Server's power is that it comes with a hefty price tag.)

I learned the organization and the differences in SQL statements on deadline. SQL Server syntax slightly differs from SQL commands in FoxPro (wildcards, for example and excluding the semi-colon after each line in a query). One handy feature with SQL Server is the color-coded command text. SELECT, DELETE, INSERT all turn blue when used properly and values turn red when your syntax is correct.

If you're transitioning from Access or FoxPro, stick with what you know (e.g. familiar queries) in the beginning. Once you get used to the software, it's easier to transition to advanced features. I continue to use Access and FoxPro for quick-hit analyses or daily CAR, but SQL Server has offered more advanced options for more organized, efficient analysis.

SQL Server also provides more advanced security and a great feature called transaction logs, which documents almost every change made to the database. Like most database management software, SQL Server provides advanced processing tools.

For the subsidy story, I used summarizing queries to produce aggregates by several different categories. My biggest interest was finding oddities and outliers. (When you see a person with a Beverly Hills address collecting cotton subsidies in Georgia, it piques your interest.) Through geographic and time-ordered slices of the data, I was able to spot trends. Besides calculating the typical aggregate totals, my objective was to create tip sheets for the reporters in order to identify individual farmers and programs for them to look into.

Combining the processing, mapping, analysis and memos, I worked on it for about five months.

The payment database includes a separate name table, which includes farm operator names and addresses. The tables are linked by a customer number, which is a surrogate for the tax ID that FSA normally uses. All of the different subsidy datasets can be linked using the customer number. The payment data also includes state codes, county codes, program names, types of crops, date and amount. It does not include the location of the farms, other than the county and state. I started cross-referencing the payment data with entity data, which identifies the members of each entity that collects subsidies. I found many recipients living quite a distance from the farms they are collecting on. People in Atlanta, New York City and even Saudi Arabia and Japan were collecting subsidies for U.S. farms.

It became apparent we needed to rework our definition of "farmer." We discovered that college students, churches, prisons, universities, corporate pension plans and even a sports bra company collect farm subsidies. Familiar names also popped up in the data, too including Chevron Corp., CNN founder Ted Turner and Georgia Gov. Sonny Perdue.

Late last year after we published our project, FSA released a new data set of subsidy recipients, called 1614, that news organizations have not had until now. The dataset, named for Section 1614 of the 2002 Farm Bill, tracks all subsidy payments to a human being when possible. The new data is only 6 GB and contains 66 million records for payments from Oct. 2002 to June 2006.

Previously, some payment records stopped at the corporate level and did not disclose the owners cashing the subsidy checks. The 1614 data connects the dots for you. With the old data, I was able to uncover most of the owners behind corporations with a few extra queries.

For those organizations that don't have access to database management software like SQL Server, The Environmental Working Group, an advocacy group, posts subsidy data online. On its Web site, *www.ewg.org*, EWG illustrates aggregates and provides a searchable database to look up specific recipients and their entities.

After analyzing the payment records, we found:

- Five percent of eligible farmers collect half of all U.S. farm subsidies.
- Farmers can easily circumvent USDA limits on subsidy payments. Nearly 200 U.S. farm operations collected more than $1 million each in 2005. That's nearly a quarter of a billion dollars to a group that could fit inside a grade school cafeteria.
- Subsidies drive up rural land prices and prevent small American growers from farming more land.
- Wealthy Americans and institutions with no apparent need for government aid, including some who live far from their farmland, collect hundreds of millions of dollars in subsidies. Enforcement of income caps for subsidy recipients is spotty.

The data also turned up great leads on individual farmers. A top USDA official was the nation's single biggest beneficiary of a disaster relief program for orchard owners. Some farm operators accused of scheming to collect millions they were not entitled to later received millions more under new corporate names. Farmers who hit payment limits organized new partnerships to double or triple their subsidies.

The findings highlighted a fundamental flaw with current U.S. farm programs: They benefit landowners, sometimes to the detriment of farmers. That's because cropland owners can collect a subsidy even if they grow nothing, or they contract with a farmer to farm the land and split the subsidy.

We took it a step further and compared subsidy payments with those of another USDA program: food stamps. We found that a third of Georgia's counties collected more in farm subsidies than food stamps.

Agricultural Census data provided an astonishing glimpse at the decline in farms and farmers in Georgia. Compiled by the National Agricultural Statistics Service, the ag census provides state and county-level numbers on everything regarding agriculture and is conducted every five years. NASS will survey farmers in December of this year; the data should be available in February 2009.

*AJC Reporter Ken Foskett contributed to this article.*

*Contact Megan Clarke at mclarke@ajc.com.*
