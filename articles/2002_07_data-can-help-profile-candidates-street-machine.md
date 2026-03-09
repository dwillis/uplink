# Spotlight: Campaign Finance — Data can help profile a candidate's street machine

**By David Gulliver, *The Virginian-Pilot***

It goes like this: Millionaire decides to be politician, millionaire throws personal fortune into race, millionaire runs TV ads day and night.

Sometimes the millionaire still loses. Just ask Michael Huffington or Ross Perot — or Mark Warner. The cell phone mogul put $6 million of his money into a Senate run from Virginia in 1996. He lost.

Last year, Warner tried again — this time for Virginia's governor.

So by November, from Seinfeld at 7 to the news at 11 you'd see ads for Warner or his Republican opponent, Mark Earley.

And when Warner won in a state that hasn't gone Democratic since Doug Wilder in 1989, it was easy to figure he did it with just the ad blitz.

But we had a way to test it.

## Data resource

In Virginia, newspapers have a great resource, the Virginia Public Access Project (VPAP).

It began when Virginia newspapers teamed up to build a campaign contributions database for the 1997 elections. David Poole, a former reporter, runs the group.

Now, VPAP takes in candidates' electronic data, codes it, makes it available on the Web site *www.vpap.org* and (for subscribers) via downloads.

The database grows every year, in size and in detail. For example, the name and address of every person or business getting campaign money is listed. Date and reason for payment also are listed.

Poole pointed out those features in midsummer, as I was importing a first round of data. We checked it then and saw Warner paying a lot of people in two cities near our region.

I planned to look at our cities when the post-election reports arrived, in mid-December.

## Cleaning and querying

A look at what kind of organizations the candidates put into the field means getting a count of "street-level" employees. On paper, that's pretty simple — but we do this stuff on computers.

(For the record, I used SQL commands in Visual FoxPro 6.0 for most work, and exported tables to Excel to build charts.)

A field called "service," or the reason for payment, helped zero in on money for staffers. The campaigns did not respond to questions, so I had to develop criteria.

Earley, the Republican, coded most payments to field people as "Literature Drop/Flush" — as in "flushing the vote," like a hunter flushes game from the brush.

But about 100 entries were coded "Salary" or "Payroll." Some of the same people were coded under flush. Others were people who were first paid close to Election Day.

Those I counted as field employees. I excluded a handful of records — payments to a handful of top aides and to companies that managed his payroll. Warner's payroll was more complicated. He had two separate committees working to elect him, and had many employees multicoded — "Election Day Staff" and "Salary," for example.

I built his employee roster using the same criteria as I did for Earley. From there, it was simple to run queries to look at how each campaign built its operations.

Running a count of employees, overall and by city, let me compare the campaigns' staffing, statewide and by region.

Having the date of payment and date of report was important. I ran queries that gave me how many employees received their first payment by each report date.

That allowed comparing how many people worked for each candidate at specific mileposts during the campaign.

Finally, addresses with several employees with different last names might help find some possible mischief — for example, dummy addresses or businesses funneling money.

## Results showed surprises

The data let us debunk some myths about millionaires like Warner.

Warner didn't just win with ads. He built a massive street-level machine and outmanned his opponent in every way — city by city, and at every stage in the campaign.

By election day, he had almost 2,600 paid staff across the state — five times as many as the Republican. Warner spent $1.4 million on staff, more than double Earley's total.

Two months before the election, Warner had six times as many paid staff getting out his message. And in our region, Hampton Roads — also Earley's home turf — Warner still had twice as many paid staff.

That was to be expected. In October, a map showed more than 1,000 contributions from five cities to the two candidates. Warner received heavy support from traditional Republican turf like the Virginia Beach oceanfront — and even in Earley's home city, Chesapeake (bottom center of map; dots represent those who contributed to Warner, and triangles show Earley contributors).

Earley's aides said they had more unpaid volunteers than Warner — something impossible to test with the data — but admitted that Warner's paid army overwhelmed them.

One weakness was that previous data was not as detailed, so there was no way to compare "street-level" efforts in past campaigns. But professors, party bosses and ward leaders told us that there'd never been an effort like Warner's, and that Democrats seemed to have stolen the Republican playbook.

The last round of queries — looking for multiple-person addresses — paid off in an unexpected way.

The suspicious addresses turned out to be families with grandparents, parents, stepbrothers and sisters all under one roof.

And so it included a human angle — and some insider stuff too. The homeowner was a part-time teacher, who got a call from the teacher's union looking for volunteers. And so she, her parents and kids got paid to put brochures under windshield wipers after church for a few Sunday mornings.

## Lessons from the data

This data was unusually clean. The story took two-plus days for data work, and two-plus days of reporting, writing and editing. If your own data needs considerable cleaning, leave more time for cleanup and verification.

If you don't have such detailed data, use the campaign's overall salary spending and office space expenses to measure its get-out-the-vote effort.

*David Gulliver can be reached by e-mail at dgulliver@pilotonline.com*

---

### readme.txt — Resources

Tipsheet #1499 from the IRE Resource Center describes the Virginia Public Access Project's campaign finance data work. Members can obtain tipsheets at **www.ire.org/resourcecenter/**. Members and nonmembers can also obtain copies by calling 573-882-3364.
