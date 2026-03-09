# Census 2000: Reapportionment

**By Griffin Palmer**
*The Daily Oklahoman*
**and Steve Doig**
*Arizona State University*

The 2000 Census isn't just a good idea – it's the law of the land. The U.S. Constitution mandates a national headcount every ten years for one purpose, and the specified reason isn't to help fast-food franchisers decide where to build their next burger joint. Rather, the census is required for fairly apportioning the 435 seats in the House of Representatives among the 50 states. All other census applications, whether drawing political district lines, allocating federal funds or siting taco stands, are just constitutional gravy.

The decennial reapportionment of Congressional seats means great stories, and they're the very first ones that will come out of actual 2000 Census data. By law, the Secretary of Commerce (who oversees the Bureau of the Census) will tell the President in late December of 2000 the official population of each state, and the President will then notify Congress. At that point, the bloodletting will officially begin.

**However, it's no trivial task to translate the states' populations into the number of seats each will get, as the two of us have learned.**

Because the number of Congressional seats is capped at 435, some fast-growing states will gain new seats at the expense of those with slower growth. Reapportionment means political musical chairs in the losing states, and a big scramble for the newly-open seats in gaining states.

However, it's no trivial task to translate the states' populations into the number of seats each will get, as the two of us have learned. A simple proportional allocation (in which, for instance, a state with five percent of the nation's population gets five percent of the 435 seats) doesn't work for two reasons. For one, there are no fractional seats in Congress (although some of the occupants certainly are fractious), and so a proper rounding scheme would have to be devised. And more important, the Constitution guarantees that even the smallest state will get at least one House seat even if its share of the nation's population is "worth" less than half a seat.

**Equal proportions**

Numerous apportionment schemes have been devised, and five different ones actually have been used at various times in the nation's history. (See *www.census.gov/population/censusdatalapportm.pdf* for a brief history of those methods, and *www.census.gov/srd/papers/pdf/rr92-6.pdf* for a more exhaustive discussion of the history and mathematics of apportionment methods.) We'll only concern ourselves here with the so-called "method of equal proportions" which has been used since 1940 and was upheld unanimously in 1992 by the U.S. Supreme Court.

**Simulation**

We won't try to explain the mathematical reasoning that underlies the method of equal proportions, because then we'd have to pretend that we actually understand it ourselves. But we have devised an Excel spreadsheet that accurately simulates the method and thus will let you figure out where your state stands in the reapportionment shuffle. To satisfy yourself that it works, first we'll build the spreadsheet using the official 1990 populations. Here's how:

- Open a new spreadsheet.
- Put these labels in the first row on the specified columns: A: "State", B: "Population", C: "Seat #", D: "Multiplier", E: "Priority value".
- Fill range A2:A51 with the names of the states.
- Fill range B2:B51 with the 1990 apportionment populations of the states (which you can find at *www.census.gov/population/censusdata/table-a.pdf*)
- Fill range C2:C51 with the number 2.

(We start this with seat 2 because every state is guaranteed at least one seat.)

- Put this formula in Cell D2: `=1/SQRT(C2*(C2-1))`. The formal name for this multiplier is the "reciprocal of the geometric mean," in case you get asked on "Who Wants to be a Millionaire?"
- Put this formula in Cell E2: `=D2*B2`
- Put this formula in Cell A52: `=A2`
- Put this formula in Cell B52: `=B2`
- Put this formula in Cell C52: `=C2+1`
- Copy range A52:C52 all the way down to Row 2951. You'll know you did it right if "Wyoming", "455975" and "60" are on that row.
- Now select range D2:E2 and copy it all the way down to Row 2951, too. It worked if you see "0.0168073" and "7663.716" down there.

(Okay, okay, here's what's happening. The method of equal proportions requires that you calculate a "priority value" for at least as many seats as each state could possibly get. As it turns out, the easiest thing to do is calculate such values for seats 2-60 for every state, on the grounds that not even California will get as many as 60 seats. And 50 states times 59 priority values means 2,950 rows.)

**The decennial reapportionment of Congressional seats means great stories, and they're the very first ones that will come out of actual 2000 Census data.**

Now open a new sheet and follow these steps:

- Go back to your first table and copy the entire thing, all 2,951 rows and five columns.
- Use "Paste Special...Values" to paste it onto the new sheet.
- Sort that second sheet by descending order of Priority Value
- Insert a blank row at Row 387. This cuts off the table at 385 seats.
- Insert 50 blank rows into Range A2:A51.
- Copy the names of the 50 states into Range A2:A51.
- Put a one (1) in Cell D2, and copy it down to Cell D51

Whew. You now have a table with 435 records, one for each seat in Congress. To find out how many seats each state gets, simply do a pivot table by dropping the State variable into both the Row and the Data boxes.

**The results**

The main table also is worth a detailed look because it shows the order in which the seats were parceled out. Notice, for instance, that California got 42 of its 52 seats before Idaho and Rhode Island got their second seats. Notice also the first few states in the remainder below your main table. Those are the ones that just missed getting another seat (at someone else's expense, of course) and where much of the wailing was heard after the 1990 Census.

Now that you've done one for 1990, repeat the process using projected populations for 2000, which you can find at *www.census.gov/population/projections/state/stpjpop.txt*. You'll see plenty of winners and losers in the data. And if your state is near the bottom of the main table, or near the top of the leftovers, you'll know how important a good census count will be to your readers – and your politicians.

(A final note for FoxPro mavens: Griffin first developed this apportionment simulation using FoxPro. If you want a copy of his method, contact him by e-mail.)

Steve Doig can be reached by e-mail at steve.doig@asu.edu

Griffin Palmer can be reached by e-mail at gpalmer@oklahoman.com

---

**The U.S. Census Bureau's 2000 Census page:**
www.census.gov/dmd/www/2khome.htm

There you can get information about data releases and download 1990 population figures.

**Recent tipsheets on the census, available from the IRE Resource Center, include:**

- "Using Census 2000 to Investigate Changes," (#1096) by Richard O'Reilly of the Los Angeles Times, for the 1999 IRE Los Angeles Regional Conference. This tipsheet gives reporters an idea of how they can start planning for the 2000 Census.
- "Preparing for the 2000 Census," (#1097) by Steve Doig, Arizona State University, for the 1999 IRE Los Angeles Regional Conference. Doig lists a series of tips on how to begin investigating census data "during the relative calm before the data storm hits."
