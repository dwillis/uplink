# Uncovering an age-old scam

By Ron Hurtibise, *Daytona Beach News-Journal*

Interested in buying some Florida swampland?

If you have any idea how much prime real estate in Central Florida sells for these days, you'd probably think twice before believing you could spend a mere $5,000 to $7,000 an acre for your future retirement home site.

That's why our newspaper's investigative team was surprised that many people are still spending thousands of dollars for soggy, inaccessible land they'll likely never be able to develop or sell at a profit.

In Volusia County, between Daytona Beach and DeLand, eBay auctioneers are amassing small fortunes by peddling lots that had been targeted for purchase by the county's wetlands acquisition program. The sales are pricing the county out of the market, creating an uncertain future for a vital water recharge area and setting up unsuspecting buyers for a bitter reality check.

We uncovered the story, in part, by analyzing property data with a geographic information system (GIS) program.

The *News-Journal* had played a prominent role exposing boiler room swampland scams to a national audience in the 1960s, but it took an alert reader and a few minutes on eBay to tip us off that the cycle is repeating itself in the Internet age.

In April 2003, I received an e-mail from a real estate agent in Flagler County, on the north side of our coverage area, alerting me to eBay sales of subdivision lots that could not be developed. So I checked it out: Sure enough, ads touting "beautiful Florida land" filled eBay's fledgling Real Estate auction pages.

A call to Flagler County's zoning department confirmed that buyers of lots in a "paper subdivision" called Flagler Estates stood little chance of getting building permits because there were no roads or utilities available.

The situation they described was fascinating, and totally new to me: Back in the 1960s, a supposed development company bought a large tract of land, carved it into hundreds of lots, named it Flagler Estates and sold the lots as "investment properties" for as much as $2,000 or $3,000 apiece, plus financing charges.

Buyers, usually retirees from the north, bought the parcels sight unseen on installment plans from telephone salespeople, and then often stopped paying local property taxes on the lots after realizing they'd been duped. The lots reverted to the county, which sold them at tax sales for as little as $300 an acre. Buyers of the auctioned properties then made thousands of dollars selling them on eBay.

After we ran a story on Flagler Estates, a Volusia County resident told me that eBay sales of lots in paper subdivisions was much more widespread than we had realized or reported, involving half a dozen large tracts in the Daytona Beach area and others throughout the state.

The most blatant example was University Highlands, a 9,400-acre watery no-man's-land between Daytona Beach and DeLand. Dozens of yellowed clippings in the newspaper's archives told the story of how the subdivision was created:

Lax 1960s-era county development regulations enabled the Firstamerica Development Corp. to plat a subdivision with no roads, sewers, drainage ditches or utilities; set up a telephone boiler room and market the lots as investment parcels to out-of-state buyers.

The county's zoning board, alarmed by the prospect of development on what was even then recognized as an important water recharge area, tried to rezone the tract for conservation in the mid-1960s. Faced with the prospect being unable to market the rezoned lots as investment properties, Firstamerica threatened legal action, contending the zoning board had overstepped its authority. After the Volusia County Commission refused to fund any legal defense of the rezoning, all five zoning board members resigned and the rezoning was rescinded.

In a way, the mess created by Firstamerica was good for conservation. With ownership of the subdivision's lots divided among thousands of owners across the nation, no developer was interested in spending the time, money and effort to assemble enough lots to create a profitable development plan – especially with larger, cheaper, drier tracts available elsewhere. Today, according to county planners, residential development on a commercial scale would require acquisition of contiguous parcels and most likely a replatting of any portion submitted for development.

But buyers who dreamed of one day building on their Florida dream lots didn't know this.

We guessed that few of today's eBay buyers were aware that prospects for developing the area remain just as slim. We set out to change that by mapping parcel data.

The availability of local land recording and appraisal data made it possible for us to identify the most prolific swampland resellers and show that some were making as much as 1,900 percent profit selling lots.

I used the Clerk of Courts' Web site (*www.clerk.org*) to identify who was buying and selling the most lots in University Highlands, how much they had paid for them, who the buyers were, and the selling price. I copied parcel numbers from the eBay ads and pasted them into the search field of the clerk's public records database. The database stores property transaction data and images of nearly all documents recorded at the Volusia County Courthouse since the mid-1990s.

The data revealed that many of the buyers had Asian surnames, leading us to suspect many were immigrants most likely unfamiliar with the historic risks of buying inexpensive Florida land.

At this point, we knew we had a powerful story. But I wanted to give readers a visual sense of the size of the tract and the high volume of sales activity there. From two highways that flank it, the tract looks like nothing more than undeveloped woods. Road maps show nothing there. Only a parcel record map, never seen by the average reader, could convey what the Firstamerica Development Corp. created.

I set out to create the most cumbersome graphic I've ever pitched – a map of the entire 9,400-acre, 6,167-lot tract that pinpoints all lots that changed hands since its discovery by the eBay sellers.

For $30, the Volusia County property appraiser sold us a copy of its entire database – with 352,000 records – in a Microsoft Access file, burned onto a CD within 24 hours.

Typing University Highlands subdivision numbers in the WHERE statement of my Structured Query Language query, I built a table of property sales in the subdivision over the past three years. I converted the Access query result to a Microsoft Excel spreadsheet table, and then exported that as a tab-delimited text file.

From the property appraiser's Web site, I downloaded aerial photographs of the subdivision that illustrated the size of the tract and the lack of development there since the 1960s. The photo, shot by the Florida Department of Transportation and made available in a Seamless Image Database (.sid) file format, was embedded with geographic coordinates enabling its precise placement in ESRI's ArcView 8 mapping program.

From the county's geographic information system Web site, I downloaded a shapefile that displayed the original plat and all of the lots.

I overlaid the parcel map onto the aerial image, then joined the property identification number field in my recent-sales table to the property ID field in the parcel map's attribute table. I sorted the joined attribute table in descending order so the recent sales records were grouped at the top. I selected those tables so the recently-sold lots appeared highlighted in blue on my map.

I created a new map layer from the selected lots, then re-sorted the attribute table of the new layer to isolate lots purchased by the county for conservation. After creating yet another map layer of just the conservation lots, I shaded them yellow and red so readers could see how the private sales, shaded in blue, were encroaching upon the taxpayer-funded conservation effort.

I exported the graphic as a camera-ready .JPG file that required minimal work from the art department before it was ready for publication in an information graphic. To bolster my pitch, I created a mock-up of how the map could look as a stand-alone graphic, with its own headline and text box. Atop the map, I pasted fact boxes pointing out five examples of quick-turn sales for big profits.

The Sunday editors liked my mock-up and approved the graphic at nearly a full page inside, with color.

None of the major eBay sellers agreed to be interviewed for the story. I emailed them through their eBay accounts, and when possible, tried to contact them via addresses and phone numbers filed with the state Division of Corporations.

The state Division of Land Sales, created 30 years ago to regulate swampland sales, said it was unaware that the practice had been revived. After an initial interview in September, the division chief said he had begun an investigation and could not comment on specific examples.

A retired division investigator living in southwest Florida had no such qualms. He reviewed several examples of eBay ads and pointed out ads that appeared to violate state laws barring sellers from claiming development was imminent and predicting how much a lot's value would increase in the future. And he pointed us to laws requiring sellers of undeveloped subdivision lots to register with the state and submit examples of advertising for review – laws the highest-volume eBay sellers we identified appeared to be ignoring because the state had no record of their registration. We continue to await results of the state's investigation.

Contact Ron Hurtibise by e-mail at ron.hurtibise@news-jrnl.com.
