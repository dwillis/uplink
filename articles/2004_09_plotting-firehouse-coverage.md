# Plotting firehouse coverage

By Thomas Gaumer
*The (Cleveland) Plain Dealer*

As part of a regionalism series, *Plain Dealer* reporter Martin Stolz decided to explore fire services. A central question was whether greater Cleveland had duplicative fire departments, equipment or stations. He quickly realized the fire stations element was a story best told visually.

Cuyahoga, the county around Cleveland, has a total of 103 fire stations. Stolz wanted to see if the county really needed that many, or if perhaps consolidation might save taxpayers millions of dollars without affecting firefighting abilities.

Stolz discovered that Cuyahoga County exceeds the national median by 47 stations, 42 ladder trucks and 67 pumper trucks. To tell the story in more than just the dull numbers, Stolz turned to mapping.

The *Plain Dealer* was making the switch from ESRI ArcView 3.3 to ArcView 8.3 and this was the first chance to do a major map with the new software. A lot of what we did was trial and error to find out what worked best to get the map to the graphics department.

The result was a map of the location of every fire station in Cuyahoga County with a one-mile radius around it. We decided on a mile, even though fire stations cover far more than a mile, because those circles showed the proximity of stations and where they overlap, particularly in the southeast area of the county. Smaller circles also avoided a cluttered map.

Generating the map was easy.

We wanted ArcView to geocode all the fire stations so we would have a dot on our map for each station. But as anyone who has done geocoding – creating map points based on street addresses stored in a data table – can attest, you rarely get 100 percent results. But we needed 100 percent.

**To tell the story in more than just the dull numbers, Stolz turned to mapping.**

To geocode, we used a map from the Street Map extension we had purchased with ArcView 3.3. Using 3.3, we made a shapefile of streets in the *Plain Dealer's* coverage area, and ArcView 8.3 read that file. We set up a geocoding service based on that file.

Stolz had created a Microsoft Excel spreadsheet with every station in the county. He called each community as he had time and typed in the address, city and ZIP code. He also assigned each a station identification number. Then it was simply a matter of converting this Excel file to dBASE, which ArcView can open.

On our first pass through geocoding, ArcView plotted all but 15 of the 103 stations. That's when the hard part started.

For several addresses, ArcView had the street name, but not an exact address, and we were able to force ArcView to geocode those addresses using a nearby address. Because of the size of the map, the reader would never be able to tell we had slightly moved a station's address.

Then it got harder, and there were still a half dozen or so addresses where there was no match at all. ArcView just didn't have any suggestions.

So we turned to the data in the streets shapefile to determine why ArcView would not find what we knew were real streets. The shape file had thousands of records so we used ArcView's sort function to alphabetize the names of the streets.

Sure enough, we found one street that was not even in ArcView. It was barely more than an alley, yet it was the legal address of the fire station. We proofread the map carefully and noticed that ArcView had put one station in the wrong suburb, although it was practically on the city line.

We turned to the paper copy of the reverse directory and looked up a known address on a major street very close to that alley. So we deliberately gave some stations the wrong address from the standpoint of the post office, but perfectly fine for ArcView.

In the case of the station that was in the wrong suburb, we had to assign a new address that was slightly changed to move it into the correct suburb. Because we did not want the station to appear twice, we used ArcView's edit table function to delete the old record from the database. Once it was deleted, the dot disappeared.

Perhaps the most puzzling to us, however, was ArcView's failure to assign stations or even to see a road named SOM Center. This is a major state route in Cuyahoga County, and it didn't make sense that it did not exist in ArcView.

SOM stands for "Solon-Orange-Mayfield Center." The letters are officially separated by periods, as in "S.O.M.," though we entered it without, as is common practice.

When we turned to the dBASE file with the fire stations, we found that ArcView had changed the name of the road to "S. O M Center Rd." The S should have been part of the name, but to ArcView, it was "South." The "OM" in SOM was seen as "O M," with a space between the letters.

Once we found the problem it was easy enough to fix. We just changed the addresses of the stations that would not geocode to S. O M Center Road. ArcView geocoded them easily.

We had gotten a map of all the communities of Cuyahoga County from Cleveland State University and added that as a layer.

Stolz had numbered all the stations, so we told ArcView to label the stations with the corresponding number on a large chart with information about each fire department.

It was easy to draw the one-mile radius around each station using ArcView's buffer wizard and telling it we wanted a buffer of one mile. At first, ArcView made circles appear as ovals, which signaled that we needed to pick a better map projection. After we selected a projection for northern Ohio the ovals turned into circles.

We exported the map in the Adobe Illustrator format and our graphics staff was able to open it with Illustrator and change colors and reposition numbers and names as they wanted.

Contact Thomas Gaumer by e-mail at tgaumer@plaind.com.
