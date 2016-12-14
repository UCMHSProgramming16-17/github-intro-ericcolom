#cvswriting.py
#import module
import csv
import math
#create file
csvfile=open('csvexample.csv','w')
#create csvwriter
csvwriter=csv.writer(csvfile,delimiter=',')
#write information
csvwriter.writerow(['apple','cat','car'])
csvwriter
#close file 
csvfile.close()