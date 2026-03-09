# Head of the Class

**By Sarah Cohen**
NICAR

When the *Arkansas Democrat-Gazette* set out to measure the quality of its schools, it didn't look to fancy statistical techniques to do its work.

Instead, reporters and editors thought through the project, read about school reports, evaluated the information they could get and culled the reporting of three experienced education reporters.

Then they came up with a simple set of criteria that they would use to define the word "best" for their readers.

Yes, test scores are good measures of a school's success.

But when parents look at schools, they often look also at the environment, diversity and other measures of quality.

*Democrat-Gazette* reporters took that into account when devising their index of excellence in schools.

They included measures of teacher training and coverage, racial disparity, performance, parent activity, and motivation. And they combined them without the regression techniques that have been used elsewhere to find over- and under-performing schools based on poverty.

"We may do that in the future," said Jeff Porter, the computer-assisted editor who crunched the numbers for the series. "But what was interesting was that the elementary and junior high schools that were at the head of the rankings weren't in the wealthy parts of town. The elementary school at the top is almost a rural school, on some road that kind of meanders around west of town."

## Beginning at the beginning

The effort shows why thinking through a project as perilous as the annual school reports is just as important as learning advanced statistical techniques.

Educators tell us there's no way we'll compare schools fairly. But if our job is to provide our readers and viewers with information, not hide it, then our other job is to do it as responsibly as possible.

That's where *Democrat-Gazette*'s indexing technique comes in. In Excel, Porter essentially ranked each indicator, then added up the ranks. The school with the biggest total came out on top.

The only numbers trick he played was to turn the rankings upside down: The school with the "best" performance got the lowest rank, giving it the most points toward the total score.

The school with the "worst" performance got the highest rank — the No. 1 we always think of in rankings — contributing the least to the total score.

Combining upside-down rankings of many indicators is one way reporters can cut the school reports down to size.

The approach seems embarrassingly simple for those who have struggled with the numbers morass of school reports.

Lots of indexes are done this way.

Most business "Top 100" lists are driven by these kinds of rankings. So are the "best places to live" indexes.

Even *U.S. News & World Report*, which ranks institutions from hospitals to colleges, uses a system something like this.

It might be more sophisticated, but the basic idea is the same — figure out what is important, assign a score for each element, and come up with a total that puts everyone on the same footing.

Is an index made up of rankings scientific?

Not entirely.

Does it have drawbacks?

Certainly.

You've lost a lot of information that you'd retain if you used z-scores instead.

All of these indexes, though, use some combination of judgment, reporting and sometimes even polling involved in deciding what's important.

Some words of caution:

**• Figure out your indicators carefully.**
If you decide that racial disparity is a bad thing for schools, then you have to find some indicator of this that will treat all schools equally. *Democrat-Gazette* reporters had criteria laid out by the court system to decide how to measure it.

The lesson is clear – find some reputable and impartial source for your standards whenever possible.

Adjust most of your numbers for the number of students. This is the "per capita" calculation that NICAR classes harp on so often.

Arkansas used many measures "per 100 students" instead. It's the same thing.

**• Make adjustments that educators say matter, but only when they do.**

Many school report stories use some kind of adjustment for poverty, often using the percent of the students who qualify for free or reduced-price school lunches.

You might want to give schools with high poverty rates (or other difficulties like English language skills or high migration rates) a leg up in your ratings.

By focusing on more than just test scores as a measure of quality, *Democrat-Gazette* reporters and editors didn't need to make these kinds of statistical adjustments.

**• Throw out redundant indicators or others that don't tell you much.**

School systems often throw out reams of information, much of which is useless in judging the quality of schools.

For instance, New York's Web site scores of indicators, some of which are nothing more than the percentage of kids who passed competency tests in each subject for each grade. This doesn't help when they're always 99 or 100 percent.

**• Decide what you'll do if there's a lot of missing data.**

In Arkansas, like many other places, reporters simply couldn't get reliable information for some grades.

You may decide to focus only on the very early grades, then junior high schools.

You may have to skip a story on middle schools if there aren't enough to make a fair ranking.

Or you may decide to include an average of the schools' other indicators as an estimate. Just don't let the missing values sit there, though. It will pull down the scores of otherwise fine schools.

**• Collect raw numbers, not rates.**
*Democrat-Gazette* reporters wanted to make sure each indicator was calculated the same way.

So instead of collecting the usual drop-out rates, reporters had to ask school officials for the raw number of dropouts.

This is different, and raises the ire of some school officials, Porter said. But it's sometimes the only way to make sure your numbers are all calculated the same way.

Once you've gotten your indicators, though, making an index of rankings is straightforward. Get your final indicators into Excel, in any order.

Now use the RANK() function to assign the scores for each indicator. Then add up all the scores. You have to figure out which direction is "good" and which direction is "bad" for each indicator.

For instance, a lower teacher-student ratio is usually considered better than a higher one. So a low number is "good."

Or a higher test score is better than a lower one, so a high number is "good."

Here's how a formula might look for a "high is good" indicator.

The RANK() function requires three pieces of information: the number you want ranked, or this test score; the group you want it ranked within, or the entire range of test scores; and the direction you want it ranked.

A "1" means that a higher number will end up higher.

A "0" means that it will rank normally, with a lower number assigned to a high score.

`=RANK(B3,B$3:B$77,1)`

Note the dollar signs.

They mean that, as you copy down, the formula will remain correct. But they also mean you can copy it across, only changing the "1" at the end when you come to an indicator in which "low is good."

Of course, using more sophisticated techniques can help you find the stories in your school system.

In the July issue of Uplink, we'll use the statistics column to profile a set of stories that used statistical techniques to find schools that overcome difficulties well, or sit on their advantages.

Sarah Cohen can be reached at **(301) 942-2199** or e-mail her at **sarah@nicar.org**

*To see the Arkansas Democrat-Gazette's full story about the quality of Arkansas schools, go to www.ardemgaz.com*

*If you have any ideas, examples or questions about statistics, e-mail Sarah Cohen, NICAR's On The Road trainer, at sarah@nicar.org. Her column appears every month and looks at useful statistical tools or other number techniques that can help boil a story down to its core elements.*
