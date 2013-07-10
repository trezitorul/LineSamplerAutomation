#This the new and revised python script for the linesampler operation. This script was created due to the need to restructure the previous version of this script.
 
#import sys
import os
#sys.path.append("/opt/visit2.6.2/src/lib/site-packages")
#from visit import *
#Launch(vdir="/opt/visit2.6.2/src/bin")
import math

def createEnviroment(expr):
	"""
	This creates the enviroment of operation by bringing into existance all of the proper variables that will eventually be used and plotted.
	
	Keyword Arguments:
	array-Gives the tuple with each of the chords specified in an array
	expr-This has four things required for every expression, the proper database from which the variables are to be accessed,The objects for which the expression will be repeated, The expression name, and the actual expression 
	
	(database, array of repeated expr, id, expression)
	"""
	print("")
	print("Beginning To Create Enviroment for Processing")
	openDatabases(expr)
	createVariables(expr)
	print("Enviroment Created Successfully with the following Variables")
	print("")
	print("")
	print(Expressions())
	print("")
	print("")
def createVariables(expr):
	print("Creating Variables for Enviroment")
	for ex in expr:
		ActivateDatabase(ex[0])
		if len(ex[1])==0:
			DefineScalarExpression(ex[2],ex[3])
		else:
			for obj in ex[1]:
				DefineScalarExpression(ex[2]+str(obj),formatExpr(obj,ex[3]))

def formatExpr(var,expr):
	print("Formatting Expression for " + str(var) + " with Expression : " + expr)
	temp =[]
	out=expr
	for i in range(len(var)):
		temp=out.split("$"+str(i))
		out=""
		for k in range(len(temp)-1):
			out+=temp[k]+str(var[i])
		out+=temp[-1]
	return out
	
def openDatabases(expr):
	for db in expr:
		print("Opening database :" + db[0])
		OpenDatabase(db[0])

#################################################################l

def setLineSamplerAttr(chan,mode,attr):
	"""
	Used to set the line sampler attributes in a modal way

	mode -- 1 is sample channel and return sample
		2 is integrate channel and return integral
		3 is toroidal sample
	attr -- an array which has the various properties of the line sampler
		for simpler sampler [res,scale]
		for toroidal sample mode [linRes,scale,startAngle, endAngle, angRes]
		for toroidal Integral mode [res, scale]
	"""
	if(mode==1):
		print("Line Sampler Mode Initiated")
    		ls=LineSamplerAttributes()
    		ls.arrayConfiguration=ls.Manual
    		ls.sampleDistance=attr[0]
    		ls.viewDimension=ls.One
		ls.channelList = chan
		ls.heightPlotScale=attr[1]
	elif(mode==2):
		print("Channel Integral Mode has not be implemented yet")
	elif(mode==3):		
		print("Toroidal Sample Mode Initiated")
    		ls=LineSamplerAttributes()
    		ls.arrayConfiguration=ls.Manual
		ls.channelIntegration=ls.IntegrateAlongChannel
		ls.toroidalIntegration=ls.ToroidalTimeSample
		ls.toroidalAngleStart=attr[2]
		ls.toroidalAngleStop=attr[3]
		ls.toroidalAngleStride=attr[4]
    		ls.sampleDistance=attr[0]
    		ls.viewDimension=ls.One
		ls.channelList = chan
		ls.heightPlotScale=attr[1]
    	SetOperatorOptions(ls)

def saveOutputData(op,expr,chan,batchName):
	createFileSys(expr,batchName)
	s=SaveWindowAttributes()
	s.outputToCurrentDirectory=0
	s.outputDirectory="./"+batchName+"/"+expr
	s.format=s.PNG
	s.family=0
	s.screenCapture=0
	s.fileName=expr+str(chan)+op
	SetSaveWindowAttributes(s)
	SaveWindow()

def createFileSys(expr,batchName):
	try:
		os.mkdir(batchName)
	except:
		pass

	try:
		os.mkdir(batchName+"/"+expr)
	except:
		pass

#####################################################
def rotSymLineSample(res,scale,expr,batchName):
	for ex in expr:
		if len(ex[1])!=0:
			for chan in ex[1]:
				rotSymChanSample(ex[0],ex[2],chan,res,scale,batchName)

def rotSymChanSample(dB,expr,chan,res,scale,batchName):
	AddWindow()
	ActivateDatabase(dB)
	activeVar=expr+"("+str(chan[0])+", "+str(chan[1])+", 0, "+str(chan[3])+", "+str(chan[4])+")"
	print(activeVar)
	#activeVar=expr+"("+str(chan[0])+", "+str(chan[1])+", 0, "+str(chan[3])+")"
 	ChangeActivePlotsVar(activeVar)
	AddPlot("Pseudocolor",activeVar)
	AddOperator("LineSampler")
	setLineSamplerAttr(chan,1,[res,scale])
	DrawPlots()
	saveOutputData("LS",expr,chan,batchName)
	DeleteWindow()

