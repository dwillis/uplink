# Ambulance Response Times: Cardiac Crapshoot

**By Jack Dolan**
*Hartford Courant*

When Mike McIntire handed a cardboard box of diskettes across the divider and said, "I don't know if you can do anything with these," I knew I'd taken the right job.

It was my first day at the *Hartford Courant*, my first job since leaving NICAR. McIntire, my new colleague on the investigative team, was working on a story about deathly slow response times by American Medical Response, one of the nation's largest private ambulance companies. AMR made several promises to Hartford officials to wrest the 911 business away from smaller, local companies including responding to 90 percent of serious medical emergencies within six minutes.

## Disks to database

McIntire had heard plenty of stories about AMR failing to meet that standard, but he knew he needed hard data to see if the anecdotes were part of a larger pattern. To that end, he got two years' worth of 911 call records from the Hartford police, who dispatch the ambulances. Each month of records came on a separate diskette as a tab-delimited text file. Those were the disks in the box Mike handed over the divider.

Before long, we'd appended all of the files into a single FoxPro table, calculated the response times by address, and sorted the 50,000 calls so that the one with the longest response time was on top. Then we picked through the data for what doctors say are indisputable emergencies: cardiac arrest, chest pains, and difficulty breathing.

We found that 34 percent of these most vulnerable patients waited more than six minutes for their ambulance – three times the number the AMR contract allowed. Hundreds of verified heart attack victims waited longer than ten minutes. Some waited longer than twenty minutes. Over two years, the number of people put at serious risk by long response times reached into the thousands.

Emergency medicine experts across the country told us that dangerously long response times are bound to happen once in a while. That's why ambulance companies, when negotiating contracts, make sure to give themselves a cushion 10 percent of the time; 34 percent shocked the experts. We were told that if we wanted to discover what happened to those who waited the longest, the best place to start checking was the morgue.

## Joining death records

So we requested a database of all recorded deaths in Connecticut from the Department of Health. Among the fields in the death data were the name and address of the deceased and the date of death. The 911 records had no names of victims, but they did have the date of the call and the victim's address.

> Once we had the hard numbers that showed just how long AMR's response times are, the rest of the CAR work just helped make an already strong story stronger.

We joined the databases on two criteria. The first was where the addresses matched. The second was when a death was recorded within one day after a wait of more than 10 minutes after a 911 call for someone suffering from one of those three most serious emergencies. A sad roll call of silent victims filled the screen. Through interviews with these victims' families, police, EMTs and AMR executives, we discovered that, like everyone else who waited too long for an ambulance, most of the dead fell into three distinct categories.

## Mapping the calls

First, some seemed to have to wait too long for the ambulance because of where they lived. We grouped all of the addresses of calls that took longer than six minutes into census tracts, then mapped the tracts using ArcView. Each tract was a different shade depending on the percentage of calls that took too long – the darker the color, the longer the response time.

The darkest tracts were on the extreme northern, southern, and western edges of the city. We expected a lot of long response times in the north, since it is the poorest part of Hartford. But the west is the wealthiest, and the darkest-colored southern tract is home to the mayor and many long-time Democratic city bosses. So much for the old adage about city services being best on the mayor's own street.

The explanation, it turned out, is that AMR retrenched on an agreement to keep a certain number of ambulances based on the edges of the city at all times. Instead, the company reduced the number of ambulances available, rotating those that remain between the city's hospitals, which are located in the center of Hartford.

A second apparent predictor of whether an ambulance would come quickly was the time of day. We expected to find that most of the longer calls happen in the early evening, when the 911 call volume is highest. Our logic was simple: if two people are waiting for one ambulance, somebody has to wait longer.

Instead, we found response times are longest at mid-morning when 911 call volume is very light. Several EMTs explained that the peak hours for the lucrative business of shuttling non-emergency, well-insured patients home from the hospital are between 10 a.m. and noon, just after doctors have made their rounds and discharged patients. Therefore, AMR is loath to send an ambulance off on a 911 call during those hours since the company has a much better chance of getting paid for the high priced taxi service.

A third contributor to long ambulance response times was the medical ignorance of some police officers thrust into the ambulance dispatcher role, often with very little medical training. We found 20 percent of confirmed cardiac arrest cases were not initially classified by police dispatchers as emergency calls, so the ambulance driver was not put on the highest alert.

Since our investigation, the *Courant* ran several stories on AMR's poor performance in Connecticut and the company's problems holding onto contracts in other parts of the country.

## Story prompts suit

Finally, in early June, the state of Connecticut reached an anti-trust settlement with AMR. The settlement forced the company to give up 30 ambulance licenses to its competitors and give up 40 percent of the Hartford market.

In Hartford, ambulances are dispatched by the police and not by the ambulance company. That was key to our investigation, because it meant the dispatch database was a public record.

Once we had the hard numbers that showed just how long AMR's response times are, the rest of the CAR work just helped make an already strong story stronger.

Jack Dolan can be reached by e-mail at dolan@courant.com
