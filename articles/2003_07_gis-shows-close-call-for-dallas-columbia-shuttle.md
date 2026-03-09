# GIS shows close call for Dallas

By John Kelly
*Florida Today*

"How many are dead on the ground?"

I must have asked that question a dozen or so times the morning of Feb. 1, as my colleagues and I scrambled to find out what happened to the shuttle Columbia in the far reaches of the Texas sky. Watching the televised images of giant steel balls, mangled fragments of wing and other heavy metal objects strewn across Texas, it seemed obvious the death toll was going to be higher than the seven astronauts. The question was, "How many?"

The still-dumbfounding answer is zero. NASA got lucky.

NASA seemed to be ignoring how many people on the ground had been in harm's way. It was a fundamental public safety issue. We weren't about to ignore it. We could have just thrown together color from Texas with dueling expert quotes for a "what-a-miracle" story. Instead, we wanted to show in a definitive way the very real risk of flying the space shuttle over populated areas.

We set out to apply the same methods that NASA, the U.S. Air Force and big aerospace contractors use when they try to assess danger to people on the ground during space launches, or when one of their unmanned satellites or rockets eventually plummets back to Earth.

That turned out to be the right approach for two reasons.

First, my colleague Todd Halvorson and I piled up a mountain of public records showing how carefully the government and aerospace companies make sure that debris from re-entering spacecraft and rockets does not strike land, let alone come down on populated areas. By contrast, Halvorson found NASA had never studied the danger to people on the ground during the very risky re-entry of its space shuttles.

Second, we learned the industry's accepted method for minimizing death and destruction on the ground was to predict the footprint, or area, where the debris would hit, and to do everything possible to control the re-entering space junk so the danger zone would contain few, if any, residents.

I knew we could use ESRI ArcView mapping software to determine the number of people who were in the path of shuttle parts. Using ArcView we layered the debris footprint over U.S. Census population data and determined that about 216,000 people lived in the largely rural area where most of the debris hit. We also used the shuttle's flight path to show the more grim consequences had the shuttle broken up about a minute earlier.

In that case, the storm of metal would have hit Dallas' suburbs. About three times as many people and houses would have been in the path of falling wreckage.

Computer-assisted reporting nerd that I am, I overcomplicated things from the start.

GIS and computer mapping tools were being used in the recovery effort. It was clear search teams were recording the precise coordinates of each piece of shuttle found. NASA was making computer maps.

I went to Stephen F. Austin University, which was helping NASA with the mapping. They made available online ArcView shapefiles of the region of Texas where debris was found. I wanted the shapefiles that were the basis of NASA's nifty handouts, showing every piece of debris as a dot on the Texas map. I had the big idea that I was going to calculate how many people lived a set distance from any one of those dots.

The university asked NASA if they could give me the data. NASA said no. We could FOIA the database, but we did not have time to wait.

I went back to what the university had released online. I found a shapefile of the 20-kilometer buffer zone calculated from the centerline of the debris field. The oval was as close as we could get to an "official" debris footprint.

We used a free ArcView 3.x extension called Two-Theme Analyst. I laid the approximated debris footprint over Texas Census data and then used Two-Theme Analyst to approximate the number of people living within the debris oval.

We ran the analysis using Census data at the block, block group and tract level. We got three sets of very similar numbers. In the end, we went with block groups because it worked best for the maps we ultimately published in the newspaper.

We also shifted the footprint northwest along the flight path to get "what-if" numbers for a break up over Dallas-Ft. Worth. I then re-created the maps in ArcView 8 and worked closely with graphic artists to convert from ArcView to Adobe Illustrator a set of maps that showed readers the dangerous consequences of the two scenarios.

That could not have been done in words alone — and certainly not without the computer analysis.

We ran a pair of population density maps side by side in the paper that we prepared with ArcView. One showed the real debris field. The other showed the scenario. The simple contrast of population density made a very clear point about NASA's good fortune. Detailed counts of people and homes were given too.

Our online staff turned the maps into a telling interactive presentation on the Web. See the story at *www.floridatoday.com/columbia/columbiastory2A52178A.htm*.

Meanwhile, Halvorson and I also were doing the research and reporting to frame the issue in the appropriate context.

We wanted to show how NASA fretted in the past about where debris from satellites the size of school buses might hit. Yet for weeks leading up to the publication of our report, the agency said it never deemed necessary a study of what might happen with a craft the size of a jetliner. Officials explained the space shuttles were designed to survive re-entry and the chance of a breakup was so remote that studying where debris might fall was neither necessary nor practical.

Our story acknowledged NASA's options are limited. There are only so many paths the shuttles can fly to get back from space. But there are options to reach landing strips in Florida and California while substantially reducing the number of population centers beneath the flight path.

Within a week of the story running, the Columbia Accident Investigation Board said it was looking for contractors to study the issue we raised. NASA Associate Administrator Bill Readdy told *The Washington Post* the agency commissioned a similar study. Neither will say if the studies were initiated before our report or because of it.

The official government investigation report will ask if public safety should have dictated that NASA try to land Columbia in California that morning instead of flying over so many major population centers — from San Francisco to Dallas. NASA is not finished studying its re-entry options for the future, but investigators agree changes to shuttle flight rules are inevitable.

Contact John Kelly by e-mail at jkelly@flatoday.net
