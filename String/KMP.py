def preprocess(P):
	m = len(P)
	cnd = 0
	pos = 2
	T = [0]*m
	while pos<m:
		if P[pos-1] == cnd:
			T[pos] = cnd
			cnd+=1
			pos+=1
		else:
			if cnd>0:
				cnd = T[cnd]
			else:
				T[pos] = 0
				pos+=1

	return T

def kmp(S,P):
	n = len(s)
	m = len(P)
	next = preprocess(P)
	i=0
	j=0
	while i+j<n:
		if P[j]==S[i+j]:
			j+=1
			if j==m:
				return i
		else:
			if T[j]>-1:
				i +=j-T[j]
				j = T[j]
			else:
				i+=1
				j=0

	return n
