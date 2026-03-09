# Making Sense of OSHA Data

**By Mike Casey**
*The Kansas City Star*

How much is a worker's life worth? What are the most deadly workplaces in your town? Are there factories in your town that are exposing workers to toxic chemicals?

The Occupational Safety and Health Administration database has the answers. OSHA is the federal agency responsible for worker safety, and its database details millions of inspections of factories, steel mills and construction sites since 1972.

Don't let the size of the database or its complexity intimidate you. For a recent project about worker safety around Kansas City, *The Star* purchased the data from the IRE and NICAR Database Library. See *www.ire.org/datalibrary/databases* for details about this database and ordering instructions.

To tailor the analysis for our circulation area, I extracted data for a dozen area counties. It's easy to do using codes assigned to each county in each state. I used Microsoft Access database manager for my analysis of nearly 30,000 records.

## The Big Picture

One way to approach the database is to think of it as a news story. The main table is like the lead of a story that gives you a little about the most important aspects of each inspection. The accompanying tables are like the rest of story; they provide more detail and context.

The main table has more than 50 fields that give the name of the company, its address, the reason for the inspection, the number of OSHA violations, penalties the company paid and a number of other items.

Other tables describe the inspection in more detail. If the inspection concerns a fatality, the database tells you the name of the accident victims as well as the accident's causes.

Another table explains the violations in more detail and references the specific regulations that the company violated. Yet another table provides details about hazardous chemicals found in the workplace.

What connects all of these tables is the unique inspection number, which OSHA calls the activity number. It's just a matter of using your database manager to connect the tables using that field.

## Job Deaths

I was interested in looking at fatalities. In OSHA's codes, a fatality is classified as an "A" in the inspection-type field. I selected all "A" inspection types from the main table and joined that to the others using the inspection number.

Here are some of the things I learned:

- Low fines for workplace deaths or injuries are common even when OSHA cites employers for a serious violation. In 80 such fatal and injury accidents, half of the fines Kansas City area employers paid were $3,000 or less.

- A table detailing the citations showed that the agency sometimes downgraded its most serious willful violations to unclassified and then substantially cut its penalties in these fatal accidents. To find the change, look in the section that details the types of violations. "W" stands for willful and "U" stands for unclassified.

- The table that details fatalities gave the names of workers and I noticed that more workers with Hispanic names were dying on the job. After checking death records, I learned that indeed more Hispanics – particularly immigrants – were killed at local worksites.

The data also showed that falls and electrocutions often caused workplace fatalities in the Kansas City area.

## Data Dirt

Like all databases, OSHA's has strengths and weaknesses. I've found the database information nearly always matched the information in the written reports. Of course you would want to get written reports to verify information about specific incidents in your story.

However, some of the OSHA fields contain dirty data. For example, Ford Motor Co. can be called Ford Motor, Ford or Ford Motor Co – no period. That creates a challenge in finding the companies with the highest number of violations.

Here's how to work with that problem: start by selecting and grouping the company names. That will give you an initial idea of the variations. Once you get the top five or 10, check their addresses to see if the name of the facility is connected to the same address. A company could have several locations, and you want to account for that.

Using the address, city and ZIP code fields can help you come up with totals for each worksite. For example, Factory A has the most violations and its address is 100 Main St. Using wild cards, you also can expand the search of names and addresses to get all of the records at the address or variations the company name. Do the same thing with the company's name using ZIP codes and city codes as a way to check. Yes, this is time-consuming work, but it helps to make your reporting more accurate.

For construction inspections, the worksite is listed as the location, so a construction company may have a number of different sites listed. That makes coming up with a top violator among construction companies very difficult, if...

*continued on page 20*
