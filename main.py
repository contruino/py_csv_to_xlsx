import csv
import xlsxwriter

ids = []
regions = []
categories = []
urls = []

with open('heis_usa.csv','r') as csvf:
    read = csv.DictReader(csvf)
    
    for i in read:
        ids.append(i['id'])
        regions.append(i['region'])
        categories.append(i['category'])
        urls.append(i['url'])

    workbook = xlsxwriter.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet('first')
    
    worksheet.write(0,0,'0')
    worksheet.write(0,1,'id')
    worksheet.write(0,2,'region')
    worksheet.write(0,3,'category')
    worksheet.write(0,4,'url')
    
    for j in range(len(ids)):
        worksheet.write(j+1,0,str(j))
        worksheet.write(j+1,1,ids[j])
        worksheet.write(j+1,2,regions[j])
        worksheet.write(j+1,3,categories[j])
        worksheet.write(j+1,4,urls[j])
        
        
workbook.close()