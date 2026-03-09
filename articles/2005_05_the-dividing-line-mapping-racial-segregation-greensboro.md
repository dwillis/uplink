# The dividing line

By Matt Williams
*The (Greensboro, N.C.) News & Record*

Not long after moving to Greensboro more than a year ago, I realized that to buy groceries or clothes or see a movie, I always drove in the same direction: west. This, even though I lived right in the middle of downtown.

Decades after the end of legal segregation, thousands of residents still did most of their shopping on the "white" side of town.

It's the same problem I'd hear often from minority residents of the east side of town: There just aren't as many places to shop in our part of town as there are in yours. The places we used to shop steadily closed and have been abandoned, while all the new stores open up on your side of town.

But community leaders were never really able to quantify the sense shared by many that there was an inequity. Faced with this, I started to piece together the *News & Record's* attempt to do that.

Putting together the numbers was the easy part. Finding out the "why" was the challenge.

I began by creating the base for my comparison, in this case block-level data from the 2000 Census. Using the smallest geographic level of Census data allowed us to see with ESRI ArcView 8.3 geographic information system (GIS) the patterns of racial distribution. We got the demographic and map data through the Census Bureau's Maps and Cartographic Resources Web site at *http://tiger.census.gov*.

In ArcView, I joined the demographic data file, which includes population by race, to the Census blocks map. I then set the symbology properties to show the percentage of whites living in each block.

Right away, the racial segregation was clear to the eye, with two major streets in the Census TIGER street file running diagonally through downtown delineating the two sides of Greensboro. We selected those roads as our "dividing line."

The western half of the city was home to a little less than two-thirds of the city's population and was 80 percent white. The eastern half was home to a little more than one-third of the total population and was 77 percent black – a virtual mirror image. Within those two there were large areas where the dominant ethnic group made up more than 95 percent of the residents.

Before we even started, we had numbers that would surprise most of our readers. Like me, they might have assumed that the city was somewhat segregated but had no way of quantifying how much it is segregated. From there, I gathered names and addresses to place businesses of all types throughout the city. Some of the data was publicly available, such as the location of bank branches insured by the Federal Deposit Insurance Corporation. Those files can be found at *http://www2.fdic.gov/idasp/main.asp*. The rest were simply copied into Microsoft Excel spreadsheets one-by-one out of online phone directories. Those were then exported to comma-delimited text fields that were imported to ArcView.

ArcView's geocoding function takes a table containing street address data and turns it into a point map using a street file, such as a Census TIGER street file, as a reference. We displayed each type of business with a different color, and we could display only banks or just grocery stores.

After those businesses were geocoded, we created a simple tally of the number of locations on either side of the dividing line. Once we took population into consideration, it was easy to see the disparities. We obtained the population of each side of the city by selecting the Census blocks for each and using ArcView's summarize function to calculate a total.

Per capita, there were half as many banks on the "black" side of town and a third fewer grocery stores. In other categories there was no contest: all of the 60 movie screens, eight urgent care centers and all but one major retailer were on the "white" side of town. If the movie screens were distributed evenly based on the population, there should be 40 on the west and 20 on the east.

Fast-food restaurants and dry cleaners, which were also included in our analysis, showed roughly equal distributions. Pawn shops, check cashers and payday loans were skewed the opposite way. They were twice as common in minority neighborhoods as white ones.
