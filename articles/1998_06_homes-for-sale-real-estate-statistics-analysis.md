# Homes for sale

**By Neill A. Borowski**
*The Philadelphia Inquirer*

Your editor mumbles "real estate story."
You immediately head for the door.

Many reporters have little or no interest in writing about homes. Yet relevant news about the typical family's most valuable investment can make for a front-page story that has impact. This doesn't mean the filler material that tends to populate many newspaper real estate sections. The emphasis is on *relevant* – stories that are local and tell readers something they want to know.

And what can be more relevant than a story that explains trends in values of their home?

First, let's consider the role of the home in the United States, according to the American Housing Survey for the United States in 1995 (http://www.census.gov/prod/2/constr/h150/h15095rv.pdf). The house is the central asset, the biggest debt and the greatest monthly expense for countless Americans:

- Out of 106 million year-round housing units in the nation, 60 percent are owner-occupied. The median value of owner-occupied homes is $92,507.
- About six out of 10 homes have one mortgage outstanding. Seven percent have two or more mortgages and 13 percent have a home-equity loan. The median number of years to repay the mortgage is 20, with median principal of $48,466 to go. The median monthly cost is $593.
- The median ratio of home value to income is 2:3. However, the home value for about 25 percent of owners is four times their income or more.

Perceptions – and misperceptions – about trends in real estate prices can influence consumer spending and the economy.

At *The Inquirer*, I did my first home price survey in 1990, looking at 1989 prices. The data was cobbled together through the cooperation of different real estate associations. I did another one in 1991 and, in later years, other reporters carried on the tradition. In the last couple of years, though, I suggested that we forego the survey until we could get better data. We got that data this year and were able to offer a more balanced look at home values in the region.

Our survey could be done anywhere. The data may be readily available in some areas and tougher to collect in others.

## The old (and flawed) way

In the past, we used median values by municipality in Pennsylvania and average values by municipality in New Jersey. The data were based on analysis of statistics furnished to the states by each county. We presented the latest year's median (or average) sale price, the previous year's price and the percentage change. In addition, we showed how many units were sold one year compared with the previous year.

However, we were uncomfortable with what the data showed. There was no way to adjust for the type of housing sold each year.

If a large number of starter homes or townhouses were sold in one year, it could drive down the median or average compared with the year before. Using our method, we would tell the reader that home prices dropped by "x" percent in that municipality. But this wasn't necessarily the case. The bottom didn't fall out of the market. Values might actually have been stronger. We were comparing two different sets of houses. The problem was most severe when looking at municipalities where there were only a handful of sales; however, the problem can be apparent even in larger areas.

Consider Montgomery County, a wealthy suburban county near Philadelphia. In 1996, the average price of a home in the county was $168,392. In 1997, the average price was $170,048 – an increase of 1 percent. However, the median price (the middle price when all prices are ranked) was down 2.5 percent. How could the data be so skewed? Part of the reason was an increase in the number of extremely high-priced properties sold in 1997 versus 1996. In 1997, the average of the top five prices was $2.2 million, compared with $1.7 million in 1996. Neither the median nor the average truly represented the change in home values in the county – and even they didn't agree.

## The new (and improved) way

Last year, we contracted with Realist Inc., a Philadelphia-based real estate statistics company, to provide *The Inquirer* with several databases. One of those databases for the Pennsylvania suburbs was the sale price of every home sold, the sale date, the previous sale price and previous sale date. Realist came through with data for 1997 and 1996.

This allowed us to do a "matched pairs" or "sales pairs" analysis. The full database also allowed us to offer the reader other statistics about each municipality. Here's what we ran and how it was done:

**Median Prices.** They're still of interest. But we successfully resisted the temptation to calculate the percentage change between years. That was the flaw we were trying to avoid. We gave the reader the median for 1987, 1996 and 1997 and indexed all suburban median prices for 1997 to show how each municipality's median compared with the overall regional median.

**Price Appreciation.** This was the measure we'd been after for years – and the one that can be done only if you have "matched pairs." This answered the question: "What is happening to housing values when you can look at the values of specific properties?" The database provided us with matched pairs for an average of six out of 10 properties sold in 1997. The formula for appreciation is the compound average annual rate of growth formula:

$$\left(\left(\frac{\text{1997 Price}}{\text{Former Price}}\right)^{\frac{1}{t}}\right) - 1$$

Where:
- the 1997 Price is just that for the given property
- the Former Price is the last available price for the given property
- t represents the number of years, found by subtracting the Former Price's sale date from the 1997 date and dividing by 365. Carry this to several decimal places.

For example, the 1997 price was $105,000 on Jan. 3, 1997. The Former Price was $52,500 on Aug. 1, 1983. The number of days is 4,904 and years is 13.4356. Plugging this into the equation above:

$$\left(\left(\frac{105,000}{52,500}\right)^{\frac{1}{13.4356}}\right) - 1 = 0.0529$$

This means the appreciation rate for this property was more than 5 percent a year – not a bad showing compared to most of the properties. The median appreciation rate for all of Montgomery County was 1 percent a year. This analysis guided us to the lede of the main story of the section:

*The residential real estate market in the Philadelphia area last year underscored the reality of home ownership in the '90s: Think shelter, not profits.*

*In fact, a low-interest passbook bank account offered more promise of profit than a home bought in the '90s and sold last year, according to an Inquirer analysis of more than 57,000 real estate sales in the eight-county metropolitan area.*

In Excel, the appreciation formula would be: `=((105000/52500)^(1/13.4356)) - 1`

In Access, the "Update to" order in the update query would be:

```
( ([MONTCO]![SALE_AMT] /
[MONTCO]![SALE_PREV] ) ^ (1/
[MONTCO]![YEARS] ) ) -1
```

where the Sale_Amt field is the 1997 sale price, the Sale_Prev field is the former sale price and the Years field is the number of years between sales.

After the appreciation rate for each property is calculated, find the median appreciation rate for the municipality.

We also indexed appreciation rates in the region, with the median for the region equaling 100. Because you also have the 1997 price and the former price, you can calculate which homes were sold at a loss. We calculated this as a percentage of total homes sold to show the percent sold at a loss. In some communities, half of the properties for which we knew the previous sale price sold at a loss. Homes with the highest probability of being sold at a loss in 1997 were those purchased in 1989 and 1990, according to our database.

**Price Distribution.** The luxury of having every sale price allowed us to find price distributions in each municipality. The distributions we used were $0 to $50,000, $50,000 to $100,000, $100,000 to $150,000, $150,000 to $225,000 and $225,000 and up.

**Housing Market Measures.** The "turnover rate" for each municipality we used was the number of homes sold in 1997 as a percentage of total homes in the municipality. We also showed the median number of years owned for each municipality as well as the estimated 1997 median household income (from Claritas Inc.).

The 12-page section, called the Guide to Home Prices: What's selling – and why, was well-received. The day it appeared (March 29), our lead real estate writer was a guest on the radio show of a well-respected real estate authority.

---

**The "Guide to Home Prices" story can be accessed online at www3.phillynews.com/packages/homes/over29.asp**

**The section's graphic artist/designer, Matthew Ericson, turned the distribution into a combined bar chart, with five shades of gray so readers could see at a glance how pricey homes in their communities were. These distributions by county and city are available at the above web site.**
