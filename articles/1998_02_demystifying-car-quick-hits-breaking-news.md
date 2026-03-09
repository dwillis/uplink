# Demystifying CAR: Quick Hits on Breaking News

**By Neil Reisner
The Miami Herald**

Okay. You've heard one too many stories about the yearlong CAR investigation using umpity-two databases, way-too-sophisticated statistics and a Pentium II 300 with 556 megabytes of RAM and a 200-gigabyte hard drive.

That just ain't the reality you live in.

But you've also heard one too many stories from one too many CAR wizards wearing a pointed cap with stars and crescents on it about the turn-on-a-dime quick hits that they produced merely by blinking their eyes.

They can be done. With just a little bit of forethought, it's possible – even easy – to apply CAR to your everyday work, even to breaking news.

That's what we've been doing at *The Miami Herald's* edition in Broward County, which, despite its connection to a major metro, is really not very different from a medium-sized daily.

That's because we put out our own edition of the paper in Broward with a remade front page, a local news section, bi-weekly neighbors sections, independent calendar listings, local sports – the whole package. We struggle along with the same limitations of staff and resources that confront most other papers. And we compete fiercely with the *Sun-Sentinel* of Fort Lauderdale, with whom we're at war.

Here are four examples of the ways we've used CAR in recent months – not to produce mega-stories but to add value to the routine. (And, for spice, examples of how we could have done better.) None took more than a day, and most were finished in several hours.

## Electing school boards

Education is the big political issue here in Broward, where the local Board of Education has about the same credibility as used car dealers and the schools are overcrowded despite the fact that they've spent $2 billion on construction over the last 10 years. The action involved an election last fall deciding whether to scrap the traditional system of electing school board members at large for a system in which most members would represent specific districts.

The change won overwhelming approval, much to the surprise of some pundits (and school board members) who figured what we call the "condo vote", mostly elderly voters loyal to the locally ruling Democrats, would rally to the status quo. The question was: How did this happen?

We covered election night as usual, downloading overall results from a BBS run by the Superintendent of Elections. The day after the election, though, precinct-by-precinct results were available. Usually, they'd been provided on paper, but last year we got them on floppy disk in a tab-delimited ASCII format.

From there, it was a simple matter to import the data using Excel's import wizard and then to move it over to Access. Teaming up with the political reporter, who knows the precincts like the back of his hand, we were able to isolate model precincts and analyze which way the vote went. The result: Young families and minorities came out in force to support a move they deemed important. The condo vote stayed home. With turnout only about 5 percent, it didn't take much to turn the election.

## Boating accidents

It was a real tragedy. A powerboat – the kind dope smugglers and men in midlife crisis love – was speeding up the Intracoastal Waterway in the dark of the night when it ran over a small cabin cruiser out for a midnight cruise, just about cutting it in half. Six people died, and more were critically injured – making it the worst boat accident in years and one that we covered intensely.

We already had about ten years' worth of data on recreational boating accidents from the Florida Marine Patrol. The dirty little secret was that it was still in the fixed-field ASCII format it arrived in. That meant writing import specifications for four tables with lots and lots of fields. And on deadline, in a competitive situation, that wasn't practical. (Remember what I said about "a little bit of forethought?" I should've imported it ahead of time.)

NICAR to the rescue. A quick phone call to Missouri and the good folks at NICAR extracted five years' worth of Florida data for us from the national data set they have. And – may God bless the inventors of the Internet – within an hour it was winging its way into my e-mail box.

Once in-house, it became clear that we'd only be able to use two years' worth of data because of changes in the field layout. But, with only a few straightforward queries, we were able to find out how many boating fatalities there had been during that time statewide and along our stretch of the coast, how many accidents, the boats most commonly involved in accidents and the most common cause of accidents. We printed out the information, turned it over to a graphic artist and put the data in the next day's paper.

We could have done better, though. As is too often the case, there was insufficient communication between the data guy (me), the reporter and the editor on the story. That meant the reporter didn't get the data soon enough and was insufficiently briefed on what it meant. Keeping everyone on the same page is real important.

## Multiple births

A local woman gave birth to quadruplets a few months ago. And, of course, the hospital PR folks were on the phone with us all agog and, of course, we prepared to go out and do something on the blessed event. (This was before the "Magnificent Seven" in Ohio made mere quadruplets passé.)

Discussing this in the morning news meeting, an editor said words to the effect of: "Geez. Every time quads are born we take the same picture and write the same story. Can we do something different this time? I wonder how much it will cost to raise these kids?"

We went out on the Web and found, oddly enough, a college professor's class lectures noting the USDA's annual cost estimate of child-rearing. A quick trip to the USDA site produced a press release announcing the most recent estimate and a full report on the estimates in *.pdf* format. The USDA estimates how much it costs to raise one child. But you can't just multiply that by four to get the cost of raising quads.

A call to the contact named on the press release got us to a USDA economist who told us the formula we needed. Plugged it all into a spreadsheet and handed it off to the graphics guy.

## Religious migration

With around 270,000 Jewish residents, Broward County makes up the fourth largest Jewish community in the country. That's why we pay a fair amount of attention to Jewish issues. So, when a long-established synagogue decided to sell its building to a charter school and move a few miles north to a more densely populated area, it was news.

The local Jewish federation had recently released a demographic study of the local community with a table showing the number of Jewish residents in each ZIP code. They faxed it to us, and a few minutes later it was typed into a database table.

We'd recently started playing with mapping software and were fortunate enough to have a copy of ArcView. It didn't take much to hang the ZIP code table onto a base map of ZIP codes we'd gotten from the county. (Forethought worked here – the base map was all ready, completed by my colleague Dan Keating.)

Once we drew the map, we saw clearly that the two ZIP codes surrounding the synagogue were among the densest Jewish areas in the county. And the area to which the congregation was moving was among the least populated.

That let us ask much more focused questions and explain that, even though the synagogue was located in a Jewish area, most of its members didn't live there. The area where the congregation was moving was closer to where most congregants lived and, more importantly, near a neighborhood where young Jewish families were moving.

Were any of these stories prize-winners? Hardly. And, with the possible exception of mapping software, they didn't use any software other than the standard spreadsheets, database managers and web browsers we all have. It's just a matter of thinking about the stories we're writing and how a little bit of data can make them better.

Neil Reisner, formerly NICAR training director, can be reached at
(954) 985-4571 or by e-mail at
nreisner@web2000.net
