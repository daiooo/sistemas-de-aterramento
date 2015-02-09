import glob
import pickle
import numpy as nu
from scipy.io import loadmat
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# load data /// for linux
# loaded_data1 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/hidro_2_08052014", matlab_compatible=True)
# loaded_data2 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/pici_3_09052014", matlab_compatible=True)
# loaded_data3 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/pici_4_09052014", matlab_compatible=True)
# loaded_data4 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/pici_5_09052014", matlab_compatible=True)
# loaded_data5 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/pici_6_20052014", matlab_compatible=True)
# loaded_data6 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/pici_7_20052014", matlab_compatible=True)
# loaded_data7 = loadmat("/media/Data/Projects/Dropbox/projeto_aterramento/treated_data_sets/pici_8_23052014", matlab_compatible=True)

# load data /// for windows
# A=glob.glob('C:\\Documents and Settings\\Owner\\My Documents\\Dropbox\\projeto_aterramento\\treated_data_sets\\*')
A=glob.glob('C:\\Users\\LabTerra_user\\Desktop\\Aquisicao\\AlgoritmoInteligentePythonFiles\\treated_data_sets\\*')
loaded_data1 = loadmat(A[4], matlab_compatible=True)
loaded_data2 = loadmat(A[6], matlab_compatible=True)
loaded_data3 = loadmat(A[7], matlab_compatible=True)
loaded_data4 = loadmat(A[8], matlab_compatible=True)
loaded_data5 = loadmat(A[9], matlab_compatible=True)
loaded_data6 = loadmat(A[10], matlab_compatible=True)
loaded_data7 = loadmat(A[11], matlab_compatible=True)
loaded_data8 = loadmat(A[5], matlab_compatible=True)
loaded_data9 = loadmat(A[0], matlab_compatible=True)
loaded_data10 = loadmat(A[1], matlab_compatible=True)
loaded_data11 = loadmat(A[2], matlab_compatible=True)
loaded_data12 = loadmat(A[3], matlab_compatible=True)

# get data from matlab file.
# hidraulica 08-05-2014
V15_hidro_2 = loaded_data1['V15_hidro_2'].squeeze()
I15_hidro_2 = loaded_data1['I15_hidro_2'].squeeze()
V14_hidro_2 = loaded_data1['V14_hidro_2'].squeeze()
I14_hidro_2 = loaded_data1['I14_hidro_2'].squeeze()
V4_hidro_2 = loaded_data1['V4_hidro_2'].squeeze()
I4_hidro_2 = loaded_data1['I4_hidro_2'].squeeze()
V8_hidro_2 = loaded_data1['V8_hidro_2'].squeeze()
I8_hidro_2 = loaded_data1['I8_hidro_2'].squeeze()

# pici 3 09-05-2014
V15_pici_3 = loaded_data2['V15_pici_3'].squeeze()
I15_pici_3 = loaded_data2['I15_pici_3'].squeeze()
V14_pici_3 = loaded_data2['V14_pici_3'].squeeze()
I14_pici_3 = loaded_data2['I14_pici_3'].squeeze()
V4_pici_3 = loaded_data2['V4_pici_3'].squeeze()
I4_pici_3 = loaded_data2['I4_pici_3'].squeeze()
V8_pici_3 = loaded_data2['V8_pici_3'].squeeze()
I8_pici_3 = loaded_data2['I8_pici_3'].squeeze()

# pici 4 09-05-2014
V15_pici_4 = loaded_data3['V15_pici_4'].squeeze()
I15_pici_4 = loaded_data3['I15_pici_4'].squeeze()
V14_pici_4 = loaded_data3['V14_pici_4'].squeeze()
I14_pici_4 = loaded_data3['I14_pici_4'].squeeze()
V4_pici_4 = loaded_data3['V4_pici_4'].squeeze()
I4_pici_4 = loaded_data3['I4_pici_4'].squeeze()
V8_pici_4 = loaded_data3['V8_pici_4'].squeeze()
I8_pici_4 = loaded_data3['I8_pici_4'].squeeze()

# pici 5 09-05-2014
V15_pici_5 = loaded_data4['V15_pici_5'].squeeze()
I15_pici_5 = loaded_data4['I15_pici_5'].squeeze()
V14_pici_5 = loaded_data4['V14_pici_5'].squeeze()
I14_pici_5 = loaded_data4['I14_pici_5'].squeeze()
V4_pici_5 = loaded_data4['V4_pici_5'].squeeze()
I4_pici_5 = loaded_data4['I4_pici_5'].squeeze()
V8_pici_5 = loaded_data4['V8_pici_5'].squeeze()
I8_pici_5 = loaded_data4['I8_pici_5'].squeeze()

# pici 6 20-05-2014
V15_pici_6 = loaded_data5['V15_pici_6'].squeeze()
I15_pici_6 = loaded_data5['I15_pici_6'].squeeze()
V14_pici_6 = loaded_data5['V14_pici_6'].squeeze()
I14_pici_6 = loaded_data5['I14_pici_6'].squeeze()
V4_pici_6 = loaded_data5['V4_pici_6'].squeeze()
I4_pici_6 = loaded_data5['I4_pici_6'].squeeze()
V8_pici_6 = loaded_data5['V8_pici_6'].squeeze()
I8_pici_6 = loaded_data5['I8_pici_6'].squeeze()

