# Write the Flipping Story!

**By Dan Browning**
*Star Tribune*

*Browning provided this handout at the 1999 NICAR National Computer-Assisted Reporting Conference in Boston.*

You'll probably never hear an editor yell that across a newsroom. Too bad. Across the United States, speculators are engaging in real estate scams called "flipping" as fast as they can. It's an old gambit. You've probably seen motivational programs on the practice on late-night TV: "Buy property with no money down! Get rich using other people's money!"

In short, flipping is the practice of buying property and turning it around quickly for a large increase in value. It's not inherently illegal. But it often is.

In an illegal flip, a speculator must find an appraiser to inflate the value of a house so that a lender will advance a mortgage that is not supported by the property's true market value. The speculator then buys the property near or below its true market value and re-sells it, either to a dupe or to a straw buyer, who finances the transaction with the loan. The purchase and resale often take place the same day.

Sophisticated power-brokers refined the scam during the S & L crisis. They flipped commercial properties and entire planned communities. Now, schemers are at work in poor neighborhoods in the nation's cities. A handful of reporters have documented flipping schemes in New Jersey, Maryland, Florida, Wisconsin and Minnesota. It's undoubtedly more widespread.

### Equity skimming and surfing

The latest flipping schemes are intriguing. Investigators have discovered fake financial records, forgeries, misrepresentation of ownership and many other ploys. Authorities suspect some flippers of laundering drug money through the purchase and resale of these homes.

When straw buyers are involved – that is, when the buyer is working with the seller, usually for a fee – equity skimming is often found. That's where the buyer rents out the property but fails to pay the mortgage. The buyer keeps the rents as the property winds through the foreclosure process, which can take up to 18 months in a state like Minnesota. By the time the authorities uncover the scam, the flippers may be long gone.

Who suffers? Entire neighborhoods may be overassessed because of the artificial inflation of property values. Unsophisticated buyers end up in foreclosure, their credit wrecked and their eligibility for first-time home-buying programs forever lost. Buildings get boarded up and condemned. Municipal utility bills go unpaid. Lenders get stuck with properties they can't sell. And they must reimburse investors who bought securities backed by these fraudulently obtained mortgages. Shareholders in the mortgage companies therefore get less return on their investments. Lenders, feeling burned, then shy away from poorer neighborhoods.

### Dealers deduced

How do you uncover property flips? It's easier than you might think.

In 1996, when I worked at the *Saint Paul Pioneer Press,* I wrote about property flips involving one well-connected speculator. A source told me that the speculator had bragged that he was putting people into business around the country, and no one would ever catch him. Two years later, I discovered that several of his associates or acquaintances had indeed gone into business.

I was following one of his associates closely. Based on a tip, I pulled his property transactions. But I found far fewer deals than I expected. The reason? Dirty data. I'd type in the name of his company, but the data entry at the county was so poor that I missed many of the deals. Later, I discovered that he used several corporations to do the deals. I talked with local assessors and found that I could buy data documenting property sales, called "certificates of real estate value" (CRV).

In Minnesota, as in most places nowadays, a buyer must file these documents attesting to the date of the sale, the buyer, the seller, the property identification number, the purchase price and the nature of the financing, among other things. I pulled a bunch of hard copies and found that most of the time, the buyer, seller, sales date, PIN and purchase price were accurate. Most everything else on the forms were unreliable.

The assessor gave me (at no charge) the database of CRVs from 1995 through March 1998. I used FoxPro to assign a transaction number on each sequential sale for a property and to clean up the names of the buyers and sellers. I had 6,575 transactions on 3,079 Minneapolis properties. Of those, 2,148 sold more than once, for a total of 4,170 transactions. Knowing that flips occur rapidly and for significant increases in value, I calculated the number of days between each repeat sale, and the percent change in value. Because many of the transactions took place on the same day, I couldn't say whether the percent change was positive or negative. So I decided to ignore the sign (plus/minus) of the percent change.

I decided to examine deals that took place in less than 45 days for greater than a 50 percent change in value. I brought everything into Access to count the number of transactions each buyer and seller made. Then I took the list of major traders and ran the corporate names through the Secretary of State's Office to find out who was behind the corporations. I called this my AKA list. Then I pulled every single deal these heavy traders made, regardless of whether it appeared to be a flip or not.

If a high percentage of the speculators' deals resembled flips, I copied their names to a short list. By contrast, if a small percentage fit the pattern of a flip, I decided to ignore them. Once my short list was built, I recounted the number of transactions these speculators had completed, both in terms of purchases and sales. Then I went to the courthouse and pulled the paper records: mortgage information, title transfers, etc. That was the hard part. It took about two months and cost me about $500 to copy these property records.

### Widespread speculators, scarce licenses

Minnesota requires anyone who makes five or more trades in property in a 12-month period to get a "limited broker's license." I took my data to the Minnesota Commerce Department and asked which of my speculators were unlicensed. The department was investigating flip sales on its own. But my database revealed that the practice was far more widespread than they had believed. They expanded their investigation. The department revealed that the FBI also was investigating.

The commerce department, concerned that the media would ignore the problem, planned a press conference. The *Pioneer Press* ran my story on flips to head that off. The *Star Tribune* followed with several stories of its own. One showed that flips can take place even when the speculator holds the property and rehabilitates it.

I later moved to the *Star Tribune.* In February, I wrote a story about the first criminal indictment here, which charged five people with conspiracy, mail fraud, bank fraud and various money laundering charges. I also noted three major civil suits filed by WMC Mortgage Corp. against 23 people and 30 business entities. My colleagues published follow-ups showing the human pain these practices can wreak. A sidebar showed how Norwest Mortgage, the nation's largest residential lender, lobbied the U.S. Attorney's Office to bring the criminal indictment. That case involved one of the lender's former mortgage brokers. So far, the state has disciplined six license holders and has targeted a total of 50 for closer scrutiny. Two FBI investigations are moving forward. The criminal division of the IRS is reportedly investigating, as is the state attorney general's office.

I'd be remiss if I failed to mention the great work done on flipping stories by the *Milwaukee Journal* and the *Asbury Park Press* in the past two years.

But I'd also be neglecting this opportunity if I failed to point out that this practice is going on around the country, yet few reporters have chosen to investigate it. I urge you to reconsider.

*Dan Browning can be reached by e-mail at dbrowning@startribune.com*

**Suggested sources for similar stories:**

*Paper sources:*
Real estate documents such as title transfers, tax records, closing statements, appraisal reports

*Human sources:*
Buyers, speculators, investigators in your state government who oversee real estate agents, mortgage brokers, mortgage wholesalers, Board of Realtors, appraisers, HUD Inspector General's Office, U.S. Attorney's Office, state attorney general's office, local assessors, neighborhood activists, housing advocates

*Digital sources:*
Property sales data (called Certifications of Real Estate Value in Minnesota), Secretary of State corporate records, Multiple Listing Service (if you've got a friendly realtor who can get you access to the database), PhoneDisc (to chart the distance between subject properties and comparables listed in the appraisals).
