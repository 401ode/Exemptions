# Tax Exemptions Report

## Files and Directories
* `Abnormalities` contains CSVs relating to the issues described below.
* `Map Layers` contains files related to exemption visualization, currently viewable at [PVD Tax Map Exemption Flag](https://ryankelly23.carto.com/viz/2ac6ece4-63ec-11e6-aed9-0ef24382571b/public_map "PVD Tax Map Link"), 
[PVD Tax Map by Exemption Size](https://designist.carto.com/viz/e7a729a8-63e4-11e6-85e0-0e05a8b3e3d7/public_map "PVD Tax Map Link")
* `Pivots` contains CSVs created by Excel pivot tables. These are the basis for the data analysis section below.
* `2016_Original.csv` contains the original CSV file provided by [data.providenceri.gov](data.providenceri.gov).
* `Worksheet.xlsx` contains all working files for this repository, including the below-referenced pivot tables and error documentation.

## Data Analysis
There are 44,339 property records in the 2016 PVD Tax Roll
7,469 property records have exemptions

##Totals
| Year | Description                              | Total           |
|------|------------------------------------------|-----------------|
| 2016 | Sum of Exemptions                        | $9,662,523,513  |
| 2016 | Sum of Total_Assessment                  | $20,006,059,962 |
| 2016 | Percent Exemption                        | 48.3%           |
| 2016 | Total Parcels Area                       | 594,288,682     |
| 2016 | Non Residential Exempt Area              | 222,154,846     |
| 2016 | Percent Non Residential Exempt Area      | 37.38%          |
|      |                                          |                 |
|      |                                          |                 |
| 2015 | Non Residential Exempt Total_Assessment  | $576,316,375    |
| 2015 | Non Residential Exempt Total_Exemptions  | $576,316,375    |
| 2015 | Sum of Exemptions                        | $588,108,773    |
| 2015 | Sum of Total_Assessment                  | $1,279,696,970  |
| 2015 | Percent Exemption                        | 45.96%          |
|      |                                          |                 |
|      |                                          |                 |
| 2014 | Non Residential Exempt Total_Assessment  | $834,510,000    |
| 2014 | Non Residential Exempt Total_Exemptions  | $834,510,000    |
| 2014 | Sum of Exemptions                        | $861,602,822    |
| 2014 | Sum of Total_Assessment                  | $2,247,265,037  |
| 2014 | Percent Exemption                        | 38.34%          |

###Non-residential exemptions
There are 2,587 properties with the Levy Code (E01) Non Residential Exempt.  11 of which do not list an exception (Total_Exem)

| Year |       Description        | Total Properties | Total_Assessment | Total_Exemptions  | 
|------|--------------------------|------------------|------------------|-------------------| 
| 2016 |  Non Residential Exempt  | 2,587            | $9,336,605,700   | $9,334,760,900    | 

* The "Vote of City" class has by far the highest average exemption among non-residential exemptions, with an average of over $77 million. Among other exemptions, the "44-3-9 Stb" and "Miscellaneous" categories see the highest exemptions, with an average of about $2.5 million each. Interestingly, these are the only two major categories of other exemptions where the assessment is always equal to the exemption value.
* Non-residential exemptions total $9,334,760,900 in value, while other exemptions total $327,762,613. The average non-zero, non-residential exemption is 54 times larger than the average other non-zero exemption.
![top15nonres](https://cloud.githubusercontent.com/assets/13228316/17568508/0a98a59a-5f12-11e6-916b-c00d9b211efc.PNG) ![top15other](https://cloud.githubusercontent.com/assets/13228316/17568519/168784a2-5f12-11e6-9869-ac553e1f8a60.PNG)

###Class Types 
There are a variety of Class Types within the exempt properties including commercial, owner occupied residencies, etc.  Table below includes modified/combined class type categroies.

|     Row Labels    | Count | Sum of Total_Assessment | Sum of Total_Exemptions | Difference   | 
|-------------------|-------|-------------------------|-------------------------|--------------| 
| School            | 451   | $4,336,022,000          | $4,336,022,000          | $0           | 
| Hospital          | 247   | $1,674,640,700          | $1,674,640,700          | $0           | 
| Municipal         | 617   | $1,154,966,800          | $1,154,966,800          | $0           | 
| Vote of City      | 11    | $851,685,700            | $851,685,700            | $0           | 
| State             | 305   | $629,091,500            | $629,091,500            | $0           | 
| Charitable/Church | 890   | $624,810,700            | $624,810,700            | $0           | 
| Residential       | 4785  | $1,065,803,700          | $133,703,674            | $932,100,026 | 
| Cemetary          | 16    | $72,673,300             | $72,673,300             | $0           | 
| Federal           | 19    | $71,627,700             | $71,627,700             | $0           | 
| Library           | 15    | $60,586,500             | $60,586,500             | $0           | 
| Amtrak NRR        | 51    | $22,701,800             | $22,701,800             | $0           | 
| Miscellaneous     | 21    | $21,400,962             | $18,027,488             | $3,373,474   | 
| Commercial        | 11    | $9,263,900              | $7,619,366              | $1,644,534   | 
| Vacant Land       | 25    | $2,778,200              | $2,296,609              | $481,591     | 
| Industrial        | 3     | $1,464,600              | $1,109,676              | $354,924     | 
| (blank)           | 2     | $960,000                | $960,000                | $0           | 
| Total Properties  | 7469  | $10,600,478,062         | $9,662,523,513          | $937,954,549 | 

## Abnormalities
*	As stated in the filtering section, 11 records with Levy Description “Non Residential Exemption” have Total_Exemptions equal to $0.00. These are stored in the “No Exemption Errors” spreadsheet.
*	There are 5 records with exemption value greater than their assessment value. These are stored in the “Exemption > Assessment” spreadsheet, and sum to an error of $84,662. Four out of five of them have class description, “Residential Vacant Land.”