# pici 7 20-05-2014
V15_pici_7 = loaded_data6['V15_pici_7'].squeeze()
I15_pici_7 = loaded_data6['I15_pici_7'].squeeze()
V14_pici_7 = loaded_data6['V14_pici_7'].squeeze()
I14_pici_7 = loaded_data6['I14_pici_7'].squeeze()
V4_pici_7 = loaded_data6['V4_pici_7'].squeeze()
I4_pici_7 = loaded_data6['I4_pici_7'].squeeze()
V8_pici_7 = loaded_data6['V8_pici_7'].squeeze()
I8_pici_7 = loaded_data6['I8_pici_7'].squeeze()

# pici 8 20-05-2014
V15_pici_8 = loaded_data7['V15_pici_8'].squeeze()
I15_pici_8 = loaded_data7['I15_pici_8'].squeeze()
V14_pici_8 = loaded_data7['V14_pici_8'].squeeze()
I14_pici_8 = loaded_data7['I14_pici_8'].squeeze()
V4_pici_8 = loaded_data7['V4_pici_8'].squeeze()
I4_pici_8 = loaded_data7['I4_pici_8'].squeeze()
V8_pici_8 = loaded_data7['V8_pici_8'].squeeze()
I8_pici_8 = loaded_data7['I8_pici_8'].squeeze()

V15_pici_3 = V15_pici_3[:,0:3]

# hidro 3 30052014
V15_hidro_3 = loaded_data8['V15_hidro_3'].squeeze()
I15_hidro_3 = loaded_data8['I15_hidro_3'].squeeze()
V14_hidro_3 = loaded_data8['V14_hidro_3'].squeeze()
I14_hidro_3 = loaded_data8['I14_hidro_3'].squeeze()
V4_hidro_3 = loaded_data8['V4_hidro_3'].squeeze()
I4_hidro_3 = loaded_data8['I4_hidro_3'].squeeze()
V8_hidro_3 = loaded_data8['V8_hidro_3'].squeeze()
I8_hidro_3 = loaded_data8['I8_hidro_3'].squeeze()
 
# alimentos 1 03062014
V15_alimentos_1 = loaded_data9['V15_alimentos_1'].squeeze()
I15_alimentos_1 = loaded_data9['I15_alimentos_1'].squeeze()
V14_alimentos_1 = loaded_data9['V14_alimentos_1'].squeeze()
I14_alimentos_1 = loaded_data9['I14_alimentos_1'].squeeze()
V4_alimentos_1 = loaded_data9['V4_alimentos_1'].squeeze()
I4_alimentos_1 = loaded_data9['I4_alimentos_1'].squeeze()
V8_alimentos_1 = loaded_data9['V8_alimentos_1'].squeeze()
I8_alimentos_1 = loaded_data9['I8_alimentos_1'].squeeze()
 
# alimentos 2 03062014
V15_alimentos_2 = loaded_data10['V15_alimentos_2'].squeeze()
I15_alimentos_2 = loaded_data10['I15_alimentos_2'].squeeze()
V14_alimentos_2 = loaded_data10['V14_alimentos_2'].squeeze()
I14_alimentos_2 = loaded_data10['I14_alimentos_2'].squeeze()
V4_alimentos_2 = loaded_data10['V4_alimentos_2'].squeeze()
I4_alimentos_2 = loaded_data10['I4_alimentos_2'].squeeze()
V8_alimentos_2 = loaded_data10['V8_alimentos_2'].squeeze()
I8_alimentos_2 = loaded_data10['I8_alimentos_2'].squeeze()
 
# alimentos 3 03062014
V15_alimentos_3 = loaded_data11['V15_alimentos_3'].squeeze()
I15_alimentos_3 = loaded_data11['I15_alimentos_3'].squeeze()
V14_alimentos_3 = loaded_data11['V14_alimentos_3'].squeeze()
I14_alimentos_3 = loaded_data11['I14_alimentos_3'].squeeze()
V4_alimentos_3 = loaded_data11['V4_alimentos_3'].squeeze()
I4_alimentos_3 = loaded_data11['I4_alimentos_3'].squeeze()
V8_alimentos_3 = loaded_data11['V8_alimentos_3'].squeeze()
I8_alimentos_3 = loaded_data11['I8_alimentos_3'].squeeze()
 
# alimentos 4 03062014
V15_alimentos_4 = loaded_data12['V15_alimentos_4'].squeeze()
I15_alimentos_4 = loaded_data12['I15_alimentos_4'].squeeze()
V14_alimentos_4 = loaded_data12['V14_alimentos_4'].squeeze()
I14_alimentos_4 = loaded_data12['I14_alimentos_4'].squeeze()
V4_alimentos_4 = loaded_data12['V4_alimentos_4'].squeeze()
I4_alimentos_4 = loaded_data12['I4_alimentos_4'].squeeze()
V8_alimentos_4 = loaded_data12['V8_alimentos_4'].squeeze()
I8_alimentos_4 = loaded_data12['I8_alimentos_4'].squeeze()

