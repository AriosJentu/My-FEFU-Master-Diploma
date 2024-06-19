k = 0.55
tau = 2

def euler(S0, I0, R0, h, t0, tmax):

	aS = [S0]
	aI = [I0]
	aR = [R0]
	aT = [t0]

	Scur = S0
	Icur = I0
	Rcur = R0

	n = int(tmax//h)

	for i in range(n):
		Snew = Scur + h*(-k*Scur*Icur)
		Inew = Icur + h*(k*Scur*Icur - Icur/tau)
		Rnew = Rcur + h*(Icur/tau)

		Scur = Snew
		Icur = Inew
		Rcur = Rnew

		aS.append(Scur)
		aI.append(Icur)
		aR.append(Rcur)
		aT.append(t0+i*h)

	return aS, aI, aR, aT

S, I, R, t = euler(10, 4, 0, 0.01, 0, 10)

import matplotlib.pyplot as plt
plt.plot(t, S, label="Susceptible")
plt.plot(t, I, label="Infected")
plt.plot(t, R, label="Recovered")
plt.legend()
plt.show()