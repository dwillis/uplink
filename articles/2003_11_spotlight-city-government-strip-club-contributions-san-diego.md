# Showing contributions from strip-club workers

By David Washburn, *The San Diego Union-Tribune*

At first blush it sounds like the premise for an episode of a TV drama chronicling the adventures of a hard-nosed newspaper reporter:

The reporter hears rumors that a strip club owner from Las Vegas bribed a few city councilmen, hoping that they will push through legislation that would allow more touching between strippers and their customers. The FBI gets wind of it and plans an afternoon raid at city hall.

The reporter gets a tip about the raid from her sources at city hall. The raid goes off as planned and the reporter has a blockbuster story.

That's what happened in San Diego. FBI agents in May visited the offices of city council members Ralph Inzunza, Charles Lewis and Michael Zucchet and seized their files, telephone records and computer hard drives. Federal agents suspected the three had solicited bribes from Michael Galardi, the owner of two strip clubs in San Diego and several more in Las Vegas.

That was where the similarities between a TV script and reality ended.

In TV-land, the strip club kingpin hires a couple of goons to whack the city councilmen. The reporter walks in on the goons getting ready to do the dirty deed. Using her martial arts skills, she knocks out the goons and the grateful councilmen confess.

But in real life everybody hired lawyers, the FBI stayed quiet and all the journalists in town hounded their frazzled city hall sources. Following the money and establishing a link between the councilmen and the strip club owner through traditional reporting was far easier said than done.

This is the spot *Union-Tribune* reporter Caitlin Rother found herself in during the days after the raid. She heard lots of rumors about Galardi and the councilmen but little in the way of hard facts.

She later got some of the hard facts from a database of campaign contributions that we built on the fly using Microsoft Access.

An analysis of the database showed that people involved in the adult entertainment industry had given more than $20,000 to the three councilmen and two other council members whose offices were not searched by the FBI.

We were able to show that strippers and bouncers were giving to the campaigns of the three councilmen. Also, we found thousands of dollars in contributions coming from Nevada, especially from Las Vegas "homemakers."

Here is what else we found:

- Campaign finance reports varied in the way they listed people associated with the adult entertainment industry and their occupations, employers and home addresses. For example, someone listed as an entertainer or waitress on one report would be listed on another as a student, homemaker or some other less obvious affiliation. Some donors had unlisted occupations.

- Several people who were listed as giving the maximum $250 contribution to more than one candidate listed apartment addresses in less-than-affluent neighborhoods that usually are not home to political donors.

- Many contributions from people in the industry were given on the same day. This fact helped Rother confirm low-profile fund-raisers held by lobbyists for the industry.

I was thrilled with the final results, but wish that the database had been built prior to the raid. The newsroom had not realized before how important it is to have a database of local campaign contributions on hand.

### Building the database

Rother needed to do a thorough analysis of years worth of campaign contributions, and she needed to do it fast. The problem was that San Diego, like the vast majority of municipalities, does not require candidates to file their contribution reports electronically. So she ended up with a box filled with dozens of reports containing thousands of contributions.

I uttered a swear word and began pounding my head on my desk. I had been pushing for a few years to have the newsroom create a database of local contributions. These databases are great for seeing who candidates may be indebted to politically.

The editors had agreed and made creating the database a newsroom priority. But, as is so often happens in newsrooms, the news of the day trumped preparing for the future. The database never got built, so we were caught unprepared when the city's biggest political scandals in a decade hit.

Nonetheless, we decided that a database of contributions to the three councilmen and two other council members who we knew had received money from Galardi was crucial for our reporting.

I created a table for the contributions and then built a data-entry form using Access' form wizard. Whenever possible, I used tools on the form to speed the data entry. For instance, someone could pick the name of a city council member from a list to enter that name into the recipient field of the table.

After that, we rounded up some news assistants, brought in a temp with data-entry skills and went to work entering details such as the name, address, occupation and employer of the contributor. We also entered the amount given and to which council member.

After more than a week of grueling data entry we had three years of contributions for the five council members.

Not long after that I caught a mistake. Some contributions had been entered twice because of addendum reports filed by the candidates. When candidates need to make a correction or addition to a report, they file the entire report over again, which means that, in some cases, the same contribution is reported twice.

It is easy to spot an addendum if you are looking for it. But a few slipped through. So I spent another day typing the data from the addendums into a table and then joining that table to the main table to identify the duplicates and remove them using a delete records query. We ended up with 7,500 records.

While the news assistants and I built the database, Rother mined her sources for names of people associated with Galardi. She compiled more than two dozen names with suspected ties. We queried the database to see whether they had contributed and found that almost everyone on the list had given to the candidates. And we found that a vast majority of those people worked for Galardi. In addition, we noticed that their occupations had been listed differently.

A federal grand jury indicted the three councilmen, Galardi and two lobbyists in August. All of them were charged with wire fraud and five of the six with extortion.

The time and the effort that went into the database were worth it and bolstered the story. Our earlier stories about the federal probe would have been much stronger if we had built the database sooner and used it.

Contact David Washburn by e-mail at david.washburrn@uniontrib.com.
