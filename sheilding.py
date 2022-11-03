import random
import math
import numpy as np


def slab_transmission(Sig_s,Sig_a,thickness,N,isotropic=False):

	Sig_t = Sig_a + Sig_s
	iSig_t = 1/Sig_t
	transmission = 0.0
	N = int(N)
	for i in range(N):
		if (isotropic):
			mu = random.random()
		else:
			mu = 1.0
		x = 0
		alive = True
		while (alive):
				#get distance to collision
			l = -math.log(1-random.random())*iSig_t
			#move particle
			x += l*mu
			#still in the slab?
			if (x>thickness):
				transmission += 1
				alive = False
			elif (x<0):
				alive = False
			else:
				"""#scatter or absorb"""
				
				if (random.random() < Sig_s*iSig_t):
					#scatter, pick new mu
					mu = random.uniform(-1,1)
				else: #absorbed
					alive = False
	transmission1 = transmission/N
	return transmission1
	

N = 1000000
Sigma_s = 0.75
Sigma_a = 2.0 - Sigma_s
thickness=3.0

transmission=[]
print("\n\n\n")
for i in range(200):
		transmission.append(slab_transmission(Sigma_s,Sigma_a, thickness,N,isotropic=True))
		print("trial no ",i+1,"Out of",N,"neutrons only",int(transmission[i]*N), "made it through. The fraction that made it through was ",transmission[i])
		
transmission=np.array(transmission)
print("\n\n#################################################################################################################################################")		
print(f"\n\n   
