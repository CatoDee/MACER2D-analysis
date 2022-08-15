import numpy as np
'''
This function is used to calculate the distance between two faces in MACER2D
'''
def r_a(x_min,x_max,x_rate,N):
    N1 = N+1
    d_r = np.zeros(N) 
    r_a = np.zeros(N1)
    dr = ((x_max-x_min)*(x_rate-1.0)) / (x_rate**N-1.0)
    r_a[0] = x_min
    for i in range(1,N1):
        r_a[i] = r_a[i-1] + dr*1.1**(i-1)  
        
    return r_a 

def thata_a(theta_min, theta_max,N):
    N1 = N+1
    th_a = np.zeros(N1)
    th_a[0] = theta_min
    d_theta = (theta_max-theta_min)/N
    for i in range(1,N1):
        th_a[i] = th_a[i-1]+d_theta

    return th_a