# extract features by computing fft, of voltage, current and impedance using the first n_pontos.
n_pontos = 400;
eps = 0.000000001;
# hidraulica 2
# top 15
FeatVTop15_hidro_2 = nu.abs(nu.fft.fft(nu.mean(V15_hidro_2[:n_pontos],1)))
FeatITop15_hidro_2 = nu.abs(nu.fft.fft(nu.mean(I15_hidro_2[:n_pontos],1)))
FeatRTop15_hidro_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_hidro_2[:n_pontos],1)+eps,nu.mean(I15_hidro_2[:n_pontos],1)+eps)))
# top 14
FeatVTop14_hidro_2 = nu.abs(nu.fft.fft(nu.mean(V14_hidro_2[:n_pontos],1)))
FeatITop14_hidro_2 = nu.abs(nu.fft.fft(nu.mean(I14_hidro_2[:n_pontos],1)))
FeatRTop14_hidro_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_hidro_2[:n_pontos],1)+eps,nu.mean(I14_hidro_2[:n_pontos],1)+eps)))
# top 4
FeatVTop4_hidro_2 = nu.abs(nu.fft.fft(nu.mean(V4_hidro_2[:n_pontos],1)))
FeatITop4_hidro_2 = nu.abs(nu.fft.fft(nu.mean(I4_hidro_2[:n_pontos],1)))
FeatRTop4_hidro_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_hidro_2[:n_pontos],1)+eps,nu.mean(I4_hidro_2[:n_pontos],1)+eps)))
# top 8
FeatVTop8_hidro_2 = nu.abs(nu.fft.fft(nu.mean(V8_hidro_2[:n_pontos],1)))
FeatITop8_hidro_2 = nu.abs(nu.fft.fft(nu.mean(I8_hidro_2[:n_pontos],1)))
FeatRTop8_hidro_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_hidro_2[:n_pontos],1)+eps,nu.mean(I8_hidro_2[:n_pontos],1)+eps)))

# hidraulica 3
# top 15
FeatVTop15_hidro_3 = nu.abs(nu.fft.fft(nu.mean(V15_hidro_3[:n_pontos],1)))
FeatITop15_hidro_3 = nu.abs(nu.fft.fft(nu.mean(I15_hidro_3[:n_pontos],1)))
FeatRTop15_hidro_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_hidro_3[:n_pontos],1)+eps,nu.mean(I15_hidro_3[:n_pontos],1)+eps)))
# top 14
FeatVTop14_hidro_3 = nu.abs(nu.fft.fft(nu.mean(V14_hidro_3[:n_pontos],1)))
FeatITop14_hidro_3 = nu.abs(nu.fft.fft(nu.mean(I14_hidro_3[:n_pontos],1)))
FeatRTop14_hidro_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_hidro_3[:n_pontos],1)+eps,nu.mean(I14_hidro_3[:n_pontos],1)+eps)))
# top 4
FeatVTop4_hidro_3 = nu.abs(nu.fft.fft(nu.mean(V4_hidro_3[:n_pontos],1)))
FeatITop4_hidro_3 = nu.abs(nu.fft.fft(nu.mean(I4_hidro_3[:n_pontos],1)))
FeatRTop4_hidro_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_hidro_3[:n_pontos],1)+eps,nu.mean(I4_hidro_3[:n_pontos],1)+eps)))
# top 8
FeatVTop8_hidro_3 = nu.abs(nu.fft.fft(nu.mean(V8_hidro_3[:n_pontos],1)))
FeatITop8_hidro_3 = nu.abs(nu.fft.fft(nu.mean(I8_hidro_3[:n_pontos],1)))
FeatRTop8_hidro_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_hidro_3[:n_pontos],1)+eps,nu.mean(I8_hidro_3[:n_pontos],1)+eps)))
 
# pici_3
# top 15
FeatVTop15_pici_3 = nu.abs(nu.fft.fft(nu.mean(V15_pici_3[:n_pontos],1)))
FeatITop15_pici_3 = nu.abs(nu.fft.fft(nu.mean(I15_pici_3[:n_pontos],1)))
FeatRTop15_pici_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_pici_3[:n_pontos],1)+eps,nu.mean(I15_pici_3[:n_pontos],1)+eps)))
# top 14
FeatVTop14_pici_3 = nu.abs(nu.fft.fft(nu.mean(V14_pici_3[:n_pontos],1)))
FeatITop14_pici_3 = nu.abs(nu.fft.fft(nu.mean(I14_pici_3[:n_pontos],1)))
FeatRTop14_pici_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_pici_3[:n_pontos],1)+0.000001,nu.mean(I14_pici_3[:n_pontos],1)+0.000001)))
# top 4
FeatVTop4_pici_3 = nu.abs(nu.fft.fft(V4_pici_3[:n_pontos]))
FeatITop4_pici_3 = nu.abs(nu.fft.fft(I4_pici_3[:n_pontos]))
FeatRTop4_pici_3 = nu.abs(nu.fft.fft(nu.divide(V4_pici_3[:n_pontos]+0.000001,I4_pici_3[:n_pontos]+0.000001)))
# top 8
FeatVTop8_pici_3 = nu.abs(nu.fft.fft(nu.mean(V8_pici_3[:n_pontos],1)))
FeatITop8_pici_3 = nu.abs(nu.fft.fft(nu.mean(I8_pici_3[:n_pontos],1)))
FeatRTop8_pici_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_pici_3[:n_pontos],1)+eps,nu.mean(I8_pici_3[:n_pontos],1)+eps)))

# pici_4
# top 15
FeatVTop15_pici_4 = nu.abs(nu.fft.fft(nu.mean(V15_pici_4[:n_pontos],1)))
FeatITop15_pici_4 = nu.abs(nu.fft.fft(nu.mean(I15_pici_4[:n_pontos],1)))
FeatRTop15_pici_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_pici_4[:n_pontos],1)+eps,nu.mean(I15_pici_4[:n_pontos],1)+eps)))
# top 14
FeatVTop14_pici_4 = nu.abs(nu.fft.fft(nu.mean(V14_pici_4[:n_pontos],1)))
FeatITop14_pici_4 = nu.abs(nu.fft.fft(nu.mean(I14_pici_4[:n_pontos],1)))
FeatRTop14_pici_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_pici_4[:n_pontos],1)+eps,nu.mean(I14_pici_4[:n_pontos],1)+eps)))
# top 4
FeatVTop4_pici_4 = nu.abs(nu.fft.fft(nu.mean(V4_pici_4[:n_pontos],1)))
FeatITop4_pici_4 = nu.abs(nu.fft.fft(nu.mean(I4_pici_4[:n_pontos],1)))
FeatRTop4_pici_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_pici_4[:n_pontos],1)+eps,nu.mean(I14_pici_4[:n_pontos],1)+eps)))
# top 8
FeatVTop8_pici_4 = nu.abs(nu.fft.fft(nu.mean(V8_pici_4[:n_pontos],1)))
FeatITop8_pici_4 = nu.abs(nu.fft.fft(nu.mean(I8_pici_4[:n_pontos],1)))
FeatRTop8_pici_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_pici_4[:n_pontos],1)+eps,nu.mean(I8_pici_4[:n_pontos],1)+eps)))

