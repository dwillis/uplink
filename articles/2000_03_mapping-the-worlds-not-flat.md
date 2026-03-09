# Mapping: The World's Not Flat

**By Andy Lehren**
*Dateline NBC*

It sounds obvious: the world is round.

Aristotle knew that back around 350 B.C. Ptolemy refined it a few hundred years later. Despite fears from the flat earth believers, Columbus made a living off the idea.

The problem is knowing the exact shape of our sphere.

You don't have to be sailing for a new world to face the question. All you have to do is get a few disparate maps and try to make them work in your GIS program.

There are two fundamental questions to ask when you get a map from anyone: what's the datum, and what's the projection. There are other details that may be helpful, but these are the most important. This column will try to explain datum, and how to convert it when you have to.

Some more history: Isaac Newton wrote in the late 1600s that, well, the earth's a bit flattened on the top and bottom. The French, after measuring their country around the same time, countered that it's more egg shaped. Newton won the debate. The French ate better food. And we live with the question: just how flat on the top and bottom?

Ever since, geodesists have been measuring this. There are hundreds of calculations that have been done figuring out our little ellipsoid. Here are the three that matter:

- **Clarke 1866**, developed by Alexander Ross Clarke. He was a busy guy, so the year is important.
- **Geodetic Reference System 80 (GRS 80)**, a group effort by an international geodetic organization.
- **World Geodetic System 84 (WGS 84)**, founded by the U.S. military and close to GRS 80, but not exactly the same.

These different measurements of our spinning ellipsoid are the underpinnings for almost all the maps we look at. You can tell from the history that this is still evolving, and you may well face other datums as you do more mapping.
