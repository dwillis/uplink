# Airport Insecurity

**By Jeff Porter**
*IRE/NICAR*

Most *Uplink* readers are true believers, knowing that CAR is a necessity, not a simple luxury, for serious news organizations. That point certainly came home when newsrooms struggled with data after terrorism struck in the U.S. Sept. 11.

In the aftermath of hijackers seizing four airlines and causing thousands of deaths, reporters began digging into the database of Federal Aviation Administration enforcement actions to find stories about the security of their local airports. The database includes lapses and violations of every level – from the passengers who innocently carries a knife to more serious security violations by airlines and airports.

Do the data prove conclusively that airport security should have prevented the attacks? No. Do the data provide potential starting points for reporters covering the security status of American air travel? Absolutely.

The IRE and NICAR data library, which provides the data to journalists, was deluged with telephone calls and data orders. During the weeks after the attacks, 119 news organizations purchased the data. IRE set up delivery via its FTP server. The database was on the library's regular schedule to be updated in October, so IRE pushed to update it even sooner. During the week of the attacks, a series of text files was obtained from the FAA, downloaded from the agency's public FTP server, and turned into a series of dBase IV files so journalists could use the data in almost any database program.

### Good timing

This turned out to be a good decision. After stories started appearing and reporters started asking questions, the FAA turned off the data spigot within a week after the attacks. The files could no longer be downloaded. It seems that the data was suddenly deemed "sensitive" by the agency that, since 1997, has provide copies of its Enforcement Information System database. At the time this was written, no one with the FAA would or could specify the concerns about the data, just the ominous message on its server: "The Enforcement Information System (EIS) is not available at this time due in part to security considerations. (14 CFR 191)" The federal regulation cited is fairly general, concerning "protection of sensitive security information."

Because of the FAA's refusal to answer questions, editors and reporters found interpreting the data daunting. Both the library and the NICAR-L e-mail discussion list agonized about trying to find answers about the complicated enforcement data. IRE members can look over that discussion at *http://www.ire.org/membership/listserv.html*. There are so many decisions to make on how to use the data – from deciding which types of violations are important to which airports or airlines to compare. But for example purposes, let's follow the path of a fictional news organization and how it reached the decisions it reached.

First, a primer: The FAA enforcement database, dating back to 1962, includes four tables of information. The "main" table contains most of it, including the dates, often the violator's name and the location. A table called "security" lists lapses or violations, often with cryptic descriptions. Table "far4" cites the specific federal regulation violated, while a table called "actions" lists the outcome of cases, from warning letters to "proposed civil penalties" in dollars.

**The FAA, of course, refused to explain the criteria of placing cases in the security table.**

One technical problem – and the first decision to make – involves the duplicate records in the last three tables. The security table, for example, might list several violations involving the same case. Some news organizations wanted to simply count events, not necessarily adding up all the violations in the same case.

### Using "distinct"

So, many CAR followers learned a technique using the DISTINCT function, an SQL statement that omits duplicated data. Since most of the questions came from Microsoft Access users, here's the Access query language that our fictional newsroom used to make a new table with one record per case identification number:

```
SELECT DISTINCT iid into cases
FROM SECURITY
```

The query simply created a new table with just id numbers, naming the new table "cases." An Access user could easily add a WHERE line to focus on certain security codes or descriptions, filtering for just some, not all, security cases.

But what to filter? Security matters are touched on in both the main and security tables. The main table includes a field called CAT_CODE, which specifies the type of violation, in broad terms, such as "security." The security table includes both descriptive and code fields that can be more specific about security violations. For example, security codes that begin with an "M" apparently deal with passengers or non-passengers carrying weapons. Security codes that begin with "C" often deal with failures of security personnel, often in connection with FAA inspections or surveillance.

### Security problem

The problem is, though, the security table includes records that link to cases in the main table that aren't coded as "security" cases. Some hazmat cases, for example, were included in the table supposedly dealing with security lapses or violations. There's another CAT_CODE dealing with "cargo security" instead of just plain "security." The FAA, of course, refused to explain the criteria of placing cases in the security table. The NICAR-L e-mail discussion list debated which fields to rely on. Some suggested including all the security table records; others were comfortable using the CAT_CODE to filter for only "security" violations.

Beyond that very basic filter, though, newsrooms dealt with further filtering. Do they want to look at only violations when the airports or airlines are blamed? And if so, do they include only certain violations, such as failing to detect a firearm, or include a wider variety of violations? Should they factor in the passenger violations as well?

Again, editorial decisions had to be made.

Our made-up newsroom decided to look at only violations by airports or airlines, and filtering by the types of violations in the security table – beginning with the letter "C" in the security table's SEC_CODE field. So we re-created our "cases" table, filtering through SEC_CODE:

```
SELECT distinct iid into cases
FROM security
WHERE SEC_CODE like 'C*'
```

The work is partially done, though. Now, we could filter out all the cases in our main table with some additional filtering criteria.
