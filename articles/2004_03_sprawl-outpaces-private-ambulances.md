# Sprawl outpaces private ambulances

By Jeff Sonderman, *Missouri School of Journalism*

Investigating emergency response times takes a lot of upfront reporting and data chasing before you know if you have a story. So how do you know if you should jump into doing this story in your community? There are a couple of ways.

If you notice specific cases where people died waiting for an ambulance, that's an obvious red flag. But you don't need to wait for such a clear signal.

In any community with sprawl and growth, journalists may wonder whether key public services, including emergency medical services (EMS), are keeping up. That's what sparked my interest and led to "A Matter of Time," a November 2003 story in the *Columbia Missourian.*

The story was based on the analysis of Boone County computer-aided dispatch data using ESRI's ArcView 8.2, as well as Microsoft Excel and Access.

I obtained three years of computer-aided dispatch (CAD) records of emergency medical calls, 39,744 total, from Public Safety Joint Communications, a city agency that operates the 911 service.

The agency's database manager was cooperative and told me what data was available. Because of privacy concerns under the Health Insurance Portability and Accountability Act of 1996 (HIPAA), the agency would only release the data to the hospitals, which then handed it to me on CD. The data came in a comma-delimited text format at no cost because it required no special programming.

HIPAA also challenged our desire to map response performance. The hospitals refused to provide addresses that were logged for each call because the information could easily identify patients. I talked to the database manager about alternatives, and he said the dispatch agency logs the general location of each call using a grid with cells of about one-half square mile each. He e-mailed me an ArcView shapefile of the geographic grid system that day.

The response data was relatively clean; 911 system computers, not people, had entered much of the data automatically. The biggest problem was that response times were not properly logged on some calls. The response time is recorded when the dispatcher presses a button at the time of dispatch and again at the arrival on scene. In some cases, the dispatcher missed one of those events, and the response time was recorded as zero. These records were excluded because the errors seemed to affect calls in a random pattern that did not skew the data. This anomaly, as well as all of my analysis, was explained to the readers in a sidebar.

We imported and analyzed the data into Access and exported the results of some of the queries in Excel.

The analysis included looking at overall response time, as well as grouping in Access to see response times by ambulance, specific location, city or town, and time of day. I looked at the division of call volume among various ambulances and locations and times of day.

To analyze performance relative to the eight- and six-minute response time standards of the hospitals, I created two fields to indicate whether the unit had reached the scene within each of those two time frames. I also created new fields to display the response time for each call in seconds, based upon the start and end times included in the data.

In ArcView, I used the grid to map responses by grid section, which produced a color-coded mosaic showing the percentage of calls in each sector that were reached within the eight-minute goal. To do this, I first used an Access query to group by the coordinates for each grid sector. I then summed the number of calls reached within the goal and counted the total number of calls in the area. I imported the result of that query into Excel to figure out the percentage of successful response times for each grid sector. Then I imported that simple table – just grid coordinates and the percentage of success – into ArcView and applied it to the shapefile that used the same grid coordinates.

Talking to the people who kept the data also helped us to extract useful data from two of the fields in the database.

The grid coordinate field of each record corresponded to a single cell on the grid map, but it also contained a letter at the end of the four or five numbers (the "B" in section 14041B, for example) that indicated the general location of the call. Each of the smaller cities and towns in the county had its own assigned letter. I parsed the grid coordinate field in Access and placed its letter into a new field so I could easily examine all the calls in those towns using grouping and counting queries.

The index field that assigns a unique identifier to each dispatch also included characters that indicate which ambulance responded, for example "M31" for Medic 31. We parsed those references into a new field, which allowed us to look at response times and emergency call volume for each ambulance.

The two ambulance services that cover Boone County are owned and operated by the two major local hospitals. The good news for residents is that they don't pay a tax for a public ambulance service. But this also means the ambulance services are departments of large institutions that have to watch their financial bottom lines.

Emergency medical services tend to lose money, and that puts the operators in a sticky position. How much money are they willing to lose on an ambulance service to provide better patient care?

This is an especially important issue in small but rapidly growing regions, such as Columbia and Boone County, which has a population of about 135,000 people, with about two-thirds of them in the city of Columbia. But Columbia is sprawling outward, away from the ambulance stations, and populations are growing in other cities around the county.

Once I had the story, it was time to make it come alive with field reporting. I went on several ambulance ride-alongs, arranged by one of the hospitals, and shadowed the paramedics when they responded to calls.

This firsthand experience helped me understand the system and the numbers I was writing about. It also gave me extended access to paramedics in their work environment, where they were talkative and comfortable. The time I spent on ride-alongs was incredibly useful. The paramedics are on the front lines of EMS, so they often provided the most insightful comments on the data I showed them.

Paramedics can also help answer the big question: How much is better patient care worth? Paramedics almost always want more ambulances and more resources. They would take an ambulance on every street corner if they could get it, because their biggest concern is patient care. Here you might find, if not a whistleblower, at least an advocate for change in the system.

Contrast that with the concerns of managers and hospital administrators. Many of them have never worked as paramedics, and their focus is more on the financial costs of adding ambulances or other resources.

So in most EMS systems, you will probably find some amount of tension between what the EMS workers want and what the administrators think is necessary or practical. Each side will be eager to convince you, and you can use information from both sides to develop a balanced story.

*Contact Jeff Sonderman by e-mail at jeffsonderman@yahoo.com.*
