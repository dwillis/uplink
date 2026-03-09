# Repaying Tickets in Boston

## Lessons from parking database never expire

**By David Armstrong**
*The Boston Globe*

Parking in Boston is often compared to a trip to the dentist: It can be painful and expensive. The city of Boston, not unlike scores of other cities across the country, dispatches meter maids to aggressively prowl the clogged city streets and hand out thousands of parking tickets each day.

Since everybody hates parking tickets, the *Boston Herald* (where I used to work) decided a year ago to request a copy of the city's parking ticket database. We had a number of stories in mind when requesting the database. We wanted to know what areas of the city were ticketed most frequently, which areas were avoided by ticket writers and why, who were the scofflaws and who was having their tickets dismissed or taken care of.

The database of 3.5 million records on 26 9-track tapes proved helpful for those ideas and more.

In fact, the most surprising information on the database was something we had never considered. The city had collected more than $2 million in *overpayments* from unwitting parking violators. This information proved to be wildly popular with the motoring public.

The newspaper published a list of those companies and individuals owed the most money by the city because of overpayments. The overpayments were the result of errors by the city in recording license plate numbers, overlapping overdue notices and poor bookkeeping by parking violators who paid for the same ticket twice.

Embarrassed parking officials were forced to admit they knew about the overpayments for years, but did nothing to return the money. The same officials set up a hotline to refund the money after the story appeared.

The mayor ordered that printouts of the 60,000 companies and individuals owed money for overpayments be placed in every city library for public inspection. Two months after the first story was published, the city had returned $1 million to parking violators.

The database provided by the city of Boston actually came from a city vendor - Lockheed Information Services. Lockheed maintains the same records for many large and midsize cities across the country.

The database has fields indicating the location of the ticket, who wrote it, the amount, the amount of overdue charges, whether or not the ticket was dismissed, the registration number of the ticketed vehicle and more.

The size of the file - 1.7 gigabytes - presented some problems. The data was analyzed on a Gateway 486 PC with an 800 megabyte hard drive. Using Nine-track Express, I heavily filtered the data to bring in only the information I absolutely needed.

Using FoxPro, I would look at 300 to 400 megabyte chunks. For instance, when looking at who had tickets dismissed, I brought in only the fields for dismissal, name, amount, location and date. This cut the record length more than 70 percent. The hardest part of this endeavor, it turned out, was getting the tapes in the first place (see sidebar).

Spending three weeks analyzing and playing with the data also drove home another point: Reporters should always do their own computer work, even if it is with the assistance of a more experienced or skilled programmer. Several story ideas were born from the long and often painful task of learning the database and attempting to analyze it.

In addition to the discovery that tens of thousands of motorists were overpaying the city for tickets, here are some of the other stories that resulted from analyzing the database:

— The police officer assigned to drive former Mayor Raymond Flynn had every parking ticket issued to his personal car, a 1987 Jaguar, dismissed. The tickets totalled $355.

— Widely hated meter maids, who endure the curses and shouts of angry ticket recipients, are major money makers for the city. We found one meter maid had written 15,210 tickets totalling $516,000 in just one year of work. The same meter maid was paid $433 a week for her work.

— We were able to produce a chart showing readers the 40 locations in Boston that would most likely result in your car getting a ticket.

— Rental car companies were the biggest scofflaws in the city. Two companies owed the city a combined $1 million for parking tickets amassed by rental drivers who never paid up.

*David Armstrong moved from The Herald to The Globe in 1994. He can be reached at 617-929-2539 or through e-mail at armstr@news.globe.com.*

---

### A Lesson on Obtaining Data

It took three years for the Boston Herald to obtain a copy of the city's parking ticket database on 9-track tapes.

The city only complied with the request when it was threatened with legal action by the state attorney general, who is charged with enforcing the state's public records law.

In repeatedly rejecting the *Herald's* request, the city maintained it had the right to decide the form of any response to a public records request. In that vein, the city offered to provide the parking records in paper form at great cost to the newspaper. The state's public records law, which is modeled after the federal FOIA, does not provide government agencies the option of responding this way.

Until recently, the city of Boston uniformly refused to comply with any requests for records in electronic form. In most of these cases, the city would offer a mile-long printout of paper as an alternative. In fact, city workers once delivered boxes of documents to the Herald newsroom after a reporter specifically requested the information on 9-track tape.

It should be noted that the city's top computer manager also served as the mayor's pollster. That combination of computer knowledge and political savvy may explain the city's reluctance to help the media and others gain access to computerized records.

*— David Armstrong*
