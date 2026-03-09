# Getting data into the right hands: the readers'

**By Chris Feola
Waterbury Republican-American
Waterbury, Conn.**

If your database ran queries in a forest, but no one was there to access it, would your readers hear about it? The Zen cliche about the tree falling in the forest is an examination of existence. My hackneyed refrain is a question of practicality.

In the end, a newspaper is no better than the editions it publishes. A paper can have racks of the latest equipment, access to every piece of data known to man, the deepest thinkers thinking the deepest thoughts — and all of that matters not if the paper that rolls off the presses each night is a piece of junk.

Here's the same question, then, in a more serious form: How do we get our data out of our databases and into the hands of our reporters?

We all know how to do it on the big projects. We all know how to run XDB on 42 bazillion records.

But what about the stories that aren't brain surgery? What if a reporter doesn't need to do an asymmetrical outer join on a series of campaign contribution tables? What if they just want to know if Mr. Big gave the mayor money — Yes or No?

And what if they need to know on deadline? What if they need to know at the council meeting, so they can ask the mayor *tonight* why he's voting on Mr. Big's project?

We faced these questions at the *Waterbury Republican-American* about a year ago when we realized we were running incomplete stories because no one outside the computer-assisted reporting team had a clue when it came to the resources we had available.

We decided to attack the problem on two fronts: We started equipping all our reporters with i386 notebooks to give them their own computer access; and we began building information appliances to allow them to get the data without having to learn Paradox Application Language or anything similar.

The notebook setup is fairly straightforward. Each reporter is given a notebook — we are currently using AST i386SX 20 megahertz machines with 100 megabyte hard drives, six megabytes of RAM and 2400 baud FAX modems.

All that comes in a six-pound package that runs on batteries and fits in a briefcase. We also hand out monochrome VGA monitors and full-size keyboards that plug into the notebooks. In effect, each reporter has a notebook for the field and a desktop for the office.

Application appliances are programs designed to give users point-and-shoot access to data — the idea is that they are no more difficult to use than a microwave.

Here's an example. We have a Paradox database listing all those who contributed to our mayor's election war chest. Rather than having all our reporters learn Paradox — we teach everyone who is interested, but we don't force anyone — we gave them access to the data through a menu choice in their word processor.

Here's how we did it. First, we stripped our Paradox tables down to raw ASCII, then imported them into WordPerfect for Windows 5.1. Then we built a WordPerfect macro and hung it on a word processor menu.

The macro pulls up the file and posts a dialog box that asks "What is the name of the person?" The reporter types the name in and clicks "OK." The macro then runs a search based on the name. If there is a hit, the information is pasted into the story the reporter is working on. If the search comes up empty, the macro tells the reporter "That person is not on the list" and sends them back to their story.

In either case, the reporter has an answer as fast as they can ask the question.

We have used this technique on more than just this list. Reporters can also search municipal employee lists for their towns with just a click of a mouse button. And we're doing the same thing with census data for their towns.

This is probably not the most elegant piece of programming you've ever seen. But here's the bottom line: Our reporters can get their hands on the data they need in seconds. And so they use it.
