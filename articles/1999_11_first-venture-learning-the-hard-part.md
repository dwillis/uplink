# First Venture: Learning the Hard Part

**By Jodi Nirode**
*The Columbus Dispatch*

I was so idealistic. After finishing IRE and NICAR boot camp this summer I thought the hardest part about doing my first solo computer-assisted reporting project would be writing Access queries. How quickly I learned how many pitfalls there can be along the way.

The project was looking at the response times of Columbus police.

On Mother's Day, a 48-year-old man was shot and killed in front of his children and grandchildren – 30 minutes after a neighbor warned a police dispatcher that a drunk man was firing shots from his front stoop.

Police called the delay a fluke – that rare case when more important calls bogged them down from getting to a run that should have been the division's second highest priority.

*The Dispatch* wanted to know for sure.

I requested a year's worth of the 911 dispatch records. In my request, I stated I wanted nothing omitted and I wanted them in a comma-delimited text format. Simple, right?

However, the woman placed in charge of my request gave me separate files for each day – 366 in all. So I'd have to input and link each file for every Access query.

The dispatchers comments weren't included, I later learned, because they are stored separately.

So, I had to make the request again.

And again, the files came back in separate databases.

The head of the department gave me a technical argument about the information being too large to store in one text file; if I wanted it in one file, he could do it, but in Access only.

God, did I feel dumb.

I should have asked for them to give it to me in Access originally. I just never dreamed they had it. It taught me the first of many valuable lessons that would resurface later – never assume.

### The data work

Alas, finally after about a month of waiting and re-requesting, I had my data. I was so excited. I signed out a new IBM Winbook and examined the 897,870 records or calls that Columbus police took that year. (By the way, I was defining response time as the time it took between the time the call was dispatched to when the first police cruiser arrived on the scene.)

I queried the data every which way. Average response times for gun runs, domestic calls, dead bodies, burglaries, stabbings – you name it.

I looked at medians. Then I looked at response times by shift and precinct using Excel's pivot table. (What a marvelous invention.)

I knew going into the project that nearly 50 percent of police in Columbus weren't logging their arrival times. It was disappointing, but we planned to use the data anyway and note the problem.

As I saw it, the information I had to use was the only information the division had to make important decisions such as staff allocations, requests for more manpower and citizen complaints. The response times might not be dead on, but I thought they would still show disparities in response times between the larger and smaller precincts. (Of course, with the help of data processing I did some more sophisticated queries first to see if the lack of reporting was similar across the city's 19 precincts and it remained fairly constant for all types of calls.)

What I didn't anticipate was a programming quirk that plugs in the same time for when the call was received, dispatched and when the officer arrived.

The self-initiated run, as Columbus police call it, is supposed to be used when an officer witnesses a crime or calls the run into a dispatcher shortly after it happens.

Those runs, though, comprised 28.9 percent of calls and couldn't be used. Factoring those out, we had about 21 percent of the total calls to use.

Three independent statisticians assured us the data would still be fine to use if we stipulated that the averages were averages of the data available – and not averages of the division as a whole.

### A new direction

As controversial as it might have been, the thought of using it didn't last long. Doing queries on the data without the self-initiated runs showed how skewed the data can get when you start slicing it too much.

Response times for officer in trouble – a call officers use when their life or well-being is in danger – jumped to 8 minutes. (Without self-initiated runs, the average was about 3 minutes.) I knew the 8 minute-average was not only absurd, it was false.

Though a young reporter, I've covered police on and off for six years and knew that was the call that police likely responded to the quickest.

Going back to police communications I got the answer I dreaded. The 911 system plugs in arrival times for the first car on scene who logs his arrival time.

So for example, if an officer shows up an hour later to handle traffic and is the first on scene to hit a button on his cruiser console signifying his arrival, that's the time the 911 system records as the arrival time.

I knew then, the project as planned was dead.

Of course, there was still a very important story: that the division has no idea how long they take to get to crime scenes. They can't.

Of course, in retrospect I felt dumb for assuming the arrival time listed in the database was for the same officer listed on the department's run. Next time, I'll be very thorough in finding out how information gets plugged into each column.

In the end, the story prompted outrage by the City Safety Director and others, but no change.

The director ordered the officers be forced to record their arrival times, but the police contract has a provision that the city can't alter any past practices, unless changed in the contract.

And the Fraternal Order of Police didn't see the lack of response times as a problem, so the director's order was moot.

The division is caught up in a battle too with the U.S. Department of Justice over claims that they abuse citizen's rights, so even with follow-ups, the issue is still likely going to be lost in the shuffle.

It was a lot of work to uncover a record-keeping problem, but I sure learned a lot along the way.

*Jodi Nirode can be reached by e-mail at jnirode@dispatch.com*
