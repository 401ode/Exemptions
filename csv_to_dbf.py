# Code courtesy of Brian McGuirk
# Requires dbf module: https://pythonhosted.org/dbf/
# dbf module supported by Conda: `conda install dbf' works fine for Python 3.5
import dbf

# Input CSV file path
file = r"""PVD-Maps/Join_Tax.csv"""

# Do not modify the headers below unless you have a very compelling reason.
# .split(',') at the end returns a list to 'headers'.
headers = "PIN,TAX_MAP,OWNER_NAME,ADDRESS1,ADDRESS2,FREE_LINE_,P_ID,YEAR_ID,ACRES,TOTAL_VALU,LAND_VALUE,BUILDING_V,PROPERTY_A,ZIP_POSTAL,Shape_STAr,Shape_STLe,Shape_ST_1,Shape_ST_2,Area,Plat,Lot_1,Unit,Class,Class_Desc,LEVY_CODE,Levy_Desc,Formatted_,Location_Z,Owner_Firs,Owner_Last,Company,OwnerAddre,Owner_Add7,Total_Asse,Total_Exem,Total_Taxe,Exempt".split(',')

# Output file name. Takes same directory as 'file' unless otherwise specified.
output = r"Join_Tax.dbf"  # Unless you want to overwrite existing .dbf file

# Combined command. 'field_names' requires a list input.
dbf.from_csv(file, to_disk=True, filename=output, field_names=headers)
