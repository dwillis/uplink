# Suspect Semantics

**By Craig R. McCoy and Tom Torok**
*The Philadelphia Inquirer*

Philadelphia sure is a law-abiding place. It's a city where people aren't held up at gunpoint. Instead, they have "disturbances," or, at worst, are subject to "threats." Victims aren't beaten or stabbed. They are deemed mere "hospital cases," coding for the police taking someone to the hospital. Pocketbooks aren't ripped off; they're booked as "missing property." Thieves don't steal cars. Instead, the car's forgetful owners lose them, and the helpful cops write up the missing vehicles as a "try and locate."

With artful classifications such as these, Philadelphia's police department for years has been fudging statistics for the FBI's influential Uniform Crime Reporting (UCR) program. This, in turn, has permitted mayor after mayor to boast of the city's low crime rate.

Until the whole statistical deck of cards came undone. In a series of articles over the last year, *The Philadelphia Inquirer* has challenged the city's crime statistics, using computerized reporting and a lot of old-fashioned, shoe-leather interviewing to document flaws in the numbers.

The finagling has had a big impact, both for the citizenry as a whole and, on a very personal level, for victims:

- At this point, no one really knows what the true crime picture is for the city. In stages, police over the last year have disowned the citywide crime stats for 1996, 1997 (twice withdrawn) and the first half of 1998.
- The scandal has damaged Philadelphia's attempt to follow New York's lead and switch over to police deployment based on computerized trend-spotting and mapping.
- Some "downgradings" – the term for converting a major crime to a minor one – have cut off cases from detectives, leaving suspects free to strike again.
- Victims have lost their claim for compensation under a state program that helps pay for uninsured medical bills. No crime, no victim, no compensation.

The stage for our reporting was set when Philadelphia Mayor Edward Rendell, finally responding to requests from the *Inquirer* and the *Philadelphia Daily News*, released seven years of underlying crime-by-crime data. This massive computer file provided details on more than 700,000 crimes deemed serious by police from 1991 to 1997. Philadelphia is one of few major American cities that release such detailed information, besides totals made public twice a year by the UCR program.

Using Access and Excel, an *Inquirer* team began to slice and dice the data. In some ways, our focus was on the dogs that weren't barking – crimes that weren't being booked.

### Boom and bust thefts

Among our early articles was a straightforward account, pegged to the FBI's national release, of the city's overall crime rate for 1997. Even as we wrote it, we noticed a weird trend in the data. When crimes were analyzed by month, Philadelphia had a puzzling drop in car thefts in the first half of the year, followed by a boom in the second. The change was without precedent for Philadelphia; we could not explain it as seasonal.

We then took our analysis to the city's police chief, John F. Timoney, for comment.

The numbers at issue had already been withdrawn from the FBI count once. In late 1997 the *Daily News* first reported that the city had been counting crimes based on when they entered data into their computer system rather than when crimes occurred. This method made comparisons between years and among cities haphazard at best.

Timoney, who inherited the mess when he took command of the force in March 1998, had released new 1997 figures after tallying them again for a regular Jan. 1-Dec. 31 calendar year.

Once he had digested the *Inquirer*'s new analysis, Timoney announced in May 1998 yet another inquiry into the 1997 figures, less than a week after their re-release. In September, he provided the results: for the first half of the year, police had by mistake dropped 3,000 property crimes – mostly stolen cars – from the city's count.

### Novelties and oddities

As we continued to explore the database, other puzzling patterns emerged. A key finding was Philadelphia's remarkably low count of aggravated assaults compared to murders. While almost every major city routinely books 50 such serious assaults for every murder, Philadelphia was logging just 15 per murder. Criminologists pointed us to data showing that murder and serious assaults rose and fell together in that ratio in most cities – a not surprising tidal effect if you think of a murder as an assault that goes too far.

Another oddity: attempted burglaries had just about vanished in Philadelphia. For example, the data let us see that two police districts, with a total population of 138,000 people, reported a total of only *six* attempted break-ins in 1997. Shoplifting figures had been similarly low-balled. So had thefts of auto licenses, a particularly troublesome Philadelphia problem.

Though Philadelphia's pervasive culture of numbers chicanery may seem unusual, there is no doubt that the problem prevails in municipalities large and small. Since the system's founding nearly 70 years ago, major UCR scandals have flared repeatedly. Experts have been warning that the problem is growing more virulent as departments put more stress on the numbers, both to fight crime and to rank commanders. In the last year statistical controversies have been sparked in New York, New Orleans, Baltimore, Atlanta and Boca Raton.

### Shoe-leather series

