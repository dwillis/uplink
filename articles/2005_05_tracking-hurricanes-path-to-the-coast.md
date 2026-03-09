# Tracking hurricanes' path to the coast

By Matthew Waite, *St. Petersburg Times*

When a hurricane barrels over water toward the coast, everyone wants to know one thing: Where is it heading? Everyone will talk about it, your family, your neighbors, your editors, your coworkers, shoppers in line at the grocery store. Where will that storm hit?

Every six hours, the National Hurricane Center uses its computer models to predict a hurricane's path and publishes the latitude and longitude coordinates for the projected track. That's good news for journalists who use geographic information system (GIS) programs to map data.

If you've used a GIS before, you've probably plotted x/y coordinates, usually latitude and longitude. It's not difficult to do, but doing it repetitively, every six hours, would be tedious. Fortunately, with ESRI's ArcView 8 to 9, you can automate the task with little effort and create updated maps for reporters and editors.

The place to start is the National Hurricane Center's Web site at *www.nhc.noaa.gov*. The storms are listed by name, with links to the Public Advisory, Forecast/Advisory, Discussion, Probabilities, Maps and Charts and Archives. If you've never been to the site, each link is worth reading. For mapping purposes, go to Discussion, where the forecast points are kept, usually toward the end.

## Building the foundation

Copy the forecast points and paste them into a new Microsoft Excel worksheet. You'll have to use to Data\Text to Columns . . . function in the menu to parse the data into individual columns. Name the columns, using lat for latitude and long for longitude so ArcView can use these later.

Now we will get the latitude and longitude in a format that ArcView can recognize. Use the search and replace tool in Excel to delete all the Ns in the lat column and then do the same to delete the Ws in the lon column. The lon needs to be represented as a negative number, so create a new column and multiply the cells in the lon column by negative 1. (Longitudes in the Western hemisphere are negative numbers). Copy the contents of the new column and choose Paste special\Values to put the values in the original lon column.

With properly formatted longitude and latitude points, you could go ahead and map these points. But let's add some more data.

Insert a column at the beginning called forecast_age. Here we're going to add data that will tell our GIS which points to display. For your newest forecast, fill in the cells in forecast_age with something that says this is what I want – I use "current" and then call the older points "old." The use for this will come later.

Next to that column, add another and call it forecast. Here, manually fill in which forecast it comes from (i.e. Friday 5 a.m. or Saturday 11 p.m.). That will help you if you want to look at the evolution of the forecast track.

Then add a column called forecast_step. Fill that in, starting with 1 and ending with 8. If you want to connect the dots later using automated means, this step will save you time in having to edit the file.

Last, and this is optional, convert the forecast wind speeds from knots in the last column to miles per hour. To do that, use search and replace to delete the KTs and multiply knots by 1.15077945 in the next column.

With each new forecast, just open the spreadsheet, paste the new information in, copy the formulas down and save it. I usually use storm names for my spreadsheet names.

## Tracking maps

Now it gets much easier.

Open Microsoft Access. Create a new Access database and import your spreadsheet. Close the database.

Open ArcMap. For hurricane tracking base maps, I've found that Census TIGER maps work just as well as anything. I have statewide county boundary maps, statewide place maps, statewide major roads (interstates and freeways) and statewide water polygons in a map.

With those layers up, go to Tools/Add XY Data in the menu. Under "Choose a table from the map or browse for another table," browse to your Access database file and find your table inside it. (The newest generations of ArcView, from versions 8.x on, directly read Access data). Make sure that ArcMap recognized your latitude and longitude fields in the box that opens. Click OK and hurricane track points should appear on the map.

If this is the first time you're mapping points, you'll only have one track on the map. If this is the fourth or fifth forecast you're mapping, you'll see more sets of points on the map. We can show just the current forecast track using the forecast_age field.

Double-click on your hurricane layer name in the ArcMap table of contents. Then select the Definition Query table and enter forecast_age = "Current" to limit the displayed data to the current points.

## Repeat as needed

When you get a new forecast, all you have to do is update your database. Copy the points into Excel, repeat the steps and be sure to change the forecast_age column to reflect the new forecast as the current one, then import it into Access and ArcMap will update the points without you having to do a thing.

If you do this consistently – putting each forecast into your database – by the end of the storm you can query all of the forecast positions that start with Initial. Those are the exact point of the storm every six hours. With those points, you have the general path of the storm. One weakness is that hurricanes don't move in straight lines, which is what your map will show. They wobble, angle and turn slowly. So remember that the path you can create from initial forecast points is relative.

If you'd like to turn your points into a line, there are few options available. The best is an extension called XTools Pro (See *www.xtoolspro.com*). XTools costs $129 for a single-use license, but is worth the money because of the number of tools in it. One of the tools converts points to a polyline file. With three clicks, you can turn your hurricane points into a hurricane path.

Since Hurricane Jeanne, I mapped the predicted track of the storms that followed, and created maps that helped editors decide where to send reporters.

Mapping forecast points won't result in a story itself, but it will help guide dozens of them. And it only takes a few minutes to pull off, after you get used to the steps.

Contact Matthew Waite by e-mail at mwaite@sptimes.com.

---

## Additional resources

Additional resources for journalists looking for hurricane and tropical storm information are available on the Web.

The University of Central Florida offers an interactive mapping application at *http://hurricane.methaz.org* that allows users to plot the results of different hurricane forecast models on one map. This allows journalists to get an idea about the uncertainty of the storm track.

The tropical weather tracking page from the U.S. Navy (*www.nlmoc.navy.mil/cgi-bin/main.pl?tropical*) contains downloadable shapefiles of forecast tracks that can be used in a GIS program and basic wind models.