# pici_5
# top 15
FeatVTop15_pici_5 = nu.abs(nu.fft.fft(nu.mean(V15_pici_5[:n_pontos],1)))
FeatITop15_pici_5 = nu.abs(nu.fft.fft(nu.mean(I15_pici_5[:n_pontos],1)))
FeatRTop15_pici_5 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_pici_5[:n_pontos],1)+eps,nu.mean(I15_pici_5[:n_pontos],1)+eps)))
# top 14
FeatVTop14_pici_5 = nu.abs(nu.fft.fft(nu.mean(V14_pici_5[:n_pontos],1)))
FeatITop14_pici_5 = nu.abs(nu.fft.fft(nu.mean(I14_pici_5[:n_pontos],1)))
FeatRTop14_pici_5 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_pici_5[:n_pontos],1)+eps,nu.mean(I14_pici_5[:n_pontos],1)+eps)))
# top 4
FeatVTop4_pici_5 = nu.abs(nu.fft.fft(nu.mean(V4_pici_5[:n_pontos],1)))
FeatITop4_pici_5 = nu.abs(nu.fft.fft(nu.mean(I4_pici_5[:n_pontos],1)))
FeatRTop4_pici_5 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_pici_5[:n_pontos],1)+eps,nu.mean(I4_pici_5[:n_pontos],1)+eps)))
# top 8
FeatVTop8_pici_5 = nu.abs(nu.fft.fft(nu.mean(V8_pici_5[:n_pontos],1)))
FeatITop8_pici_5 = nu.abs(nu.fft.fft(nu.mean(I8_pici_5[:n_pontos],1)))
FeatRTop8_pici_5 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_pici_5[:n_pontos],1)+eps,nu.mean(I8_pici_5[:n_pontos],1)+eps)))

# pici_6
# top 15
FeatVTop15_pici_6 = nu.abs(nu.fft.fft(nu.mean(V15_pici_6[:n_pontos],1)))
FeatITop15_pici_6 = nu.abs(nu.fft.fft(nu.mean(I15_pici_6[:n_pontos],1)))
FeatRTop15_pici_6 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_pici_6[:n_pontos],1)+eps,nu.mean(I15_pici_6[:n_pontos],1)+eps)))
# top 14
FeatVTop14_pici_6 = nu.abs(nu.fft.fft(nu.mean(V14_pici_6[:n_pontos],1)))
FeatITop14_pici_6 = nu.abs(nu.fft.fft(nu.mean(I14_pici_6[:n_pontos],1)))
FeatRTop14_pici_6 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_pici_6[:n_pontos],1)+eps,nu.mean(I14_pici_6[:n_pontos],1)+eps)))
# top 4
FeatVTop4_pici_6 = nu.abs(nu.fft.fft(nu.mean(V4_pici_6[:n_pontos],1)))
FeatITop4_pici_6 = nu.abs(nu.fft.fft(nu.mean(I4_pici_6[:n_pontos],1)))
FeatRTop4_pici_6 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_pici_6[:n_pontos],1)+eps,nu.mean(I4_pici_6[:n_pontos],1)+eps)))
# top 8
FeatVTop8_pici_6 = nu.abs(nu.fft.fft(nu.mean(V8_pici_6[:n_pontos],1)))
FeatITop8_pici_6 = nu.abs(nu.fft.fft(nu.mean(I8_pici_6[:n_pontos],1)))
FeatRTop8_pici_6 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_pici_6[:n_pontos],1)+eps,nu.mean(I8_pici_6[:n_pontos],1)+eps)))

# pici_7
# top 15
FeatVTop15_pici_7 = nu.abs(nu.fft.fft(nu.mean(V15_pici_7[:n_pontos],1)))
FeatITop15_pici_7 = nu.abs(nu.fft.fft(nu.mean(I15_pici_7[:n_pontos],1)))
FeatRTop15_pici_7 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_pici_7[:n_pontos],1)+eps,nu.mean(I15_pici_7[:n_pontos],1)+eps)))
# top 14
FeatVTop14_pici_7 = nu.abs(nu.fft.fft(nu.mean(V14_pici_7[:n_pontos],1)))
FeatITop14_pici_7 = nu.abs(nu.fft.fft(nu.mean(I14_pici_7[:n_pontos],1)))
FeatRTop14_pici_7 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_pici_7[:n_pontos],1)+eps,nu.mean(I14_pici_7[:n_pontos],1)+eps)))
# top 4
FeatVTop4_pici_7 = nu.abs(nu.fft.fft(nu.mean(V4_pici_7[:n_pontos],1)))
FeatITop4_pici_7 = nu.abs(nu.fft.fft(nu.mean(I4_pici_7[:n_pontos],1)))
FeatRTop4_pici_7 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_pici_7[:n_pontos],1)+eps,nu.mean(I4_pici_7[:n_pontos],1)+eps)))
# top 8
FeatVTop8_pici_7 = nu.abs(nu.fft.fft(nu.mean(V8_pici_7[:n_pontos],1)))
FeatITop8_pici_7 = nu.abs(nu.fft.fft(nu.mean(I8_pici_7[:n_pontos],1)))
FeatRTop8_pici_7 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_pici_7[:n_pontos],1)+eps,nu.mean(I8_pici_7[:n_pontos],1)+eps)))

