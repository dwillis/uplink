# Neighborhood report

**By James Derk**
*Evansville Courier*

The *Evansville Courier* (65,000 daily, 125,000 Sunday) was the first newspaper in the world to publish weekly crime maps on the World Wide Web.

I say that not to boast, but instead to emphasize the major benefit of working in a smaller market – the ability to map out every crime in an entire city for a whole year and not have the whole town covered by thousands of colored dots.

Even so, our beginnings in mapping were modest. I talked my editor into forking out the $1,295 for Mapinfo for Windows after seeing Jennifer LaFleur of the *San Jose Mercury News* use the software at NICAR's boot camp several years ago.

### Extending coverage

I launched the weekly crime map in an effort to spread more information to residents of our community. When I got my first phone call from an angry realtor who my maps had "destroyed property values" in one neighborhood, I knew we were on to something. But we didn't do it just to tick off the realtors.

Anyone who has worked the city desk knows the phone call. "My neighbor's garage was broken into last night, and someone took their Snapper lawn mower and their chainsaw, nearly new. How come there was nothing in the paper?"

There was nothing in the paper because newspapers and the people who run them don't care about neighborhood crime. Sure, we cover the bank robberies and murders. But we don't cover the burglaries, thefts, vandalized mailboxes and other parts of daily life in a community.

The crime map helps us do that. We can't print a story in the paper every time some kid kicks in a yard barn and takes the mower. We can at least give our readers a dot on a map and maybe help prevent some crimes in the process.

### Quid pro cop

How is this done? In 1995, Art Gann, Evansville's chief of police, agreed to a trial run of giving The *Evansville Courier* online access to police blotter information. We started to archive the logs and soon had a month's worth of information. I started to play with Mapinfo and showed the cops what we could do with their boring data.

The police had a civilian employee whose job it was to stick colored pins into a large map of Evansville that hung on the wall of the detective office. I showed them how we could do that with Mapinfo. We soon struck a deal: They would email me a week's worth of data, and I would produce a color map for them every week.

In case the map could inadvertently identify a victim's home, the police had a moment's pause about mapping the location of sex crimes. After a prototype map was developed, their fear was allayed because one dot covered an entire city block.

### Uncontrolled exports

Once the maps were on the Web, we turned to getting them published in the newspaper. What I thought would take a day or two ended up taking more than a year and a half. Turns out Mapinfo does not export data in a graphical form in a high-enough resolution to be used in the newspaper.

I waited about a year for the next upgrade of Mapinfo because an engineer told me exporting would be improved in Version 4.1. It was, but not enough. I later bought Version 4.5, which also did not help.

We eventually heard about Map Publisher, an add-on tool from Avenza (www.avenza.com) that for $495 made exporting to our graphics and pagination system possible. Because of shortcomings in both programs, we still can print only in black and white the weekly map in the newspaper.

### Be careful about...

The address given by the police may not be the address where the crime occurred. A woman is assaulted but drives to her parents' home across town. They call police. The report (at least in Evansville) will list the parents' address because that's where the report was taken.

Some reports will list the addresses of hospitals and police stations because that's also where the victims reported the crimes. They need to be filtered out and handled differently – or it will look like those areas have major crime sprees.

Be careful about theft. Mapping theft can take up lots of time and show nothing. My weekly maps filter out shoplifting because there are hundreds of reports every week.

Consider which crimes deserve weekly reporting. Just because you get all the data doesn't mean you use it all. My maps show all felonies and some Class A misdemeanors, such as sexual battery.

Be careful about arrests. There are two ways to look at mapping crime. When a burglary report is filed, it's because a crime has taken place. When a prostitution report is filed, it's because an arrest has taken place. Just because a lot of arrests are made in a certain area does not mean that's where the prostitutes are. That just means it's where the police are.

Be prepared to fiddle with the "street-level maps" you buy from vendors. Some are old; some are inaccurate. If you live in Washington, D.C., or Detroit, I would expect they are reasonably up to date. But it does take them a while to work their way to Evansville, Indiana. So if someone builds a new subdivision or renames a road from Don Mattingly, then you need to change your database, too. And be prepared for cops who still use old names for roads long changed. Old habits die hard, and the data can be filled with addresses like "540 Old Highway 41" or "540 Business 41 N" or "540 Fares Ave." – all of which are the same place.

Mapinfo is not a beast to be conquered in a few days. If you are going to spend the money for mapping software, include training in the price. It also helps if you know how to use a relational database, such as Access or Paradox, and a spreadsheet for basic tasks.

James Derk can be reached at (812) 464-7409 or by email at jderk@evansville.net
