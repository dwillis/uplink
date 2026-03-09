# Answers Found in the Data: Tracking Rail Safety

## By Penny Loeb
*U.S. News and World Report*

A train crashes in your city. What's the accident record of that railroad? Several people in a car are killed at a crossing. How many people have been killed at crossings in your state? Some of the answers are in the databases distributed by the Federal Railroad Administration at its Web site, and also by NICAR.

In May, *U.S. News and World Report* and ABC's PrimeTime Live released a joint investigation of safety problems with railroads. It revealed that accidents have remained pretty steady for a decade while the FRA and railroads ignored calls for better braking systems, tracks, passenger safety and working conditions from Congress and the National Traffic Safety Board.

The FRA's user-friendly Web site has .dbf files ready for download, as well as record layouts and code lists. There are four files. One is accidents, which are available from 1991 through February 1996. Reports provide rich detail, including railroad, time, weather, place, cause, type of track, number killed, number injured, number evacuated and number of cars with hazardous materials. The one catch is that there is a record for each railroad and track owner involved in the accident, making for as many as three records for one accident. The FAQ file explains that the unique identifier is year3, month3, rr3 and incdno3. The data also has a field with the same state-county code used by MapInfo. I mapped the serious accidents for December 1995, which made a compelling graphic.

There are also separate tables on casualties, grade-crossing accidents and number of miles traveled by each railroad. Casualties contains injuries to employees, trespassers, passengers and others. Grade crossings has accidents at railroad crossings. A few of these will be reported in the accident file, if damages to the train were more than $6,300. The grade crossing database also has multiple entries for some accidents, so you need to group by the same four fields.

The FRA has put the entire, very detailed 1994 Accidents/Incidents bulletin on the Web site for downloading. You can spot check your calculations against those in the report.

There are several weaknesses in the data. First, it is self-reported by railroads. Second, the accidents database only has those with damages over $6,300. The damage threshold omits more than 90 percent of the accidents. CSX, one of the largest railroads, had 104 reportable accidents in 1995, but the total number was 1,755. I found a number of small spills of hazardous materials on the Hazmat database, but missing from FRA.

We got total numbers of inspections and violations from the FRA, but did not get the data. It is available on nine-track tape, but it is difficult to use because the inspection system changed in the past two years, as did some of the data. The FRA database administrator, Robert Finkelstein, is very helpful, though.

If you are contemplating a story on railroads in your area, check NTSB accident reports and recent Congressional testimony for detailed background. You will need to develop sources among rail workers, who can guide you to the worst problems. Smaller railroads often have higher accident rates.

Here are some useful Web sites:

- **Railroad Definitions:** http://pavel.physics.sunysb.edu/rr/railroaddefinitions.html — This includes a glossary of railroad terms, such as FREDs, blue flags, bottling air.

- **Stone Railroad Switching:** http://www.fortnet.org/%7fdk/uprrhome.htm — This links to many railroad sites.

- **Track Warrants:** http://www.aimnet.com/~steves/n/twar/twmenu.htm — This is a personal Internet publication with information on some crashes.

*Penny Loeb can be reached at (202) 955-2640, or send e-mail to ploeb@usnews.com*

---

**The Federal Railroad Administration offers downloadable databases (in ASCII or dbase format), including railroad incidents and accidents, casualties, rail grade-crossing accidents and railroad operations, at gopher://gopher.dot.gov:70/11/fra/safety/rrsafety**

**NICAR offers a cleaned-up version of this data with additional documentation for $40 to $60, depending on size of news organization. Call (573) 882-0684 to order.**
