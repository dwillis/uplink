# Mapping soil tests shows legacy of lead

By Tina Lam and Wendy Wendland-Bowyer, *Detroit Free Press*

Lead poisoning is still a big problem in Detroit and other Michigan cities. Because many of our readers think it is old news, we wanted to bring a fresh perspective.

"We didn't want to write an anecdotal story," said Alison Young, then project editor and now an investigative reporter for Knight Ridder's Washington bureau. "We wanted to break news and give readers new information that would get their attention." Our early research showed little had been done to alert the public to the dangers of lead-contaminated soil and the legacy of long-forgotten lead smelters.

Eight reporters, a data analyst and three photographers spent seven months working on a series published in January. We interviewed 300 people, examined more than 10,000 pages of documents, filed a dozen public records requests and performed computer-assisted reporting. Since January, we've written follow-ups and three other major stories, including an analysis of a state database of children's lead test results.

We hired a soil expert who has studied lead left in soil from leaded gasoline – Howard Mielke, professor of environmental toxicology at Xavier University. His team took more than 400 soil samples, spread randomly along lines drawn through the Detroit metro area, from downtown radiating out into the suburbs. They used global positional satellite gear to determine where to dig each sample and then tested them in their lab in New Orleans for lead and other heavy metals.

When we got the soil test data, it arrived with coordinates of where each sample was taken. Victoria Turk, our data analyst, loaded the data into the ArcView 3.2 geographic information system (GIS) program to plot the locations of samples using the latitude and longitude coordinates. She then placed the sample point file over a streets layer and on printed maps. Turk also added a map layer containing the locations of schools hosting children from kindergarten through fifth grade to see how close they were to the contamination locations. Turk obtained the school data from the National Center for Education Statistics Web site (*http://nces.ed.gov*) and geocoded it in ArcView to create a point map.

Turk had to convert the schools data to match the projection of the soil sample layer.

Using the sample maps, reporters and photographers fanned out, interviewing people who lived near the spots we'd sampled. The research showed that lead was highest in the soil in the inner city, with levels dropping near and in the suburbs. Our story talked about similar findings in other cities and the fact that some scientists think contaminated soil is as great a contributor to lead poisoning among children as lead paint and dust.

One of the five days of the series was devoted to a defunct lead smelter in Detroit and the Environmental Protection Agency's failure to notify people nearby that lead might have blown into their homes and yards. We asked the Xavier University team to return to Detroit and sample areas around the smelter. They found elevated levels. The EPA had taken just seven samples before determining there was no neighborhood contamination. We did 100 and found that there was contamination, some of the levels astronomically high. Turk again used ArcView to map the results. She also used EPA's TRI Explorer on the Web (*www.epa.gov/triexplorer*) to find out how much lead and lead compounds had been emitted in the three counties near Detroit.

Our series included graphics showing what we found. It also had plenty of human tales, portraits of families all over the state who had been affected by lead poisoning. One story focused on how the city and state fumbled efforts to abate houses for lead paint and left millions of dollars unspent or used on homes where no children lived.

During the project, we filed a FOIA request asking the Michigan Department of Community Health for its database of the results of all blood-lead tests for young children during the previous five years. The state requires that all clinics or physicians who do blood-lead tests report them to the state. After denying the database existed, the state eventually agreed to give it to us, but only on paper and only for $2,445. It was already too late for the series. But we sued the Department of Community Health in January in Oakland County Circuit Court and won our case – and $10,000 in attorney fees – in June.

The state provided nearly half a million records with names redacted. The main fields were a specimen ID (unique for each test, not each child), test date, result and the child's birth date, address to the block level, race and sex. We wanted to find the most-poisoned blocks in the state and see whether health officials were targeting them.

Megan Christensen, a former NICAR data analyst interning at the *Free Press*, joined us on the story. We used VEDIT to remove formatting glitches in the original file and then ran the addresses through ParseRat to separate a single field into components, such as block, street, direction and P.O. Box. We wanted a clean block and street number for each record. (For more about ParseRat, see p. 16 in this issue of *Uplink*).

The state had rounded the house numbers to the 100s. For example, 1500 Elm represented all houses from 1450 Elm to 1549 Elm, so that's how we defined our blocks. But we also had to separate Southwest Elm from Northeast Elm. We had to visit some of the streets and cross-reference others in street directories to make sure we had it right.

Once we separated the records by block, we had to throw out the duplicates. Some records were redundant because the same child was tested in multiple years. Because we had no names, we settled for a grouping of birth date, race, sex and address to identify each child. Unfortunately, we did not come up with a reliable programming solution to throw out duplicates. Instead, we used Microsoft Access to query the data and group results by block. Then we printed out block results and picked out the duplicates by hand based on matches of birth date, race and sex. Then we ran new block sums to determine how many separate children were poisoned on each block.

This forced us to focus on only the top 10-15 blocks because it would have been too time consuming for every block statewide. Had we been able to eliminate all the duplicates, the story would have produced more concrete numbers. But we were still able to focus on the blocks with the most poisonings and report on those families.

The analyst for the Michigan Department of Community Health admitted they'd never done this. He thought the data was too dirty to eliminate double counting, so had never attempted it. Our story showed that most health officials didn't know which were the worst blocks and were not targeting those areas. The state had even denied funding to one county with some of the worst blocks.

Our lead stories have triggered results. Embarrassed health officials have already started knocking on doors in the poisoned blocks that we found. Days after the January series ended, the EPA announced it would finish the cleanup of the abandoned lead smelter and sample the yards near it. The agency set up a satellite office in the neighborhood, got permission to test widely and discovered that 75 percent of the homes they sampled within one-quarter mile of the smelter had lead-contaminated yards. They're working on cleaning them up.

After another story we did on 16 other old smelters in Detroit that hadn't been investigated, the state sent environmental officials to examine every site. They've discovered that all but three were indeed lead smelters and could still be causing contamination. Soil sampling is in the works.

Our lead stories also led directly to legislation requiring inspectors to check for lead in day care centers. In August the governor introduced a 33-page plan to mount a new attack on lead poisoning, citing our work in the second paragraph. It should generate new legislation on several fronts, including requiring more lead testing and penalizing landlords who don't repair lead-contaminated apartments. We'll be watching.

Contact Tina Lam by e-mail at lam@freepress.com.

Contact Wendy Wendland-Bowyer by e-mail at wendland@freepress.com.

---

### Databases for lead poisoning reporting

Here are some databases journalists can use when reporting on lead poisoning:

**Child blood-lead test data** – often contains a record for each lead poisoning test. Children who are lead poisoned often will receive follow-up tests so they can have more than one record. Data should include the test result, type of test (finger stick or blood draw, for example), date of test, gender, race and age of the child.

**Environmental lead inspection data** – contains detailed information about properties inspected for the presence of lead. Since this data identifies properties rather than poisoned kids, agencies may be more willing to provide a detailed street address. You can also get the name of the owner, test results, building type and inspection results.

**Abatement loan data** – contains information about loans granted by public agencies and housing authorities to homeowners for correcting lead paint hazards. The information includes loan recipient, home address, abatement address, loan amount and loan due date.
