#Installed camelot with PIP
#Installed GhostScript with:
# sudo apt update
# sudo apt install ghostscript

import camelot
file = "SalesReport.pdf"
tables =   camelot.read_pdf(file)

print("Total  tables extracted: ", tables.n)
#This is Panda Data frame
print(tables[1].df)
tables[0].to_excel('Diego.xlsx', index = False) #Didn't work well for tables