As we worked over the data, we also interviewed serving and retired police from beat cops to commanders; victims and victims' advocates; town watch and civic group leaders; and academic and policing experts nationwide. We also consulted court records and ordered scores of individual incident reports.

The department's long-time culture of "going down with crime" – as the cops called it internally – began to surface. Detectives and street cops told us how crimes were blown off to lighten their workload. Others spoke of constant pressure from the top, of district commanders and even more senior officials seeking to raise performance ratings by putting a thumb on the scale of justice.

Our work culminated Nov. 1-2 in a series that was actually sparing in its use of numbers and charts. Instead, we told story after story of actual victims and how the crime against them had been downgraded. One article explored violent crime; another tackled crimes against property. Among the more dramatic evidence were graphic reproductions of complete police reports that had been rewritten to downgrade the crimes. In the rewrites, key information vanished, including descriptions of suspects and weapons.

### Wrongdoing and response

The issue has engendered considerable outrage in Philadelphia. For the first time, the city controller, the top financial watchdog for the city, is planning an audit of crime figures. U.S. Attorney General Janet Reno has asked her aides to examine the Philadelphia figures.

Timoney has sworn the 1998 figures will be accurate, "if it kills me." He has transferred two captains whose numbers were questioned and created an aggressive auditing unit to check figures. So far their investigation suggests that as many as 5,500 crimes were buried in the first half of 1998 – one out of every 10.

After our series, Timoney ratcheted the pressure higher. He announced that undercover police would pose as crime victims to "sting" officers mishandling paperwork.

### Character overload

While examining the Philadelphia figures, we also looked at national data. We drew, in part, upon unpublished FBI statistics that the agency provides on magnetic tape (available from NICAR) that includes in its entirety crime data collected for the UCR program – much more detailed information than what is available in print in the well-known *Crime in the United States* publications. One problem is the FBI sends the data in text that runs 8,000 characters across, four times the length that most databases can handle. Using a Visual Basic script, Torok helped break down the data into usable sections. *(Note from the Database Library: NICAR processes the raw FBI data so software using the .dbf format can handle them.)*

At the paper's request, a sociologist at Temple University had built an ArcView GIS map of Philadelphia, which tagged each of the city's 400 police sectors by neighborhood. With this in hand, for one article graphics artist Matthew Ericson allocated crime by sector to each of Philadelphia's 56 neighborhoods. We ranked them by violent crime and property crime rates.

### Online database

With leads flowing in, we are still at work on the issue. In one recent development, we posted on *The Inquirer*'s Web site, Philadelphia Online, the 700,000-crime database that underpinned the entire effort. It took considerable grooming to get the database into usable form. Using Visual Basic, Torok "parsed" the chaotic address field into discrete block and street fields. His program correctly separated all but 15,000 of the crimes. Ericson then wrote a program in Perl that solved another particularly bad 6,000 addresses or so. We also deployed scripts that fixed more than 100,000 misspellings of street names.

Using Microsoft SQL Server, Torok then created active server pages on the Web site that permit readers to search the database rapidly for crimes on their block over seven years, on any one day, and by other methods. His program ingeniously separates and indexes the data by search method to produce quick results from an immense dataset. It received more than 24,000 page views its first day online. For comparison, a well-browsed *Inquirer* sports story receives around 3,000 "hits."

One of our first responses came in an e-mail, edited slightly for confidentiality: "I looked for an assault," a browser wrote us. "It must have been downgraded since it is not listed at all. It infuriates me that an assault is not reported. The two men who did this meant to cause bodily damage, but their act of cowardice won't be known because the police department is playing games with our lives."

We're looking into it.

*Craig McCoy can be reached by e-mail at mccoyc@philly.infi.net*
*Tom Torok can be reached by e-mail at Tom.Torok@phillynews.com*

> **McCoy writes:** Our reporting has also triggered follow-up coverage from other media. CNN, NBC's Dateline, NPR, the new 60 Minutes II, the All Points Bulletin crime-news Web site (http://www.apbonline.com/911/1998/11/16/phillystats1116_1.html), and a fledgling RealAudio-based Internet news service called WorldStream Communications, among others, are all taking a look at the issue.

> The 1991-97 crime database can be reached at http://home.phillynews.com/crime. The site also includes a discussion of the data, a collection of many of the news stories discussed in this article and other crime-related databases for our region.

> Other examples of Web sites devoted to crime statistics and mapping include:
> - The Charlotte Observer at http://www.charlotte.com/crime
> - The Evansville Courier at http://courier.evansville.net/crime
> - Omaha World-Herald at http://www.omaha.com/owh/crimereport
>
> McCoy also suggests visiting the Web site of the San Diego Police Department at http://www.sannet.gov/police/crime-facts/index.html
