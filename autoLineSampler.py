#This the new and revised python script for the linesampler operation. This script was created due to the need to restructure the previous version of this script.
 
import sys
import os
sys.path.append("/opt/visit2.6.2/src/lib/site-packages")
from visit import *
Launch(vdir="/opt/visit2.6.2/src/bin")
import math
#import xml.etree.ElementTree as ET

#def getExpr(fileName):
#	tree=ET.parse(fileName)
#	root=tree.getroot()

def createEnviroment(expr):
	"""
	This creates the enviroment of operation by bringing into existence all of the proper variables that will eventually be used and plotted.
	
	Keyword Arguments:
	expr-This has four things required for every expression, the proper database from which the variables are to be accessed,The objects for which the expression will be repeated, The expression name, and the actual expression 
	
	(database, array of repeated expr, id, expression)
	"""
	print("")
	print("Beginning To Create Enviroment for Processing")
	openDatabases(expr)#Opens the databases required for the variables
	createVariables(expr)#Batch generates all of the expression variables from the file
	print("Enviroment Created Successfully with the following Variables")
	print("")
	print("")
	print(Expressions())#Outputs all of the expressions that vist has stored away
	print("")
	print("")

def createVariables(expr):
	"""
	Creates all of the expressions specified in the expr data structure

	Keyword Arguments:
	expr-This has four things required for every expression, the proper database from which the variables in the expression are to be accessed, the objects for which the expression will be repeated, The expression name, and the actual expression.

	Output:
	Loads the proper variables into visit with the variables that contain an array having an expression being defined for every individual chord.
	"""

	print("Creating Variables for Enviroment")
	for ex in expr:#Iterate through expression
		ActivateDatabase(ex[0])#Load the proper database for the particular term of expr
		if len(ex[1])==0:#If there is no array for the variable (IE helper variable) then just defne expr with expr id
			DefineScalarExpression(ex[2],ex[3])
		else:
			for obj in ex[1]:#If there is an array then define an expr for each chord element with the name exprID+chordTuple
				DefineScalarExpression(ex[2]+str(obj),formatExpr(obj,ex[3]))

def formatExpr(var,expr):
	"""
	The expr when defined references the array values by the insertion of $X where X is the location in the chord tuple that the value of the variable that you want in the expression. For example chord is (6,3,0,181) the expression is cos($3) thus the formatExpr will output cos(181)

	Keyword Arguments:
	var-chord tuple
	expr-A visit expression string that has not yet been parsed

	Output:
	The expression string with all of the variables inserted in the proper places
	"""

	print("Formatting Expression for " + str(var) + " with Expression : " + expr)
	temp =[]
	out=expr
	for i in range(len(var)):#For the number of slots in the chord tuple split expr by $X and then insert the correct values
		temp=out.split("$"+str(i))
		out=""
		for k in range(len(temp)-1):
			out+=temp[k]+str(var[i])
		out+=temp[-1]
	return out
	
def openDatabases(expr):
	"""
	This opens all of the databases referenced in the expr datastructure.

	KeywordArguments:
	expr-data structure containing the database, array, expression id, and expression data

	Output:
	Loads all the databases to be used by the expressions to befined
	"""
	for db in expr:#Repeat for all databases in expr
		print("Opening database :" + db[0])
		OpenDatabase(db[0])

#################################################################l

