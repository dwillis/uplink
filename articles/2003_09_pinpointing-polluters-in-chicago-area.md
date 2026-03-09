# Pinpointing polluters in Chicago area

By Jeff Porter, *IRE and NICAR*

Environmental reporting is a natural – pun intended – for journalists looking to use their analytic mapping skills and find information for news stories.

Environmental data that can be mapped from state and federal agencies is often a simple download away on the Internet. For example, go to the U.S. Environmental Protection Agency Web site at *www.epa.gov* and search for the phrase "underground storage tank." You'll get a list of state agencies that manage data about leaking tanks and, often, links to that data.

The environmental agencies often include the locations, reported in latitude and longitude, of regulated entities. For example, the Toxics Release Inventory data (*www.epa.gov/tri*) from the EPA includes the latitude and longitude. A journalist using a geographic information system can create a pin map based on those coordinates and, going further, use density mapping tools to show high concentrations.

The Toxics Release Inventory and other environmental datasets include even more geographic information that can be mapped: counties, cities and ZIP codes. While ZIP code areas may or may not have precise boundaries, most people know their own Zip codes.

The IRE and NICAR Database Library recently used those geographic elements when it assisted WMAQ-Chicago in pinpointing contaminated sites targeted for cleanup by the Illinois Environmental Protection Agency. The data included hazardous waste sites and leaking underground storage tanks. The Database Library used ArcView 3.3 and the Spatial Analyst extension to conduct the analysis.

The data, obtained by station producer Michele Youngerman, came from the Illinois EPA in dBASE files, easily opened in ArcView after we cleaned up the data using Visual Fox Pro to convert nine-digit ZIP codes to five-digit codes and convert the coordinates from text to number.

(A note of caution about latitudes and longitudes: Make sure you have them reported properly. ArcView 3.x requires decimal degrees. Occasionally the coordinates are reported in degrees, minutes and seconds and will have to be converted.)

After we cleaned up the data, our analysis took several steps.

1. We created a point map using the numeric latitude and longitude coordinates via the View\Add Event Theme menu command.

2. The first map was too laden with dots; we wanted to restrict our results. So we used the definition query tool to include only larger polluters.

3. With some advice from GIS expert Matthew Waite of the *St. Petersburg Times*, we used the Spatial Analyst extension to identify "hot spots" of regulated sites. The resulting density maps weren't pretty, but they helped us focus on specific areas and confirmed some suspicions for the station.

4. We limited the maps to the specific ZIP codes provided by WMAQ that define its viewing area by using definition queries. Then we used ArcView's Geoprocessing wizard extension to clip base map layers – roads, cities and rivers – for just the viewing area.

5. Using the clipped data, we summarized the number of regulated sites by ZIP code and mapped the results.

The resulting maps highlighted areas where large polluters — generating, hauling or managing hazardous materials – are also close to residential areas. The television station reported about thousands of contaminated sites near homes and playgrounds, although homeowners often don't know about the contamination. The analysis also helped give perspective for the story of three families facing serious illness. All three families believe the illnesses were caused by companies releasing toxic waste.

The stories can be found at: *www.nbc5.com/nbc5/2203768/detail.html*

Contact Jeff Porter by e-mail at jeff@ire.org.

---

*Would you be willing to share a mapping example with fellow journalists? Send an electronic copy of the map along with details to David Herzog at dherzog@nicar.org*
