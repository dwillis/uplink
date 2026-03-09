# Finding a snow job after storm

By Janet Roberts
*St. Paul Pioneer Press*

## MAPPING IT OUT
*The latest uses of mapping in news reporting.*

Our story began when a reporter's friend woke up one winter morning to find her car had been towed. She'd come face to face with St. Paul's confusing snow-emergency rules, which govern on-street parking after a significant snowfall.

Over lunch that day, the reporter and his colleagues wondered whether the rules are applied fairly. Are some neighborhoods towed more heavily than others?

With a few computer-assisted investigations under his belt, reporter Chuck Laszewski knew he could answer that question. ESRI ArcView 3.2 geographic information system (GIS) software — and a powerful extension called Spatial Analyst — would make it possible. All Laszewski needed was the right data.

Confusion aside, the snow-emergency rules make sense: Plows can't get the snow off the streets if parked cars are in the way. If streets aren't plowed clean, neighbors cope with a mess of frozen slop that can last all winter long.

But the rules cause a lot of consternation for newcomers — and even long-time residents who pay them too little mind.

Laszewski set out to get ticketing and towing data.

It would be the following winter before we sat down at our computer and began mapping. To make a long story short, it took more than six months — and the intervention of our lawyer — to wrest towing records from the St. Paul Police Department. The ticket records proved to be an even bigger hurdle, so Laszewski spent about three weeks' time, spread over five months, typing in ticket addresses for one snow emergency — about 1,200 in all.

Now we were ready to fire up ArcView, right? Not so fast.

Imagine it's just snowed more than 3 inches. A bunch of tow-truck drivers go to work. It's cold. It's wet. It might even be dark. The drivers get out of their trucks, hitch the car to their rigs and — oh, yeah — scribble down the address. Then it becomes the job of a clerk at the Public Works Department to decipher that scrawl and type the address into the database.

You can imagine how clean the address field was. We had gems such as "CAR X HUH?" Other records contained street names but no house numbers. The "good" addresses were listed this way: "Sherburne/1033." I used Microsoft SQL Server and VB Script to parse the address field and format it in a way ArcView would recognize.

My first pass at geocoding the records — asking ArcView to plot the tow locations on a street map — yielded a disappointing success rate, so it was back to address cleaning. Fewer than two-thirds of the addresses plotted, so I spent the better part of a week examining the records that failed to geocode and correcting misspellings. Ultimately, we had an 88 percent success rate — lower than I like, but the best we could do for this project.

### Concentration of tows

Finally, we could begin our analysis. Immediately, we noticed the tows appeared to concentrate north of Grand Avenue, a commercial thoroughfare that roughly divides the city in half from east to west. Indeed, a quick count in ArcView and a few calculations in Microsoft Excel showed 78 percent of the tows were north of Grand. We had a story.

The Grand Avenue observation would become part of our nut graf: "It's almost as if the towing companies and city officials stood on Grand Avenue and drew a line in the snow. To the south, considerably fewer cars get hauled away."

Next, we overlaid a map of the neighborhood boundaries and did a spatial join to assign each towing record to its neighborhood. Exporting the data back to SQL Server, I summed the records by neighborhood. Clearly, towing was heavier in some neighborhoods. But we wondered if that was because more scofflaws parked in those neighborhoods. Enter our ticketing data.

In ArcView, I geocoded the ticketing data Laszewski had gathered. Here, there was no "line in the snow." Ticketing was dispersed fairly evenly across the city. Again, I summed by neighborhood. With those totals in hand, I was able to compute each neighborhood's tow rate: the number of tows as a percentage of tickets issued.

We found wild variation: The neighborhoods with the most tickets had some of the lowest tow rates. Neighborhoods with far fewer tickets had high tow rates.

### Fine-tuning with extension

Our story was getting better. But we wanted to make more sense of our data. In particular, we wondered where the densest concentrations of tows were. Common sense told us they probably were in areas closest to the impound lot, where towed cars are taken. We knew — because we used ArcView to draw one-mile buffers around the impound lot and counted the tows in each circle — that 68 percent happened within four miles of the impound lot.

It was difficult, however, to see concentrations in the geocoded points. Because we mapped so many tows, they all blended together into a blob of largely undecipherable color.

Enter Spatial Analyst, an ArcView extension that can do density analysis. We didn't have the software, and at $2,500, it's not cheap. So we sought help from a college mapping instructor. We brought our data to her lab, and she showed us how to use Spatial Analyst to draw our hot spots. The result was eye opening.

We drew separate hot-spot maps for the ticketing and the towing data. The density patterns did not correspond. In particular, a definite concentration of ticketing on the city's West Side lacked any corresponding concentration in the towing map.

Where did the towing hot spots concentrate? Around the impound lot.

Now, not only did we have a story, we had a great publishable map and good reason to buy the Spatial Analyst software.

With time to play with our own software we tested several more theories: that towing patterns would correspond with density of population, rental housing, retail development and immigrant populations (language barriers make it hard for immigrants to understand the complicated parking rules).

All of these theories had some truth. But they didn't explain why the city wasn't towing on the densely populated West Side, an area with many Hispanic immigrants, dense clusters of rental housing and a high ticketing rate.

This is where Laszewski's shoe-leather reporting was invaluable. Tow-truck operators told him they are loath to cross the Mississippi River to tow on the West Side because it is a long round-trip to the impound lot. The city's towing contracts offer incentives to operators the more cars they tow. Towing operators said they focus their efforts north of Grand Avenue because that strategy yields the most cars.

The city's public works director, who coincidentally lives in the seldom-towed West Side neighborhood, said he would review city policies in light of our story. Across the river in Minneapolis, city officials were so enchanted with our analysis, they did a similar one of their own, finding the same disparate patterns.

Read the story online at *www.twincities.com/mld/pioneerpress/4658246.htm*.

Contact Janet Roberts by e-mail at jroberts@pioneerpress.com.

*Would you be willing to share a mapping example with fellow journalists? Send an electronic copy of the map along with details to David Herzog at dherzog@nicar.org*