def rotSymToroidalInt(linRes,angRes,scale,startAng,stopAng,expr,batchName):
	for ex in expr:
		if len(ex[1])!=0:
			for chan in ex[1]:
				rotSymToroidalIntChan(ex[0],ex[2],chan,linRes,angRes,startAng,stopAng,scale,batchName)

def rotSymToroidalIntChan(dB,expr,chan,linRes,angRes,startAng,stopAng,scale,batchName):
	AddWindow()
	ActivateDatabase(dB)
	activeVar=expr+"("+str(chan[0])+", "+str(chan[1])+", 0, "+str(chan[3])+", "+str(chan[4])+")"
 	ChangeActivePlotsVar(activeVar)
	AddPlot("Pseudocolor",activeVar)
	AddOperator("LineSampler")
	setLineSamplerAttr(chan,3,[linRes,scale,startAng,stopAng,angRes])
	DrawPlots()
	saveOutputData("TI",expr,chan,batchName)
	DeleteWindow()

def rotSymToroidalSampling(array,dBFile,BFile,linRes,startAng,stopAng,angRes,scale, batchName):
	for ang in range(startAng,stopAng,angRes):
		expr=updateExpr(array,dBFile,BFile,ang)
		rotSymLineSample(linRes,scale,expr,batchName)

def updateCurrentArray(array,phi):
	"""
	Causes the position of the chords origin to rotate around the plasma at a fixed R, Z
	
	Keyword Arguments:
	array -- array of chord specification tuples
	phi -- angle to update all of the chords positions to

	Returns:
	The rotated array in the same format as the original array 
	"""

	newArray=array
	k=0
	for chord in newArray:
		newArray[k]=(chord[0],chord[1],phi,chord[3],chord[4])
		k+=1
	return newArray

def updateExpr(array,dBFile,BFile,phi): 
	newArray=updateCurrentArray(array,phi)
	expr=[#(BFile,newArray,"dn","npert")
(BFile,[],"R","{1,0,0}*coord(B)[0]/sqrt(coord(B)[0]^2+coord(B)[1]^2)+{0,1,0}*coord(B)[1]/sqrt(coord(B)[0]^2+coord(B)[1]^2)")
,(BFile,[],"B_R","B*R")
,(BFile,[],"B_Z","B*{0,0,1}")
,(BFile,newArray,"dnB","$4*(B_R*cos($3*(3.14159/180))+sin($3*(3.14159/180))*B_Z)")
#,(BFile,newArray,"dnB","npert*$4*(B_R*cos($3*(3.14159/180))+sin($3*(3.14159/180))*B_Z)")
#,(dBFile,newArray,"dBn","density*$4*(dB_R*cos($3*(3.14159/180))+sin($3*(3.14159/180))*dB_Z)"),
,(dBFile,[],"dB_R","dB*R")
,(dBFile,[],"dB_Z","dB*{0,0,1}")
#,(BFile,newArray,"n","density") ]
]
	return expr
##################################################################

array=[(6.08864,1.132,0, 181.701,.1),(6.08864,1.132,0, 184.642,.1),(6.08864,1.132,0, 187.853,.1),(6.08864,1.132,0, 192.718,.1)]
#array=[(6.08864,1.132,0,3.1712,.1),(6.08864,1.132,0,3.2226,.1),(6.08864,1.132,0,3.2786,.1),(6.08864,1.132,0,3.3635,.1)]

BFile = "hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo"
dBFile="hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo"
#expr=[(BFile,array,"dn","npert")
#,(BFile,[],"R","{1,0,0}*coord(B)[0]/sqrt(coord(B)[0]^2+coord(B)[1]^2)+{0,1,0}*coord(B)[1]/sqrt(coord(B)[0]^2+coord(B)[1]^2)")
#,(BFile,[],"B_R","B*R")
#,(BFile,[],"B_Z","B*{0,0,1}")
#,(BFile,array,"dnB","npert*$4*(B_R*cos($3)+sin($3)*B_Z)")
#,(BFile,array,"dBn","density*$4*(dB_R*cos($3)+sin($3)*dB_Z)",
#(dBFile,[],"dB_R","dB*R")
#,(dBFile,[],"dB_Z","dB*{0,0,1}",
#,(BFile,array,"n","density")]
expr = updateExpr(array,dBFile,BFile,0)
createEnviroment(expr)
batchName="B*dl Verification"
rotSymLineSample(.1,1,expr,batchName)
#rotSymToroidalSampling(array,dBFile,BFile,.1,0,360,360/8,1,batchName)
#rotSymToroidalInt(.1,1,1,0,360,expr,batchName)
