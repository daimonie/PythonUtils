import sys
import numpy as np

def printMatrix(M):
	shaper = M.shape;
	for i in range(shaper[0]):
		row = "";
		for j in range(shaper[1]):
			row = "%s\t%.3f+%.3fj" % (row, np.real(M[i,j]), np.imag(M[i,j]));
		print >> sys.stderr, row

	print >> sys.stderr, "\n"
def asciiOutput(list):
	row = "";
	for i in len(list):
		row = "%s\t%.3f" % (row, list[i]);
	print >> sys.stderr, "%s\n" % row