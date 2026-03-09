# Sticker Shocked

**By David Heath and Justin Mayo**
*The Seattle Times*

Talk around the office espresso machine in Seattle often includes gee-whiz accounts of a neighbor's house that sold at some astounding price.

Tales of properties going for $100,000 over list price are common. One 3,000-square-foot house in trendy Washington Park overlooking Lake Washington recently sold for $1 million over the $1.6 million asking price.

The sentiment is that prices are getting out of reach.

However, a detailed analysis by *The Seattle Times* showed that houses are more affordable today than at almost any time in the past 15 years. Rising incomes and falling interest rates during that period have actually overcome soaring home prices.

What's more, home prices in the more desirable Seattle neighborhoods have risen at double-digit rates over the past fifteen years — especially since 1995 — while the market has been much tamer in other areas.

The thrust of the eight-part series, called "Sticker Shocked," was to break down housing trends by neighborhood.

The newspaper obtained 15 years' worth of sales data from assessor's offices in three counties, and some GIS maps, that served as the backbone to the analysis.

We used SQL Server for the primary database work, ArcView for the mapping, and SPSS, a statistical software, to calculate medians. Excel proved extremely useful for computing financial information, such as interest rates, payment over time and annuities.

*The Seattle Times* had for some time been looking for a way to delve deeply into the local housing market. We routinely report changes in average home prices by neighborhood. But as we all know, averages can be very misleading.

In Bill Gates' neighborhood of Medina, the average house sold for $811,000 last year, while the median price was $469,000. Depending on which number you use, prices rose either 55 percent or 15 percent in a year. The latter is far more accurate.

We knew we wanted to calculate median prices by neighborhood. But even medians can be misleading. For example, if smaller, less-expensive homes suddenly become hot sellers in a neighborhood, the median price could fall even though prices for comparable homes are rising.
