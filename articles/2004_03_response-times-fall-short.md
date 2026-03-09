# Response times fall short

By Enric Volante, *(Tucson) Arizona Daily Star*

Manager Shawn Bell called for medical help when a man collapsed in a diabetic seizure one night at Lil Abner's Steak House. Then Bell waited 10 minutes for help – even though an ambulance station is one minute down the road.

No wonder Bell's interest was keen when I sat down at the steak house bar the next day and showed him a map that compared how long ambulances took to respond to emergencies in his neighborhood and others.

Thousands of people peered at that map a few days later. Last April the *Arizona Daily Star* published "Rescue Roulette," a three-day series that revealed that the Tucson Fire Department ambulances failed more than half the time to reach emergencies within the eight-minute goal recommended by a national industry group.

The stories also showed how other local ambulance operators often missed the target. And many – including the company that responded to the diabetic man in the steak house – operated under licensing requirements less stringent than Tucson's.

We analyzed emergency response data using ESRI's ArcView 3.2 geographic information system (GIS) software to find out where emergency medical workers were going and how long they took to respond.

## Getting dispatch data

If you want to analyze EMS response, you'll need to get the CAD, or computer-aided dispatch, database. CAD data typically includes all the information found on traditional ambulance logs, such as time dispatched and time arrived, as well as information on the incident, patient, property and vehicles that responded.

Our city serves as dispatcher for the area's largest ambulance operator, the Tucson Fire Department, and for several fire districts and private ambulance companies. I requested the city's data for all agencies under the Arizona Public Records Law.

Tucson officials balked. In addition to patient names, they refused to release addresses to which ambulances responded, saying that might identify patients. They cited medical privacy concerns and the new restrictions posed by the Health Insurance Portability and Accountability Act of 1996 (HIPAA). They also withheld all medical data, such as whether the call involved cardiac arrest or an asthma attack.

My colleague Rhonda Bodfield and I met with city officials to negotiate which fields of data should be released.

We would have liked to follow the lead of journalists at *The Hartford* (Conn.) *Courant*, who joined a database of EMS responses with a public database of deaths to identify patients who died after long waits for medical aid. (For more information see "Cardiac crapshoot" in the July/August 1999 *Uplink*.) But death certificates are not public in Arizona, despite a fairly broad public-records law that hasn't been tinkered with much since territorial days.

So we gave up the address fields on condition that the city substitute plat numbers from a grid of quarter-mile land sections. Unable to argue that patients would be identified, the city then also gave up the medical data for each ambulance call.

Lacking names and addresses, we found patients to interview the old-fashioned way. We hit the courthouse to review civil lawsuits and we asked sources in the EMS business to name people who had waited a long time for help.

The city provided the database reluctantly and slowly, but at no cost. We ended up with a text file of 270,968 records of dispatch calls over 18 months that included fires, routine medical transports and medical emergencies.

By querying in Microsoft Access we found 92,400 were emergency ambulance calls. We deleted calls in which an ambulance was diverted to another scene. Sometimes in the heat of an emergency, drivers simply forgot to record when they arrived, so we also threw out calls with imprecise arrival times. That left 89,818 records.

Then we tabulated how long it took from the time an ambulance was dispatched to the time its crew reported arriving at the scene. We flipped the results into Excel to chart a comparison of the different agencies.

We mapped the calls in ArcView using a quarter-mile grid layer downloaded from the county transportation department's Web site, along with shapefiles of streets, fire stations and subdivisions that helped us see routes to the most populated areas. We used ArcView's legend editor to create a color-graduated grid of response times within each cell of the grid. Slower response times on the edges of the metropolitan area immediately jumped out, particularly in the northwest, where a once-rural fire district was coping with a growth boom.

But, like many parts of the country where fire departments and private ambulance companies have fought for turf, the Tucson region is a patchwork of competing providers. So we also asked the county's largest ambulance operator outside the city for its CAD database. Rural/Metro Corp. denied the request. That lack of accountability to the public became part of the story.

We knew the Arizona Department of Health Services had paper logs of ambulance calls submitted by Rural/Metro as part of its three-year license renewal. We ordered copies. Typing the data into Excel and double-checking it took three days, but it was worth it.

Unlike the city, the state had no problem releasing the patient addresses in those logs. We used ArcView's geocoding function to display about 7,500 addresses as points on a street map from the county transportation department. As we queried the data in ArcView, we saw long waits of 15 minutes or more had occurred in many places, not just distant areas. Dennis Joyce, assistant managing editor for news, had us run side-by-side maps showing different wait times.

While Arizona doesn't release death certificates, it was one of the first states to make campaign finance records available by FTP download. We found Arizona-based Rural/Metro kicks off the legislative session each year by spending close to $20,000 on a bash for lawmakers at places such as Phoenix's Ritz-Carlton hotel. As one ex-legislator told Bodfield, "I always graded the party by the shrimp – and they would have shrimp."

After we mapped the data, I visited some neighborhoods with long response times. I spoke to a few people on the street and then walked into Lil Abner's Steak House. When a cook mentioned that a man had been convulsing and kicking tables the night before while the manager phoned for an ambulance, I knew I'd brought the map to the right place.

You can read the stories online at *www.azstarnet.com/specialreports/emsresponse.html*

*Contact Enric Volante by e-mail at volante@azstarnet.com.*
