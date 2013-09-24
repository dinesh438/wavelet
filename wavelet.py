#!/usr/bin/python

import pywt,numpy,csv,pprint

from pywt import Wavelet, dwtn, dwt_max_level

from pywt.numerix import as_float_array,transpose,apply_along_axis

counter = 0
col_list = []
obv_list = []
data_list = []

f = open("C:\Users\Kvantum\Desktop\Huggies_INF_inputdata.csv",'r')  # reading input data file
reader = csv.reader(f)
for row in reader:
         if counter == 0:
             for col in row:
                col_list.append('%s' %(col))
         else:
             idata = []
             for i in range(0,len(row)):
                colname = col_list[i]
                if colname != 'timestamp' and i !=0:
                   if colname == 'sales':
                     obv_list.append(float(row[i]))
                   else:  
                     idata.append(float(row[i]))
             data_list.append(idata)      
          
         counter += 1  

f.close()

a = numpy.array(data_list)            # conversion of input data into array

d = numpy.shape(a)                    # Dimension of input data array

t = numpy.size(a)                     # total no. of elements in input data array

w = pywt.Wavelet('db20')              # wavelet object with handle

max_ld = pywt.dwt_max_level(t,w)      # maximum useful decomposition level of given input data length(total elements) and wavelet object

results = pywt.dwtn(a, w, max_ld)     # N-Dimensional DWT on huggies data

pprint.pprint(results)                # print results

t2 = numpy.size(results)              # total no. of elements in results


lpd = w.dec_lo                        # decomposition filter coefficients of LPF for the defined wavelet

hpd = w.dec_hi                        # decomposition filter coefficients of HPF for the defined wavelet

lpr = w.rec_lo                        # reconstruction filter coefficients of LPF for the defined wavelet

hpr = w.rec_hi                        # reconstruction filter coefficients of HPF for the defined wavelet

dl = int(w.dec_len)                   # Decomposition filter length for the defined wavelet

rl = int(w.rec_len)                   # Reconstruction filter length for the defined wavelet

fc = w.filter_bank                    # all filter(LPF,HPF)coefficients for the defined wavelet

[phi,psi,x] = w.wavefun(20)           # approximations of scaling function(phi) and wavelet function(psi) at given level of wavelet('db')


keys = results.keys()                 # keys of dictionary (results)    

values = results.values()             # values of dictionary (results)

numpy.shape(values)                   # dimension of the list (values)

c1 = results["aa"]                    # 1st coefficient 

c2 = results["ad"]                    # 2nd coefficient

c3 = results["da"]                    # 3rd coefficient

c4 = results["dd"]                    # 4th coefficient


## Reconstruction 

x = numpy.zeros(numpy.shape(results['aa']))

for k,v in results.items():
    x += v

print "hererere"
print x    
    
for item in results.values():
    for items in item:
        sum(items)


f1 = open("C:\Users\Kvantum\Desktop\Huggies_INF_outputdata.csv",'w')   # writing coefficients to file
writer = csv.DictWriter(f1,delimiter=',',fieldnames=coefficients)
for row1 in results:
    writer.writerow(row1)
f1.close()

