
import urllib.request
#We will build date list for pulling images,
#note that for summer crops like Corn and Soybeans, important months are from April till August
#I also find out that gif replaced with png in 2019 series, hence first links are till 2018
Years = list(range(2010,2019,1))
Months = ['04','05','06','07','08']
Date_List=[]
for j in Months:
    for i in Years:
        Date_List.append(str(i)+str(j))

Date_List.sort()
root='https://www.ncdc.noaa.gov/monitoring-content/sotc/national/grid-prcp/prcp-pon-'
root_end='.gif'
Date_Urls=[]
for i in Date_List:
    Date_Urls.append(root+str(i)+root_end)

for i,j in zip(Date_Urls,Date_List):
    urllib.request.urlretrieve(i, './Data/'+str(j)+root_end)

#Apparently link needs to be changed to png from gif
Years2 = ['2019', '2020']
Date_List2 = []
root_end2 = '.png'
for j in Months:
    for i in Years2:
        Date_List2.append(str(i)+str(j))
Date_List2.sort()
Date_Urls2=[]
for i in Date_List2:
    Date_Urls2.append(root+str(i)+root_end2)

#Adjusted New Links:

for i,j in zip(Date_Urls2,Date_List2):
    urllib.request.urlretrieve(i, './Data/'+str(j)+root_end2)

