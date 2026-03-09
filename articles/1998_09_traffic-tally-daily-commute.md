# Traffic tally

**By Neill A. Borowski**
*The Philadelphia Inquirer*

"Ca-chunk, ca-chunk, ca-chunk." Cars and trucks travel over the black hose stretched across the road. Each "ca-chunk" registers on a roadside counter as the government tallies the vehicles using the road each day.

The data are loaded into databases – at state departments of transportation or county planning departments – and adjusted for the number of axles. Fascinating information, but it is most often used only by the departments themselves for proposing future road projects or by marketers to decide where to locate the latest fast-food restaurants.

Earlier this year we decided to do a project looking at the daily commute. For several years, I had collected snippets of Average Daily Traffic (ADT) information from a variety of sources. I had pieces from various marketing reports and text files from online DOT databases. What I wanted to do, however, was pull together a comprehensive look at ADT in the Philadelphia metropolitan area. A map was the logical choice to convey the commute to readers. (The special section, called "Drive Time," was published on May 31, 1998.)

### Traffic averages

The result was a map loaded with about 600 different points. Each point represented a spot on a road or highway and showed the average daily traffic. I produced the early map with ArcView and passed the project along to our graphics department, which also uses ArcView. Graphics artist Matthew Ericson broke down the points into five different categories, ranging from less than 10,000 cars per day to more than 75,000 cars per day.

We acquired the data from the Delaware Valley Regional Planning Commission in Philadelphia. The commission traffic specialists' first reaction was: "What intersections are you interested in?"

Our answer was the usual CAR response: "We want the whole database."

The planners viewed the request as odd, but after some negotiating they shared the data. The result was an illuminating map. One marketing firm in the Philadelphia suburbs eagerly ordered several copies of the map because they had never been able to capture the whole region on one map before.

### Coordinated accidents

While the project, we thought, was interesting and useful, the most exciting mapping aspect came in the use of latitude and longitude coordinates provided with the file. I brought the lat/lon coordinates in as an added event theme in ArcView (a *.dbf file) and overlaid them on our regional streets file. We found the coordinates were amazingly accurate, matching perfectly with the street file.

Lesson learned: Always ask if the file has lat/lon coordinates built in.

Shortly after the "Drive Time" project, we put together a large story looking at where accidents occurred in South Jersey (Pennsylvania won't give exact locations of accidents). This was far more difficult than the Drive Time/ADT project.

The database file listed accidents by intersection or milepost on highways. That prompted my call to the New Jersey Department of Transportation in which I asked, "How am I supposed to know just where milepost 27.33 is on Route 70?"

"Oh," the highway guy said, "you need our straight-line diagrams. We'll send you a CD-ROM."

The CD is a compilation of Acrobat *.pdf files. You click on a route, and it gives you the breakdown in miles. Click on 26-28, for example, and you can see exactly where milepost 27.33 is located and its nearest cross street.

The process of finding these sites was far from automated, but the straight-line file made it easier than it might have been. Check with your state DOT to see if it has straight-line diagrams in book or computer form. I sent a copy of the CD along to our graphics department, which was delighted to get it. Seems that they are forever getting accident reports on deadline and trying to figure out how to locate mileposts on highways.

Accident files provided to us by the state did not include lat/lon coordinates. However, a more recent accident file, which the state told us not to use because it had bugs that could affect our findings, did include the coordinates. I managed to look up latitude and longitude for the accident spots we wanted to map. However, when we mapped the coordinates with our streets file, we discovered that many were off a bit. Some were several miles away from where they should have been.

### Navigation's convert

Despite some wrinkles, I've come to believe in latitude and longitude as an essential tool. I remember doing a story on some GPS (Global Positioning System) fans a few years ago. One predicted that latitude and longitude would supplant ZIP codes and addresses in the future. Your address would be your latitude and longitude – a universal system. I rolled my eyes a bit, but now I'm wondering whether they were on to something. Yes, I've joined the GPS Cult.

A couple of years ago, we purchased two hand-held GPS receivers. We bought Eagle Explorers, but there are many good brands out there for less than $200. I gave one to a technically astute *The Philadelphia Inquirer* photographer, Michael Mally. We kept the other one in our CAR department.

The GPS receiver uses readings from three (out of a total of 24) GPS satellites to calculate the latitude and longitude of the spot where you're standing. The accuracy is said to be within 100 feet.

Mally became a navigational convert. Besides the GPS unit, he also uses a laptop computer with Delorme's Street Atlas USA. He's often the photographer who goes up in helicopters to shoot aerials. Mally realizes helicopter time is precious – particularly when it runs as high as $600 an hour.

He routinely uses Street Atlas to find the lat/lon of the points he wants to visit and maintains that this cuts deeply into time in the air. He merely gives the headings to the pilot; then they sit back without having to locate highways or landmarks below to determine if they are on the right track.

The navigational tool can work in the other direction, too. Mally says he has been flying when they discover a column of smoke. From the air, it's difficult to determine where the smoke is coming from. But, with a lat/lon reading, he can plug the coordinates into his map program and pinpoint the location.

Mally also used the handheld GPS unit when shooting the construction of an artificial reef off the Jersey coast (the National Guard was sinking old tanks). The GPS allowed him not only to determine where the reef was being built but also to estimate the reef's length by calculating the difference between the first coordinates and the last.

### A GPS future

I believe that one day the Metro Desk will have a stock of GPS units in a drawer. Maybe they'll be common "pool" items like company cars and cell phones. Those company cars also might come with the GPS units built in to provide directions to reporters as well as to report coordinates.

A reporter running out to cover a major forest fire would grab a GPS to give accurate coordinates to the graphics department to map the fire. In fact, the report could take coordinates for the perimeter of the fire so the map in the next day's paper would be an accurate portrayal of where the fire was burning.

We were prompted to purchase the GPS units after trying to figure out the site of a major bus accident-on-deadline in a wooded area in South Jersey's Pine Barrens. Even with regular maps open in front of us, we weren't clear where the accident occurred. A photographer or reporter with a GPS unit could have given us lat/lon coordinates, and we could have pinpointed the location.

The potential uses seem endless: a murder victim is dug up in the woods; an oil truck flips and spills on a back road; a new development is going up in the middle of a farm in a rural area without new roads.

Neill A. Borowski can be reached by email at nborowski@phillynews.com.
