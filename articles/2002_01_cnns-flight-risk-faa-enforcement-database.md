# CNN's 'Flight Risk'

**By Denise Prodigo-Herrmann, *Database consultant***

In the weeks following 9-11, journalists around the country were scrambling to make sense of the Federal Aviation Administration Enforcement Information System (EIS) database.

Under the guise of "national security and safety" the Federal Aviation Administration refused to comment about any information relating to the enforcement database, making it difficult to decipher the meanings of some codes within the database. The NICAR listserv was flooded with information, ideas, concerns and strategies relating to the data and was a helpful resource during the entire analysis process.

Because CNN was interested in security issues relating to the top 25 airports and the top 10 airlines in the country, I obtained a list of the top 25 airports based on passenger load from Airports Council International and a list of the top 10 airlines from the U.S. Department of Transportation. My analysis focused mainly on the FAA EIS database, but reports about airport security and safety from the General Accounting Office also were used. While the enforcement data was said to date back to 1962, the earlier years of data did not seem complete. The final CNN analysis covered a 10-year period from 1991-2000.

Within the FAA database, the main table included all incidents relating to enforcement, such as flight operations, training, drug testing, hazardous materials and security. Using Microsoft Access, security incidents were isolated using cat_code = 20 in the main table. The security table detailed the type of security violations.

When linked with the main table, the database started to tell a story. For example: On April 19, 1991, at Anchorage International Airport, concourse B, a male passenger, whose identity is expunged in this database, had a firearm in his possession. The firearm was detected in the X-ray machine, and the firearm was unloaded.

### Focus on Weapons

With more than 300 security codes and no FAA confirmation, it was difficult to ascertain the meanings of these codes. After much debate and research, I decided to focus on all security breaches related specifically to weapons. Weapons were defined using the following security descriptions: bludgeon, explosive, firearm, firearm – hand gun, firearm – long gun, incendiary, knife, other weapon, stun gun and tear gas/chemical.

Grouping these descriptions into one category showed the number of weapons detected at each airport by year with further breakdowns of the number of weapons.

Security descriptions allegedly relating to tests conducted by the FAA, where FAA employees dress in plain clothes and try to get items through security check points, were not used as the meanings of the code descriptions were unclear. Some reports, for example, stated that the code "Fail Detect HG" meant failure to detect a handgun while others reported that it meant failure to detect a hand grenade. Without FAA confirmation of the meanings, I decided to take a more cautious approach to my analysis.

### Stories and Graphics

The six-week project produced nine stories written by CNN.com reporter Mike Fish and a number of detailed graphics designed by the CNN.com staff. The graphics showed:

- The number of incidents and violations at the top 25 airports and the top 10 airlines over a decade. For each incident, there could be numerous violations. The numbers were broken down year by year for each airport and airline in separate charts.
- The number of weapons found at the top 25 airports over a 10-year period. These numbers also were broken down year by year for each airport in separate charts.
- The dollar amount paid in fines by the top 10 airlines from 1998–2000, according to the FAA quarterly enforcement reports.
- The annual turnover rate of security screeners at 18 airports as reported by a GAO aviation security report from June 2000. The percentages of security violations for the same period also were reported from the enforcement database.

Denise Prodigo-Herrmann can be reached by e-mail at dmph@bellsouth.net
