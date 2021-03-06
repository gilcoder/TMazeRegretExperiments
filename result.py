import numpy as np

trained_agent = {(0, 0) : [[7.56945],   [9.9931324e-01, 3.5007455e-04, 1.1699159e-05, 3.2503571e-04]],
							(0, 1) :  [[8.781567],  [9.9924266e-01, 3.1534981e-04, 5.0686107e-05, 3.9132038e-04]],
							(0, 2) :  [[9.993687],  [9.9929440e-01, 1.7835051e-04, 1.8016310e-04, 3.4709848e-04]],
							(0, 3) :  [[11.205805], [9.9895132e-01, 1.0082869e-04, 6.4013345e-04, 3.0775202e-04]],
							(0, 4) :  [[12.417924], [9.9739885e-01, 5.6933462e-05, 2.2716911e-03, 2.7253549e-04]],
							(0, 5) :  [[13.630039], [9.9169946e-01, 3.2013868e-05, 8.0281319e-03, 2.4034319e-04]],
							(0, 6) :  [[15.669212], [9.7181129e-01, 1.7741850e-05, 2.7962137e-02, 2.0889653e-04]],
							(0, 7) :  [[17.82245],  [9.0705454e-01, 9.3650406e-06, 9.2763223e-02, 1.7293393e-04]],
							(0, 8) :  [[19.97569],  [7.3331606e-01, 4.2818037e-06, 2.6655555e-01, 1.2400397e-04]],
							(0, 9) :  [[22.128927], [4.3627763e-01, 1.4406462e-06, 5.6365544e-01, 6.5434258e-05]],
							(1, 0) :  [[27.06679],  [9.9998403e-01, 1.1336301e-05, 8.9132513e-08, 4.5229431e-06]],
							(1, 1) :  [[29.870958], [9.9997973e-01, 1.2124559e-05, 4.8853724e-07, 7.6772249e-06]],
							(1, 2) :  [[32.122322], [9.9997187e-01, 1.2513727e-05, 2.7093718e-06, 1.2865772e-05]],
							(2, 0) :  [[43.52655],  [9.9999964e-01, 3.0831467e-07, 7.1780903e-10, 5.9016259e-08]],
							(2, 1) :  [[46.33072],  [9.9999952e-01, 4.0661220e-07, 3.6712353e-09, 1.0799323e-07]],
							(2, 2) :  [[49.134888], [9.9999928e-01, 4.1966621e-07, 2.0360408e-08, 1.8098019e-07]]}


regreted_agent = {(0, 0) :  [[5.6222916], [9.9919599e-01, 3.4575362e-04, 8.0364052e-06, 4.5023029e-04]],
											(0, 1) :  [[5.349821],  [9.993129e-01, 2.368704e-04, 2.120606e-05, 4.290885e-04]],
											(0, 2) :  [[5.0773516], [9.9947637e-01, 1.1881906e-04, 5.1123476e-05, 3.5370616e-04]],
											(0, 3) :  [[4.804881],  [9.9952567e-01, 5.9595211e-05, 1.2323416e-04, 2.9153351e-04]],
											(0, 4) :  [[4.5324097], [9.9943274e-01, 2.9886571e-05, 2.9701644e-04, 2.4025542e-04]],
											(0, 5) :  [[4.259939],  [9.9907136e-01, 1.4983818e-05, 7.1566983e-04, 1.9794311e-04]],
											(0, 6) :  [[3.9874704], [9.9810612e-01, 7.5077005e-06, 1.7233846e-03, 1.6298411e-04]],
											(0, 7) :  [[3.714996],  [9.9571806e-01, 3.7563991e-06, 4.1441130e-03, 1.3400779e-04]],
											(0, 8) :  [[3.582722],  [9.8995715e-01, 1.8730768e-06, 9.9311871e-03, 1.0980819e-04]],
											(0, 9) :  [[3.9128997], [9.7630185e-01, 9.2646104e-07, 2.3607945e-02, 8.9253801e-05]],
											(1, 0) :  [[24.874039], [9.9996305e-01, 2.2185812e-05, 1.4028117e-07, 1.4707202e-05]],
											(1, 1) :  [[27.010244], [9.9995565e-01, 2.0994936e-05, 5.2119941e-07, 2.2899461e-05]],
											(1, 2) :  [[26.74901],  [9.9994898e-01, 1.8432040e-05, 1.7841099e-06, 3.0759162e-05]],
											(2, 0) :  [[40.16312],  [9.9999833e-01, 1.2139218e-06, 2.4332187e-09, 4.4123226e-07]],
											(2, 1) :  [[42.307903], [9.9999785e-01, 1.4648048e-06, 8.5563530e-09, 7.3301345e-07]],
											(2, 2) :  [[44.452682], [9.9999762e-01, 1.2798776e-06, 3.2370078e-08, 1.1172995e-06]]}

states = [(0, 0), (0, 1), (0, 2), (0, 3),  (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0,9), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]



def default_def():
	Q1 = {}
	Q2 = {}
	for s in states:
		r1 = trained_agent[s]
		r2 = regreted_agent[s]
		for a in [0, 1, 2, 3]:
			Q1[(s, a)] = r1[0][0] * r1[1][a]
			Q2[(s, a)] = r2[0][0] * r2[1][a]

	for s in states:
		r = trained_agent[s]
		r2 = regreted_agent[s]
		a = np.argmax(r[1])
		b = np.argmax(r2[1])
		newvalue1 = Q2[(s, b)]
		newvalue2 = Q2[(s, a)]
		print("Regret(%s)"%(s, ), " = ", newvalue1 - newvalue2)	

def probabilistic_def():
	Q1 = {}
	Q2 = {}
	for s in states:
		r1 = trained_agent[s]
		r2 = regreted_agent[s]
		for a in [0, 1, 2, 3]:
			Q1[(s, a)] = r1[0][0] * r1[1][a]
			Q2[(s, a)] = r2[0][0] * r2[1][a]

	for s in states:
		r = trained_agent[s]
		r2 = regreted_agent[s]
		newvalue1 = 0
		for b in [0, 1, 2, 3]:
			newvalue1 += r2[1][b] * Q2[(s, b)]
		newvalue2 = 0
		for a in [0, 1, 2, 3]:
			newvalue2 += r[1][a] * Q2[(s, a)]
		
		print("Regret(%s)"%(s, ), " = ", newvalue1 - newvalue2)


if __name__ == "__main__":
	probabilistic_def()



