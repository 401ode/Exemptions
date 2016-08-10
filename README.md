# Tax Exemptions Report
## Files and Directories
* `Abnormalities` contains CSVs relating to the issues described below.
* `Pivots` contains CSVs created by Excel pivot tables. These are the basis for the data analysis section below.
* `2016_Original.csv` contains the original CSV file provided by [data.providenceri.gov](data.providenceri.gov).
* `Worksheet.xlsx` contains all working files for this repository, including the below-referenced pivot tables and error documentation.

## Filtering the Data
Of 44339 records, only 2587 are non-residential exemptions. Almost all of these have non-zero exemptions, except for 11 edge cases that are recorded in the “No Exemption Errors” spreadsheet. Most of the remaining 41752 records, which consist of commercial, owner occupied residencies, etc., do not have exemptions, but 4893 do. In the report below, we compare and contrast these 4893 records with the 2576 remaining non-residential exemptions. (Total of 749 records with exemptions.)

## Data Analysis
* The differences between assessments and exemptions is always $0.00 for non-residential exemptions, but it adds up to $937,954,549
out of a total $9,662,523,513 in other exemptions.
* The "Vote of City" class has by far the highest average exemption among non-residential exemptions, with an average of over $77 million. Among other exemptions, the "44-3-9 Stb" and "Miscellaneous" categories see the highest exemptions, with an average of about $2.5 million each. Interestingly, these are the only two major categories of other exemptions where the assessment is always equal to the exemption value.
* Non-residential exemptions total $9,334,760,900 in value, while other exemptions total $327,762,613. The average non-zero, non-residential exemption is 54 times larger than the average other non-zero exemption.
![top15nonres](https://cloud.githubusercontent.com/assets/13228316/17568508/0a98a59a-5f12-11e6-916b-c00d9b211efc.PNG) ![top15other](https://cloud.githubusercontent.com/assets/13228316/17568519/168784a2-5f12-11e6-9869-ac553e1f8a60.PNG)

## Abnormalities
*	As stated in the filtering section, 11 records with Levy Description “Non Residential Exemption” have Total_Exemptions equal to $0.00. These are stored in the “No Exemption Errors” spreadsheet.
*	There are 5 records with exemption value greater than their assessment value. These are stored in the “Exemption > Assessment” spreadsheet, and sum to an error of $84,662. Four out of five of them have class description, “Residential Vacant Land.”
