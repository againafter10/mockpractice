####################################
####################################
### merge xls sheets for quarterly maintenance,and then enter data to sqlite db
####################################
####################################

####################################
### convert xls to csv format
####################################

import csv,os
import sqlite3 as lite
from xlrd import open_workbook
from subprocess import call


#print((os.listdir(os.getcwd()))) # returns a list

#['.DS_Store', 'cmpcsv.py', 'data', 'data.csv', 'datacsv.py', 'example.tsv', 'headerRemoved', 'numpy_version.py', 'output.csv', 'output2.csv', 'pdit.py', 'removeheader.py']
filearr=[]
for i in os.listdir(os.getcwd()):
    
    if i[-4:] == "xlsx":
        print("\nconvert \"%s\" to csv format\n" %i)
        filearr.append(i)
print("\nFiles to be converted are \n")
print(filearr)

#make a csv directory
      
c_csv=os.getcwd() + "/formattedcsv"
if (os.path.exists(c_csv)):
    print ("path already exists,not recreating the directory")
else:
    os.mkdir(c_csv)
    
#convert all xlsx file to csv and move them to c_csv directory

for i in filearr:
    wb=open_workbook(i)
    sheet=wb.sheet_by_name('Sheet1') ## assuming there is only one sheet in the excel sheet
    #compress all spaces in filename
    with open("%s/%s.csv" %(c_csv,i.replace(" ","")[:-5]), "w") as file:
        w_csv = csv.writer(file,delimiter =",")
        header = [cell.value for cell in sheet.row(0)]
        w_csv.writerow(header)
        for rowid in range(1, sheet.nrows):
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sheet.row(rowid)]
            w_csv.writerow(row)
file.close()
### csv files created from xml files


####################################
### put this csv data into sqlite db and then query
####################################


'''
[[data]] $ls formattedcsv/
sample.csv	samplecopy.csv	samplecopy2.csv	samplecopy3.csv	samplecopy4.csv	samplecopy5.csv	samplecopy6.csv
[[data]] $

'''
'''

CREATE TABLE quat_maint (
 env_name text NOT NULL,
 temp_name text NOT NULL,
 bootload text NOT NULL,
 pool_name text NOT NULL,
 srv_name text NOT NULL,
 unit_host text NOT NULL,
 unit_image text NOT NULL,
 compute integer NOT NULL,
 cores integer NOT NULL,
 memory integer NOT NULL,
 status text NOT NULL,
 futr_status text NOT NULL,
 cmts text NOT NULL
 
);


'''

os.chdir(c_csv)
os.system('clear')
#print(os.getcwd())
db_name="formattedcsv.db"
conn = lite.connect('formattedcsv.db')
query="insert into quat_maint values ("
'''
################################################
################################################
################################################
################################################
################################################

## with one single file
with open("sampleshort.csv",'rb') as csvfile:
   
    csvReader = csv.reader(csvfile)
    data = list(csvReader)
    for i in data:
        for data in i:
            query = query + "'" + data + "'" + ","
        query=query[:-1]
        query = query + ");"
        #print query
        with conn:
            cur = conn.cursor()
            cur.execute(query)
        query="insert into quat_maint values ("
        cur.close()
        
################################################
################################################
################################################
################################################
################################################      
'''
## for all files in the directory
print "\ncurrent working directory is\n"
print(os.getcwd())
# pull data only from .csv files and enter into db
filearr=[]
for i in os.listdir(os.getcwd()):
    if i[-3:] == "csv":
        
        filearr.append(i)
        
for f_csv in filearr:
    with open(f_csv,'rb') as csvfile:
        csvReader = csv.reader(csvfile)
        data = list(csvReader)
        for i in data:
            for data in i:
                query = query + "'" + data + "'" + ","
            query=query[:-1]
            query = query + ");"
            #print query
            with conn:
                cur = conn.cursor()
                cur.execute(query)
            query="insert into quat_maint values ("
            cur.close()
    csvfile.close()
      

        
''' 
    
#['SOASPR111D01', 'soa0106', 'apol5u8', 'TECHPROD-NADC-01', 'srv13411', 'unit24317', 'SOASPR111D01_SOA', '24', '4', '12', 'Prod', 'Retire 10/09/15', '']

#INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);
    

# sqlite> select count(*) from quat_maint;
15104
sqlite> 

-rw-r--r--  1 Archana  admin  2699264 Apr 27 15:00 formattedcsv.db
db has 24.5k records
'''      
################################

### query data and write back the csv as xml

print("\nIdentifying the productions to be retired\n")
#make a newcsv directory where fetched records will be kept
# shutdown all prod vms marked to retire
#CREATE VIEW retire_maint AS select * from quat_maint where  cmts like '%Retire%' and status='Prod'

w_csv=os.getcwd() + "/prodtoretire"
if (os.path.exists(w_csv)):
    print ("path already exists,not recreating the directory")
else:
    os.mkdir(w_csv)
os.chdir(w_csv) 

query="CREATE VIEW IF NOT EXISTS retire_maint AS select * from quat_maint where  cmts like '%Retire%' and status='Prod';"
with conn:
        conn.execute(query)

## csv file name where all prods to be retired are listed
w_csv=os.getcwd() + "/prodtoretire.csv"
print("\n %s \n" %w_csv)
query="select * from retire_maint;"
'''
### adding header to the csv file ---- did that manually later

head_csv=['env_name','temp_name','bootload' ,'pool_name' ,'srv_name' ,'unit_host' ,'unit_image' ,'compute' ,'cores' ,'memory' ,'status','futr_status','cmts']

with open(w_csv,'w') as newcsvfile: 
    writer = csv.writer(newcsvfile)
    #writer.writerows(row + [0.0] for row in reader)
    #writer.writerows(row  for row in head_csv)
    writer.writerows('env_name','temp_name','bootload' ,'pool_name' ,'srv_name' ,'unit_host' ,'unit_image' ,'compute' ,'cores' ,'memory' ,'status','futr_status','cmts')
newcsvfile.close()

'''
head_csv=['env_name','temp_name','bootload' ,'pool_name' ,'srv_name' ,'unit_host' ,'unit_image' ,'compute' ,'cores' ,'memory' ,'status','futr_status','cmts']

with open(w_csv,'a') as newcsvfile: 
    #header = [cell.value for cell in head_csv]
    #w_csv.writerow(header)
    with conn:
        cur = conn.cursor()
        cur.execute(query)
        rows=cur.fetchall()
        writer = csv.writer(newcsvfile)
        for row in rows:
            writer.writerow(row)
        cur.close
        newcsvfile.close()


###########################
        
   

      
      
