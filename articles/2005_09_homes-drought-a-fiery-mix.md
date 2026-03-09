# Mapping It Out: Homes, drought a fiery mix

By Scott North
*The (Everett, Wash.) Herald*

It was a moment of potentially dangerous convergence.

My editors looked at their story budget and saw a hole on the front page a few days hence. At that moment, I didn't have anything pressing on my schedule.

### Tag. I was it.

The assignment — find out how an unusual winter drought had affected this normally soggy place — could have been just another weather yarn. Instead, some quick data analysis using geographic information system (GIS) software highlighted a developing hazard that had been taking shape for years in the forestland outside area cities and towns.

The *Herald* serves a community of more than 630,000 people in rapidly growing Snohomish County. The county, roughly a half-hour drive north of Seattle, is about the size of Connecticut. Most of the population is concentrated not far from the tideland shores of Puget Sound. To the east are rugged foothills, evergreen forests and thousands of acres of Cascade Mountain Range wilderness, including a slumbering volcano.

Lots of rain and snow usually keep this place green. Not this year. The driest winter in 110 years led the governor to declare a drought emergency. Officials forecast what could be the worst wildfire season in years.

If the fires got going, where would they likely appear, and who would be at greatest risk?

Using mostly free data arrayed in a GIS, we were able to report that 5,500 people in our county appear to be living in the areas most at risk for wildfires. We found planners have been approving about 100 new homes in those fire-prone areas each year, many outside fire-protection districts.

My partner on the story, Diana Hefley, knew the state Department of Natural Resources had identified portions of the county as particularly at risk for wildfires. The determinations were based on a number of factors: fire history, presence of brushy fuel, terrain, ease of access, a low level of organized fire protection.

A quick check showed the department had created mapping shapefiles of these fire zones and had posted them on the Web. The state also had 30 years' of wildfire incidents, their locations mapped using X,Y coordinates.

After consulting the metadata for these records, we opened the files in ESRI ArcView 9. It is at moments like this that I love Washington's strong public records laws. In addition to the free data on wildfire threats, past and future, my GIS data cache already contained shapefiles of property parcel lines, a decade of building and construction permits already geocoded into points for use in another project, fire district and city boundaries, major roads and rivers, population estimates at the Census block level, plus a fat database containing property tax assessment records.

After making sure all the GIS data was in the same projection, I set ArcView to the task of clipping information that would form the core of our analysis.

Clipping has become one of my most-used GIS tools. The process is simple. First, decide what data you want to clip, and place that into an ArcView map. Next, overlay the shapefile that describes the area you want to use as a cookie cutter to punch out the relevant records. If you have your GIS ducks in a row, clipping works equally well to extract a section of points (say wildfire locations, or building permits) or to snip out relevant polygons, such as census blocks, or property parcels.

We clipped data using the state's shapefiles of fire hazard zones. ArcView automatically creates a new shapefile of the data it clips, complete with its own underlying database table in dBASE format.

ArcView has SQL query capability, but I still like to export data tables to Microsoft Access database manager for analysis. In short order, I knew how many people lived in the fire zones (by analyzing clipped Census block data), how many new homes on average had received construction permits each year (by analyzing clipped building permits) and the parcel numbers of each piece of property within the hazard areas.

Parcel numbers are the key to making joins to property data. Using Access, I joined the data table of clipped parcels to property assessment records. Because assessors record the year of construction for each home they record, I was able to track the development history in the clipped area, year by year.

It was then time to help the data start talking.

After tabulating the home construction data, I dropped the results into a Microsoft Excel spreadsheet and prepared a chart. The resulting trend line, and some quick math, showed that more than three-fourths of the homes in the fire-prone areas had been built

*continued on page 22*
