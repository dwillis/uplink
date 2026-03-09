# Adding the 3rd dimension

By Stephen K. Doig
*Arizona State University*

A few months ago, I was wowed by a demonstration of a mapping tool that was new to me. It was 3D Analyst, an extension to ESRI's popular ArcView geographical information system (GIS) software.

3D Analyst can take a two-dimensional map, such as a thematic map of census tracts, and transform it into a three-dimensional image in which the height of each area on the map can represent another variable. The resulting depiction of data, which looks like a cityscape of skyscrapers, can then be "explored" by turning it every which way, zooming in and out and even flying through it up close.

I decided I had to learn how to use this cool toy. Like most journalists interested in computer-assisted reporting, I learn new tools best when I have some real journalistic task to accomplish. The trick was to find something interesting to do.

I knew that an extension like 3D Analyst adds substantial new capabilities to the base GIS software, but also substantial new costs. 3D Analyst lists for $2,500, out of reach for all but the most well-heeled newsrooms — or for the lucky people like me who can afford to pay lower academic licensing costs. So I posted a note on NICAR-L listserv offering a free 3D map to the first newsroom that offered me a project with which I could learn the basics of this tool. Full trial versions of the extension for ArcView versions 3.x and 8.x are available on CD from ESRI.

Janet Roberts of the *St. Paul Pioneer-Press* quickly took up my offer. Having seen a nice 3D map of median income change data created by the *Chicago Tribune* (see *http://images.chicagotribune.com/media/graphic/2002-08/4286800.gif*), she wanted to do something similar for the city of St. Paul, looking at percentage change in median household income since 1989. However, she needed it in less than a week, and I fretted it would take me longer than that to figure out the software. (I do have a full-time job, you know.) But I gulped and said, "Sure, I can do it."

Turns out I needn't have worried. If you already know how to use ArcView, doing the basic work with 3D Analyst is a snap. So here's a handy step-by-step for ArcView 8.x in case you get your hands on the extension:

- The first step is to activate the 3D Analyst extension. Assuming you have installed and registered 3D Analyst, just launch the ArcMap application, then choose Tools\Extensions in the menu and click on the box next to 3D Analyst.

- Next, prepare the shapefile (a map file with associated data) that you want to turn into a 3D image. You can do this in ArcView, just as you already know how to do. Janet sent me a shapefile of St. Paul Census tracts already loaded with an attribute table that included for each tract the median household income for 1989 and 1999, the dollar change and the percentage change.

- To make a 3D image, launch ArcScene, which is 3D Analyst's workspace. You'll see that it looks a lot like ArcView, except with a few different buttons. Make sure you have the 3D Analyst toolbar turned on.

- Hit the Add Data button and find your shapefile. You'll see the expected map in one color, but at an odd angle. That's because the map already is in 3D. Click on the Navigate tool (the one that looks like a compass with four points) and then use the mouse to move the map around a bit, just to see how it works.

- Now right-click on the layer name and open the Properties window. You'll see the usual tabs, including Symbology where you can choose "Quantities...Graduated Color" to make the usual thematic map. Go ahead, make that map. So far, nothing much new.

- But notice that the Properties window has a few unfamiliar tabs, including Extrusion. That's the one that's going to give you the 3D effect. Click on the "Extrude features in a layer" box, and then the little calculator-like icon to the right of the expression box.

- In the Expression Builder window that pops up, click on a field you want to have provide the height (or z-value) variable. It can be anything numeric – altitude, population, density, income, percent, whatever. Tell it OK, then Apply.

- Here's the tricky part. Chances are, the variable's value by itself won't do what you want. If the values are small, it may not show much height at all; if they're large, the height may shoot off the screen. In either case, go back to the expression builder window and multiply the variable (if it was too small) or divide (if too high) by some arbitrary number, let's say 100. Your expression then might look something like [PCTCHG]*100. Hit Apply.

- If the new expression works, great. If still not, then pick another value in the right direction and try again until it starts to look like you want it to.

- Now explore the image using the Navigate and other pointers on the ArcScene toolbar. Note that you can twist and turn the image and even look underneath, so that it seems to be like Laputa, the flying island of "Gulliver's Travels." When you look underneath, you'll see that any areas with negative values are extruded downward. Move it around until you have an angle that illustrates what you are trying to show.

- Finally, go to File\Export Scene\2D on the menu to save the image in whatever graphics format you want.

3D Analyst will do much more than simply making a 3D version of a flat thematic map. But I'll learn more of those capabilities when someone comes to me with another project to try. Maybe it'll be you?

Contact Steve Doig by e-mail at steve.doig@asu.edu.

*Would you be willing to share a mapping example with fellow journalists? Send an electronic copy of the map along with details to David Herzog at dherzog@nicar.org*
