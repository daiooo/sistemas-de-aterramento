#coding: utf-8
import numpy as np

def trainAndStoreTheModel():
    from scipy.io import loadmat
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import preprocessing
    import pickle
    
    loaded_data = loadmat("dataToTrainRfModel", matlab_compatible=True)
    rforee = RandomForestClassifier(n_estimators=2000)
    
    X = loaded_data['X'].squeeze()
    y1 = loaded_data['y1'].squeeze()
    y2 = loaded_data['y2'].squeeze()
    
    scaler = preprocessing.StandardScaler().fit(X)
    X=scaler.transform(X)  
    rfore = rforee.fit(X, y1)
    f = open('projATT_strfore.pckl', 'wb')
    pickle.dump(rfore, f,protocol=pickle.HIGHEST_PROTOCOL)
    f.close()    

    rfore_exact = rforee.fit(X, y2)
    f1 = open('projATT_strfore_exact.pckl', 'wb')
    pickle.dump(rfore_exact, f1,protocol=pickle.HIGHEST_PROTOCOL)
    f1.close()

    f3 = open('projATT_scaler.pckl', 'wb')
    pickle.dump(scaler, f3,protocol=pickle.HIGHEST_PROTOCOL)
    f3.close()


def returnNumberRods(V, I):
    import pickle

    eps = 0.1
    n_pontos = 250
    # extract variables from data
    # [V,I]=function_loadData( path , var )
    # extract features

    #[V,I] = extract_transient(V1,I1)

    FeatV = np.abs(np.fft.fft(np.mean(V[:n_pontos],1)))
    FeatI = np.abs(np.fft.fft(np.mean(I[:n_pontos],1)))
    FeatR = np.abs(np.fft.fft(np.divide(np.mean(V[:n_pontos],1)+eps,np.mean(I[:n_pontos],1)+eps)))
        
    #X=np.zeros(shape=[1, n_pontos])
    X = FeatR[:int(n_pontos/2)]
    #X[0,200:400] = FeatV[:200]
    #X[0,400:600] = FeatI[:200]
    f2 = open('projATT_scaler.pckl','rb')
    scaler = pickle.load(f2)
    f2.close()
    X = scaler.transform(X)

    f = open('projATT_strfore.pckl','rb')
    rfore = pickle.load(f)
    f.close()
    C = rfore.predict(X)
    print('Approximated class: %s', C )
    
    f1 = open('projATT_strfore_exact.pckl','rb')
    rfore = pickle.load(f1)
    f.close()
    C_exact = rfore.predict(X)
    print('Exact class: %s', C_exact )
    
    return C,C_exact

def extract_transient(dataV, dataI):
    sizeToSave = 5e4
    
    #[m,n]=dataV.shape()
    n=dataV.ndim
    
    V=np.zeros([sizeToSave,1])
    I=np.zeros([sizeToSave,1])
    ind_maxI_toSave = np.zeros([1,n])
    ind_maxV_toSave = np.zeros([1,n])
    

    for k in range(n):
    # voltage
        RV = dataV
        RV[range(1000)] = np.zeros([1000])
        Rav = movingaverage(RV, 1000) # exclui a possobilidade de selecionar um maximo "falso"
        ind_max = Rav.argmax()
        ind_max2 = RV[ind_max-1000:ind_max].argmax()
        ind_max = ind_max - (1000-ind_max2) # valor de pico do sinal de tensao
    
        # current
        RI = dataI
        ind_max3 = RI[ind_max-1000:ind_max+1000].argmax()
        if ind_max3 >1000:
            ind_maxI = ind_max + (ind_max3-1000)
        else:
            ind_maxI = ind_max - (1000-ind_max3)
    
        if RI[ind_maxI]<50 and RV[ind_max] > 80 and ind_max<8e5-sizeToSave: # Utiliza apenas medicoes em que a tensao esteja acima de 200V
            print('V ---> indice: %s | maximo: %s' % (ind_max, RV[ind_max]))
            # voltage
            C=np.reshape(RV[ind_max-10:ind_max+sizeToSave-10],(sizeToSave,1))
            V=np.append(V,C,axis=1) # armazena dado em B
    
            # current
            E=np.reshape(RI[ind_maxI-10:ind_maxI+sizeToSave-10],(sizeToSave,1))
            I=np.append(I,E,axis=1) # armazena dado em B
            print('I ---> indice: %s | maximo: %s'% (ind_maxI, RI[ind_maxI]))
            
            # utilizado para ver a defasagem.
            ind_maxI_toSave[k] = ind_maxI # iudice de tensao
            ind_maxV_toSave[k] = ind_max # indice de corrente
        
    V = np.delete(V,0,1)
    I = np.delete(I,0,1)
    return V,I,ind_maxI_toSave,ind_maxV_toSave


