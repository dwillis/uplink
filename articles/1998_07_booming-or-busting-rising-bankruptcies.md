# Booming or Busting? Rising Bankruptcies

**By Valerie Lilley**
*Peoria Journal Star*

The economy is booming and so are bankruptcy filings. What gives?

In a week-long series, we told readers everything about the Tri-County area's bankruptcy filings. Through computer-assisted reporting, we used numbers to show who the filers were, as well as the causes, losers and winners in the surge of filings.

Surprisingly, we found that most people who filed had been living below or near the poverty level. They weren't the rich – a popular misconception.

The oddest fact we found was that many filers listed the mail-order company Fingerhut, which made it to the top of the list of creditors. Bills were run up using cellular phones and charge cards at Bergners, a local, upscale department store.

Credit cards were the main cause of the bankruptcies. Medical debt trailed far behind.

## Incomplete Data

To gather these statistics, we had to build our own database because we couldn't find an existing database with complete information.

The U.S. Bankruptcy courthouse had PACER (Public Access to Court Electronic Records), but it didn't list all creditors. The Administrator of the Courts in Washington, D.C., didn't have a complete listing of case contents, either. The courthouse clerks and office manager didn't know of anything else.

We decided to collect the data ourselves. This was our first big dive into computer-assisted reporting, and naiveté drove it from a mini-project of a few months to a year-long study. Collecting the data took the most time in preparing the project.

The first lesson we learned is that mining data is not as easy as it looks. From 2,906 cases, we gleaned data such as: filers' names; ZIP codes; residential market value and money owed on it; car market value and money owed; attorneys; assets and liabilities; government support type and income; child support income and expense; income figures from the two years prior to filing up to the present; monthly expenses; and creditors and amounts owed them. (Some cases listed more than 200 creditors.)

Initially, another reporter and I went to the court house armed with laptops. For a week, case by case, we inputted the data in comma-delimited format. Both of us made multiple mistakes. By the end of the week, we only had 90 cases in our database. We ended up hiring someone to input for us.

Because of the time cases can take to close, we ended up using cases opened and closed between January, 1996, and February 1997.

To check for errors, we ranked by case number and by the minimum and maximum amounts in each column. The cleanliness of the database was also double-checked by a professor at Illinois Central College.

We used Excel to find the averages, sums, minimums, maximums, and the time each case took from open to close. To find how many filers owned a house, we ranked the database by the "residence market value" field and found where the cells dropped off to zero. Only 753 people owned a home. Its average value was $41,701.

## Tagging Along

We also used Visual FoxPro to find the top creditors, total credit card debt, total unsecured debt and total medical debt. To differentiate between credit cards and regular bank loans, identifiable credit cards were tagged with a "-C." We put a "-M" after doctor's names, physician offices, clinics, hospitals and other medicine-related creditors. We also wanted to know how much wasn't going to get paid back – total unsecured debt, which we clearly listed on a separate schedule in the files and tagged with a "-U."

To find the top creditors, I cut and pasted the creditor columns and the amounts into one super-long, two-column spreadsheet. To double check that I had gotten all of the creditors and amounts in the cut and paste process, I compared the sum to the sum in the original Excel spreadsheet. I imported the two-column spreadsheet into FoxPro and then used the "order by" and "group by" commands.

I used the same table to select the creditors and the amounts where the creditor had the "-C" for credit card. The "order by" and "group by" gave the top ten. I repeated this to find top unsecured creditors and medical debt.

The hardest part was finding out the average credit card debts per case because the "-C" tags were included with any "-U" and "-M" tags. I didn't know how to write a loop or what a scan/endscan was. Justin Mayo of NICAR worked out a program for us using a table with the creditors in the original block form.

## Handle Results with Care

We approached the data results in the same manner as a press release. I put the results in sentence format — it was as if we were reading the traditional government and commercial studies we were used to.

During weekly meetings, people threw out questions like "How many filers live with the city limits?" and "What's the median debt per case?" We made cheat sheets and used them as a starting point for reporting.

For example, Sears and CEFCU, a local credit union, were owed the most money — $2.9 million and $2.7 million respectively. Central Illinois Light Co. and Ameritech were also up there. I interviewed company executives and other spokespeople. They provided the story behind the numbers.

## Finding Real Voices

We talked to the people who filed. They were hard to find because most led transient lifestyles. We used the Journal Star's electronic library to get their personal information — we publish bankruptcies in "Matter of Record" along with divorces, marriages, births.

Getting people to talk about their filing was our biggest problem. Some didn't want to rehash old, sour memories. Others didn't want their names published in the newspaper — again. So we ended up with a mix of full names and first names only.

Organizing everything for our readers also challenged us. We had so much data that we could have easily bombarded them with stat-packed stories, covering a broad range. In our numerous weekly meetings, however, we had isolated specific elements of the bankruptcy phenomenon. These elements became the stories and sidebars of our week-long series.

---

*Valerie Lilley can be reached by e-mail at vlilley@pjstar.com or by phone at (309) 686-3260.*

**The week-long bankruptcy series focused on the following questions:**
- What are the elements of the bankruptcy dilemma in the Peoria area?
- What is bankruptcy? It is full of contradictions.
- What's the debate? Congress is grappling with the two sides of bankruptcy.
- What causes Peoria bankruptcies? Credit cards get much of the blame.
- Who loses in bankruptcies? We all do.
- Who wins? The business of bankruptcy is booming too.
- What can be done? A look at the possibilities.
