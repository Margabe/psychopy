from psychopy import calibTools
import numpy

yy=[0,0.2,0.4,0.8,1.0]
minLum=2.0
maxLum=100.0
gamma=2.2

xxTest=numpy.array([ 0.,          0.48115651,  0.65935329,  0.90354543,  1.        ])
def testGammaInverse_Eq1():
    xx= calibTools.gammaInvFun(yy, minLum, maxLum, gamma, b=0, eq=1)
    assert numpy.allclose(xx,xxTest,0.0001)
def testGammaInverse_Eq4():
    xx= calibTools.gammaInvFun(yy, minLum, maxLum, gamma, b=0.5, eq=4)
    assert numpy.allclose(xx,xxTest,0.0001)