def phasor_angle(a,b):
    angle=np.arctan(np.imag(a)/np.real(a)) - np.arctan(np.imag(b)/np.real(b))
    angle = angle*(180.0/np.pi) #degree
    return angle

def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

def function_return_Full_V_and_I(path, var):
    import glob
    
    A = glob.glob((path + var + 'V*'))
    V=np.zeros([5e4,1])
    I=np.zeros([5e4,1])

   
    for k in range(len(A)):
        f1 = open(A[k])
        dataV = np.loadtxt(f1)
        
        # open current file
        B = A[k].replace((var+'V'),(var+'I'))
        f2 = open(B)
        dataI = np.loadtxt(f2)

        if np.prod(dataV.shape)>5e4: 
            I=np.append(I,dataI[:,1],axis=1)
            V=np.append(V,dataV[:,1],axis=1)
    
    V = np.delete(V,0,1)
    I = np.delete(I,0,1)
    return V,I

def function_loadData( path , var ):
    import glob
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
        #print(np.prod(dataV.shape))
        if np.prod(dataV.shape)>5e4: 
                # voltage
                RV = dataV[:,1]
                RV[range(1000)] = np.zeros([1000])
                Rav = movingaverage(RV, 1000) # exclui a possobilidade de selecionar um maximo "falso"
                ind_max = Rav.argmax()
                ind_max2 = RV[ind_max-1000:ind_max].argmax()
                ind_max = ind_max - (1000-ind_max2)
    
            # current
                RI = dataI[:,1]
                ind_max3 = RI[ind_max-1000:ind_max+1000].argmax()
                if ind_max3 >1000:
                    ind_maxI = ind_max + (ind_max3-1000)
                else:
                    ind_maxI = ind_max - (1000-ind_max3)
    
                if RI[ind_maxI]<10 and RV[ind_max] > 150 and ind_max<44000: # Utiliza apenas medicoes em que a tensao esteja acima de 200V
                    print('V ---> indice: %s | maximo: %s' % (ind_max, RV[ind_max]))
                    # voltage
                    C=np.reshape(RV[ind_max-10:ind_max+4990],(5000,1))
                    V=np.append(V,C,axis=1) # armazena dado em B
    
                    # current
                    E=np.reshape(RI[ind_maxI-10:ind_maxI+4990],(5000,1))
                    I=np.append(I,E,axis=1) # armazena dado em B
                    print('I ---> indice: %s | maximo: %s'% (ind_maxI, RI[ind_maxI]))
    V = np.delete(V,0,1)
    I = np.delete(I,0,1)
    return V,I

def function_LabviewResults(path, var):
    import pickle

    eps = 0.000000001;
    n_pontos = 400;
    # extract variables from data
    [V,I]=function_loadData( path , var )
    # extract features
    FeatV = np.abs(np.fft.rfft(np.mean(V[:n_pontos],1)))
    FeatI = np.abs(np.fft.rfft(np.mean(I[:n_pontos],1)))
    FeatR = np.abs(np.fft.rfft(np.divide(np.mean(V[:n_pontos],1)+eps,np.mean(I[:n_pontos],1)+eps)))
        
    X=np.zeros(shape=[1, 600])
    X[0,0:200] = FeatR[:200] 
    X[0,200:400] = FeatV[:200]
    X[0,400:600] = FeatI[:200]

    f = open('projATT_strfore.pckl','rb')
    rfore = pickle.load(f)
    f.close()

    C = rfore.predict(X)
    print('Class: %s', C )
    return C

def function_extractFeatures(V,I):
    import numpy as nu
    n_pontos = 400;
    n_variaveis = 600;
    eps = 0.000000001;
    FeatV = nu.abs(nu.fft.fft(nu.mean(V[:n_pontos],1)))
    FeatI = nu.abs(nu.fft.fft(nu.mean(I[:n_pontos],1)))
    FeatR = nu.abs(nu.fft.fft(nu.divide(nu.mean(V[:n_pontos],1)+eps,nu.mean(I[:n_pontos],1)+eps)))    

    X=nu.zeros(shape=[0, n_variaveis])
    X[0,0:200] = FeatR[:200] 
    X[0,200:400] = FeatV[:200]
    X[0,400:600] = FeatI[:200]
    
    return X
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
