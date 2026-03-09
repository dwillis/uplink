# Intranet Start-Up

**By Robert Gebeloff**
*The Record*

When word spread in Norwood, N.J., that authorities had granted a variance for a Korean congregation to build a large church, some residents began pressuring town leaders to reverse the decision.

The primary argument against the new building: It would draw hundreds of "outsiders" into town and disrupt the peaceful suburban atmosphere.

But before he even set foot in Norwood, reporter Adam Geller knew more about the community than some of its residents.

At his desk in *The Record's* Hackensack newsroom, Geller made a few clicks on our CAR Lab intranet and was able to compile various demographic facts about the town.

**Two years after we laid down the first line of intranet code, we can attest that there's no better way to have an impact on the daily news report than to 'democratize' your data.**

By throwing a few simple stats up against the perception of some Norwood residents, Geller was able to illustrate a major component of the conflict better than he could have with a thousand words of explanation.

And he didn't have to touch a spreadsheet or database manager.

Examples like this are exactly what we hoped to see when we began planning our newsroom intranet in 1998. While we use CAR in projects and short-term enterprise, we also subscribe to the philosophy that CAR should be for everyday use.

And two years after we laid down the first line of intranet code, we can attest that there's no better way to have an impact on the daily news report than to "democratize" your data — making it widely available to all journalists in the shop, regardless of computer skill level.

Our staff of about 100 reporters and editors is now averaging 80 queries a day through our intranet. Not every single query gets in the paper, of course, but it shows that our staff is using this tool as a regular part of the reporting process.

I won't mislead you — building and maintaining an intranet does not produce the same high-profile results as hardcore CAR enterprise work. But if you plan it right, and pick the proper tools, you can minimize the workload and lay the groundwork for newsroom-wide CAR.

Before delving into an overview of intranet planning and development, a few comments are in order about the advantages of an intranet over other systems for building database front-ends for general staff use.

Many of you use Microsoft Access, which has fantastic tools for building search forms that allow users with no Access experience to query databases.

The problem with Access front ends, however, is that they're not as efficient over a network as a "client-server" system. If you build front ends into Access databases and put them in a common folder on the network, vast quantities of data have to move back and forth between the user's computer and the computer where the database resides. This can become a major drain on network bandwidth.

A client-server intranet, on the other hand, keeps network traffic to a minimum. The user types input into the client machine – a Web page on their desktop – and the input is passed on to the server. The query is run on the server, and just the results are sent back to the client. The database itself stays put and bandwidth use is minimal.

So if you're hoping to make data available to a lot of users, an intranet is the way to go. But before you begin, you'll need to plan thoroughly in three areas:

## The Back End

This is the guts of your intranet, the stuff behind the scenes that makes it all work. Your back end has to include some kind of Web server and a scheme for handling database queries.

There are different types of servers, and I'm not going to advocate any specific model. For specs, just get as powerful a machine as you can. I can happily report that our Web server is a low-end Pentium and still does an adequate job.

The question of server type is thornier. There are a LOT of ways to build an intranet, and a lot of different opinions about the best way.

If your Web server is fueled by the Microsoft Back Office suite, there is one set of tools for building the front-end user interface. If you have a Unix box, then the set of tools is completely different.

**It's ultimately a compromise. The downside is it takes some work to build and maintain. But the upside is that you're helping reporters help themselves.**

My advice, which admittedly will irk the purists of specific technologies, is to use the tools that are most accessible. If your company already has a corporate intranet on a Windows server, then see if you can get space on it. If your IT department is filled with Unix geeks, then tap into their knowledge.

As for data, we now have our tables stored on an SQL Server. But when we started, we used Access and achieved acceptable results.

Our Web server knows where to find our data because we use "open database connectivity," or ODBC. This is a simple setting in the Control Panel of our Web server. You give each of your databases a name, and then give the Web server actual location of the data on the network. Then, when you're building a Web page and want to tap into a database, you just insert the ODBC name and your Web server knows where to get the data.

Whatever scheme you use, the key to efficiency is to make sure all your tables are indexed on the fields that your users will query.

## The Front End

Once you know what's running your server, you'll need to decide what to use for building Web pages. We use Microsoft Front Page for our static Web pages – our Internet guide, CAR newsletter, etc. – and Active Server Pages for our databases.

There are many other options, however. ColdFusion is used in some newsrooms. I've seen people on the NICAR list talking about MySQL too.

I don't want to talk about the pros and cons of each, but rather about some general design concepts.

First of all, the whole point of doing this is not to give users the power to do every conceivable trick with a database that you can do with Access.

Rather, the goal should be to pick out the queries that will be most useful to the staff as a whole. In many databases, all your staff really will want are simple name and town look-ups.

We try to add value to the results. If a reporter is looking at campaign contributions by the late local oil baron Leon Hess, they can click on the results and see what other employees of Amerada Hess contributed. If the reporter is running a name through our crime database, they can click on the results and see what happened to the co-defendants.

We also have learned not to cram every field into the results. With our criminal background search, the user types in a name, and if there's a hit, the page displays the county and case number. One more click yields about 80 fields of information.

Front-end software such as ColdFusion and FrontPage offer wizards that will quickly build simple look-ups, which is a good way to get started. But we found ourselves wanting to do more than the wizards provided, so we learned how to build Active Server Pages with Visual Basic Script.

Knowing how to code gives you absolute freedom to build whatever front-ends your reporters will need, and it's not the most difficult skill to pick up. I learned by studying a few sample scripts donated by Tom Torok when he was at *The Philadelphia Inquirer*, and then by picking up the wonderfully simple *Active Server Pages for Dummies.*

## Operation/Maintenance

Like a lot of things, you'll get out of your intranet what you put into it. I'm fortunate enough to have CAR specialists, plus a part-time data entry person to help me out.

That has allowed us to expand the site to keep more than two dozen databases up to date. Still, we have a dozen more that I haven't found time for yet.

Keeping a good intranet is a job, but the question is who does the job. At our place, the library is heavily involved in maintaining the corporate intranet, and the CAR intranet is our baby. But at your paper, the library might be interested in helping out, and the more help you can get the better.

I should caution, however, that you should resist the temptation to turn your intranet over to non-journalists. Sure, the technical skills and labor can be handled by anyone, but the real gold in doing this is in the design.

It takes a database editor to decide what databases to post and to design an interface that will best serve reporters.

Most of us dread the notion of becoming a "service bureau." And rightly so. As journalists, our ambition should not be to become the source of fascinating facts for stories by other reporters.

At the same time, however, I feel that it's a disservice to our news organizations if we simply acquire and horde databases. I can cite countless stories in *The Record* that were made better because of information or ideas a reporter developed from using our intranet.

It's ultimately a compromise. The downside is it takes some work to build and maintain. But the upside is that you're helping reporters help themselves, and that, in turn, gives you the freedom to pursue your own work.

*Robert Gebeloff can be reached by e-mail at gebeloff@bergen.com*

---

## Using Newsroom Intranets: Examples from The Record

Reporters at *The Record* use the intranet in a variety of ways.

- Political reporter Maia Davis uses voter registration records all the time, not just for finding the names of party members in certain towns, but also to learn the home address of a person in the news.
- On deadline, Scott Fallon pulled the salary and title of a teacher accused of sexual assault.
- Reporter John Chadwick regularly finds unlisted phone numbers in the voter registration records.
- Alex Nussbaum discovered that the mayor in one of his towns was giving out incorrect information about property assessments.
