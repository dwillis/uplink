# Connections that pay off

## St. Louis Post reporters use computers to uncover scandal involving state worker's comp lawyers and Missouri Attorney General.

**By David Raziq, MICAR**

For years, few Missourians had heard of the state's Worker's Compensation Second Injury Fund. Created by a tax on insurance premiums, it gave workers the opportunity to sue the fund for extra disability when an on-the-job injury aggravated a previous injury or medical condition. The fund was created to ensure that workers got a square deal from worker's comp. However, by early 1992 some Missouri lawyers had voiced complaints about the way in which the fund was being administered.

"A couple of attorneys who had worked on the fund had been calling us for months," says reporter George Landau of the St. Louis Post-Dispatch. "They were disgusted with the way it worked."

And how it worked, claimed these attorneys, bordered on the illegal. Fifteen private lawyers had been hired by state Attorney General William Webster to defend the Second Injury Fund. However, Webster also allowed these lawyers to bring suit against the same fund on behalf of their own clients. Hence, these "Special Attorneys General" would negotiate settlements among themselves, one lawyer suing the fund one day while another lawyer would defend it. Later, they would switch roles.

In addition, the Post's sources claimed that these lawyers or their firms had made contributions to Webster's campaign for Governor. Hence, claimant's lawyers who had also contributed allegedly received better settlements for their clients.

After receiving the complaints, the Post launched an investigation and planned to use a computer to create a database that combined election contribution data with records from the second injury fund to support the allegations.

But, like many states, Missouri's state election contribution data is not computerized, but kept in a hardcopy format. State law also requires agencies to charge 50 cents per photocopy which can become prohibitively expensive.

However, foresight and a little serendipity nipped these problems in the bud. "Post reporter Terry Ganey and the capital bureau had campaigned for a few years for a database of campaign contributions," Landau said. So when the story came along, an office manager had already been typing the contribution reports into a Foxpro data entry program. Plus, the Post bought the reports in a microfilm format for five dollars per reel, with each reel containing two thousand pages.

"We were just lucky," says Landau, "because she had just finished the Webster campaign contributions from 1988 to 1991 when I got the second injury fund database from the Division of Worker's Comp."

Acquiring the database, which listed the names of attorneys filing claims, attorneys defending the fund and approving settlements, and the settlement amounts, was a difficult task. The Post team had to negotiate with the Attorney General's office for the tapes. At first the Attorney General's office gave the Post the runaround saying they didn't have the information the newspaper had requested.

Ganey, Landau, and the Post lawyers decided that it was time to give the bureaucrats an attitude adjustment. "This involved a lot of hassling and discussions between our attorney and the Attorney General's office." And five weeks later: "They finally agreed we were entitled to the electronic data."

On the nine-track tape Landau received was a "print-image" of a print-out the Post had previously acquired, with column headings and page numbers. "The data had the same position in each line of the file," says Landau, so he just edited out those lines containing the page-numbers and headings. The result: a fixed position ASCII document that he could now convert to Foxpro. It was time to get to work.

"The hard part of a project like this is matching names because they are spelled differently in each database," says Landau. "So I developed some little tricks." For example, the Second Injury database had dozens of attorneys with more than 20 cases, each with their names spelled differently from case to case. "So, what I would do," says Landau, "is sort the names alphabetically into a new table and the like-names would usually cluster. Once I was sure this cluster was the same person, I put a 'plus' in front of the first name-occurrence and a 'minus' in front of the last name-occurrence. Then I would write a program that replaces a new field in the original database with a consistent name, usually the first name in the cluster. So now everything was spelled consistently."

Landau says he applied this technique throughout the data, saving him "hours and hours of time." Then he wrote another Foxpro program that allowed him to link the record numbers in the Webster contributors database with the record numbers of the now consistently-named attorneys in the Second Injury database. Another program then went through both databases, looked at each record number, and aggregated all the contribution data for each lawyer into the 2nd Injury table. "That may be a complicated way to do it," says Landau, "but I wanted to end up with a single table that told the whole story."

However, Landau says it took more than a computer table to tell the story and praised his partner's reporting skills. "I did all the computer stuff but Terry Ganey did some really dynamite reporting by working her sources. And if it hadn't been for those sources saying how the fund worked, we wouldn't have had as clear an idea of what we were looking for."

Landau continues: "It can be hard to analyze a database and if you don't know what you're looking for the story won't jump out at you. That's obvious, but people can forget it when you do computer stories."

---

**The Post's Mission:** Prove that private lawyers hired by Missouri Attorney General William Webster to defend the state's second injury fund and lawyers who made contributions to Webster's campaign received better settlements than attorneys who did neither. Using computer tapes from the State Division of Worker's Compensation and a special state contribution database, the Post discovered:

| Attorney Category | Average Award |
|---|---|
| Attorneys who didn't contribute to Webster nor defended the fund | $3,548 |
| Attorneys who did contribute to Webster's campaign | $5,300 |
| Attorneys hired by Webster | $11,808 |
