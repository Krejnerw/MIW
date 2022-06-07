import numpy as np
from wartosci_wlasne import find_matrix_eigenvalues
from wektory_wlasne import eigenvectors
from math import sqrt

def sprawdzenie(u, sigma, v):
    h = len(u)
    w = len(v)
    if(h<w):
        z = np.zeros((h,1), dtype=float)
        sigma = np.append(sigma, z, axis=1)
    else:
        z = np.zeros((1,w), dtype=float)
        sigma = np.append(sigma, z, axis=0)
    spr = np.dot(u.T,sigma)
    spr = np.dot(spr, v)
    print(np.round(spr))
    
def svd(macierz):
    h,w = macierz.shape
    # =============obliczanie macierzy u =========================
    aat = np.dot(macierz,macierz.T)
    # print("----------aat---------",aat,sep="\n")
    u = eigenvectors(aat)  
    for ui in u:
        a = 1/sqrt(np.dot(ui.T, ui))
        ui *= a 
    print("----------u---------",u,sep="\n")
    # ========obliczanie wektorów własnych macierzy v ============
    ata = np.dot(macierz.T, macierz)
    # print("----------ata---------",ata,sep="\n")
    vectors_v = eigenvectors(ata)
    # =============obliczanie macierzy sigma ======================
    if(h>w):    
        sigma = sorted(find_matrix_eigenvalues(ata),reverse=True)
    else:
        sigma = sorted(find_matrix_eigenvalues(aat),reverse=True)
        
    for ind, si in enumerate(sigma):
        sigma[ind] = sqrt(si)
    sigma = np.diag(sigma)
    print("----------sigma skrocona---------",sigma,sep="\n")
    
    # =============obliczanie macierzy v =========================
    v = []
    for i in range(len(sigma)):
        tmp = np.dot(macierz.T,u[i].T) * (1/sigma[i][i])
        v.append(tmp)
    if(w>h):
        v.append(vectors_v[-1])
    v = np.array(v)
    print("----------v---------",v,sep="\n")
    
    print("=============SPRAWDZENIE=========================")
    sprawdzenie(u,sigma,v)
    return v
        
    
macierz_a = [[2., 1., 3.],[1., 6., 7.],[3., 7., 9.]]
macierz_d = [[0., 1., 2.],[1., 0., 7.],[9., 7., 9.]]
macierz_b = [[2., 1., 3.],[0., 6., 7.],[0., 0., 9.]]    

b = [[1.,2.,0.],[2.,0.,2.]]
c = [[1.,2.],[2.,0.],[0.,2.]]

a = np.array(
    [
        [1.0, 2.0, 3.0, 4.0, 5.0],
        [2.0, 2.0, 3.0, 4.0, 5.0],
        [3.0, 3.0, 3.0, 4.0, 5.0],
        [4.0, 4.0, 4.0, 4.0, 5.0],
        [5.0, 5.0, 5.0, 5.0, 5.0],
    ])

# macierz_c = np.array(macierz_b)
# macierz_c = a
macierz = np.array(b)

print("-------------------macierz--------------------",macierz,sep="\n")
svd(macierz)
