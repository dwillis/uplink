# Errant Electioneering

**By Dan Keating**
*The Miami Herald*

When the election results for mayor of Miami came in on the night of Nov. 4, it seemed obvious that something strange had gone on in the voting, the first for the new "strong mayor" form of government that would give the city's chief executive a new level of power.

Incumbent Joe Carollo won a majority of the votes cast at the polls. But he was trounced by a 2-1 margin in absentee ballots by one of his challengers, former mayor Xavier Suarez. The absentee tide stopped Carollo 155 votes short of a outright election, forcing a runoff that he then lost.

The strange voting pattern and unprecedented number of absentees – more than 10 percent of the ballots cast – prompted Carollo, the Florida Department of Law Enforcement and *The Miami Herald* to launch investigations into what had gone on.

The Herald has tracked down and published more than 300 "problem" votes so far:

- A dead guy.
- People who don't live in the city or live in different city commission districts than where they voted.
- People who swore they didn't vote, despite a record showing a ballot cast in their names. Many said their names had been forged.
- People who said ballots were taken from them.
- People who said they were paid $10 to vote absentee.
- People who were solicited to vote by a former food stamp eligibility officer who still worked as a facilitator for elderly immigrants.
- People whose absentee ballots were "witnessed" by people who never saw the voter or by false signatures.
- More than 100 felons who had lost their civil right to vote.

Contacting more than 1,400 voters required a unique shoe-leather effort that lasted more than two months. But the project also involved a heavy dose of computer-assisted reporting to set the plate for the reporters fanning out into the community, organizing what they found and painting the emerging portrait of fraud.

The essence of the computer work – to find potentially suspicious activity – was matching different lists against the list of people who voted in the election. Though Florida law specifically forbids releasing the voting list to the public, *The Herald* obtained it.

With that voter roll, we could wrest great value out of the other public records that we keep on hand.

## Movers and Matchmakers

To start off, we matched the voter list against the Social Security Master Death List we had obtained from NICAR, though that list is somewhat spotty by having fields for ZIP codes but not full addresses. Since the voter list did not include a social security number, we had to match by name, date of birth and ZIP code. To broaden our search, we matched name and date of birth to anyone whose last ZIP code was in our county.

It looked exciting – we had eight exact matches. But, much to our disappointment, our field reporters found the purportedly dead voters quite alive and quite well: each proved that the rumors of their deaths had been greatly exaggerated. Most told tales of fighting with the Social Security bureaucracy about being listed as deceased.

(We learned from reporters around the country that such errors aren't at all unusual. And the one dead man we did identify didn't appear in the Master Death List.)

## Packed Voting Houses

Our next step was more straightforward. With the list of 44,000 voters, we simply grouped by address and sorted descending to find the addresses housing the most voters. Since addresses included apartment or unit numbers, the search aggregated individual living units rather than apartment buildings and showed many residences with six, seven, eight or more voters.

To make the list of voters per home more useful, we merged the addresses with the county's property appraiser roll, which we obtain each year for real estate analysis. Matching the addresses didn't go smoothly because the two agencies are inconsistent when it comes to "3 Ave." or "3rd Avenue," and "S.W. 29th Ter." or "SW 29 Terr."

Using SAS for Windows, we cleaned the addresses from both lists. We removed all punctuation and letters ("th," "st," and "rd") from the fields with numeric street names and scanned to replace variations of "ave," "avenue," "av," and so on.

Matching with the property roll allowed us to identify single-family homes with one or two bathrooms and more than five voters. It also showed us vacant and non-residential properties with voters. When we visited the properties with many voters, we found out-of-town and phantom voters stashed there.

To confirm that people lived elsewhere, we used driver's license and vehicle registration information through AutoTrak. We also used homestead exemptions, a tax deduction that can be taken only on your primary residence. We found people whose driver's license, vehicle registration and homestead records indicated that they lived outside the city. In every case, we spoke directly to the person or, if that was impossible, sent a letter asking for proof of being a legitimate voter.

