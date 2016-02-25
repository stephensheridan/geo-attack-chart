import os
import pygeoip
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
from collections import Counter


## Some Globals
geofilename = "/GeoLiteCity.dat"
alertfilename = "/alerts.txt"
filepath = os.getcwd()
ips = []
countries = []
rawdata = pygeoip.GeoIP(filepath + geofilename)

def ipquery(ip):
  data = rawdata.record_by_name(ip)
  country = data['country_name']
  city = data['city']
  longi = data['longitude']
  lat = data['latitude']
  ## Add the ip's to a list
  ips.append(ip)
  ## Add the countries to a list
  countries.append(country)
  ## Do some output to the console
  print ''
  print '[x] ' + ip
  print '[x] '+str(city)+',' +str(country)
  print '[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi)


def main():
  ## Open the file with read only permit
  f = open(filepath + alertfilename)
  ## Read the first line 
  line = f.readline()
  ## If the file is not empty keep reading line one at a time
  ## till the file is empty
  while line:
      if "User IP:" in line:
        ipquery(line[9:-1])
      line = f.readline()
  f.close()
  
  ## Count the unique IP
  ip_data = Counter(ips)
  ## Count the unique countries
  country_data = Counter(countries)
  ## Find the index of the largest entry to explode on chart
  indx = country_data.values().index(max(country_data.values()))
  explode = [0] * len(country_data.values())
  explode[indx] = 0.1
  
  ## Draw the chart
  a = np.random.random(20)
  cs = cm.Set1(np.arange(20)/20.)
  plt.pie(country_data.values(), explode=explode, labels=country_data.keys(), colors=cs, autopct='%1.1f%%', startangle=90)
  plt.axis('equal')
  plt.show()
  
if __name__ == '__main__':
  main()
