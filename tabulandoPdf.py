#Needed to install Java https://serverspace.io/support/help/how-to-install-java-with-apt-on-ubuntu-18-04/
# Import the required Module "tabula"
import tabula

# Read a PDF File
df = tabula.read_pdf("SalesReport.pdf", pages='all')
# convert PDF into CSV
tabula.convert_into("SalesReport.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)