# pici_8
# top 15
FeatVTop15_pici_8 = nu.abs(nu.fft.fft(nu.mean(V15_pici_8[:n_pontos],1)))
FeatITop15_pici_8 = nu.abs(nu.fft.fft(nu.mean(I15_pici_8[:n_pontos],1)))
FeatRTop15_pici_8 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_pici_8[:n_pontos],1)+eps,nu.mean(I15_pici_8[:n_pontos],1)+eps)))
# top 14
FeatVTop14_pici_8 = nu.abs(nu.fft.fft(nu.mean(V14_pici_8[:n_pontos],1)))
FeatITop14_pici_8 = nu.abs(nu.fft.fft(nu.mean(I14_pici_8[:n_pontos],1)))
FeatRTop14_pici_8 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_pici_8[:n_pontos],1)+eps,nu.mean(I14_pici_8[:n_pontos],1)+eps)))
# top 4
FeatVTop4_pici_8 = nu.abs(nu.fft.fft(nu.mean(V4_pici_8[:n_pontos],1)))
FeatITop4_pici_8 = nu.abs(nu.fft.fft(nu.mean(I4_pici_8[:n_pontos],1)))
FeatRTop4_pici_8 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_pici_8[:n_pontos],1)+eps,nu.mean(I4_pici_8[:n_pontos],1)+eps)))
# top 8
FeatVTop8_pici_8 = nu.abs(nu.fft.fft(nu.mean(V8_pici_8[:n_pontos],1)))
FeatITop8_pici_8 = nu.abs(nu.fft.fft(nu.mean(I8_pici_8[:n_pontos],1)))
FeatRTop8_pici_8 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_pici_8[:n_pontos],1)+eps,nu.mean(I8_pici_8[:n_pontos],1)+eps)))

# alimentos 1
# top 15
FeatVTop15_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(V15_alimentos_1[:n_pontos],1)))
FeatITop15_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(I15_alimentos_1[:n_pontos],1)))
FeatRTop15_alimentos_1 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_alimentos_1[:n_pontos],1)+eps,nu.mean(I15_alimentos_1[:n_pontos],1)+eps)))
# top 14
FeatVTop14_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(V14_alimentos_1[:n_pontos],1)))
FeatITop14_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(I14_alimentos_1[:n_pontos],1)))
FeatRTop14_alimentos_1 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_alimentos_1[:n_pontos],1)+eps,nu.mean(I14_alimentos_1[:n_pontos],1)+eps)))
# top 4
FeatVTop4_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(V4_alimentos_1[:n_pontos],1)))
FeatITop4_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(I4_alimentos_1[:n_pontos],1)))
FeatRTop4_alimentos_1 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_alimentos_1[:n_pontos],1)+eps,nu.mean(I4_alimentos_1[:n_pontos],1)+eps)))
# top 8
FeatVTop8_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(V8_alimentos_1[:n_pontos],1)))
FeatITop8_alimentos_1 = nu.abs(nu.fft.fft(nu.mean(I8_alimentos_1[:n_pontos],1)))
FeatRTop8_alimentos_1 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_alimentos_1[:n_pontos],1)+eps,nu.mean(I8_alimentos_1[:n_pontos],1)+eps)))
 
# alimentos 2
# top 15
FeatVTop15_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(V15_alimentos_2[:n_pontos],1)))
FeatITop15_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(I15_alimentos_2[:n_pontos],1)))
FeatRTop15_alimentos_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_alimentos_2[:n_pontos],1)+eps,nu.mean(I15_alimentos_2[:n_pontos],1)+eps)))
# top 14
FeatVTop14_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(V14_alimentos_2[:n_pontos],1)))
FeatITop14_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(I14_alimentos_2[:n_pontos],1)))
FeatRTop14_alimentos_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_alimentos_2[:n_pontos],1)+eps,nu.mean(I14_alimentos_2[:n_pontos],1)+eps)))
# top 4
FeatVTop4_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(V4_alimentos_2[:n_pontos],1)))
FeatITop4_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(I4_alimentos_2[:n_pontos],1)))
FeatRTop4_alimentos_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_alimentos_2[:n_pontos],1)+eps,nu.mean(I4_alimentos_2[:n_pontos],1)+eps)))
# top 8
FeatVTop8_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(V8_alimentos_2[:n_pontos],1)))
FeatITop8_alimentos_2 = nu.abs(nu.fft.fft(nu.mean(I8_alimentos_2[:n_pontos],1)))
FeatRTop8_alimentos_2 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_alimentos_2[:n_pontos],1)+eps,nu.mean(I8_alimentos_2[:n_pontos],1)+eps)))
 
