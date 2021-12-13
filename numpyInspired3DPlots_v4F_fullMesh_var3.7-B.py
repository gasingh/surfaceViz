"""
numpyInspired3DPlots_v0

03:21 13/06/2021 | 03:54 13/06/2021 | 05:12 13/06/2021 | 03:54 14/06/2021 | 04:50 14/06/2021

EQUATION: 
WEB: https://medium.com/@sebastiannorena/3d-plotting-in-python-b0dc1c2e5e38
IMG: https://miro.medium.com/max/349/1*_FLXTG8c8qGgRrklLN_axg.png
"""

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext
import itertools as it
import math

# numpyStylized lambdas!
np_linspace = lambda vStart,vStop,vSteps : [vStart+(abs(vStart-vStop)/vSteps)*i for i in range(vSteps+1)]
ijLoop = lambda v1,v2: [(i, j) for i in v1 for j in v2]                         #SQUARE!
#scatterplot3D_byZFunc = lambda vX,vY,vZFunc : map(lambda v: [v[0],v[1],vZFunc(v[0],v[1])],ijLoop(vX,vY))
#scatterplot3D_simple = lambda vX,vY : map(lambda v: [v[0],v[1],0],ijLoop(vX,vY))

scatterplot3D_byZFunc_grouper = lambda vX,vY,vZFunc : rs.AddObjectsToGroup(map(rs.AddPoint, map(lambda v: [v[0],v[1],vZFunc(v[0],v[1])],ijLoop(vX,vY))),rs.AddGroup())
scatterplot3D_simple_grouper = lambda vX,vY : rs.AddObjectsToGroup(map(rs.AddPoint, map(lambda v: [v[0],v[1],0],ijLoop(vX,vY))),rs.AddGroup())

scatterplot3D_byZFunc = lambda vX,vY,vZFunc : map(rs.AddPoint, map(lambda v: [v[0],v[1],vZFunc(v[0],v[1])],ijLoop(vX,vY)))
scatterplot3D_simple = lambda vX,vY : map(rs.AddPoint, map(lambda v: [v[0],v[1],0],ijLoop(vX,vY)))

np_arraySplit = lambda L,n: [L[i: i+n] for i in xrange(0, len(L), n)]
chunks = lambda vL,vN : [vL[i:i + vN] for i in range(0, len(vL), vN)]

# ==============================================================================
density = 75 #45 #200 #45
X = np_linspace(-6,6,density)
#print "X:{}".format(X)
Y = np_linspace(-6,6,density)


zEquationFunction1 = lambda vX,vY : (math.sin(math.sqrt(vX** 2 + vY** 2)))*4.5
#zEquationFunction1 = lambda vX,vY : (math.sin(vX*5)*math.cos(vY*5))*0.5
#zEquationFunction1 = lambda vX,vY : (50 - (vX**2 + vY**2))*.08
#zEquationFunction1 = lambda vX,vY : 50 - (vX**2 + vY**2)
#zByFunction = lambda vX,vY : 50 - (vX**3 +vY**2)
#zByFunction = lambda vX,vY : (vX**2 +vY**2)

rs.EnableRedraw(False)
# FLAT...
#scatterplot3D_simple(X,Y)
# 3D...
ptLstID = scatterplot3D_byZFunc(X,Y,zEquationFunction1)
#print ptLstID
rs.EnableRedraw(True)


ptLstRC = map(rs.coerce3dpoint,ptLstID)
ptLstRC2 = chunks(ptLstRC,density+1)
#ptLstRC2 = np_arraySplit(ptLstRC,46)

#for i,j in enumerate(ptLstRC2): print i,len(j), j
"""for i,j in enumerate(ptLstRC2): 
    #print i,len(j), j
    for m,n in enumerate(j):
        print i,m,len(n),"__"
"""



#rg.Mesh.Vertices
#rg.Collections.MeshVertexList.Add(

mMega = rg.Mesh()
for i in range(0,len(ptLstRC2)-2,1):
    localLst = ptLstRC2[i]
    #print len(localLst)
    #print localLst[0]
    for j in range(0,len(localLst)-2,1):
        #print j
        #print type(localLst[j])
        m = rg.Mesh()
        m.Vertices.Add(localLst[j])
        m.Vertices.Add(localLst[j+1])
        m.Vertices.Add(ptLstRC2[i+1][j+1])
        m.Vertices.Add(ptLstRC2[i+1][j])
        m.Faces.AddFace(0,1,2,3)
        m.Normals.ComputeNormals()
        m.Compact()
        mMega.Append(m)
        #scriptcontext.doc.Objects.AddMesh(m)

mMega.Normals.ComputeNormals()
mMega.Compact()
scriptcontext.doc.Objects.AddMesh(mMega)
#rs.DeleteObjects(ptLstID)


# LET'S FORGET ABOUT A SURFACE FOR THE MOMENT!
#rs.AddNurbsSurface([45,45],ptLst,,,[3,3],