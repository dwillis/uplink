# Data shows judges set suspects free

**By Joe Ellis and Brian Collister, *KMOL San Antonio***

Thousands of accused criminals in Bexar County, Texas, are off the hook because the county justice system couldn't get their cases to court fast enough.

We broke the story after four months of investigating, but fought more than a year for the data. No other news organization in San Antonio had investigated the Bexar County Court system with a database of its court records. And some county officials wanted to make sure we didn't either.

The battle began in December 2000. We asked for all Bexar County criminal court records to be provided electronically. We needed a complete database to see how judges run their courts.

At first, the county's Information Services Department quoted a $17,000 cost for our request, citing costly programming since there was no existing program for the job. After gathering advice from the NICAR-L listserv, researching the cost, and seeking help from the state's General Services Commission, we negotiated the cost down to about $2,000. But the county folks still dragged their feet.

Via the Texas Open Records Law, we monitored the correspondence between county officials regarding our request and bothered them constantly. Agreed deadlines for providing the data were not met. So finally, we contacted the company that set up the county's computer records system and hired one of its employees to write and run the program for $1,000. Within weeks, we had a "flat file" we imported into an Access database.

## Querying the data

Our first objective was to see how tough – or lenient – the criminal court judges were on crimes like DWI, drugs, assaults or sex offenses. However, when we looked at the "COURT DISPOSITION" field, we kept noticing cases "dismissed for lack of speedy trial." That got our attention. So we isolated all the "DSMD-SPEEDY TRIAL" cases, and we counted them by the "DISPOSITION YEAR" field we created from the "DISPOSITION DATE" field in the data table.

We noticed a dramatic increase from the 607 cases dismissed for "lack of a speedy trial" between 1996 and 1998 to the 5,200 cases dismissed for the same reason from 1999 to 2001. We decided to focus on the latter three-year period and filtered out those 5,200 records and put them in a separate table.

Through further querying we calculated how long these cases were on file. Some were 15, 10, and five years old. But it seemed strange that many would be less than two years, or even one year old. Law experts agreed.

We then started looking through hundreds of individual case files, looking for answers, and people to help with our story.

In those files we found victims like Virginia, who had been beaten by her husband once and had a restraining order against him when he assaulted her the second time.

She didn't know, until we told her, that a criminal court judge had thrown out the case against her now ex-husband because he didn't get a speedy trial.

A "count" query of the "OFFENSE DESCRIPTION" field of our data table, showed more than 400 other assault cases that didn't get to court fast enough.

We also found 734 DWI-related cases where the driver was never prosecuted, including the driver who hit Myrna Ellison.

"I assumed something was done," Ellison said.

Nothing was done, though. Even though it was the driver's second DWI arrest, Judge M'Liss Christian dismissed the case.

Christian wouldn't agree to an interview, but when we caught up with her outside the courthouse, she claimed the misdemeanor cases she was tossing didn't have victims.

The judge obviously never met Myrna and Virginia.

Overall, we found Judge Tim Johnson, a judge with 14 years on the bench, tossed out the most cases with 1,528 speedy trial dismissals. Fourth-year judge Al Alonso had 1,057 dismissals, followed by seventh-year judge Karen Crouch with 920, and Christian with 802 dismissals.

None of these judges would agree to an on-camera interview, but Johnson, sent a statement on behalf of all county court judges: "The cases dismissed in Bexar County are dismissed under appropriate circumstances with the proper procedures and are justified both by statutory and case law."

But we found the courthouse crisis unique to Bexar County.

We checked with the Office of Court Administration in Austin and its records show: Harris (Houston), Dallas (Dallas), and Travis (Austin) County Courts *combined* report only 129 cases dismissed for "lack of a speedy trial" over the past three fiscal years. Bexar County courts report dismissing close to 4,200 cases on speedy trial grounds over the same period.

## Tallying the cost

Courthouse sources explained that the judges had created a "speedy trial docket" in 1999, an aggressive dismissal procedure. On the docket, judges choose cases they want dismissed and assign them to attorneys who help get rid of them, sometimes hundreds at a time.

For taxpayers, we found another concern.

We obtained electronic payment records from the Bexar County Auditor's Office. This data details how much money each court-appointed attorney made in each court, case by case, for the past five years. With the "CASE NUMBER" field as the unique identifier, we matched the payment records with the speedy trial dismissals for the three-year period. We soon realized Bexar County Criminal Court judges were using thousands and thousands of dollars in public funds to get rid of cases never even heard in court.

By joining and comparing the court records data table and the attorney payment records table we discovered more than $100,000 in taxpayer money spent by judges appointing criminal cases on the "speedy trial docket." Christian was tops in this category, spending $28,076. Alonso spent $21,446, while Crouch spent $17,623 on appointed attorneys.

We found that basically the judges bypass the district attorney's office and handpick cases they want dismissed. They also handpick attorneys to help dismiss them. One lawyer, who asked not to be identified in our story, described the dismissal process.

Because of our investigation the county commissioners met to propose plans to stop judges from spending public funds dismissing cases and letting accused criminals go free. The commissioners created a task force to come up with some recommendations. The suggestions include: court coordinators and the County Warrants Division work together to make sure warrants are served; judges and the district attorney checking caseloads in criminal courts to make sure cases are heard in a timely manner; and fugitives being picked up when getting a marriage license, car registration, etc.
