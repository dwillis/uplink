# Valuable Accident Data

**By Hurst Laviana**
*The Wichita Eagle*

Wayne Louden has been involved in 37 traffic accidents since Jan. 1, 1990, making him the most accident-prone driver in Kansas. Thomas Spicer has been involved in 27 wrecks, 21 of which resulted in inattentive driving tickets.

Louden and Spicer were key players in a series of stories about accident-prone drivers in Kansas. The series was based on a Kansas Department of Transportation 1990-1999 database that covered 703,000 traffic accidents involving 1.1 million drivers.

Acquiring the database was a struggle, but it has proved to be one of the most valuable data sets in our newsroom. It has yielded stories about the growing number of car-deer accidents in the state, the reluctance of drivers in the nation's "beltless belt" to use seatbelts and the fact that accidents involving police chases doubled in Kansas during the 1990s. The data also allows us to quickly generate lists of accidents that have occurred at any intersection in the state.

But the biggest reader reaction came from the story about accident-prone drivers. Many were surprised to learn they were sharing the roads with 20 Kansas drivers who had 10 or more accidents in the 1990s. And some of those drivers had dozens of traffic convictions.

How did they keep driving?

It turned out that the Kansas Division of Motor Vehicles hasn't been enforcing a law that allows it to suspend the license of any driver convicted of three moving violations in a 12-month period. Instead, the DMV only takes action after the fifth conviction.

It also turned out that Spicer's inattentive driving tickets – as well as 70,000 other inattentive driving citations issued each year by Wichita police – don't even count against a driver's record. Inattentive driving is a ticketable offense in many Kansas cities, but state law does not prohibit it. So the state doesn't count it.

## Doing the Stories

The seeds for the story were planted more than a year ago when Crime & Safety team leader Jim Lewers asked KDOT for five years of accident data. KDOT mailed him copies of the 1990 through 1996 annual traffic accident reports.

Lewers tried again, this time asking for a comprehensive electronic database with detailed information about each accident. KDOT's response: for $51,710 we could have the data – minus the drivers' names and accident locations. KDOT, which wanted 5 cents a line for just more than 1 million lines of data, said giving us the names and accident locations could result in the information being used against it in court.

KDOT held its ground until February, when a judge ruled that the agency was improperly withholding railroad crossing accident data from another Kansas newspaper, the Garden City Telegram. KDOT eventually gave us the accident data – names and all – for $87.11.

## Crunching Numbers

The file arrived in the newsroom on a CD-ROM in the form of a 550-megabyte Microsoft Access database, which included separate tables for such variables as drivers, accidents and vehicles. My three-gigabyte hard drive was no match for that much data, but we did turn around some quick stories using pieces of the data.

On March 22, the day the Kansas House of Representatives approved a bill designed to cut car-deer accidents by increasing the number of out-of-state hunting permits, we sliced the deer accidents from the accidents table and loaded them into an Excel spreadsheet.

Excel's Chart Wizard produced an interesting graphic that showed a steady rise in the number of car-deer accidents. It also revealed a sizable blip every November, when the males were out seeking mates, and a smaller blip every May, when females were out looking for places to give birth.

Our lead: "Cars, trucks and buses crashed into more than 10,000 deer in 1999, a record for the state."

Once a bigger hard drive was installed in my computer, we set out to find the accident-prone drivers. We needed the extra room in order to link the tables so we could track such variables as injuries, fatalities and accident causes.

A single "group-by" query on the driver's license field generated a list of hundreds of Kansans who had been involved in three or more accidents during the decade. The process was complicated by the fact that Kansas changed its driver's license numbering system in the mid-1990s, so most drivers had two driver's license numbers.

Other "group-by" queries on the firstname, lastname and DOB fields turned up another batch of candidates. We ended up working with a list of 1,960 drivers who had five or more accidents in the 1990s. Their 11,165 accidents left 50 people dead (including 14 of the accident-prone drivers) and 5,171 injured.

We eventually decided to focus on the six drivers who had 12 or more serious accidents during the decade.

## Doing the Legwork

The next step was to ask KDOT for hard copies of the accident reports for the six drivers. We also asked local law enforcement agencies for copies of reports for non-injury accidents involving less than $500 in damage – accidents that aren't reported to the state.

The written reports, which often had narratives and diagrams, included more detailed information than the KDOT database. Based on this information, reporters interviewed drivers.

The series ran in late September, and a week later we put the list of drivers with five or more accidents on our Web site with a disclaimer noting that the listed drivers were not necessarily at fault in any of the accidents.

The only negative reaction from readers came on the following Wednesday, when a woman who works at City Hall called to say our on-line information was wrong – that she hadn't been involved in six accidents. When given the dates and locations she retreated, then insisted that none of the accidents was her fault.

Hurst Laviana can be reached by e-mail at hlaviana@wichitaeagle.com

---

**"Bad Drivers," is available online at *http://web.wichitaeagle.com/content/wichitaeagle/2000/10/02/special/driverslist1002.htm***

**It is also available in the IRE Resource Center, story #16839.**

**For more on the *The Wichita Eagle's* story see the January/February 2001 issue of the *IRE Journal*.**

**Software: Microsoft Access and Excel**

**Data: Kansas traffic accidents, 1990-1999**
**Source: Kansas Department of Transportation**
