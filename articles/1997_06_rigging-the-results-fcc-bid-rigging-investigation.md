# Rigging the Results

**By Bob Sullivan**
MSNBC

*Bob Sullivan graduated from the Missouri School of Journalism in May 1996.*

MSNBC's investigation into bid-rigging in FCC spectrum auctions was an interesting mix of a long-term CAR project and spot CAR reporting.

My editor, Mark Pawlosky, had charged me with finding databases regarding the FCC's auctioning of spectrum bands to telecommunications companies.

There is so much money changing hands in these auctions — $23 billion has been raised since the auctions started three years ago — that the process was worth taking a look at.

With our telecommunications reporter, David Bowermaster, I had been in touch with Andy Lehren at NICAR regarding what data could be found or FOIA'ed.

We had asked for some pretty thorough data, not knowing what we were looking for, and NICAR was assembling it in Missouri.

## A public fight

Then on May 1, Reuters reported that two small companies involved in the January auction for Personal Communications Services licenses (PCS devices) were in a public squabble.

High Plains Wireless filed a complaint with the FCC accusing Mercury PCS of "bid-signaling" in January's DEF block auctions.

The complaint spurred an investigation by the Justice Department, and reports said the last three digits of bid amounts were somehow involved.

That was the burst of sunlight which we needed.

Now we had something to look for. Companies issued bids that ended in unexpected numbers, like $1,100,136, as a signal to competitors.

The signal might tell others to stop bidding on that market, or it might contain a message about bidding in another of the 1,479 licenses available in that auction.

In any case, the hypothesis was that companies used this signaling to limit competition for licenses and by mutual unspoken agreements, keep prices down.

Now, NICAR was able to point me to the enormous and unruly data the FCC had posted on its Web site regarding the PCS license auctions.

In the DEF blocks, there were 276 rounds of bidding. Sure, all the data was on the Web site — in over 1,000 different .dbf files.

There were six files for each round — one with all the round's bids, one with the high bid before the round, one with the high bid after the round, one with that round's withdrawn bids, etc.

## A sample test

At first, we agreed it might be futile to download all of it. But we figured there might be a way to test a sample of the data to see if it might bear fruit.

First, we looked at the winning bids for the 1,479 licenses, to see if anything about the last three digits of the winning bids stuck out. Not really.

So then we cherry-picked every 20th round, and ran some tests on a mini-version of the data. We had some notion that bidders were allowed to lower their bids as the process progressed if they weren't challenged in a market.

That seemed odd, so we went hunting for markets where the winning bid was less than a bid made during the rounds. We found a few, but that was also basically a dead end.

It did point to a few markets, though, and when examined, the bidding in those markets exhibited what seemed to be odd bidding behavior — and about half of them involved a company named Western Wireless.

There seemed to be multiple instances of the same dollar amount being bid by the same company for the same license. That didn't make any sense — why would they have to make redundant bids?

## Expanding the search

We now figured it was worth our while to get a picture of what happened in all 276 rounds of bidding.

It took most of a weekend, but we grabbed all the bids made in all 276 rounds. We then imported the tables into Microsoft Access.

Had I more experience, I would have written some kind of script to bundle them all into one table.

But not knowing any other way, I used one append query at a time to compile into one table all the bids made in all the rounds on the DEF block.

Fortunately, each round had a field with the round number, so we could assemble them into one table without losing data or being forced to add markers.

The results were now quite good – I built a quick front end which allowed me to query one market at a time and showed the bidders and bids as they marched from first round to winning bid.

## The results and more work

What emerged? The most noticeable was Western, which seemed to have a habit of making the same bid over and over — in fact, it won 10 licenses in the 136th round with that kind of redundant bid.

There were plenty of other signals, too — like Comcast's bid for a Philadelphia license that ended in 346.

*Bob Sullivan's story on the FCC and supplemental charts can be viewed at http://msnbc.com/news/73393.asp*
