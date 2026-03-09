# Blocking out unsolved murders

By Doug Smith, *Los Angeles Times*

Sometimes a database story starts with an idea. Other times it arises from the data itself. In this case, it was both.

Every once in a while, a reporter walks up to my desk with a diskette or a CD-ROM in hand and asks forlornly, "Can you open this?"

I always try to stop what I'm doing and take a look at their data, knowing that the question really means, "Can you find out if there is anything worthwhile on this disk and tell me what it is?"

Most of the time I give a few tips on using Microsoft Excel, and the reporter goes away with one or two nuggets to put into a story that was largely reported by traditional means. But the result was quite different when reporter Jill Leovy, who was covering homicide, showed up at my desk with a CD. Leovy had a specific question. She wanted to know whether the data on the CD would help resolve her suspicion that the Los Angeles Police Department was deploying too few detectives in South Los Angeles where homicides were most prevalent.

Besides hanging out with detectives and spending nights and weekends with the families of homicide victims, Leovy also had built a back-channel connection in the LAPD's Information Technology Division. Through it she had acquired a database of every homicide investigated by the LAPD since 1988. Even though this was public information, my experience with the LAPD was enough to tell me this was a real find. If I had asked for it six months ago, I'd still be waiting for an interview to talk about what format it should come in.

I quickly looked through the table and had to inform Leovy that it wouldn't answer her question. It would be easy to break down homicides geographically, but there was no information on the detectives' identities. We couldn't calculate caseloads.

Leovy looked disappointed and went away. Then I started getting handwritten notes on my desk. Each one had the name of a police division, a list of years and a number for each year. She was going to each of the 18 police divisions to look through old detective rosters. I started keypunching.

When she was done, I did a simple calculation that showed the caseload for every division for every year. It was obvious that detectives working South Los Angeles had consistently been burdened with more cases than those in the Westside or Valley. This provided the statistical support for Leovy's account of hardworking detectives inundated with cases they seldom could solve.

All the while, I was doing my own analysis of the data. The division breakdown showed that homicides were far more frequent in South Los Angeles, but that wasn't news. In 1995, Dick O'Reilly, the then-*Times* director of computer-assisted reporting, did an exhaustive analysis of homicide in Los Angeles County. He established the prevalence of homicides in South Los Angeles and the fact that only about half of homicides are solved. Leovy and I had data covering twice the period in O'Reilly's study, but we had to ask ourselves what was new.

Our concept began to focus on Leovy's experience that the perception and fear of violence are always present in some neighborhoods. I did a little math in my head and realized that with a 50 percent clearance rate, there would be a lot of killers who were never brought to justice roaming the streets of South Los Angeles. We shifted our focus to unsolved homicides, and I turned to mapping to find patterns.

Using ESRI ArcView 8.2, I geocoded the homicides and made a subset of the unsolved ones. Geocoding is one of the most useful tools – it turns street addresses in data tables into point maps. I use it to analyze geographic data for patterns, to present story ideas to editors and to prepare graphics for publication. It doesn't take long to do a first pass that will match 80 percent or more of the addresses in a data table. That's enough to show me whether there is anything worth pursuing.

The first pass yielded startling results. By laying the dots over a street map, I saw that a large area had one or more unsolved homicides on almost every block.

My next step was to produce theme maps to show unsolved homicides as a ratio of population and area of Census tracts. To do this, I had to use ArcView's spatial join function, so I could assign data from one layer to another. These made strong presentation tools when Leovy and I pitched the project to our senior editors. We got the go-ahead to build a graphic and to pursue the story.

Now that I was working toward publication, it was important to get the highest match rate possible in the geocoding. That meant spending a couple of days using ArcView's interactive geocoding feature to manually match about 2,000 unmatched addresses. In the end, I got about 95 percent of the total.

I also reconsidered the measurements for our story. Not only was I comparing a 12-year accumulation of unsolved killings against the current population, I realized there was little visual or visceral impact in showing homicides as a rate per 10,000 people or per square mile.

It finally hit me that the ideal base was the city block. By shading individual blocks with the number of unsolved homicides that occurred on them, I produced the dramatic pattern that was ultimately published. It was easy to see that a person walking in many parts of South Los Angeles couldn't avoid the scenes of one unsolved homicide after another. No rate was necessary because everyone knows what a block is.

So I switched to using a Census block map and did a spatial join with the homicide points. This added a new field to the block map table with the number of homicides within each block, which I used to create a theme map.

To emphasize the difference between the Valley and South Los Angeles, I gave graphics artist Rebecca Perry blowups of two parts of the city with the individual homicides showing. One had almost no dots while the other had a dense pattern.

I also added an elementary school shapefile and made a table showing the number of unsolved homicides within a quarter mile of each elementary school in the blowups.

The scale was too large to accommodate a complete street grid, which would have delineated the individual blocks. The pattern worked well enough without them except for a few very large blocks in the mountains that run around and through Los Angeles. Some of these are so large they made a single homicide look like a crime wave. We made an executive decision to leave out blocks that are greater than a quarter square mile. We noted this omission in the graphic text.

Once the graphic was done, I went to work on the Web presentation. I wanted readers to be able to see the unsolved homicides in their own neighborhoods. After some experimentation, I broke Los Angeles into map areas to get a small enough scale to show individual dots. Over a couple of days, I made 25 Adobe Acrobat Portable Document Files with the street grid showing lightly in the background. The Web staff turned this into an interactive display that allowed users to click on a master grid of the city and open one of the 25 detailed maps.

There's no way to gauge the impact of these two stories. They generated significant reader response but did not prompt any overt policy change by the LAPD. In fact, the new police chief William Bratton quickly observed on his own that violent crime in South Los Angeles was not getting the attention it deserved. Even before our stories were published, he started tinkering with deployments to beef up the detective strength in overworked bureaus, which meant taking resources away from the San Fernando Valley. This is the kind of reallocation that in the past would have resulted in an outcry from Valley constituents and possibly would have cost the chief his job.

Contact Doug Smith by e-mail at doug.smith@latimes.com
