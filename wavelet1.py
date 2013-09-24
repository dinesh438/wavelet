#!/usr/bin/python

import pywt,numpy,csv,pprint,pylab

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

a = numpy.array(obv_list)             # conversion of input data (sales) into array

d = numpy.shape(a)                    # Dimension of input data array

t = numpy.size(a)                     # total no. of elements in input data array

w = pywt.Wavelet('db20')              # wavelet object with handle

max_ld = pywt.dwt_max_level(t,w)      # maximum useful decomposition level of given input data length(total elements) and wavelet object

# Single level 1-Dimensional  DWT

coeffs = pywt.dwt(a, w)               # 1-Dimensional single level DWT on huggies data

pprint.pprint(coeffs)                 # printing decomposition coefficients

cA,cD= coeffs

pprint.pprint(cA)

pprint.pprint(cD)

d1 = numpy.shape(cA)                  # Dimension of approximation (cA)

d2 = numpy.shape(cD)                  # Dimension of details (cD)

t1 = numpy.size(cA)                   # total no. of elements in cA

t2 = numpy.size(cD)                   # total no. of elements in cD


reconst = pywt.idwt(cA,cD,w)          # reconstruction of sales data

pprint.pprint(reconst)                # printing reconstruction results

d3 = numpy.shape(reconst)             # Dimension of reconstructed data 

t3 = numpy.size(reconst)              # total number of elements in reconstructed data


##### Multilevel 1-Dimensional decomposition

coeffs1 = pywt.wavedec(a,w,level = 3)   # 1-Dimensional decomposition on huggies data

pprint.pprint(coeffs1)                  # printing decomposition coefficients

cA3,cD3,cD2,cD1= coeffs1

pprint.pprint(cA3)                     # Approximation coefficients

pprint.pprint(cD3)                     # Details coefficients

pprint.pprint(cD2)

pprint.pprint(cD1)


pylab.plot(a)                          # plotting original data 

pylab.show()

pylab.plot(cA3)                        # plotting approximations

pylab.show()

pylab.plot(cD3)                        # plotting lower frequency details (cD3)

pylab.show()                            

pylab.plot(cD2)                        # plotting medium frequency details (cD2)

pylab.show()

pylab.plot(cD1)                        # plotting higher frequency details (cD1)

pylab.show()


reconst1 = pywt.waverec(coeffs1,w)     # reconstruction of sales data

pprint.pprint(reconst1)                # printing reconstruction results

pylab.plot(reconst1)                   # plotting reconstruction results

pylab.show()


d4 = numpy.shape(cA3)                   # Dimension of approximation (cA3)

d5 = numpy.shape(cD3)                   # Dimension of details (cD3)

t4 = numpy.size(cA3)                    # total no. of elements in cA

t5 = numpy.size(cD3)                    # total no. of elements in cD3

d6 = numpy.shape(cD2)                   # Dimension of details (cD2)

t6 = numpy.size(cD2)                    # total no. of elements in cD2

d7 = numpy.shape(cD1)                   # Dimension of details (cD1)

t7 = numpy.size(cD1)                    # total no. of elements in cD1


d8 = numpy.shape(reconst1)             # Dimension of reconstructed data 

t8 = numpy.size(reconst1)              # total number of elements in reconstructed data



numpy.savetxt("C:\Users\Kvantum\Desktop\sales_output_approximations@1-D.csv",cA3,delimiter=",")

numpy.savetxt("C:\Users\Kvantum\Desktop\sales_output_lower_details@1-D.csv",cD3,delimiter=",")

numpy.savetxt("C:\Users\Kvantum\Desktop\sales_output_medium_details@1-D.csv",cD2,delimiter=",")

numpy.savetxt("C:\Users\Kvantum\Desktop\sales_output_higher_details@1-D.csv",cD1,delimiter=",")

with file('C:\Users\Kvantum\Desktop\sales_output_all@1-D.csv', 'w') as outfile:
    outfile.write('# Array shape: {0}\n'.format(numpy.shape(coeffs1)))
    for slice_2d in coeffs1:
        numpy.savetxt(outfile, slice_2d, fmt='%-7.2f')
        outfile.write('# New slice\n')                   # Writing out a break to indicate different slices


#### OR #####

f3=open("approximations.csv","w")
out = csv.writer(f3, delimiter=',')
out.writerow(cA3)
f3.close()

f4=open("lower frequency.csv","w")
out = csv.writer(f4, delimiter=',')
out.writerow(cD3)
f4.close()

f5=open("medium frequency.csv","w")
out = csv.writer(f5, delimiter=',')
out.writerow(cD2)
f5.close()

f6=open("higher frequency.csv","w")
out = csv.writer(f6, delimiter=',')
out.writerow(cD1)
f6.close()
















