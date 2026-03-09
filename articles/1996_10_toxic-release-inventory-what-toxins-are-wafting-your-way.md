# Toxic Release Inventory
## What toxins are wafting your way?

**By Greg Reeves**
The Kansas City Star

For a high-impact story using one of the most interesting databases around, take a look at the Toxic Release Inventory data from the Environmental Protection Agency.

Company by company, across the nation, you can produce fascinating reports on the toxic pollutants that waft into our air, float down our rivers, are dumped in a landfill or — the way some toxins are removed — are shot a mile underground.

### Good for beginners

If you are a beginner at computer-assisted reporting with no more than a spreadsheet at hand, the TRI database would be an excellent entry point — it's cheap, clean data with lots of public interest.

If you've thrown around a few gigabytes, you can generate great maps offering a detailed portrait of pollution in your community, neighborhood by neighborhood.

Since 1987, federal law has required companies to report "toxic releases" to the EPA. They must report what chemicals were involved and what amounts (in pounds) ended up in the air, land, water, sewer or storage site. Each chemical emission is a separate report. And each report becomes a record in the TRI.

The easiest way to get the data you want is probably a call to your local EPA office, state environmental office, or NICAR. Various Web sites also offer some TRI data.

TRI data is not harmful to your computing environment. The files are roughly one megabyte per state per year. Missouri data, for example, contained 1,845 records for 1994 and fit neatly on one diskette. That included mid-Missouri lead smelter country, where lead emissions in some places total nearly 12 tons per child.

### What's in the data

There are 38 fields in the TRI database, and by now you are surely hungry to know them. Basically half the fields identify the "facility," or company site, and the other half identify the chemical and where it went.

For each facility you get: an ID number, name, street address, city, state and zip; parent company (if any) and contact name and phone; and, for map-making purposes, the latitude and longitude of the facility.

For each chemical you get an English name (acetone, styrene, zinc, 1,2,4-trimethylbenzene, etc.), and a unique identifying code from the Chemical Abstracts Service (CAS) registry. Use the CAS number rather than the chemical name to sort and group data.

For each release, you get: how much went up a smokestack ("stack" air); how much just drifted away ("fugitive" air); and how much went into the water, in the ground, to sewers or to offsite recycling plants.

Finally, each record contains one or more industry codes and federal ID numbers to help identify the facility.

### How to use it

One of the best uses you can make of the TRI data is to report how pollution has changed in your community over the past eight years.

Have the worst companies from the 1980s cleaned themselves up? In FoxPro, you might want to find the biggest overall polluters first:

```
SELECT tri_id, facility, SUM(alw);
FROM tri;
GROUP BY 1;
ORDER BY 3 DESC
```

The first field, tri_id, is the facility ID number mentioned above. The "alw" field ("air-land-water") is the sum of stack-air, fugitive-air, land emissions and water emissions. Another handy add-up is stack-air plus fugitive-air, which equals total air pollution.

This query will give you a company name at the top and some huge number of pounds-emitted. Take the first 10 or so companies and see how they've fared since 1987:

```
SELECT tri_id, year, facility, SUM(alw);
FROM tri;
WHERE INLIST(tri_id, "1st tri_id", "2nd tri_id...");
GROUP BY 1,2 ORDER BY 1,2,3 DESC
```

You're on your way to a story that people need to know. And there's much more. Maps bring out TRI's impact in vivid clarity: per capita toxic waste, the most polluted ZIP code, the center of zinc toxicity in your community.

## Cancer-causing chemicals

Not all of these 75 known carcinogens may show up in the TRI data for your area. In the Missouri and Kansas data for 1994, for example, 48 of the chemicals appear. The following list includes the CAS number, followed by the chemical name and can be used in a look-up table.

- 000140885 — Ethyl Acrylate
- 000151564 — Ethyleneimine
- 000075218 — Ethylene Oxide
- 000096457 — Ethylene Thiourea
- 000050000 — Formaldehyde
- 000118741 — Hexachlorobenzene
- 000302012 — Hydrazine
- 010034932 — Hydrazine Sulfate
- 007439921 — Lead
- 000058899 — Lindane
- 000101144 — 4,4'-Methylenebis (2 Chloroaniline)
- 000101779 — 4,4'-Methylenedianiline
- 000090948 — Michler's Ketone
- 000134327 — Alpha-Naphthylamine
- 007440020 — Nickel
- 000139139 — Nitrilotriacetic Acid
- 000079469 — 2-Nitropropane
- 001336363 — Polychlorinated Biphenyls
- 001120714 — Propane Sultone
- 000075558 — Propyleneimine
- 000075569 — Propylene Oxide
- 000081072 — Saccharin (Manufacturing)
- 000100425 — Styrene
- 000096093 — Styrene Oxide
- 000127184 — Tetrachloroethylene
- 000062566 — Thiourea
- 000584849 — Toluene-2,4-Diisocyanate
- 000091087 — Toluene-2,6-Diisocyanate
- 026471625 — Toluene Diisocyanate (Mixed Isomers)
- 000095534 — O-Toluidine
- 000088062 — 2,4,6-Trichlorophenol
- 000051796 — Urethane
- 000593602 — Vinyl Bromide
- 000075014 — Vinyl Chloride
- 000075070 — Acetaldehyde
- 000060355 — Acetamide
- 000079061 — Acrylamide
- 000107131 — Acrylonitrile
- 000060093 — 4-Aminoazobenzene
- 000092671 — 4-Aminobiphenyl
- 000090040 — O-Anisidine
- 007440417 — Beryllium
- 000542881 — Bis(Chloromethyl) Ether
- 000106990 — 1,3-Butadiene
- 007440439 — Cadmium
- 000056235 — Carbon Tetrachloride
- 000067663 — Chloroform
- 000107302 — Chloromethyl Methyl Ether
- 007440473 — Chromium
- 008001589 — Creosote
- 000120718 — P-Cresidine
- 000135206 — Cupferron
- 000615054 — 2,4-Diamino Anisole
- 000101804 — 4,4'-Diaminodiphenyl Ether
- 025376458 — Diaminotoluene (Mixed Isomers)
- 000095807 — 2,4-Diaminotoluene
- 000106934 — 1,2-Dibromoethane
- 025321226 — Dichlorobenzene (Mixed Isomers)
- 000106467 — 1,4-Dichlorobenzene
- 000091941 — 3,3'-Dichlorobenzidine
- 000107062 — 1,2-Dichloroethane
- 000075092 — Dichloromethane

## Reproductive toxins

Not all of these chemicals, which are known to damage reproductive organs, may show up in the TRI data for your area. The following list includes the CAS number, followed by the chemical name, useful for look-up tables.

- 000071556 — 1,1,1-Trichloroethane
- 000071432 — Benzene
- 007440439 — Cadmium
- 000020042 — Cadmium Compounds
- 000075150 — Carbon Disulfide
- 000106898 — Epichlorohydrin
- 000107211 — Ethylene Glycol
- 000075218 — Ethylene Oxide
- 000020100 — Glycol Ethers
- 007439921 — Lead
- 000108383 — M-Xylene
- 007439965 — Manganese
- 007439976 — Mercury
- 000095476 — O-Xylene
- 000106423 — P-Xylene
- 000100425 — Styrene
- 000127184 — Tetrachloroethylene
- 000108883 — Toluene
- 000079016 — Trichloroethylene
- 001330207 — Xylene (Mixed Isomers)