## The Cell Bloc

One seemingly straightforward match proved tricky: matching voters with the list of people sentenced to state prison or probation in Florida. The list, available on CD-ROM from the state Department of Corrections, doesn't include those sentenced to time or probation locally, but it captures a good population of convicted felons, who have lost their right to vote.

Because the prison list doesn't have an address field and the voter roll doesn't have a social security number field, we matched by first name, last name, middle initial and date of birth for people convicted in our county or neighboring counties. Of the more than 400 matches, almost none were false matches caused by two people having identical names and birthdays. So it looked like we had a lot of illegal voters.

Complications arose when we checked court files for our first batch of interesting felons. Almost none, it turned out, had been convicted. Miami's overloaded court system is notorious for convicting rarely. Almost everyone can reach a plea agreement with "adjudication withheld." About three-quarters of the people sentenced to state probation had not been convicted. People who would probably be convicted elsewhere in the state and lose voting rights had not lost them in our county.

We accessed online the local criminal court docket to find which of the 400 offenders had been actually convicted. We determined that more than 130 had been, but the search still wasn't over. We ran those 130 names past the state's Executive Clemency Board that handles restoration of rights. Sorting through the index cards where they keep their records, we found more than 100 felon voters who did not have their rights restored.

We also compared the list of people who voted with the entire list of registered voters and looked for people who had changed addresses into the city or between city commission districts near the election. Under Florida's implementation of the motor-voter law, you can announce on election day that you've moved into the district. And you're allowed to vote.

## Available Absentees

Computer matching helped us draw webs of conspiracy involving the organizers of bad votes. A database of people who witnessed absentee ballots showed that many campaign workers witnessed dozens of ballots. If any witnessed ballots that we knew were bad, we checked other ballots handled by them.

We checked bad ballots against a database of campaign contributions and expenditures we had made from paper records for stories before the election. We found people who used their real, out-of-city address to contribute but an in-city address to vote.

Mapping uncovered the operation that paid people $10 to vote absentee in the runoff election. Using ArcView 3.01, we found participants and proved the scope of the operation being run from a parking lot in a poor neighborhood.

In that neighborhood, the primary election included the mayor's race and a contested city commission race involving a popular candidate.

People had months to obtain and fill out an absentee ballot for the election. In the runoff, voters had less than a week to obtain and return an absentee ballot. By mapping all absentees within three-quarters of a mile of the parking lot in both races, we discovered unlikely results: Dozens more absentees were in the runoff than in the main election. By comparing the list of voters from the two elections, we found people who had troubled themselves to vote absentee in the runoff but had not bothered to vote at all in the primary election. We targeted that list in our search for paid voters. Several confessed, and others admitted knowing of the operation but denied that they were personally involved.

## Maiden Intranet Voyage

To keep track of our contacts of more than 1,400 voters, reporters carried paper forms to collect consistent information. Results were then entered in an Access database. As the project progressed, the Access frontend was replaced by a Web-based version that christened our Intranet.

We used the Intranet to set up Web-based search forms so everyone could look up reporter notes on voter contacts. Reporters and editors could search lists of people who had voted or witnessed absentee ballots. Empowering team members to handle their own look-up chores was instantly popular and prevented a bottleneck at the geek's office.

After a three-week, non-jury trial, a judge in March overturned the election and called for a new vote. An appellate court then went a step further by putting Carollo back into office and declaring that the voting-fraud participants should be punished rather than simply forced to compete in another election.

The Florida Department of Law Enforcement has followed our tracks frequently, arresting the man we identified as running the paid-voter scam and several of the illegal voters we uncovered. More arrests are pending.

*The archive of stories from this project is available at www.herald.com/dade/archive/elect97/index.htm*

*Dan Keating can be reached at (305) 376-3476 or by e-mail at dkeating@herald.com*
