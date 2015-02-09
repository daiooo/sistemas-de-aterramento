import numpy as np
import glob
import projATT_functions as pat
path ='/home/alex/pici8_planop_23052014/'
var = 'M15'
A = glob.glob((path + var + 'V*'))

V=np.zeros([5000,1])
I=np.zeros([5000,1])

for k in range(len(A)):
	# open voltage file
	f1 = open(A[k])
	dataV = np.loadtxt(f1)
	
	# open current file
	B = A[k].replace((var+'V'),(var+'I'))
	f2 = open(B)
	dataI = np.loadtxt(f2)

	# verifica se acquisicao esta completa
	if dataV.shape[1]==2: 
		# voltage
		RV = dataV[:,1]
		RV[range(1000)] = np.zeros([1000])
		Rav = pat.movingaverage(RV, 100) # exclui a possobilidade de selecionar um maximo "falso"
		ind_max = Rav.argmax()
		ind_max2 = RV[ind_max-300:ind_max].argmax()
		ind_max = ind_max - (300-ind_max2)

		# current
		RI = dataI[:,1]
		ind_max3 = RI[ind_max-300:ind_max+300].argmax()
		if ind_max3 >300:
			ind_maxI = ind_max + (ind_max3-300)
		else:
			ind_maxI = ind_max - (300-ind_max3)

		if RV[ind_max] > 200 and ind_max<44000: # Utiliza apenas medicoes em que a tensao esteja acima de 200V
			print('V ---> indice: %s | maximo: %s', (ind_max, RV[ind_max]))
			# voltage
			C=np.reshape(RV[ind_max-10:ind_max+4990],(5000,1))
			V=np.append(V,C,axis=1) # armazena dado em B

			# current
			E=np.reshape(RI[ind_maxI-10:ind_maxI+4990],(5000,1))
			I=np.append(I,E,axis=1) # armazena dado em B
			print('I ---> indice: %s | maximo: %s', (ind_maxI, RI[ind_maxI]))



  
