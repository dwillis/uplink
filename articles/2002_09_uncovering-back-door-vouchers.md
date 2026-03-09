# Uncovering "back-door vouchers"

By James E. Wilkerson, *The* (Allentown, Pa.) *Morning Call*

Late last year, the superintendent of schools for the Roman Catholic Diocese of Allentown, Pa., told our education reporter Nancy Averett that the schools had received more than $600,000 in tuition donations from local businesses under a new state tax-credit program.

She already knew about the program, but was surprised by the amount going to one diocese. Dubbed "back-door vouchers" by critics, the scholarship tax credits were clearly funneling a lot of tax dollars to private, nonprofit schools. So Nancy came to me wondering if we could find out exactly how much.

Program administrators with the state Department of Community and Economic Development said they didn't know. In fact, there was a lot about the donations they didn't know. So we ended up having to build our own database, one that allowed us to show how millions of dollars in tax money was being funneled to religious schools with very little supervision or follow-up from the state.

The program, started in early 2001, gives businesses up to 90 percent state tax credit for money they donate to nonprofit organizations, which then distribute the money to students for tuition. Unlike full-blown vouchers, voted down in the state legislature three times in recent years, supporters emphasized that the tax credit took no money directly from public school funds.

That argument seemed a little flimsy to us, however. The program diverted money away from the state coffers, money that could have easily gone to education. And, we suspected, most of that money went to private religious schools. In past legislative sessions, the potential of public money aiding private religious schools had triggered vehement opposition.

## Background research

To do the job right, we had to examine more than 100 organizations approved by the state to receive scholarship money.

That's where the computer-assisted reporting work started. Nancy was familiar with Access, so I created an easy-to-use database that we could both use whenever our schedules allowed. Using the Forms Wizard, I created a simple data entry form that included the organization's name and other basic information, and provided space for us to add research notes, Web sites and other information we found.

The state had lists of approved organizations on its Web site, including address, contact information and Web address. I copied those into a powerful text editor, UltraEdit, (available at *www.ultraedit.com*) and designed macros that parsed the five rows of data for each organization into a fixed-width text file that I later imported into Access. I added the fields from the table we had created in Access and we were ready to roll.

We relied almost exclusively on the Internet, Lexis-Nexis and our own newspaper archive for researching the organizations. Especially useful was GuideStar (*www.guidestar.com*), a database containing the financial disclosure forms (Form 990) that nonprofit organizations are supposed to file annually with the Internal Revenue Service. In some cases we were unable to find information about an organization elsewhere, but the 990s on GuideStar provided details about how the groups were distributing money.

## Merging data

Within three weeks or so we had finished the bulk of our research. By that time, the state had given us a list of contributing businesses and the donation amounts that went to the nonprofits.

Unfortunately, the data was in two files, with the business name and address information in Word and the donation amounts in Excel. I converted the Word document into a text file and again used UltraEdit to convert the information into columns and rows. Once that was completed, I imported the fixed-width text and Excel files into Access and merged them into one table.

Fortunately, with few exceptions, the nonprofit names were the same in all of the documents I was using. That allowed me to join on the name field with little clean-up.

When it came time to produce numbers, I had whittled the data down to two tables: Our research table, which included data about the organizations receiving money, and the business and donation table.

## Tallying results

I used SQL Server for my analysis, but the work could have just as easily been done in Access or any other database program. I joined the two tables on the organization name field and ran some simple Group By queries to look at the distribution of the donations.

In the end, we found that more than half of the $17 million in donations had gone to scholarship organizations that primarily benefited religious schools. Looking only at scholarship organizations, about 75 percent of donations had gone to religious schools.

After running our findings by state officials and finding out that they had higher totals, we realized that we were missing some data. We put the story on hold until the year-end data became available in April. However, in the following weeks we kept plugging away at organization research and updated other data. When the final data became available we were ready to start writing.

Though the total contribution tally had climbed to about $30 million, the share of scholarship contributions going to religious organizations held steady, at about 75 percent, so our story did not change drastically during the delay.

Our final story, which ran Aug. 4, showed not only that the lion's share of money was going to religious groups, but that the state was doing very little to track how the money was being used.

In fact, interviews with administrators at some of top contribution-getters in the state showed that much of the money was being distributed to students already in private schools, undermining the state's claim that needy students in poorly performing public districts were being targeted.

Along with the story, I built a Web lookup tool that allows readers a look at contribution lists. The story and query are available at *www.mcall.com/all-a1_5voucheraug04.story*

*James E. Wilkerson can be reached by e-mail at james.wilkerson@mcall.com*

---

**Pennsylvania Nonprofits Ordered by Total Contributions**

| # | Organization | Type | City | State | Total |
|---|---|---|---|---|---|
| 1 | Scholastic Opportunity Scholarship Fund (SOS) | SO | Pittsburgh | PA | $1,982,864 |
| 2 | The Mennonite Foundation, Inc. | SO | Goshen | IN | $1,200,053 |
| 3 | Business Leadership Organized for Catholic Schools (BLOCS) | SO | Philadelphia | PA | $1,152,090 |
| 4 | Diocese of Scranton Scholarship Foundation | SO | Scranton | PA | $1,142,977 |
| 5 | Henkels Foundation | SO | Blue Bell | PA | $776,499 |
| 6 | Neumann Scholarship Foundation | SO | Harrisburg | PA | $718,386 |
| 7 | Eastern Pennsylvania Scholarship Foundation | SO | Allentown | PA | $682,840 |
| 8 | Pittsburgh Jewish Educational Improvement Foundation | EIO | Pittsburgh | PA | $623,622 |
| 9 | Philadelphia Youth Network, Inc. | EIO | Philadelphia | PA | $621,736 |
| 10 | STAR Foundation | SO | Erie | PA | $582,455 |
| 11 | Foundation for Jewish Day Schools of Greater Philadelphia | SO | Philadelphia | PA | $517,796 |
| 12 | Abington Friends School | SO | Jenkintown | PA | $462,000 |
| 13 | Junior Achievement of South West PA | EIO | Warrendale | PA | $452,083 |
