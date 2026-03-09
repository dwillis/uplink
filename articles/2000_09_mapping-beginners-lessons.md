# A beginner's lessons

**By Jeff Thomas**
*Colorado Springs Gazette*

The first moral of this story is: New CAR tools don't always make life easier. They can help you tell a smarter story – as our first attempt at using mapping software did for us in one case – but you're still likely to break a sweat getting up the learning curve.

Shortly after I returned from NICAR's three-day mapping seminar in Columbia, Mo., last October, voters in our largest school district rejected a bond issue. Three years earlier, they had approved an even larger bond. Naturally, we asked: Why the turnaround? Finding the neighborhoods where the drop was most dramatic would steer us to the kind of people we needed to talk to. Mapping software could help us do this. It also could help us see if the swing precincts had older or younger people, more or fewer kids, higher or lower income, etc.

We had used spreadsheets in the past to unearth voting trends in the precincts, but the chore usually wasn't complete until we had broken out the colored pencils and a large precinct map. Mapping software gave us the ability to automate the colored-pencil part, giving us much more lead time to report the story. It also would show us the underlying demographics of the precincts where the vote swing was most pronounced.

### Getting started

I dusted off a copy of ESRI's ArcExplorer CD, which I had picked up at NICAR's Boston conference several months earlier. This is a stripped-down version of ArcView, the standard in most GIS-equipped newsrooms. As I found out, it did the job, barely. For example, ArcExplorer lacks the extensions necessary to export a map in a format the art department can work with. Publishing a map would have been nice, but more-informed reporting was our first goal, and the tight turnaround on the story precluded building a map from scratch on the Macs, so we went without the map.

We poured the precincts' "yes" and "no" votes on the bond issue into two columns of a spreadsheet, and poured the votes from the 1996 election into two other columns. For each precinct in each year, we calculated a support ratio (yes votes/no votes). Then, for each precinct, we calculated the percentage change in the ratio from 1996 to 1999. Precincts with the most-negative change numbers were those where support had dropped most dramatically. We added a column indicating voter turnout in each precinct. This took just a few minutes.

The bigger job was to assemble the needed digitized maps, which ESRI calls shapefiles: voting precincts (to plot the change in voting behavior), Census tracts (to plot demographics), and streets (to help the eye navigate the map).

I asked the county's GIS department for a digital map of precinct boundaries. No problem, they said: That will be $500. The GIS manager, however, was on my side and sneaked me onto the next day's county commission agenda, where I made my plea for a fee waiver, which was granted. I left the meeting with the CD.

I downloaded a street shapefile from the Census Bureau's TIGER service (*http://tiger.census.gov*). A Census tract shapefile was downloaded from CEISIN (*http://sedac.ciesin.org*).

Files in hand, I opened ArcExplorer, launched a new project, and used the "add theme" function to bring the three files in. The first beads of sweat began to form when I tried to view all three themes at once. When viewing the street and Census-tract themes, I could not add the precinct theme. Or, when viewing the precinct theme, I could not add streets and tracts to the view.

### Glitches

Which brings me to the second moral of the story: Always check the projections of your digitized maps. After wailing to the NICAR listserv, I was instructed to check the metadata of each map to make sure the projections matched. Sure enough, the precinct map was in a different projection than the street and tract maps. This is a potential pitfall that Andy Lehren spent a fair amount of time hammering into our heads at the NICAR seminar, but I guess it took a real-life example to drive the point home.

In any case, ArcView can convert projections, but ArcExplorer cannot (and won't let you add the necessary conversion extensions), so the county converted the precinct map projection and shipped me the new shapefile. All three themes now could be seen at once: precinct boundaries, census tracts, and beneath them both, streets.

The next step was to pour the demographic into the Census-tract map. This required joining a table of demographics to the table underlying the tract shapefile in ArcExplorer. I bummed a MapInfo CD of 1996 Census-tract demographics from our marketing department and moved the selected records to an Excel sheet. To make the join, I had to modify the short tract ID numbers (e.g., 2.01) in Excel to match the longer ID contained in ArcExplorer tract shapefile (e.g., 080410002.01).

I saved the table as a .dbf file, closed it and used the "add table" function in ArcExplorer to open it. More problems. For reasons still unknown, the lengthened tract ID numbers on the Excel sheet did not survive the transition to a table within ArcExplorer. Again I ran to the NICAR list, where I was advised to move the Excel data to Access, export the table from Access as a .dbf file, then pick up the table with ArcExplorer. This worked. I used the same routine to move the precinct voting numbers into ArcExplorer.

In ArcExplorer, I joined the voting-numbers table to the table underlying the precinct shapefile, and the demographic table to the table underlying the Census-tract shapefile. This was the point where ArcExplorer could start doing its job.

### Results

Now that the demographic numbers were a part of each census tract's record in the shapefile, we could identify the tracts with the greatest concentration of, say, school-age kids. The ones with the highest concentrations were indicated by, say, vertical lines.

And now that the vote-swing numbers were part of each precinct's record in the shapefile, the precincts with the biggest swings against the bond issue could be indicated with a color. Precincts where the swing was less dramatic appeared in successively lighter shades of the color. This is quick, point-and-click stuff.

Looking at both themes – demographics (lines) on top of vote swing by precinct (color) – we were able to produce this story nut: "A Gazette computer-assisted analysis shows that [the] steep drop in support was spread across the district. Perhaps surprisingly, the reversal was evident in precincts on the northeast and northwest sides, where simple demographics would seem to indicate strong support for schools. Those neighborhoods are filled with young families. Median household income is higher – by several thousand dollars – than it is countywide. Voter turnout tends to be high."

We never published a map, but the reporter was able to zero in on the critical precincts, ask better questions, and force the school district to confront the reality that it has serious credibility issues to deal with in neighborhoods it had counted on.

Which brings me to the final moral of this story: The effort is worth it.

Jeff Thomas can be reached by e-mail at jeff@gazette.com
