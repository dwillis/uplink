# Showing deadly crashes

By Garry Lenton
*The (Harrisburg, Pa.) Patriot-News*

Pennsylvania isn't called the Keystone State for nothing. It's hard to reach any location in the northeastern United States without crossing the state.

And nowhere is this phenomenon more apparent than in the state's capital city, Harrisburg. This town is like the hub of a wheel, criss-crossed by three major highways, and railroads heading off in all directions.

This fact is not lost on the trucking and warehousing industry, which has become one of the largest employers in the region. Truckers can reach every major market in the eastern United States within 10 hours. But, along with the high-paying jobs that the industry brought, is an unwelcome consequence: fatal crashes with 80,000-pound trucks at almost three times the national average.

My editors wanted to get a handle on how our region compared to others when it came to fatal crashes with large trucks. So we turned to the U.S. Department of Transportation's Fatality Analysis Reporting System (FARS) database – purchased from the IRE and NICAR Database Library – for help.

### Finding death counts

It took a while to get familiar with the tables, but Database Library staffers and the DOT helped us sift out the data we needed – the number of accidents involving tractor-trailer trucks that occurred in our region, and the death count.

But the FARS data could only take us so far. Our editors were impressed, but not really sure what they were looking at. Frankly, I wasn't so sure myself. We needed to focus the story on something readers could understand. That's when George Ginter, the assistant city editor overseeing the project, chipped in: What's the most dangerous highway we have? The answer was easy: Interstate 81. The question then became, just how dangerous is it? And how do we communicate that to readers?

The answer to the second question turned out to be a map.

But before we could turn to ESRI ArcView 3.2, our geographic information system software (GIS), we had to go back to the FARS data.

We aggregated the data in Microsoft Access to get a table that I could map. That took grouping the deaths along I-81 by the county of the accident. The result was the hook for the story.

From 1997-2001 no county along the 855-mile highway had more deaths from accidents with tractor-trailers than Cumberland County, which is the heart of our circulation area.

In our area, 40 percent of all people killed in crashes with a truck died on I-81. In the process of investigating the story we also found that the proportion of trucks on the highway was approaching 43 percent in some regions. That meant that the slightest error in judgment by a driver could result in a fatal accident with a truck.

Motorists who used the highway told us that they hated it. Too congested, too many trucks. But they also told us something else: It was the passenger-car drivers they most often saw driving erratically, not the truckers. The data verified that and we interviewed the authors of studies showing that car drivers accounted for the 80 percent of all crashes between trucks and cars.

### Maps verify problems

The map helped us to bring that message home to readers most directly.

The first step in the GIS analysis was to chart I-81's 855-mile course from the New York-Canada line into Tennessee.

I used only three layers to build the map: roads, counties, and state boundaries – all files that came with ArcView.

First, I mapped all the U.S. counties. This was overkill, but I later pared this down to just the counties that I-81 passes through.

Next I added the roads shapefile. This turned the map nearly black with a web of lines representing everything from the simplest two-lane highway up to the interstates. Using the theme properties options, I filtered out everything but I-81.

I learned that it helps to spend some time scrutinizing the road layer's data table first to see how the highway is identified in each state.

### Inconsistent names

Sometimes local authorities rename portions of highways, rendering the Name field useless as a filter. I tried filtering by Name and got just a dotted line for my trouble.

But I-81 was named consistently in the Sign1 and Sign2 fields of the table. So I used this syntax to get the entire highway:

```
([sign1]="I81") or
([Sign2]="I81")
```

Now I had a single red line stretching across a mosaic of multi-colored counties. But what we wanted was a map of the highway and just the counties it passed through.

I identified those counties by using the Theme\Select by Theme menu item. I activated the roads layer and then used Select by Theme to have ArcView highlight each county feature that I-81 intersected.

Then I opened the table for the county layer and hit the promote button on the tool bar. This moved all of the selected features to the top of the table.

Now it was time to create a layer of the selected counties. I closed the data table and selected Theme\Convert to Shapefile from the menu and added the new file to my view.

Then I added the deaths data table to my project, joined it to the counties map and, using the legend editor, shaded each county along I-81 by its death count.

For reference, I added the state shapefile and, in the theme properties, selected the six states that I-81 passes through.

I exported the map to a PostScript file and e-mailed it to the newspaper's graphics editor. The end product was a centerpiece map graphic for the story, which attracted a lot of positive attention from readers.

Contact Garry Lenton by e-mail at glenton@patriot-news.com

*Would you be willing to share a mapping example with fellow journalists? Send an electronic copy of the map along with details to David Herzog at dherzog@nicar.org*