# alimentos 3
# top 15
FeatVTop15_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(V15_alimentos_3[:n_pontos],1)))
FeatITop15_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(I15_alimentos_3[:n_pontos],1)))
FeatRTop15_alimentos_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_alimentos_3[:n_pontos],1)+eps,nu.mean(I15_alimentos_3[:n_pontos],1)+eps)))
# top 14
FeatVTop14_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(V14_alimentos_3[:n_pontos],1)))
FeatITop14_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(I14_alimentos_3[:n_pontos],1)))
FeatRTop14_alimentos_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_alimentos_3[:n_pontos],1)+eps,nu.mean(I14_alimentos_3[:n_pontos],1)+eps)))
# top 4
FeatVTop4_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(V4_alimentos_3[:n_pontos],1)))
FeatITop4_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(I4_alimentos_3[:n_pontos],1)))
FeatRTop4_alimentos_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_alimentos_3[:n_pontos],1)+eps,nu.mean(I4_alimentos_3[:n_pontos],1)+eps)))
# top 8
FeatVTop8_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(V8_alimentos_3[:n_pontos],1)))
FeatITop8_alimentos_3 = nu.abs(nu.fft.fft(nu.mean(I8_alimentos_3[:n_pontos],1)))
FeatRTop8_alimentos_3 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_alimentos_3[:n_pontos],1)+eps,nu.mean(I8_alimentos_3[:n_pontos],1)+eps)))
 
# alimentos 4
# top 15
FeatVTop15_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(V15_alimentos_4[:n_pontos],1)))
FeatITop15_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(I15_alimentos_4[:n_pontos],1)))
FeatRTop15_alimentos_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V15_alimentos_4[:n_pontos],1)+eps,nu.mean(I15_alimentos_4[:n_pontos],1)+eps)))
# top 14
FeatVTop14_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(V14_alimentos_4[:n_pontos],1)))
FeatITop14_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(I14_alimentos_4[:n_pontos],1)))
FeatRTop14_alimentos_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V14_alimentos_4[:n_pontos],1)+eps,nu.mean(I14_alimentos_4[:n_pontos],1)+eps)))
# top 4
FeatVTop4_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(V4_alimentos_4[:n_pontos],1)))
FeatITop4_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(I4_alimentos_4[:n_pontos],1)))
FeatRTop4_alimentos_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V4_alimentos_4[:n_pontos],1)+eps,nu.mean(I4_alimentos_4[:n_pontos],1)+eps)))
# top 8
FeatVTop8_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(V8_alimentos_4[:n_pontos],1)))
FeatITop8_alimentos_4 = nu.abs(nu.fft.fft(nu.mean(I8_alimentos_4[:n_pontos],1)))
FeatRTop8_alimentos_4 = nu.abs(nu.fft.fft(nu.divide(nu.mean(V8_alimentos_4[:n_pontos],1)+eps,nu.mean(I8_alimentos_4[:n_pontos],1)+eps)))
 
# Set features
X15=nu.zeros(shape=[12, 200])
X15[0,0:200] = FeatRTop15_hidro_2[:200] 
#X15[0,200:400] = FeatVTop15_hidro_2[:200]
#X15[0,400:600] = FeatITop15_hidro_2[:200]
X15[1,0:200] = FeatRTop15_pici_3[:200] 
#X15[1,200:400] = FeatVTop15_pici_3[:200]
#X15[1,400:600] = FeatITop15_pici_3[:200]
X15[2,0:200] = FeatRTop15_pici_4[:200] 
#X15[2,200:400] = FeatVTop15_pici_4[:200]
#X15[2,400:600] = FeatITop15_pici_4[:200]
X15[3,0:200] = FeatRTop15_pici_5[:200] 
#X15[3,200:400] = FeatVTop15_pici_5[:200]
#X15[3,400:600] = FeatITop15_pici_5[:200]
X15[4,0:200] = FeatRTop15_pici_6[:200] 
#X15[4,200:400] = FeatVTop15_pici_6[:200]
#X15[4,400:600] = FeatITop15_pici_6[:200]
X15[5,0:200] = FeatRTop15_pici_7[:200] 
#X15[5,200:400] = FeatVTop15_pici_7[:200]
#X15[5,400:600] = FeatITop15_pici_7[:200]
X15[6,0:200] = FeatRTop15_pici_8[:200] 
#X15[6,200:400] = FeatVTop15_pici_8[:200]
#X15[6,400:600] = FeatITop15_pici_8[:200]
X15[7,0:200] = FeatRTop15_hidro_3[:200] 
#X15[7,200:400] = FeatVTop15_hidro_3[:200]
#X15[7,400:600] = FeatITop15_hidro_3[:200]
X15[8,0:200] = FeatRTop15_alimentos_1[:200] 
#X15[8,200:400] = FeatVTop15_alimentos_1[:200]
#X15[8,400:600] = FeatITop15_alimentos_1[:200]
X15[9,0:200] = FeatRTop15_alimentos_2[:200] 
#X15[9,200:400] = FeatVTop15_alimentos_2[:200]
#X15[9,400:600] = FeatITop15_alimentos_2[:200]
X15[10,0:200] = FeatRTop15_alimentos_3[:200] 
#X15[10,200:400] = FeatVTop15_alimentos_3[:200]
#X15[10,400:600] = FeatITop15_alimentos_3[:200]
X15[11,0:200] = FeatRTop15_alimentos_4[:200] 
#X15[11,200:400] = FeatVTop15_alimentos_4[:200]
#X15[11,400:600] = FeatITop15_alimentos_4[:200]
 
