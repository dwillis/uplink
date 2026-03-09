# Stats from the Road: Continuing with Crosstabs

**By Sarah Cohen**
*NICAR*

Last month's Uplink column had all kinds of reasons to use crosstabs: They're easy to do, easy to understand and easy to explain. But a few key issues were missing. Among them were ways to paraphrase their results to get a key number for your story.

In this month's column, we'll look at three ways to get meaning from your crosstab: relative risk, odds ratios and attributable risk.

Here's a crosstab of uncomplicated births derived from Florida hospital discharge data for one quarter last year. "Insured" means that the women had some kind of traditional fee-for-service insurance. "Medicaid" means the women were covered under the state's health insurance program for the poor. The question: Do women with expensive traditional insurance get C-sections more frequently than women with less generous government-supplied care?

Here are the raw numbers, rounded off to make it easier:

|  | Insured | Medicaid | Total |
|---|---|---|---|
| C-Section | 3,000 | 2,000 | 5,000 |
| No C-Section | 8,000 | 10,000 | 18,000 |
| Total | 11,000 | 12,000 | 23,000 |

Here's how it would look as a simple crosstab, like the ones described last month. The first row is the C-section rate, or the percent of all women within the insurance plans who got C-sections:

|  | Insured | Medicaid | Total |
|---|---|---|---|
| C-Section | 27% | 17% | 22% |
| No C-Section | 73% | 83% | 78% |
| Total | 100% | 100% | 100% |

Of course, this difference could be explained in other ways. For instance, women covered by traditional insurance are typically older than Medicaid recipients, and their pregnancies may be riskier.

But the same kind of analysis might be done within a single age group, like women in their 20s.

Looking just at the row for C-sections, how can you describe the difference?

You could just use the percentage point difference. The C-section rate for women in Medicaid is 10 percentage points lower than those covered through traditional insurance.

But that's a rough sentence for your readers or viewers to swallow. If the difference were much smaller, there'd also be a problem with proportion: Is 1 percentage point a lot?

The simplest correction is to calculate the relative risk of getting a C-section by computing the simple ratio between the numbers. That's how the *Wall Street Journal* reported mortgage denial rates by race for the nation's top lenders a few years ago. In our case, the relative risk is 1.63.

A typical sentence might read: Women in traditional insurance plans get C-sections 63 percent more often than those women covered by Medicaid.

The problem with this approach is that it doesn't work very well if there's no reason to choose one of the rows rather than the other in the crosstab.

Let's say the data reflected pass and fail rates on an employment exam, and you wanted to compare these rates for signs of discrimination. Are you more worried about the difference in pass rates or fail rates? It could make a big difference.

Using the same ratios as above, but just reversing the math, women might have failed 63 percent more often than men, but men would have passed only 15 percent more often than women.

One solution to this problem is the odds ratio. It's pretty easy to compute: Divide the odds for one group by the odds for the other group.

Don't confuse odds with percents. An odds calculation uses its counterpart as its base instead of the total of all groups. The easiest way to remember it is how you figure out betting odds: odds of 3-to-1 mean that you could get a $3 windfall or you could lose $1.

So the odds of getting a C-section with traditional insurance are 3,000-to-8,000 or 3-to-8. For every three women who get C-sections, there are eight who don't. The odds of getting one in under Medicaid are 2,000-to-10,000, or 1-to-5.

The odds ratio is (3/8)/(1/5) = 1.88. That means the odds of getting a C-section under traditional insurance are 88 percent greater than for women covered under Medicaid. (It always works like this: Odds ratios are always higher than relative risk for numbers over 1, and always lower for numbers under 1.)

The most compelling reason to use this ratio, instead of relative risk, is that it doesn't matter how you express your problem.

In the employment exam example, the odds ratio for men passing is the same as the ratio for women failing.

Attributable risk is used most commonly in medical stories, but lawyers have used it for years in product liability and discrimination cases. When you see statements like, "20 percent of all lung cancer could be avoided if everyone stopped smoking," the authors are talking about attributable risk.

It's a little harder to calculate, especially if you have lots of age groups or other control factors.

Here's a shortcut, which works for comparable numbers expressed as percents or any other kind of rate, such as a rate per 100,000 people: 1-(Rate in the control group, or the group not affected / Overall rate)

So for the C-sections, you would calculate it using the top line of the crosstab: 1-(Medicaid rate/ Total rate), or 1-(17/22), or .23. This says that about one-quarter of C-sections could be avoided if doctors paid by traditional insurers acted like Medicaid providers, so long as that's the only important difference between the two groups. Put another way, you could multiply the result by the number of C-sections there were, and estimate the number that might have been avoided: 700.

This is useful when there's a specific outcome you care about, and the proportions are very small, like in cancer clusters.

So is it two-thirds more women get C-sections in traditional insurance, are the odds almost 90 percent higher, or could you have avoided one-quarter of the C-sections among insured mothers if they were in Medicaid?

They're all true, assuming you've controlled for factors like age and health of the mother.

Pick your weapon carefully.

*Sarah Cohen can be reached at (301) 942-2199 or e-mail her at sarah@nicar.org*
