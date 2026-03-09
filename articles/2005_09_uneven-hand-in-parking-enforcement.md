# Parking: Uneven hand in enforcement

By Patrick Lakamp, *The Buffalo News*

Our idea to map Buffalo's parking tickets originated in a coffee shop where employees shout warnings to customers when they spot a parking enforcement officer. The ritual can render them practically hoarse.

Having coffee with a source for an unrelated story, we heard four warnings in an hour. Meanwhile, the source complained about her eight tickets in two years and $300 in fines.

After that meeting, staff reporter Jay Rey and I — under the supervision of Susan Schulman, head of *The News'* investigative reporting team — decided to study the hundreds of thousands of parking tickets issued in the city using computer-assisted reporting. (For more details about reporting the story, see the September-October issue of *The IRE Journal*.)

We filed a state Freedom of Information Law request for an electronic database of all tickets written January 2003 through October 2004. The city provided, at no cost, a Microsoft Access database on CD containing 366,500 parking tickets.

We ran hundreds of queries in Access and analyzed the data using ESRI ArcView 3.2 geographic information system (GIS) software. News researcher Andrew Bailey helped with the data work.

The data was fairly clean. Parking officers issue tickets by using a hand-held device capable of scanning a vehicle registration sticker and automatically recording the time and date. The officers enter the location and violation type.

We found inconsistencies in the recorded street addresses. Some officers, for example, entered "Bailey Ave." while others entered "Bailey Avenue." We needed consistency with addresses, because we planned to use ArcView's geocoding function to turn those addresses into points on a map. We wanted one map showing the tickets by neighborhood.

Bailey created a new table from a GroupBy and Count query of street name to identify streets with the most parking tickets.

### Mapping patterns

Bailey had a good handle on the geocoder's preference for how street names should be identified (Northrup West, rather than W. Northrup), so that's how he standardized street names.

Sometimes he used Access' Find and Replace function to standardize addresses, but more often he relied on update queries. When Bailey standardizes addresses, he usually creates a table that has one column containing the variations of the street name and then creates a column that contains the correct, standardized, street name. He then uses this table in the update query.

Bailey geocoded the cleaned-up addresses and we ended up with 290,000 matches out of our original 366,500 records. Complete success is elusive when geocoding. Some ticket addresses couldn't be mapped because officers sometimes failed to record the street number in the violation location field.

We could overcome that for violations on short streets contained in one neighborhood, but not for those on streets that cut through several neighborhoods. Ashton Place, for example, is a one-block street in Buffalo's South Park neighborhood. Tickets written on Ashton Place, but lacking a precise address, could therefore be attributed to South Park.

Bailey calculated the number of tickets for each neighborhood by using ArcView's spatial join. Spatial joins allow you to assign information from one map layer to another. Bailey overlayed the polygon neighborhoods map from City Hall and joined it to a map layer of parking ticket points. Then, after the join, he calculated the number of tickets in each neighborhood. That number was then displayed for each neighborhood as the percentage of all tickets mapped.

We could see downtown had the greatest percentage of all parking tickets. But several Upper West Side neighborhoods, each having 5 percent to 10 percent of the tickets, stood out, too. This indicated the Upper West Side was the most ticketed residential area of the city.

### Zooming in

Another map created using ArcView showed the Upper West Side close up. Here, Bailey took the county property parcel map and zeroed in on the residential neighborhood. He grouped individual parcel polygons into street blocks — grouping roughly 3,500 parcels into the roughly 160 blocks in our area and assigning a name for each block. Bailey did this by manually selecting the polygon parcels and then using the Dissolve Feature tool in the Geoprocessing Extension

*continued on page 21*