X14=nu.zeros(shape=[12, 200])
X14[0,0:200] = FeatRTop14_hidro_2[:200] 
#X14[0,200:400] = FeatVTop14_hidro_2[:200]
#X14[0,400:600] = FeatITop14_hidro_2[:200]
X14[1,0:200] = FeatRTop14_pici_3[:200] 
#X14[1,200:400] = FeatVTop14_pici_3[:200]
#X14[1,400:600] = FeatITop14_pici_3[:200]
X14[2,0:200] = FeatRTop14_pici_4[:200] 
#X14[2,200:400] = FeatVTop14_pici_4[:200]
#X14[2,400:600] = FeatITop14_pici_4[:200]
X14[3,0:200] = FeatRTop14_pici_5[:200] 
#X14[3,200:400] = FeatVTop14_pici_5[:200]
#X14[3,400:600] = FeatITop14_pici_5[:200]
X14[4,0:200] = FeatRTop14_pici_6[:200] 
#X14[4,200:400] = FeatVTop14_pici_6[:200]
#X14[4,400:600] = FeatITop14_pici_6[:200]
X14[5,0:200] = FeatRTop14_pici_7[:200] 
#X14[5,200:400] = FeatVTop14_pici_7[:200]
#X14[5,400:600] = FeatITop14_pici_7[:200]
X14[6,0:200] = FeatRTop14_pici_8[:200] 
#X14[6,200:400] = FeatVTop14_pici_8[:200]
#X14[6,400:600] = FeatITop14_pici_8[:200]
X14[7,0:200] = FeatRTop14_hidro_3[:200] 
#X14[7,200:400] = FeatVTop14_hidro_3[:200]
#X14[7,400:600] = FeatITop14_hidro_3[:200]
X14[8,0:200] = FeatRTop14_alimentos_1[:200] 
#X14[8,200:400] = FeatVTop14_alimentos_1[:200]
#X14[8,400:600] = FeatITop14_alimentos_1[:200]
X14[9,0:200] = FeatRTop14_alimentos_2[:200] 
#X14[9,200:400] = FeatVTop14_alimentos_2[:200]
#X14[9,400:600] = FeatITop14_alimentos_2[:200]
X14[10,0:200] = FeatRTop14_alimentos_3[:200] 
#X14[10,200:400] = FeatVTop14_alimentos_3[:200]
#X14[10,400:600] = FeatITop14_alimentos_3[:200]
X14[11,0:200] = FeatRTop14_alimentos_4[:200] 
#X14[11,200:400] = FeatVTop14_alimentos_4[:200]
#X14[11,400:600] = FeatITop14_alimentos_4[:200]
 
X4=nu.zeros(shape=[12, 200])
X4[0,0:200] = FeatRTop4_hidro_2[:200] 
#X4[0,200:400] = FeatVTop4_hidro_2[:200]
#X4[0,400:600] = FeatITop4_hidro_2[:200]
X4[1,0:200] = FeatRTop4_pici_3[:200] 
#X4[1,200:400] = FeatVTop4_pici_3[:200]
#X4[1,400:600] = FeatITop4_pici_3[:200]
X4[2,0:200] = FeatRTop4_pici_4[:200] 
#X4[2,200:400] = FeatVTop4_pici_4[:200]
#X4[2,400:600] = FeatITop4_pici_4[:200]
X4[3,0:200] = FeatRTop4_pici_5[:200] 
#X4[3,200:400] = FeatVTop4_pici_5[:200]
#X4[3,400:600] = FeatITop4_pici_5[:200]
X4[4,0:200] = FeatRTop4_pici_6[:200] 
#X4[4,200:400] = FeatVTop4_pici_6[:200]
#X4[4,400:600] = FeatITop4_pici_6[:200]
X4[5,0:200] = FeatRTop4_pici_7[:200] 
#X4[5,200:400] = FeatVTop4_pici_7[:200]
#X4[5,400:600] = FeatITop4_pici_7[:200]
X4[6,0:200] = FeatRTop4_pici_8[:200] 
#X4[6,200:400] = FeatVTop4_pici_8[:200]
#X4[6,400:600] = FeatITop4_pici_8[:200]
X4[7,0:200] = FeatRTop4_hidro_3[:200] 
#X4[7,200:400] = FeatVTop4_hidro_3[:200]
#X4[7,400:600] = FeatITop4_hidro_3[:200]
X4[8,0:200] = FeatRTop4_alimentos_1[:200] 
#X4[8,200:400] = FeatVTop4_alimentos_1[:200]
#X4[8,400:600] = FeatITop4_alimentos_1[:200]
X4[9,0:200] = FeatRTop4_alimentos_2[:200] 
#X4[9,200:400] = FeatVTop4_alimentos_2[:200]
#X4[9,400:600] = FeatITop4_alimentos_2[:200]
X4[10,0:200] = FeatRTop4_alimentos_3[:200] 
#X4[10,200:400] = FeatVTop4_alimentos_3[:200]
#X4[10,400:600] = FeatITop4_alimentos_3[:200]
X4[11,0:200] = FeatRTop4_alimentos_4[:200] 
#X4[11,200:400] = FeatVTop4_alimentos_4[:200]
#X4[11,400:600] = FeatITop4_alimentos_4[:200]
 
