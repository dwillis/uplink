## Diagnosing hospital health — 'Vital Signs'

**By Rick Linsk and Paul D'Ambrosio**
Asbury Park Press

How healthy are New Jersey hospitals?

A year ago, we asked ourselves that question at the Asbury Park Press. The answers turned into "Vital Signs," a series that ran from July to December and rocked the state's medical establishment.

The project's roots go back two years, to the day someone slipped projects reporter Rick Linsk several pages of statistics on all New Jersey hospitals, including mortality rates, mortality rates after cardiac bypass surgery, and Cesarean section rates.

Thinking these might be internal reports from the state Department of Health, Linsk called there. Not us, officials said; the state publishes no such performance measures on hospitals. But, they said, if you have $1,600 handy, we can sell you the data and you can do it.

We were struck by this irony. In the very area where the stakes were so high — literally life and death — it is virtually impossible for consumers in New Jersey to get any meaningful information about their hospital or doctor. Across in the border in New York and Pennsylvania, by contrast, state agencies routinely publish bypass-surgery mortality rates and other figures for the public.

### Jumping in

We took the plunge. The first step was buying New Jersey's hospital uniform billing or "UB" data. About 30 states sell these inpatient discharge records, which contain demographic information such as age and gender plus myriad fields for conditions diagnosed and procedures performed. The price varies by state. To find out whether your state sells the data, contact the National Association of Health Data Organizations (703-532-3282).

Diagnoses and procedures are represented by codes under the International Classification of Diseases (ICD for short). You can decipher them with a $17 CD-ROM sold by the National Center for Health Statistics. Several medical publishers put out coding manuals that are good to have handy.

Using UB data for medical research is not without controversy. Pitfalls include inconsistency in coding between hospitals, especially when it comes to areas with fuzzy definitions like various complications of labor. Experts also question whether hospitals reliably code their mistakes. And experts point out that the ICD codes do not yet distinguish between ailments that patients came in to the hospital with and those they acquire during their stay (pneumonia and infections being prime examples). Despite all this, a growing number of health researchers are using UB data because it's the best and only database available.

New Jersey's public UB records identify the hospitals, but not doctors' or patients' identities. Date fields are also scrubbed. Some states reportedly withhold even the hospital names.

### Next hurdle

If you get this far, the next hurdle is risk adjustment. Hospitals argue, and experts agree, that it's unfair to compare hospitals that have different kinds of patients. The place with a higher mortality rate may have older or sicker patients. To compare apples and apples, you have to adjust for the patient case mix.

We briefly considered trying risk adjustment in-house using SPSS's logistic regression, but quickly became convinced it would not be a wise move. (Logistic regression takes string variables and predicts relationships. In medical data, it will tell if there is a strong relationship between, say, diabetes and kidney failure.)

The major concern was credibility. We were about to launch the most ambitious review of hospitals in the state's history. We were going to tell 7.7 million residents which hospitals were great and which ones were killing too many patients. Our information had to be solid, and we had to present evidence that was acceptable to the medical and regulatory communities. No one would take us seriously unless we used a well-known vendor who did risk-adjustment for hospitals and insurance companies.

Fortunately, we were able to forge a relationship with Inforum, Inc., a Nashville, Tenn., company whose parent firm, MedStat, essentially invented the medical risk-adjustment methodology 15 years ago. Inforum was looking to break into the New Jersey market and we were looking for attack-proof data.

Inforum provided us risk-adjusted data in three areas: cardiac bypass surgery, stroke treatment and pneumonia/influenza care. We got the adjusted death rates, adjusted lengths of stays, and complication rates in each area and compared it to hospitals in eight other states. This was the basis for the report cards we published.

We went a step further and extracted insurance, demographic and geographic data from the UB tapes. This helped us show how minorities of all ages were less likely than their white counterparts to undergo bypass surgery or pneumonia treatment. We also found women with insurance were more likely to have C-sections than poor women insured by Medicaid. Rates varied too between cities and suburbs.

### Words of caution

Don't trust anybody or anything. We found errors with the raw UB data (incorrect hospital ID numbers), and Inforum's information (they told us one facility did not note secondary diagnoses when it did). Send your results to your target hospitals before you run and ask them to provide any data that is inconsistent with yours.

Be prepared for a heavy barrage of misinformation, lies and damn lies from all fronts.

Hospital executives and trade groups will talk out of both sides of their mouths. In the same breath that they disparage your consultant's work, they will tell you they use the same data for their own internal reviews. Ironically, the hospital association — which laughed at an early inquiry from us about how to examine the discharge data — came in mid way through the series and asked to work with us. Our response: Pucker up and kiss our...

The impact of the series was almost immediate. The state's health commissioner promised to issue his own bypass report card in 1997, moved to standardize stroke and pneumonia care, promised to beef up his hospital inspection staff, and crack down on a Newark bypass center that was violating its license.

Rick Linsk and Paul D'Ambrosio can be reached at (908) 922-6000, or send e-mail to linsk@app.com or to pmd@app.com. The series can be found on-line at www.app.com
