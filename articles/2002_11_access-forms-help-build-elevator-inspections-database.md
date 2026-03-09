# Access forms help build inspections database

**By Mike Sherry, *CQ Weekly***

Elevators have become as much a part of everyday life as cars.

But while journalists investigate many facets of vehicle safety, such as fatal accidents and faulty equipment, there is precious little reporting about elevators – even though they carry millions of people every year.

So, when I came across the Missouri Elevator Safety Board on the state Web site, it piqued my interest. If the state was worried enough about elevator safety to appoint a board to oversee it, then perhaps a story was there.

The result was a computer-assisted reporting story – written as part of my master's degree final project at the University of Missouri School of Journalism – that ran July 7 in the *St. Louis Post-Dispatch*. Given that the United States has an estimated 700,000 elevators, this is a story that can be replicated in just about any community.

Some of the unique challenges of this story forced me to learn important CAR lessons that others can benefit from.

## Designing databases

Using Access 97 and Access 2000, I grappled with database design for a relatively small database. It had many tables, but the largest one only had about 20,000 records. Everyone needs to think about database design when information must be entered from paper records.

The state Elevator Safety Unit had an extensive Access database that included a lot of data, such as inspection dates and elevator locations. But the unit was so understaffed that the staff had no time to enter all the violations uncovered by inspectors. The violations were detailed in color-coded folders (with a different color for every month) that contained more than 10,000 reports. I took a random sample of about 260 reports that had an average of about four violations. This gave me a good idea of the types of problems inspectors found.

Next, I created an Access form for data entry using a Tech Tip in the April 2000 *Uplink* as a guide. (*Uplink* articles from 1990 to the present are available to IRE members at *www.ire.org/resourcecenter.*)

The problem, however, was that inspectors did not record violations consistently. Some inspectors referenced particular sections of the code book, some just jotted down notes, and some did both. I needed consistency, however, so I could use Access to group by and count the records to identify the most common violations.

## Learning lookups

So I created a lookup table, where I coded each type of violation with a number. For instance, machine room door problems got a code of "3." I linked my data-entry form to that table, which gave me a drop down menu each time I needed to enter a particular violation.

After running the queries, I found that many elevators had serious problems like broken phones. Machine room doors that didn't close and lock on their own were also hazards because someone could walk in and be hurt or damage equipment that could harm passengers. This was the first time anyone – including agency staff – evaluated the seriousness of the problems.

Setting up the violation codes solved one quandary, but another remained: how to link the violations table with the activity table that the Elevator Safety Unit had created to keep track of inspection dates and other information.

Each elevator had a unique state ID number, which I entered in my violations table. The problem, however, was that each elevator often appeared more than once in the activity table – mainly because the state entered a record when that elevator was registered, then created separate records for the subsequent inspections. Meanwhile, each one of my violation records included the equipment ID, so if an elevator had four violations, that ID would be in four records. I needed to modify the tables so I could avoid a many-to-many join.

I needed a unique identifier to identify each inspection, so I created one in both tables. Then I ran update queries that combined the equipment ID with the inspection date.

Creating a violation code table and unique IDs may seem like old hat to CAR veterans, but for people like me – who have not built a lot of databases – these were good skills to learn. They apply to any sort of story that requires building a database or guarding against many-to-many joins.

## Finding the story

But what about the story? I found an agency that was underfunded and understaffed. The database analysis showed that the state had inspected only about 40 percent of the elevators in Missouri, even though the program was created nearly a decade ago. Additionally, of those that were inspected, about 13 percent went more than year before they were reinspected – letting potentially harmful deficiencies persist.

**The database analysis showed that the state had inspected only 40 percent of the elevators in Missouri.**

States handle elevator inspections differently. Some make this a state function while others leave it up to municipalities. No matter who is doing it, you will probably find an agency that lacks the manpower to thoroughly inspect elevators annually. Getting a sense of the inspection budget and inspection staff is a starting point for this story.

Additionally, plan on reading lots of lawsuits – in both state and federal courts. It's a good bet that the enforcement agency lacks great information on accidents, but lawsuits against elevator companies are a treasure trove.

Contact Mike Sherry, a former data analyst in the IRE and NICAR database library and now a reporter for *CQ Weekly* by e-mail at MSherry@cq.com

---

## readme.txt

Mike Sherry's story about elevator safety can be ordered from the IRE Resource Center. Call 573-882-3364 or e-mail rescntr@nicar.org and ask for Story No. 19663.

Missouri's state auditor released a report in November finding that the Division of Fire Safety has not established procedures to identify unregistered elevators and to report registration violations for enforcement. See the report at *www.auditor.state.mo.us/press/2002-110.htm.*

A three-part Boston Globe series examined declining safety standards for elevators and escalators in Massachusetts and in the rest of the nation. The Globe reported that lax inspection standards and a lack of federal supervision helped result in an alarming frequency of crippling accidents and death. The investigation prompted one public official in charge of elevator safety to resign, and spurred the Massachusetts Public Safety Commissioner to order an overhaul of the inspection system. (Story No. 11001)

The IRE Resource Center provides stories and tipsheets to journalists. Search the story and tipsheet databases at *www.ire.org/resourcecenter.* Call 573-882-3364 or e-mail rescntr@nicar.org to order copies.
