# Tax Exemptions Report
## Files and Directories
* `Abnormalities` contains CSVs relating to the issues described below.
* `2016_Original.csv` contains the original CSV file provided by data.providenceri.gov.
* `Worksheet.xlsx` contains all working files for this repository, including the below-referenced pivot tables and error documentation.

## Filtering the Data
Of 44339 records, only 2587 are non-residential exemptions. Almost all of these have non-zero exemptions, except for 11 edge cases that are recorded in the “No Exemption Errors” spreadsheet. Most of the remaining 41752 records, which consist of commercial, owner occupied residencies, etc., do not have exemptions, but 4893 do. In the report below, we compare and contrast these 4893 records with the 2576 remaining non-residential exemptions. (Total of 749 records with exemptions.)

## Abnormalities
*	As stated in the filtering section, 11 records with Levy Description “Non Residential Exemption” have Total_Exemptions equal to $0.00. These are stored in the “No Exemption Errors” spreadsheet.
*	There are 5 records with exemption value greater than their assessment value. These are stored in the “Exemption > Assessment” spreadsheet, and sum to an error of $84,662. Four out of five of them have class description, “Residential Vacant Land.”
