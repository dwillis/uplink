# School test scores

**By Seth Hemmelgarn**
*San Jose Mercury News*

In California, school funding is tied to schools' performance on standardized tests. Starting with the 1999 scores, each school is given a 1 to 10 ranking. Schools with a 1 are in the bottom 10 percent of the state, and schools with a 10 are in the top 10 percent.

The state released the data in January. We wanted to map where schools with the highest and lowest ranks were in our county. The only problem was, we had the score for each school, but we didn't have the address. So we got the addresses from the state, and created a dbaseIV file with all of the information we needed.

After I geocoded the file in ArcView, I used the query wizard to pinpoint the schools with ones and tens. Not surprisingly, most of the highest-ranked schools formed a blob running along the county's western foothills, where millionaires are commonplace. The lowest-ranked schools showed up in a patch on the city's eastside, where incomes are generally lower.

This was my first official mapping assignment after I attended NICAR's incredibly worthwhile mapping bootcamp, so I wanted to have somebody else review my work. That's where Carl Neiburger, mapping guru and *Mercury News* cohort, came in.

I'd used two different queries to show the highest and lowest ranking schools, which resulted in two different shape (shp) files. Carl suggested selecting all of the ranks – from 1 to 10 – into one shp file. Then, I just eliminated the ranks we didn't need. This meant one less shp file to keep track of.

Carl also enlisted the help of Nadine Selden, from the paper's marketing research department. Nadine pulled the median income for each of our county's Census tracts from Claritas, and Carl included this in the map. The result was a map that not only showed where the high and low-scoring schools were, but what the income ranges in those areas were.

Seth Hemmelgarn can be reached by e-mail at SHemmelgarn@sjmercury.com
