# On the World Wide Web
## Many happy returns

**By Tom Foster**
The (Syracuse, N.Y.) Post-Standard

The Syracuse Newspapers used a multilayered approach to report 1995 election results to their central New York readers in real time.

Using NewsLine, the newspapers' audiotext service, and Syracuse OnLine, the newspapers' World Wide Web site (www.syracuse.com), the newspapers delivered up-to-the minute returns on everything from the county executive campaign to dozens of town council races.

The newspapers used three terminals connected via modem to Onondaga County's Board of Elections mainframe to monitor results in real time. Those were transferred by typists to a master Paradox database of results that resided on the newsroom's Novell network.

### Getting results

Once the results were on the newspapers' PC network, those single keystrokes did a lot of things at the same time. Results were posted at our web site. The newsroom as a whole was able to track the evening's events. And reporters got instant printouts for the races they were covering. Here are the details:

- **Internet documents:** Paradox's report writing functions allow HTML tags to be built into templates. Using templates makes it easy to accommodate changing data. The functions let us create HTML documents containing the latest results on the fly by telling Paradox to make the right web page. We had to prepare. Prior to the election, fields in the Paradox table had been filled in with the names of the HTML files for the fact boxes, profiles and preview stories for each race. That let us publish more than just numbers. On election night, the files were sent to an update folder on the newsroom network, where they were transferred to the web server.

- **Newsroom updates:** Real-time electronic updates were available to all reporters and editors. One newsroom PC running Netscape was hooked up to a TV mounted above the city desk. That allowed point-and-click access to results that could be viewed by dozens of people at once. To speed things up, the PC connected to the television was used to monitor the results file from the newsroom network rather than our web server.

- **Customized reports:** To keep reporters who were working on the more than 140 races efficiently updated, the Paradox table also included a field listing the name of the reporter covering the race. A Paradox script triggered paper printouts so each reporter received a report listing results on just the races that reporter covered.

A Paradox script running in the background generated automatically all of the HTML and paper reports. That script monitored the system clock and triggered updates every 10 minutes. It allowed the typists, reporters and editors to work without interruption throughout the night.

### What we learned

Generally, the process worked smoothly. We usually were able to pass results from the board of elections mainframe to our staff and online users within five minutes. The ability to update all races simultaneously tended to put us ahead of broadcast media. A local public radio station used our web page as a source of its report to listeners. The Board of Elections also monitored our page and referred callers to our site. There is always room for improvement.

We confined our updates for Onondaga County to one file that was fairly large, about 49K. That's with no images. Because we only had to replace one file, that sped up our ability to update our site. Its size meant reloading via modem took an annoyingly long time in some cases. This was particularly true when using America OnLine's browser.

On the newsroom side, we learned the hard way that low-tech approaches can be more effective. On election night in 1994, reporters got an icon on their PCs that allowed them to monitor the master Paradox results table as it was updated. Two problems arose: Some reporters weren't comfortable multitasking, so they would view the results, take notes by hand and then exit that application to write. And when about 35 reporters tried to run Paradox over the network at the same time, the load brought traffic to a crawl and finally a crash.

We used paper reports this year to guard against network overload, but it turned out that most reporters were more comfortable with that system anyway.

*Tom Foster can be reached at (315) 470-3071, or send e-mail to tsfoster@mailbox.syr.edu.*