X8=nu.zeros(shape=[12, 200])
X8[0,0:200] = FeatRTop8_hidro_2[:200] 
#X8[0,200:400] = FeatVTop8_hidro_2[:200]
#X8[0,400:600] = FeatITop8_hidro_2[:200]
X8[1,0:200] = FeatRTop8_pici_3[:200] 
#X8[1,200:400] = FeatVTop8_pici_3[:200]
#X8[1,400:600] = FeatITop8_pici_3[:200]
X8[2,0:200] = FeatRTop8_pici_4[:200] 
#X8[2,200:400] = FeatVTop8_pici_4[:200]
#X8[2,400:600] = FeatITop8_pici_4[:200]
X8[3,0:200] = FeatRTop8_pici_5[:200] 
#X8[3,200:400] = FeatVTop8_pici_5[:200]
#X8[3,400:600] = FeatITop8_pici_5[:200]
X8[4,0:200] = FeatRTop8_pici_6[:200] 
#X8[4,200:400] = FeatVTop8_pici_6[:200]
#X8[4,400:600] = FeatITop8_pici_6[:200]
X8[5,0:200] = FeatRTop8_pici_7[:200] 
#X8[5,200:400] = FeatVTop8_pici_7[:200]
#X8[5,400:600] = FeatITop8_pici_7[:200]
X8[6,0:200] = FeatRTop8_pici_8[:200] 
#X8[6,200:400] = FeatVTop8_pici_8[:200]
#X8[6,400:600] = FeatITop8_pici_8[:200]
X8[7,0:200] = FeatRTop8_hidro_3[:200] 
#X8[7,200:400] = FeatVTop8_hidro_3[:200]
#X8[7,400:600] = FeatITop8_hidro_3[:200]
X8[8,0:200] = FeatRTop8_alimentos_1[:200] 
#X8[8,200:400] = FeatVTop8_alimentos_1[:200]
#X8[8,400:600] = FeatITop8_alimentos_1[:200]
X8[9,0:200] = FeatRTop8_alimentos_2[:200] 
#X8[9,200:400] = FeatVTop8_alimentos_2[:200]
#X8[9,400:600] = FeatITop8_alimentos_2[:200]
X8[10,0:200] = FeatRTop8_alimentos_3[:200] 
#X8[10,200:400] = FeatVTop8_alimentos_3[:200]
#X8[10,400:600] = FeatITop8_alimentos_3[:200]
X8[11,0:200] = FeatRTop8_alimentos_4[:200] 
#X8[11,200:400] = FeatVTop8_alimentos_4[:200]
#X8[11,400:600] = FeatITop8_alimentos_4[:200]
 
Y15 = 0*nu.ones([12]);
Y14 = 0*nu.ones([12]);
Y4 = 1*nu.ones([12]);
Y8 = 1*nu.ones([12]);
# define input and output matrix
X = nu.concatenate((X15, X14, X4, X8), axis=0)
y = nu.concatenate((Y15, Y14, Y4, Y8), axis=0)

# define classification model.
dtree = DecisionTreeClassifier()
rfore = RandomForestClassifier(n_estimators=1000)
perce = linear_model.Perceptron(penalty='l1')
rlasso = linear_model.RandomizedLasso()

# evaluate classification model
y_dtree_est = nu.zeros([12,4])
y_rfore_est = nu.zeros([12,4])
y_perce_est = nu.zeros([12,4])
y_rlasso_est = nu.zeros([12,4])
y_test = nu.zeros([12,4])

y_dtree_prob = nu.zeros([12,4])
y_rfore_prob = nu.zeros([12,4])
y_perce_prob = nu.zeros([12,4])
y_rlasso_prob = nu.zeros([12,4])

for k in range(12):
	d_trainn = nu.arange(48)
	d_test = [k, 12+k, 24+k, 36+k]
	d_train = nu.delete(d_trainn,d_test)

	X_train = X[d_train,:]
	X_test = X[d_test,:]
	Y_train = y[d_train]
	Y_test = y[d_test]

	# normalization - 0 mean and unit variance
	#scaler = preprocessing.StandardScaler().fit(X_train)
	#X_test=scaler.transform(X_test)  
	#X_train=scaler.transform(X_train)

	# feature selection
	# data reduction
	# randomized lasso
	#rlasso = rlasso.fit(X_train, Y_train)
	#rlasso.transform(X_train)
	#rlasso.transform(X_test)

	#print('Selected features: %s' % (rlasso.get_support()))

	# classification model
	# decision tree
	dtree = dtree.fit(X_train, Y_train)
	y_dtree_est[k,:] = dtree.predict(X_test)
	tmp = dtree.predict_proba(X_test)
	y_dtree_prob[k,:] = tmp[:,1]

	# random forest
	rfore = rfore.fit(X_train, Y_train)
	y_rfore_est[k,:] = rfore.predict(X_test)
	tmp = rfore.predict_proba(X_test)
	y_rfore_prob[k,:] = tmp[:,1]

	# perceptron
	perce = perce.fit(X_train, Y_train)
	y_perce_est[k,:] = perce.predict(X_test)



	# real output
	y_test[k,:] = Y_test

print('Decision Tree: \n %s' % (y_dtree_est))
print('Random Forest: \n %s' % (y_rfore_est))
print('Perceptron: \n %s' % (y_perce_est))

print('Performance (Decision Tree): %s' % nu.divide(nu.sum((y_dtree_est==Y_test)),48.0))
print('Performance (Random Forest): %s' % nu.divide(nu.sum((y_rfore_est==Y_test)),48.0))
print('Performance (Perceptron): %s' % nu.divide(nu.sum((y_perce_est==Y_test)),48.0))

# train with all samples
scaler = preprocessing.StandardScaler().fit(X)
scaler.transform(X)  
rfore = rfore.fit(X, y)

# save archive to reload later
f = open('projATT_strfore_win.pckl', 'wb')
pickle.dump(rfore, f)
f.close()

f1 = open('projATT_scaler_win.pckl', 'wb')
pickle.dump(scaler, f1)
f1.close()
#pl.stem(nu.arange(n_pontos),FeatRTop15_hidro_2,'r')
#pl.stem(nu.arange(n_pontos),FeatRTop15_pici_4,'g')
#pl.stem(nu.arange(n_pontos),FeatRTop15_pici_5,'k')
#pl.stem(nu.arange(n_pontos),FeatRTop15_pici_6)
#pl.figure(1).show()
#raw_input()

