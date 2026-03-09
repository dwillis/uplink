# Debunking some myths about speeders

By Holly Whisenhunt Stephen, *WOAI-San Antonio*

My first computer-assisted reporting story started shortly after I arrived at WOAI last year. The data involved more than 1.6 million municipal court records from Bexar County, Texas. The investigative producer I was replacing had already put the wheels in motion to get the data. It took some time to convince the court system what information was public. I'm told there was some grappling over obtaining the information, but it wasn't the biggest fight either. I picked up the data, which cost a couple hundred dollars, a few weeks after I started the new job.

During an IRE and NICAR Boot Camp, I learned to always make copies and never work with the original data. So, after loading the information, I put the disks in a safe place where they wouldn't get back into the mix. We received 10 years of data on a CD-ROM that had 12 comma-delimited text tables. I imported the data into Microsoft Access, making sure to bring all the fields in as text, and later changed the number fields in Access table design view.

When I imported the data, I selected the advanced options and created specifications to control the importing of the data. This was very helpful and saved lots of time when it came to importing the remaining tables, which had the same fields and same data types. The one point I cannot stress enough is to make sure the specifications are absolutely correct, or the resulting data table will be a mess, and you'll have to clean it up or repeat the import.

After importing each table, I checked to make sure all records were imported properly. Then I performed an append query to create tables with more than one year of data and joined all other tables. Before that I tallied the total number of records in the individual tables, so I could check whether the append query was successful. Each record represented a case in municipal court.

The municipal court data table contained 85 fields. The complaint description field was very helpful because it told us what the actual violation was. Other helpful fields included the violation date, time and location. The data also contained the officer's name and badge number, which made it easy to find out how many tickets an officer issued. We analyzed five years worth of data. The information contained several violations ranging from disorderly conduct to wasting water. We chose to focus on speeding, and ended up with more than 400,000 records that I merged into one table.

To separate the information, I queried the complaint description field. Because there are several different variations for speeding, I used the "*" wildcard in my Structured Query Language (SQL) WHERE statement to make sure all speeding violations were included in the query. After isolating the information, I performed a make-table query, so I would be working with a smaller table containing the data I needed.

This first project taught me the important steps of cleaning data, so it can be analyzed more easily. I performed several counts including how many tickets were written for speeding and speeding in a school zone. We wanted to find out where the most tickets were issued in the city. To accomplish this I needed the street address of the violation in one field, which was originally spread over four. I concatenated the contents of the four fields into a new one using SQL.

I must admit this is one of my favorite tricks because it seems like a huge task to accomplish, but with concatenating it's easy. Before doing this I made a new field called speeding1.fulladd to hold the new addresses.

Here is the SQL I used:

```sql
UPDATE speeding1 SET
speeding1.fulladd = trim
([speeding1].[new vioblk1] & " " &
[speeding1].[new vioblk2] & " " &
[speeding1].[vio street1] & " " &
[speeding1].[vio street2]);
```

After concatenating the addresses, I was able to get a better look at traffic-ticket patterns. I ran queries to group by address and count the number of times each appeared in the data. I chose not to change the names of all streets and highways. For instance, Highway 281 @ Bitters Road was also listed as Hwy 281 @ Bitters Rd. I decided that standardizing all of the addresses would be too time consuming.

Instead, I chose to use Access and an Excel spreadsheet to get an estimate of how many tickets were issued at specific locations. I queried the data in Access to show the streets and the count of accidents for each. I ordered the results in descending order so the streets with the highest number of accidents appeared at the top.

Then I noted the top streets and did another query to get the records for those streets. I put the records for each street into its own Excel worksheet and worked with the data there.

Although it was not scientific, we were able to estimate ticket locations and counts. We chose to publish the speeding sites where more than 1,000 tickets were issued in the San Antonio area.

Another thing we wanted to know was the average amount of time that passed from when a ticket was issued until it was resolved. I created a new field to hold the calculated times and ran an update query that inserted the number of days, as calculated using the violation and adjudication dates. Here is the SQL:

```sql
UPDATE speeding1 SET ADJTIME =
INT(([NEWADJ DATE]-[NEW VIO
DATE])/1)
WHERE [NEW VIO DATE] IS NOT NULL
OR [NEWADJ DATE] IS NOT NULL;
```

We were able to look at the data and determine some of the common "myths" linked with speeding tickets – for instance, that red vehicles are ticketed most often – weren't true in San Antonio.

Other fun facts we were able to find in this data:

- The officer who issued the most tickets and what time of day most tickets were issued. The prime time was 3 pm. A judge stated that's when people are picking up kids from school and maybe shift workers are leaving for home.
- A monthly breakdown when most tickets are issued. We found the dates with the most tickets were at the beginning of the month (the 3rd, 2nd, and 6th). The reason this was surprising is most drivers talk about and assume that officers strive to meet quotas at the end of the month and write more tickets then.
- The average age of drivers who get tickets: 31.
- The average speed over the posted limit that results in a ticket: 17 mph.
- The amount of tickets dismissed because officers did not show up for court or did not remember the traffic stop: 3 percent of all speeding tickets.
- The color vehicle received most tickets. We ran into some difficulties with this because not all records indicated the color of the vehicle. The Texas Department of Transportation does not record vehicle color on car titles because those colors can change. So we could only report on those who records included the data. White vehicles were the most-often ticketed.

Overall this was a great database to work on after Boot Camp. Many of the lessons I learned during the Boot Camp helped me to clean and analyze the data. The best advice was to be methodical and not overwhelmed by the volume of data. My advice to others is take your time, concentrate and understand what you are trying to accomplish before you start trudging through steps that might not be helpful.

As far as SQL goes, I now know it is impossible to learn everything you think you should know at Boot Camp. I started compiling a list of SQL statements and what they can accomplish. I find this to be very helpful when working on different data that has similar challenges. Another great resource is the NICAR-L listserv, where journalists doing CAR assist each other. Whenever I've had any questions (especially on deadline) I just post it online and usually receive several answers.

Contact Holly Whisenhunt Stephen by e-mail at HollyWhisenhunt@woai.com.
