### Pictures better than words
## Mapping reveals data trends

**By Ronald Campbell**
*Orange County Register*

Databases are wonderful tools, but sometimes you've got to have a picture to tell the story. When *The Register* set out to document whether bankers were serving poor neighborhoods, the raw numbers told us they were. Intuition told us they weren't. A mapping program proved our intuition correct.

For years my editor and I have speculated about the paucity of banks in Santa Ana, a heavily Hispanic city of 300,000. Orange County has hundreds of banks; in some neighborhoods they are clustered as thickly as gas stations once were. But not in Santa Ana.

We both thought a computer mapping program could help us document the pattern. But then we ran into a barrier, and it stopped us cold. The problem was data entry. It wouldn't be enough to locate all the branches in Santa Ana; to make a valid comparison, we had to find all the branches in neighboring cities. Finding the raw data was easy enough: The state banking and savings-and-loan associations each printed annual directories. But some poor schmuck (most likely me) would have had to type all those names and addresses into a database. Then I (no alternatives this time) would have had to plot the branches on a computer map, a process known as geocoding.

The idea of geocoding several hundred banks was so terrifying that I stopped thinking about it for a year.

But late in 1993, banking writer Dawn Yoshitake discovered a database maintained by Sheshunoff Information Services. It also let us look beyond Orange County to examine statewide patterns. Finally, and maybe most importantly, it sidestepped geocoding.

Geocoding is a messy business. Most databases that I have used contain a cacophony of conflicting address styles. Is it "625 N Grand Ave" or "625 North Grand Avenue" or maybe "625 N. Grand Ave."? To the database user, it hardly matters. But in mapping software, the distinction between "N" and "North" or "Ave" and "Avenue" is a vital one; every address must match the internal style of the computer map. And since computer maps often omit valid addresses, even a correctly styled address may not geocode.

With Sheshunoff, I did not have to worry about geocoding. I could locate banks by their census tract or zip code.

My first step was to look for statistical patterns. I loaded the Sheshunoff database into FoxPro. After hand-eliminating hundreds of credit unions (listed only once in the database, regardless of the number of branches), I used FoxPro to count the number of bank branches in each of Orange County's 484 census tracts. Then I compared that with income data. I assigned each tract to an income range (low, low-moderate, upper-moderate and upper), based on that tract's median family income. Finally I compared the number of bank branches serving neighborhoods of a given income range with the number of people living in those tracts.

Surprise! It appeared that bankers were about as likely to set up shop in a lower-middle class barrio as in a glitzy neighborhood overrun with BMWs. The numbers in Orange County looked especially strange after I reviewed the statewide numbers. The statewide analysis, done by zipcode instead of census tract, showed that bankers avoided lower-middle-class areas.

Then I dumped the data into my mapping program, MapInfo, and the county pattern suddenly became clear. Bankers willingly put branches in poor or minority neighborhoods — but only if those neighborhoods bordered wealthier, whiter neighborhoods. When MapInfo shaded census tracts by the number of bank branches, the resulting map had a gaping hole in the middle. The hole corresponded with Orange County's largest and poorest barrio.

The map told a lot. Graphic artist Danny Sullivan found a way to make it tell even more. MapInfo census tables contain population and housing data; draw a line around several census tracts, and MapInfo will add the numbers together to produce statistics for the region. Danny joined the basic MapInfo table with a database table I had created, which included the median income, ethnicity and population for every census tract. Then he circled five areas on the county map. MapInfo calculated the average income (actually, the average of median family income for each tract in the selected area), as well as population and the number of bank branches for each of those areas.

---

### Where to find banking info

Sheshunoff Information Services' Bancpen database includes geographic and financial summaries on every bank branch, every savings-and-loan, every credit union.

Fields include company name, branch number, street address, city, Zip code, county, state, Metropolitan Statistical Area (MSA) code number and census tract number. In addition, the database lists deposits (broken down between deposits by public agencies and deposits by individuals, partnerships and corporations) year by year for the past five years.

Sheshunoff sells the database on diskette for $595 per state. Tape versions go for $700. Orders for two or more states qualify for a 20-percent discount. The national database is sold for $5,000 on diskette or $5,500 on tape. To order, call (800) 456-2340.
