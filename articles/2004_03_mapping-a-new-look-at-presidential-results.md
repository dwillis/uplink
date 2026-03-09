# Mapping a new look at presidential results

By Robert David Sullivan, *CommonWealth*

"Beyond Red & Blue," an exclusive report on *CommonWealth* magazine's Web site, takes a fresh look at presidential elections by identifying 10 distinct political regions that cross state boundaries. Drawing the new political map of the U.S. required elections and Census data, mapping and spreadsheet analysis and some judgment calls.

The project evolved from "The Lay of the Land," a story about the political regions of Massachusetts. That story, by comparison, was a no-frills affair. I typed election results for all of the 351 cities and towns in Massachusetts into Microsoft Excel, and then assigned each city and town to one of 10 regions with almost equal voting strength.

For "Beyond Red & Blue," I did the same for the 3,117 counties in the United States and used ESRI ArcView 3.3 geographic information system (GIS) to create detailed colored maps that later were turned into graphics for the report on our Web site. (See *www.massinc.org/commonwealth/new_map_exclusive/beyond_red_blue.html*).

## Data into Excel

As I built an Excel master data file with the names of the U.S. counties I added elections data collected from Web sites and printed sources. In each state, the Secretary of State's office – or whichever agency oversees voting – posts this information on the Internet. In many cases you can download or cut and paste data directly into Excel. (See *www.politics1.com/states.htm* for links to all 50 states.)

Other great sources of data are Dave Leip's Atlas of U.S. Presidential Elections (*www.uselectionatlas.org*) and the "America at the Polls" books edited by Richard M. Scammon.

The first column of the spreadsheet listed the county and state like this: "Jefferson, AL," "Jefferson, AR," to distinguish between counties having the same name in different states.

In the adjacent columns, I entered how each county voted in every presidential election since 1976. (This was not as time-consuming as it sounds. I often used Excel's "fill handle" to mark all the counties in a state as Democratic or Republican, then went back and noted the exceptions, which were usually few.)

I then sorted the results and used formatting tools to color the counties according to which party carried them in the close presidential elections of 1976 and 2000. I ended up with four categories: Democratic both times (blue), Republican both times (red), Democratic then Republican (yellow), and Republican then Democratic (green).

That was a good starting point, and I used it to get a preliminary picture of the 10 regions. I added another column to the spreadsheet and assigned each county to one of the 10 regions, basing the decision not only on the voting history but also on the results of certain state elections, and geographic factors.

To come up with 10 regions that had an equal numbers of voters (as far as that was possible), I added another column to the spreadsheet that included the total number of votes cast in each county during 2000.

Using Excel, I was able to automatically add up all the votes cast in every county labeled as being part of, for example, the Appalachia region that I had defined. That way, whenever I reassigned a county from one region to another, I immediately saw how the change affected the totals for both regions. By keeping an eye on which regions were significantly larger or smaller than 10 percent of the electorate, I was able to keep redrawing the boundaries so that none of them got too large or small.

At this point, I got greedy for more data. I wanted to use demographic factors to further refine the 10 regions. So I created separate Excel spreadsheets for criteria such as age, family income, and population growth. I downloaded county-level data for all of these factors from the U.S. Census Web site (*www.census.gov*).

## Smart linking

I also linked all of these new spreadsheets to my original spreadsheet through the VLOOKUP function. Thus, each row of data in my Census spreadsheets included a county name and state, and I told Excel to find the equivalent county name and state in my master data file, then plug in the right region names in the new spreadsheet.

As in the master data file, I used the SUMIF function – and simple calculation formulas – to get raw Census numbers and percentages for each region. Because all the spreadsheets were linked to the master data file I only had to reassign a county from one region to another on my original spreadsheet to change all the spreadsheets.

If I looked at the spreadsheet for educational attainment and discovered that the demographics in an Appalachian county more closely matched the Farm Belt region, I would change the county's designation in the master data file, and it would automatically change in all the other Excel files, producing new regional totals in each of them. Because of this system I didn't have to make any final decisions as to which counties were in which regions until the *(continued)*
