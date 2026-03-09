# Lobbying Lawmakers: 'Out to the Ball Game'

**By Kit Wagar**
*The Kansas City Star*

Missouri lawmakers are an avaricious lot. Many states prohibit or severely limit gifts from lobbyists on the premise that no one gives you something for nothing. But Missouri is one of 19 states that put no restrictions on lobbyists' gifts.

As a result, a spending spree surrounds every legislative session, feeding a culture that sees no conflict in conducting the public's business while on a corporate tab. The one nod the law makes to public interest is a requirement that lobbyists report their spending on individual lawmakers to the state Ethics Commission.

Though filled with loopholes, the monthly reports offer a glimpse at the gifts used to appease lawmakers: Cases of wine and beer. Tickets to see pop singer Alanis Morissette and tenor Luciano Pavarotti. Season passes to the St. Louis Cardinals. One lawmaker took $780 in tickets to the St. Louis Blues.

### Build a database

To get a handle on the extent of the spending, the *Star* built a database of all 3,438 gifts given to lawmakers during this year's 4 1/2-month session. The conclusion: A lobbying technique that began as a bit of clubby salesmanship has evolved into a legislature on the dole.

The analysis determined that lobbyists gave individual lawmakers gifts worth $139,219. That includes only one-on-one gifts and does not include the money spent on the constant stream of receptions, parties and meals for groups of legislators.

The top recipient personally received gifts worth $5,843, or nearly $1,300 a month. Only once during the entire session did he go a week without taking something.

The analysis also showed that:

- House Democrats took 63 percent of the gifts;
- 30 percent of the gifts involved tickets, lodging or transportation;
- One in four lawmakers took more than $1,000 in gifts;
- Three lawmakers received more than $1,000 in freebies from a single lobbyist.

The analysis was done using Excel 5.0 and FoxPro 2.6. The first problem was the volume of the gifts, which are listed only in handwritten reports. The newspaper hired two people to enter the early data, but interns and reporters had to finish it.

### Start with Excel

The resulting spreadsheet listed the lawmaker, his or her title and party, the lobbyist, the date of the transaction and a description of the gift and its value. The biggest weakness in the data was the way lobbyists described their gifts. While some lobbyists listed "beverages," other lobbyists listed the same gift as "food and/or beverages." Others combined freebies, describing them as "tickets/parking/meal."

I used Excel's Filter command — the Extract command in earlier versions — to divide the gifts into different categories, and pasted them into other spreadsheets in the same workbook. I eventually combined them into five general categories: food & drink; tickets; lodging, transportation and entertainment; gifts; and all other. I then went through each category to eliminate redundancies. Gifts described as two things were picked up twice, others three times. To eliminate those, I sorted the spreadsheets by lawmaker, date and amount so the same records would be in adjacent rows. I then used a logical function to find rows that exactly matched the row next to it.

### Move to FoxPro

After eliminating the redundant records, I saved each of those spreadsheets and the master list in Excel 4.0. Then I imported them into FoxPro databases. That allowed me to total all the gifts by lawmaker, lobbyist, party, chamber or date. The biggest expenditures were on the first day of the session; many of the other big days came in the last three weeks of the session.

One thorny problem was revisions in the records. State law allows lawmakers to have the record of the gift expunged if they dispute the expenditure or repay the lobbyist. The paper began building the database in March. By May, a few dozen gifts were no longer listed in the records. We decided to base the articles on the final versions.

One representative, for example, had taken his family on a lobbyist-paid, four-day vacation to Branson, Mo., in March. After he was interviewed about the trip in June, he repaid the lobbyist, so the trip was not listed on the final reports.

The entire project took a little more than three weeks – a week of data entry, three days to crunch the numbers and about eight days to report and write. *The Star* put the master database on its Web site so readers could call up the gifts each lawmaker received.

All the lobbyists and the recipients of large amounts insisted that the gifts had no effect on legislation. Then why, the biggest recipient was asked, do lobbyists spend all that money?

"What kind of stupid question is that?" he replied. "I'm not going to answer that. How would I know?"

*Kit Wagar can be reached by e-mail at kwagar@kcstar.com*
