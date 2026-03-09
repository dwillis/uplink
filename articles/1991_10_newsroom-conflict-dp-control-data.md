# Newsroom conflict: *Anything can (and possibly will) go wrong when too many DPs work with your data*

**Jerry Uhrhammer
Tacoma Morning News Tribune**

I felt vaguely uneasy when I attended MICAR last May and listened to Elliot Jaspin talk about the importance of maintaining newsroom control over computer-assisted reporting projects.

Before leaving for Missouri, I'd been talking to our newsroom computer systems technician about the hardware needed for a computer-assisted reporting program.

He didn't think that a separate nine-track tape drive was necessary. He was convinced it would make better sense — and be less expensive — to download nine-track government tapes on the newspaper's VAX business computer, then transfer the data to the newsroom network's servers where it could be accessed with a PC.

That's why I was uneasy. Jaspin was telling us that if you're going to use a computer to analyze government data from nine-track tapes, that's a reporting function. And it's important that the reporter have control of the software and hardware involved in the process.

I happen to be a computer enthusiast as well as an investigative reporter. I also know my own limitations — I'm a non-programmer and non-technician. And I had no illusions about being given access to the business computer to load my own tapes. I knew that if we used the VAX system, I effectively would lose a good deal of control over what I was doing.

As it turned out, Jaspin's words foreshadowed a summer of frustration and delays that effectively stalled my newspaper's venture into computer-assisted reporting for months.

Returning from Missouri, I wrote a memo that raised the control issue. But management opted instead to first try the VAX-fileserver-network approach. Why spend $10,000 on new hardware if you can do the job as well, if not better, with existing resources?

I soon learned first-hand what Jaspin had been talking about.

Just the simple act of loading a nine-track tape involved working through two tiers of bureaucracy and across departmental lines. First I had to give the tapes to the newsroom computer technician, who then took them to the data processing department. The data processing professionals (DPPs) actually loaded the tapes on the VAX.

The technicians and DPPs are stretched thin with their own projects and I learned that an assurance that something would be done the next day or the next week was not something to bank on. Days had a way of stretching into weeks.

When things did get done, the results were not always predictable.

The first tape loaded contained 1990 census data. But when I tried to extract data into my XDB database program, my 386sx computer labored mightily for a long time and brought forth absolutely nothing. I tried again and again. Still nothing.

Thus began a recurring pattern. I was the only one who knew about my XDB software. And when something didn't work, it was up to me to find out why. I spent hours on the telephone calling people familiar with XDB and census tapes.

Elliot Jaspin provided the clue that solved the first mystery. The VAX computer did not recognize the character/linefeed signal that marked the end of a record. The absence of such a command left the computer huffing and puffing through 170 megabytes of census data without finding the end of the first record.

When the VAX reprogrammed and the census tapes were loaded again, more funny things happened.

Asked for specific information on a certain census tract, the computer began spewing out data of all shapes and sizes.

I finally realized I hadn't set up the right filters to narrow down my request. But when I did, I still got two "hits" where I should have gotten only one.

After much detective work, I determined that the tapes had been loaded with an incorrect record length.

The good news was that all we had to do was reload the tapes using the correct record length. The bad news was that data processing was busy with end-of-the-month business-side tasks. My tapes had to wait.

More bad news followed. After end-of-the-month time, the DPP who loaded the tapes left on vacation. Thirteen days elapsed before the tapes were reloaded.

In the interim, I learned another lesson about what can happen when you aren't in control of your own data.

Earlier, we had loaded a different governmental database into the fileserver. But when I finally examined the file, I found the data unreadable.

A couple days later, after getting advice on how to cure the problem, I tried to access the database again and found it missing altogether. I had been moved, without my knowledge, to make room for the anticipated reloading of the census tapes.

I was told the data would be restored the next day. Nine days later it still hadn't reappeared. I finally stopped asking about its whereabouts because I had new worries.

The 40-megabyte hard drive on my computer didn't have enough memory to handle the loads of data I was pulling into XDB. The solution: reprogram the system so that I would do all my work in the network's G-drive, which had plenty of memory.

That sounded like a pretty good idea, but when we tried it, my XDB software refused to work in G-drive.

XDB technical support finally figured out what was wrong. The AUTOEXEC batch file written to put XDB on the G-drive contained a command referring to C-drive, which was overriding all subsequent instructions to switch to G-drive.

The VAX-fileserver-network approach turned out to be something less than advertised. For much of the summer, it seemed as if getting our computer-assisted reporting project off the ground was operating according to Murphy's Law: Whatever can go wrong will.

In retrospect, it illustrated again the basic truth of the adage, too many cooks can spoil the broth.

The troubles of summer had a happy ending. My editors agreed that we had to bring all of the program back inside the newsroom, giving us control over our own data.

We bought our own hardware for the newsroom, a 486-33 mhz computer with a 330-mg hard drive, a Qualstar 1260 tape drive and a printer. Now it's up to me, a reporter, to make it all work. As it should be.
