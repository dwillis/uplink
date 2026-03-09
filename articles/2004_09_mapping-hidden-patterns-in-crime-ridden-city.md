# Mapping hidden patterns in crime-ridden city

By Brad Branan, *Tucson Citizen*

I found an investigative story last spring before I even moved to Arizona to work as a projects reporter at the *Tucson Citizen*.

The Tucson metro area had the nation's highest crime rate, Sperling's BestPlaces found in a study of FBI data.

It wasn't the ranking that intrigued me, though. It was the Tucson Police Department's response.

Department officials gave an explanation that will be familiar to many police reporters: They blamed the FBI's Uniform Crime Reports for providing a distorted picture of crime.

The UCRs equate a rape with the theft of a garden hose, a department spokesman said, in what became a mantra for city officials.

The statement was true on its face but also suggested that Tucson didn't have a problem with violent crime, and residents didn't need to worry about safety. That seemed unlikely.

Using Microsoft Excel, I crunched the FBI numbers that I downloaded from the FBI Web site to come up with rankings for violent crime – murder, manslaughter, robbery, rape and aggravated assault. The violent crime rate for the Tucson area was 55th out of 280 metro areas, ahead of places such as Philadelphia and Washington, D.C.

Violence was clearly a problem in Tucson. Still, the numbers didn't reveal the story that needed to be told. I needed to find out where the violent crime was concentrated and what it was doing to the neighborhoods.

The skills I learned at an IRE and NICAR mapping mini-Boot Camp this year helped me answer those questions.

## Mapping crime

An electronic map has streets, city boundaries and other elements found in the paper map on the newsroom wall. In a geographic information system (GIS) program, those elements are called layer files.

GIS clearinghouses across the country collect layer files of highways, voting precincts, Census tracts and other important map elements from various government agencies. The files are often available for free on the Internet.

Go to the Center for Advanced Spatial Technology Web site (*www.cast.uark.edu*), click on "Starting the Hunt," and you'll find a list of GIS sites nationwide. That's where I found a county transportation GIS site that had all the map layers I needed. I opened them in my mapping program, ESRI's ArcView 8.3.

I was ready to add the crime reports to the map. The Tucson police provided me with an electronic file of the reports but wouldn't give me exact street addresses, saying the information could violate the privacy of crime victims.

I didn't argue because ArcView allows you to map data such as crime reports without exact addresses. The reports were listed by city block, which was specific enough for my needs. For example, a crime that might have happened at 4850 S. Park Ave. would be listed at 4800 S. Park Ave.

I created a spreadsheet of the crime reports in Excel and then opened the file in ArcView. I had the program place a dot on the map for the location of each report, a process called geocoding. The resulting map showed dots throughout Tucson and not a definitive pattern. I had to dig deeper.

To find the areas with the greatest number of crimes, I needed to count the reports within smaller geographic areas. I attached the geocoded crime reports to a map of 38 police patrol areas. ArcView joined the two files, creating a single file of crime reports grouped by patrol area.

I opened the database in Microsoft Excel and counted the number of violent crimes in each patrol area. The results still didn't tell me which area had the most violent crime. Some of the patrol areas covered more area or had larger populations than others.

The crime reports had to be assigned a rate to account for the differences. I based the rate on square mileage instead of people because of rapid and uneven population growth in Tucson since the 2000 Census.

While I was putting together the map, editors and reporters speculated that the highest violent crime rate would be found on Tucson's south side. Drive-by shootings and other forms of gang violence in that part of town receive a lot of headlines and TV news coverage.

The perception proved to be wrong. The area with the highest violent crime rate was on the other side of town – the north side. After confirming my results with the police department's statistics expert, I was ready to report.

## Observations

By placing a map of city neighborhood associations over the crime clusters, I knew who to talk to in each community.

The neighborhood activists were defensive at first. They thought my story would detract from recent efforts to reduce crime and redevelop their communities.

They became more cooperative after I explained that I wanted to know about the causes and the effects of the violence, not simply label Tucson's most dangerous neighborhoods.

The north side had long been the site of the city's red-light district, attracting prostitutes and drug dealers who operate around inexpensive motels and strip clubs. The activity has created a volatile mix, producing violence that spills into nearby neighborhoods.

Most victims are involved in some sort of criminal activity, police told me. Wanting drugs or a prostitute, they end up getting robbed, beaten or killed.

Law-abiding residents were also paying a price. The violence convinced many of them to move to safer parts of town, neighborhood activists told me. The activists themselves had been subjected to threats and other forms of intimidation.

Census 2000 provided the data to document their observations. Adding Census tract data to my crime map, I found that only 23 percent of residents in the highest crime areas had lived there more than five years.

**The perception proved to be wrong.**

The Census also provided some statistical evidence for an explanation police had for the crime clusters: poverty. The areas with the highest crime rates also had some of the city's highest poverty rates.

## Feds respond

The ability to downplay violent crime was diminished after the story was published. Police and other city officials acknowledged the destructive effects of violence in the neighborhoods that were profiled.

In June, the Bureau of Alcohol, Tobacco, Firearms and Explosives announced a violent crimes task force for the city. A city official said my story was the reason the task force was formed. An ATF special agent said the story helped build support for the task force.

ATF said it would use "new innovative technology in combination with analytical investigative resources" to reduce crime. An ATF map of "gun-related hot spots" in Tucson mirrored the one published in the newspaper.

The task force promised to bring federal, state and county law-enforcement resources to Tucson, where police department staffing is well below the national average.

Despite a budget crunch, the Tucson City Council approved the police department's request for $4 million to hire 71 more officers. And Attorney General John Ashcroft visited the ATF-led task force here and praised its initial efforts.

Previously reluctant to discuss violent crime, neighborhood activists and city officials said the story was helping to attract needed attention and resources to the area.

"Your report of the prevalent problems in the Oracle-Miracle Mile corridor gives neighbors and businesses hope that people are really paying attention to the needs of the area," a city councilwoman wrote me. "I truly appreciate your work."

Contact Brad Branan by e-mail at bbranan@tucsoncitizen.com.