def setLineSamplerAttr(chan,mode,attr):
	"""
	Used to set the line sampler attributes in a modal way
	
	Keyword Arguments:
	mode -- 1 is sample channel and return sample
		2 is integrate channel and return integral
		3 is toroidal sample
	chan -- an array which has the various properties of the line sampler
		for simpler sampler [res,scale]
		for toroidal sample mode [linRes,scale,startAngle, endAngle, angRes]
		for toroidal Integral mode [res, scale]
	attr -- An array that is used to pass in the attributes depending on mode
		For mode 1: [resolution, plotScale]
		For mode 3: [resolution, plotScale, startAng, stopAng, angRes]
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
	"""
	Sets the properties for saving and the file attributes of the saved file

	Keyboard Arguments:
	op - Adds a flag in the name for the different type of mode for instance LS for just linesample and TI for toroidal integrals
	expr - This is the expression type that is being used for instance dnB or dBn
	chan - This is the channel that is currently being saved
	batchName - This is the batch name for the whole run
	"""

	createFileSys(expr,batchName)#This creates the filesystem to save the file system
	s=SaveWindowAttributes()
	s.outputToCurrentDirectory=0
	s.outputDirectory="./"+batchName+"/"+expr
	s.format=s.CURVE
	s.family=0
	s.screenCapture=0
	s.fileName=expr+str(chan)+op
	SetSaveWindowAttributes(s)
	SaveWindow()

def createFileSys(expr,batchName):
	"""
	Creates the file system to store the output files
	Keyword Arguments:
	expr - expression id for the files being created
	batchName - the name of the batch run being done

	Output:
	A file system in the same directory as the script
	With the following structure
	batchName
		-Expr
	"""

	try:
		os.mkdir(batchName)
	except:
		pass

	try:
		os.mkdir(batchName+"/"+expr)
	except:
		pass
#The methods above are used to create the enviroment in visit
#####################################################
#The methods below are used to automate the linesampler system

def rotSymLineSample(res,scale,expr,batchName):
	"""
	This runs through each of the expressions in the expr data structure and runs the line sampler and returns the output at the angles specified by the chord arrays 
	NOTE: For vector products without a dependence on phi 
	Keyword Arguments:
	res - resolution of the line sampler
	scale - plot scale of the line sampler
	expr - the expression datastructure that we are executing
	batchName - name of the batch 

	Output:
	Linesample ascii files at the sample location given by arrays
	"""

	for ex in expr:
		if len(ex[1])!=0:
			for chan in ex[1]:
				rotSymChanSample(ex[0],ex[2],chan,res,scale,batchName)

def rotSymChanSample(dB,expr,chan,res,scale,batchName):
	"""
	Samples at a particular channel and saves the output to ascii

	Keyword Arguments:
	dB-The database of being used by the expression for the channel
	expr-The expression id
	chan-The channel being sampled
	res-resolution of the lineSampler
	scale-The plot scaling of the output
	batchName-The name of the batch being executed

	Output:
	Saves the output of the particular channel into an ascii file
	"""
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
	"""
	Goes through and gives the toroidal integral for each of the arrays in the expr data structure
	Note: For vector products which have no dependence on phi only.
	Keyword Arguments:
	linRes-The linear resolution of the lineSampler
	angRes-The angular resolution
	scale-The plot scale of lineSample
	startAng-Starting angle of the lineSample of the toroidal integral fxn
	stopAng-Stoping angle of the lineSample fo the toridal integral fxn
	expr-datastruct containing the expression data
	batchName-name of the batch being executed

	Output: 
	Outputs many files for each of the channels being integrated into the proper file system
	"""
	for ex in expr:
		if len(ex[1])!=0:
			for chan in ex[1]:
				rotSymToroidalIntChan(ex[0],ex[2],chan,linRes,angRes,startAng,stopAng,scale,batchName)

def rotSymToroidalIntChan(dB,expr,chan,linRes,angRes,startAng,stopAng,scale,batchName):
	"""
	This takes the toroidal integral of a channel with a specified expression
	Note: For expressions which have no dependence on the phi direction only
	Keyword Arguments:
	dB-The database used by the expression variables
	expr-The expression being evaluated
	chan-channel tuple being integrated
	linRes-Linear resolution of the lineSampler
	angRes-Angular resolution of the toroidal integrator in degrees
	startAng-Starting angle for the toroidal integration in degrees
	stopAng-Stopping angle for the toroidal integrator in degrees
	stopAng-Stopping angle for the toroidal integrator in degrees
	scale-Plot scale for the lineSampler
	batchName-Name of the batch currently being run

	Output:
	Ascii file for one channels toroidal integral plot
	"""
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
	"""
	Returns the channel sampling at different phi angles
	NOTE: For expressions which have no dependence on the phi angle only
	NOTE: THIS METHOD WAS HARD CODED FOR THE BERG POLARIMETER AND SHOULD BE GENERALIZED

	Keyword Arguments:
	array-The array of chord tuples being sampled
	dBFile-The dB database file
	Bfile-The B data base file
	linRes-The linear resolution of the linesampler
	startAng-Where to start sampling
	stopAng-Where to stop sampling
	angRes-The angular resolution
	scale-The plot scale of the lineSampler
	batchName-Name of the batch currently executing

	Output:
	Files containing the channel samples for various toroidal angles
	"""

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
	print("HELLO WORLD UPDATING CURRENT ARRAY")
	newArray=array
	k=0
	for chord in newArray:
		print(newArray)
		newArray[k]=(chord[0],chord[1],phi,chord[3],chord[4])
		print(newArray)
		print("#######")
		k+=1
	return newArray
def calculateChordLength(theta,R1,R0,Z1):
	dR=R1-R0
	Z0=Z1-math.tan(theta*(math.pi/180)-math.pi)*dR
	dZ=Z1-Z0
	return math.sqrt(dR**2+dZ**2)

def updateExpr(array,dBFile,BFile,phi): 
	"""
	Changes the array toroidal angle and updates the expr data structure
	NOTE: THIS WAS HARDCODED FOR THE BERG POLARIMETER AND SHOULD BE GENERALIZED
	
	Keyword Arguments:
	array-Array of chord tuples
	dBFile-The dB database location
	BFile-The B database location

	Output:
	The expression with the chord at a different angle
	"""

	newArray=updateCurrentArray(array,phi)
	expr=[#(BFile,newArray,"dn","npert*"+str(cl)),
(BFile,[],"X","coord(mesh)[0]"),
(BFile,[],"Y","coord(mesh)[1]"),
(BFile,[],"B_X","dot(B,{1,0,0})"),
(BFile,[],"B_Y","dot(B,{0,1,0})"),
(BFile,[],"B_R","(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)"),
(BFile,[],"B_Z","dot(B,{0,0,1})"),
#(BFile,newArray,"BdL",str(cl)+"*(B_R*cos($3*(3.14159/180))+B_Z*sin($3*(3.14159/180)))"),
#(BFile,newArray,"dnB",str(cl)+"*npert*(B_R*cos($3*(3.14159/180))+B_Z*sin($3*(3.14159/180)))"),
#(BFile,[(6,0,0,180,.1)],"BdlHORTEST", "6*(B_R*cos($3*(3.14159/180))+B_Z*sin($3*(3.14159/180)))"),
#(dBFile,newArray,"n",str(cl)+"*density"),
(dBFile,[],"dB_X","dot(dB,{1,0,0})"),
(dBFile,[],"dB_Y","dot(dB,{0,1,0})"),
(dBFile,[],"dB_R","(dB_X*X+dB_Y*Y)/sqrt(X^2+Y^2)"),
(dBFile,[],"dB_Z","dot(dB,{0,0,1})"),
#(dBFile,newArray,"dBdL",str(cl)+"*(dB_R*cos($3*(3.14159/180))+dB_Z*sin($3*(3.14159/180)))"),
#(dBFile,newArray,"ndB",str(cl)+"*density*(dB_R*cos($3*(3.14159/180))+dB_Z*sin($3*(3.14159/180)))")]
(BFile,newArray,"nB", str(cl)+"*density*(B_R*cos($3*(3.14159/180))+B_Z*sin($3*(3.14159/180)))")]
	return expr
##################################################################
array=[(6.08864,1.132,0,192.718,.1)]
#array=[(6.08864,1.132,0, 181.701,.1),(6.08864,1.132,0, 184.642,.1),(6.08864,1.132,0, 187.853,.1),(6.08864,1.132,0, 192.718,.1)]
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
cl=calculateChordLength(192.718,6.08864,0,1.132)
print(cl)
expr = updateExpr(array,dBFile,BFile,0)
createEnviroment(expr)
batchName="ReScaleRun 7-16-13"
#rotSymLineSample(.1,1,expr,batchName)
#rotSymToroidalSampling(array,dBFile,BFile,.1,0,360,360/8,1,batchName)
rotSymToroidalInt(.1,1,1,0,360,expr,batchName)


#expr=[#(BFile,newArray,"dn","npert")
#(BFile,[],"R","{1,0,0}*coord(B)[0]/sqrt(coord(B)[0]^2+coord(B)[1]^2)+{0,1,0}*coord(B)[1]/sqrt(coord(B)[0]^2+coord(B)[1]^2)")
#,(BFile,[],"B_R","B*R")
#,(BFile,[],"B_Z","B*{0,0,1}")

#,(BFile,newArray,"dnB","$4*(B_R*cos($3*(3.14159/180))+sin($3*(3.14159/180))*B_Z)")
#,(BFile,newArray,"dnB","npert*$4*(B_R*cos($3*(3.14159/180))+sin($3*(3.14159/180))*B_Z)")
#,(dBFile,newArray,"dBn","density*$4*(dB_R*cos($3*(3.14159/180))+sin($3*(3.14159/180))*dB_Z)"),
#,(dBFile,[],"dB_R","dB*R")
#,(dBFile,[],"dB_Z","dB*{0,0,1}")
#,(BFile,newArray,"n","density") ]#]
