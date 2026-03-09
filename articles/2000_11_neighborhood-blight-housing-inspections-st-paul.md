# Neighborhood Blight

**By Janet Roberts**
*St. Paul Pioneer Press*

Anyone who's spent time answering the newsroom phone has heard from them — the people who live next door to the house with the falling-down garage or the giant trash pile or the rodent den.

One at a time, the sad tales don't amount to much — maybe a news feature on a slow day. But start digging around in your city's housing inspections data, then plot what you find on a map, and the story gets better.

We all know which neighborhoods in our city suffer from blight. All you have to do is drive down those streets and look for the boarded up windows, overgrown yards and peeling paint. But what is the scope of that blight? That's where mapping software, such as ArcView, can help tell the story in an eye-opening way.

At the *St. Paul Pioneer Press*, one of our city hall reporters, Charles Laszewski, wanted to investigate complaints that the housing inspections chief wasn't tough enough on owners of run-down properties. So we asked for the city's housing inspections database.

We wanted to find out if the critics were right: Were inspectors too lax? We found the story was more complicated. Among our findings: Inspectors were responding promptly to complaints and following up on them. But the system does a lousy job policing repeat offenders. And the Twin Cities has lots of chronic problem properties.

We defined a problem property as one with repeated violations spanning two years or more. Then we turned to our mapping software. We wanted to plot the properties on a map so we could see how bad the problem was in specific neighborhoods.

Our inspections data listed the street address for every property inspectors visited. We winnowed the list to just the chronic offenders. Then we asked ArcView to geocode the addresses — in other words, plot them on a map of St. Paul.

That didn't produce a very useful map. There were so many problem properties in some neighborhoods that we ended up with a giant blob of red points.

So we set out to produce a better map: one that would show the rate of problem properties in each neighborhood, shaded from best to worst. We had an ArcView map that showed all the census tracts for St. Paul. For each census tract, we had the number of housing units. We wanted a map showing the rate of problem properties per 1,000 housing units.

But we had a problem: our inspections data didn't list the census tract for each property. How would we count the number of problem properties in each tract?

We did it by asking ArcView to do a "spatial join." It's like joining data tables in Access or FoxPro, except the join is on geographic attributes instead of on matching data fields. The result was a data table that listed the census tract for each problem property. From there, we ran some counts in FoxPro, and then we were able to ask ArcView to shade the census tracts to show the extent of blight in each.

The result: In one St. Paul neighborhood, one of every three houses has chronic housing code violations. Others weren't much better.

The series brought about some results: The City Council added money to the budget to hire more housing inspectors. The mayor announced a police sweep to arrest property owners with outstanding housing court warrants. And the county is spending more money to maintain tax-forfeited properties.

*The St. Paul Pioneer Press story, "A Blight on the Cities," is available in the IRE Resource Center story #15948. Also available online at www.pioneerplanet.wm/archive/problemproperties/*

Janet Roberts can be reached by e-mail at jroberts@pioneerpress.com.
