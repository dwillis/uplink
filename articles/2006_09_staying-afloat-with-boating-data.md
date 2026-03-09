# Staying Afloat with Boating Data

By John Ferro
*Poughkeepsie (N.Y.) Journal*

A couple of years ago, when I was city editor, we sent our political reporter to the IRE and NICAR Computer-Assisted Reporting Boot Camp at the Missouri School of Journalism. When he returned, I asked him how it went.

"I can't wait to use this stuff," he said.

I recalled that comment when I jetted off to Columbia in late March. I was sure I would be coming back flushed with a "CAR high." Instead, I returned CAR-petrified.

I had skills, but what to do with them? And the warning from IRE Executive Director Brant Houston's was ringing in my head – "Use it, or lose it."

So I started casting about.

We purchased the Environmental Protection Agency's Comprehensive Environmental Response, Compensation and Liability Information System (CERCLIS) from the IRE and NICAR Database Library. Too many tables. Too many joins. No clear trends. I was in over my head.

> Several journalists found timely summer stories in the boat accident data, including Mike Sherry of *The Kansas City Star* and Marc Chase of *The* (Northwest Indiana) *Times*. Find these stories and others in the Transportation archives of Extra!Extra!, www.ire.org/extraextra.

I sent a Freedom of Information request to the state education department for special-education data, but it took several months until the department and I worked out our differences over the request.

The clock was ticking. My bosses were tapping their feet, waiting for results. I could feel my little bitty CAR muscles atrophying each day.

I went back to the Database Library's Web site at *www.ire.org/datalibrary*. And there it was, after a few clicks:

> The Recreational Boat Accident database allows reporters to find information about the vessels, people and conditions involved in the accident. Because of the simplicity of this database, it is a good one for beginning CAR reporters to use.

Perfect. A database on training wheels.

I purchased the U.S. Coast Guard files, downloaded them from NICAR's FTP server and imported them into Microsoft Access database manager. Before I started running queries, I searched Nexis for stories that reported not only individual accidents, but also trends and recent legislation. I limited my searches to New York. (I kept hearing that line from the Jodie Foster film "Contact" – "Small steps, Ellie. Small, steps.")

In 2004, New York had completed its phase-in of a law that requires operators of personal watercraft to take an eight-hour safety course and pass a test before they revved up their JetSkis. My first queries examined accident trends involving personal watercraft.

The database has just four tables, and they are easily joined. I used Access to do counts and filter. Then I pasted the results into Microsoft Excel spreadsheets to create pivot tables and do percent-change calculations.

I am the kind of guy who spends a little too much time making sure his stack of *Poughkeepsie Journal* copies is piled neatly on his desk and reference books are organized by size. So, as the number of my Access queries increased, my efforts to name them became more, shall we say, compulsively obsessive.

I found it useful to name each query starting with its type: Filter, Count, MakeTable or Sum. So my list of queries looked something like this:

```
CountAllPWCByState
CountBoatTypesForHudsonRiver
CountEducationForPWCForNY
FilterForDutchessUlsterInjuries
FilterForHudsonRiverDeaths
MakeTableForDutchessUlsterAccidents
```

This saved time when I went back to my query list. All the counts were in one place, all the filters in another. (I got a little obsessive-compulsive rush every time I opened up the query window.)

My first analysis counted the number of boating accidents for each boat type – pontoon, personal watercraft, powerboat, etc. I did totals by year for New York and for the United States. I took each of those counts and pasted them into Excel. I used a pivot table to line up the totals for each boat type and each year. This allowed me to calculate the percentage of accidents for each boat type for any year.

I noticed the percentage of accidents involving personal watercraft in New York had dropped significantly during the 1995-2004 period I was examining. The rate of decline was faster than any of the more commonly used vessels.
