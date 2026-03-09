# Discarded and Decayed

**By Ron Shawgo**
*The Journal Gazette*

Landlords affect thousands of lives and have a major impact on the urban landscape.

With that in mind, *The Journal Gazette* set out in April 1999 to identify the top players in Fort Wayne's rental housing industry.

Although *The Journal Gazette* has several computer-assisted stories under its belt, this was our most ambitious CAR project.

Eight months after drudging through lengthy data negotiations, importing hassles and mind-numbing data cleaning, reporter Lisa Shidler and I had a three-day package, "Discarded and decayed."

Our stories revealed that by failing to take over tax-delinquent properties, the county was one of the biggest violators of housing ordinances. We also talked to some typical slumlords and the city's largest landlords, who view housing violations as a cost of doing business.

### The Data Hurdle

Of course, getting data was our first hurdle. We figured that if we had a database of Fort Wayne housing violations we could link those addresses with property tax records to find the owners.

We knew our main task would be identifying property managers, the landlords who rent houses owned by other people. Because their names would not be listed as titleholders, we worked on the assumption that an address that receives numerous tax bills could be a property manager's business address. The assumption largely held true.

We contacted the county treasurer, the county building department, the city-county health department and the city office that inspects buildings for code violations. The six databases we ultimately acquired from those agencies contained county property tax records, health code violations, rodent inspections, building code violations, building demolitions and a list of properties the county could claim for back taxes.

While some agencies gave us free data, the county wanted nearly $3,000 for the property records. After we informed officials that their 2-cents-per-record fee violated state law, the price was greatly reduced.

Officials I dealt with ran the gamut. One health official was the office's main computer authority and e-mailed files to me for free. Another county official knew little about copying data, so I helped guide him through his archaic software to save the data on disk in ASCII format.

### Data Slicing

We primarily used Microsoft Access and Excel to sort the data. (Although the project would have benefited from mapping software, it was done in our pre-mapping days.)

There was a lot of data slicing to do. For example, the rodent inspection office, a division of the health department, had its data on 10 files, one for each year since 1990. Taking into account that new fields were added to the files from one year to the next, I spliced them together.

We then added the rodent database to a much larger one listing health code violations, such as improperly disposed trash, discarded tires and appliances, and child neglect. That database also came in several files with slight differences and had to be spliced.

Our two largest databases came from the county treasurer. One contained information on the property being taxed, and the other contained tax payment details, including addresses where tax bills are sent. Although the files contained a massive amount of information, we needed them only for current and former owners and the billing addresses.

The tax files caused our only data importing headaches. As our information systems people worked out the kinks, we began cleaning the data we had in hand.

Because we wanted to link all of our tables by their address fields, making addresses uniform was important. Input errors, omissions, misspellings and a general lack of uniformity in those addresses made the task time consuming and nearly overwhelming.

### Address Problems

Some addresses had no directional prefix (N, S, E or W); others had no street type (road, drive, circle). Data cleaning took several months and required combining address fields and eliminating leading spaces, a couple of new Access tricks I learned with the help of NICAR-L subscribers.

We also got a list of county and city streets with their numerical address ranges. Knowing the ranges — addresses where a street starts and where it ends — was essential in handling streets with common names and placing a violation in the proper locale.

Although our focus was Fort Wayne, health code violations covered the entire county, and the city or town was not always listed. A violation on Main Street could be in Fort Wayne or any of eight other towns with a Main Street in the county. Having address ranges, which often vary from town to town, helped us narrow our options.

The ranges also helped us correctly place violations on Fort Wayne streets with similar names. For example, if a violation was written as 1234 Reed, we had to verify if it was Reed Road or Reed Street, both of which are in the city. If an address could not be verified, the violation was discarded.

We also used the Census Tract Street Locator (http://tier2.census.gov/ctsl/ctsl.htm) to verify some addresses. The locator allows you to select a county and search for street address ranges by entering a partial street name. It is good for all but the newest streets.

Because our violations databases seldom listed homeowners, we linked addresses in them to the treasurer's database, which contained current and past owners and dates the property transferred to their names. Those transfer dates were important, because they identified who owned a house when a violation was committed. Using violation and transfer dates as sorting criteria, we ran Access queries to link owners with offenses.

But that was only partially helpful with our database of building code inspections, which covered things such as peeling paint, rotting eaves and crumbling foundations. The date on that database referred only to when the house was first inspected for violations. Subsequent inspection dates were not listed.

The database also gave no details on the number of violations a house received over the years under various owners, making it impossible to rank problem landlords. Although it gave us a starting point in our search, we had to delve into paper records for details.

### County Titleholders

It was clear from the time we started compiling the data that the county would be part of the story. Although not landlords, the county commissioners, who have the authority to take title to properties for back taxes, were listed as the titleholder of many properties with violations.

Concerned about maintenance and liability issues, the county in the mid-1980s decided to leave tax-delinquent property in the owner's name with the option of claiming it at any time. After discovering the county connection, we asked for and received a database of about 1,000 properties "certified" to the county.

Many of the houses are vacant. Some properties eventually are turned over to nonprofit agencies. But many are left to decay.

As a result of our series, the county has initiated ways to eliminate some of the complications for giving unwanted properties to nonprofit agencies. The county also formed a committee to address the housing problem and decided to have an additional tax sale in an attempt to get the properties back on the tax rolls.

Ron Shawgo can be reached by e-mail at rshawgo@jg.net.

*The Journal Gazette's* series on "Discarded and decayed" can be found at: www.journalgazette.net/projects/landlords/series1_1.htm. Also in the IRE Resource Center, story #15931.
