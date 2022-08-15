#!/usr/bin/env python
# filename:vector.py (zmgan@shao.ac.cn)
# created: nov.13, 2014
###########################################################     
from numpy import array,sum,sin,cos,sqrt
'''
this script to implement 3D coordinate transform, and some 
vector operations.
'''

def CART_XYZ(coord,geom):
    '''
    this script to transform a position vector into 
    a cartesian coordinate system.
    '''
    if  (geom == "spherical polar"):
        sinseta = sin(coord[1])
        cosseta = cos(coord[1])
        sinphi  = sin(coord[2])
        cosphi  = cos(coord[2])
    
        z = coord[0]*cosseta
        w = coord[0]*sinseta
        x = w*cosphi
        y = w*sinphi
        
    elif(geom == "cylindrical"):
        sinphi  = sin(coord[2])
        cosphi  = cos(coord[2])
        
        z = coord[0]
        w = coord[1]
        x = w*cosphi
        y = w*sinphi
        
    elif(geom == "cartesian"):   
        x = coord[0]
        y = coord[1]
        z = coord[2]
        
    else:
        print "UNKOWN COORDINATE SYSTEM"
    
    return array([x,y,z])


def dot_product(u,v):
    u=array(u); v=array(v)
    return sum(u*v)


def cross_product(u,v):
    x = u[1]*v[2]-u[2]*v[1]
    y = u[2]*v[0]-u[0]*v[2]
    z = u[0]*v[1]-u[1]*v[0]
    return array([x,y,z])


def normalise(u):
    u = array(u)
    return u/sqrt(sum(u*u))

