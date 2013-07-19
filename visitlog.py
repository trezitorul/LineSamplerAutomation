# Visit 2.6.2 log file
ScriptVersion = "2.6.2"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
visit.ShowAllWindows()
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo", 0)
OpenDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo", 0)
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("B_Z", "dot(B,{0,0,1})")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("B_Z", "dot(B,{0,0,1})")
DefineScalarExpression("dB_X", "dot(dB,{1,0,0})")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("B_Z", "dot(B,{0,0,1})")
DefineScalarExpression("dB_X", "dot(dB,{1,0,0})")
DefineScalarExpression("dB_Y", "dot(dB,{0,1,0})")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("B_Z", "dot(B,{0,0,1})")
DefineScalarExpression("dB_X", "dot(dB,{1,0,0})")
DefineScalarExpression("dB_Y", "dot(dB,{0,1,0})")
DefineScalarExpression("dB_R", "(dB_X*X+dB_Y*Y)/sqrt(X^2+Y^2)")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.Bhel_p288000_dBvector2.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("B_Z", "dot(B,{0,0,1})")
DefineScalarExpression("dB_X", "dot(dB,{1,0,0})")
DefineScalarExpression("dB_Y", "dot(dB,{0,1,0})")
DefineScalarExpression("dB_R", "(dB_X*X+dB_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("dB_Z", "dot(dB,{0,0,1})")
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
DefineScalarExpression("X", "coord(mesh)[0]")
DefineScalarExpression("Y", "coord(mesh)[1]")
DefineScalarExpression("B_X", "dot(B,{1,0,0})")
DefineScalarExpression("B_Y", "dot(B,{0,1,0})")
DefineScalarExpression("B_R", "(B_X*X+B_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("B_Z", "dot(B,{0,0,1})")
DefineScalarExpression("dB_X", "dot(dB,{1,0,0})")
DefineScalarExpression("dB_Y", "dot(dB,{0,1,0})")
DefineScalarExpression("dB_R", "(dB_X*X+dB_Y*Y)/sqrt(X^2+Y^2)")
DefineScalarExpression("dB_Z", "dot(dB,{0,0,1})")
DefineScalarExpression("nB(6.08864, 1.132, 0, 192.718, 0.1)", "6.24177937881*density*(B_R*cos(192.718*(3.14159/180))+B_Z*sin(192.718*(3.14159/180)))")
AddWindow()
ActivateDatabase("hopper.nersc.gov:/project/projectdirs/m3dls/h5.cmod_jrtv3_vp-01404_np12000_Bhel_p288000.silo")
ChangeActivePlotsVar("nB(6.08864, 1.132, 0, 192.718, 0.1)")
AddPlot("Pseudocolor", "nB(6.08864, 1.132, 0, 192.718, 0.1)", 1, 1)
AddOperator("LineSampler", 1)
LineSamplerAtts = LineSamplerAttributes()
LineSamplerAtts.meshGeometry = LineSamplerAtts.Toroidal  # Cartesian, Cylindrical, Toroidal
LineSamplerAtts.arrayConfiguration = LineSamplerAtts.Manual  # Geometry, Manual
LineSamplerAtts.boundary = LineSamplerAtts.Data  # Data, Wall
LineSamplerAtts.instanceId = 0
LineSamplerAtts.nArrays = 1
LineSamplerAtts.toroidalArrayAngle = 5
LineSamplerAtts.nChannels = 5
LineSamplerAtts.channelProjection = LineSamplerAtts.Parallel  # Divergent, Parallel, Grid
LineSamplerAtts.channelLayoutType = LineSamplerAtts.ChannelRelative  # ChannelAbsolute, ChannelRelative
LineSamplerAtts.channelOffset = 0.1
LineSamplerAtts.channelAngle = 5
LineSamplerAtts.nRows = 1
LineSamplerAtts.rowOffset = 0.1
LineSamplerAtts.arrayOrigin = (0, 0, 0)
LineSamplerAtts.arrayAxis = LineSamplerAtts.Z  # R, Z
LineSamplerAtts.poloidalAngleStart = 180
LineSamplerAtts.poloidalAngleStop = 220
LineSamplerAtts.poloialAngle = 0
LineSamplerAtts.poloialRTilt = 0
LineSamplerAtts.poloialZTilt = 0
LineSamplerAtts.toroidalAngle = 0
LineSamplerAtts.flipToroidalAngle = 0
LineSamplerAtts.viewGeometry = LineSamplerAtts.Surfaces  # Points, Lines, Surfaces
LineSamplerAtts.viewDimension = LineSamplerAtts.One  # One, Two, Three
LineSamplerAtts.donotApplyToAll = 1
LineSamplerAtts.heightPlotScale = 1
LineSamplerAtts.channelPlotOffset = 0
LineSamplerAtts.arrayPlotOffset = 0
LineSamplerAtts.displayTime = LineSamplerAtts.Step  # Step, Time, Cycle
LineSamplerAtts.channelGeometry = LineSamplerAtts.Line  # Point, Line, Cylinder, Cone
LineSamplerAtts.radius = 0.1
LineSamplerAtts.divergence = 1
LineSamplerAtts.channelProfile = LineSamplerAtts.TopHat  # TopHat, Gaussian
LineSamplerAtts.standardDeviation = 1
LineSamplerAtts.sampleDistance = 0.1
LineSamplerAtts.sampleVolume = 1
LineSamplerAtts.sampleArc = 10
LineSamplerAtts.channelIntegration = LineSamplerAtts.IntegrateAlongChannel  # NoChannelIntegration, IntegrateAlongChannel
LineSamplerAtts.toroidalIntegration = LineSamplerAtts.ToroidalTimeSample  # NoToroidalIntegration, ToroidalTimeSample, IntegrateToroidally
LineSamplerAtts.toroidalAngleSampling = LineSamplerAtts.ToroidalAngleAbsoluteSampling  # ToroidalAngleAbsoluteSampling, ToroidalAngleRelativeSampling
LineSamplerAtts.toroidalAngleStart = 0
LineSamplerAtts.toroidalAngleStop = 360
LineSamplerAtts.toroidalAngleStride = 1
LineSamplerAtts.timeSampling = LineSamplerAtts.CurrentTimeStep  # CurrentTimeStep, MultipleTimeSteps
LineSamplerAtts.timeStepStart = 0
LineSamplerAtts.timeStepStop = 0
LineSamplerAtts.timeStepStride = 1
LineSamplerAtts.channelList = (6.08864, 1.132, 0, 192.718, 0.1)
LineSamplerAtts.wallList = (0, 0)
LineSamplerAtts.nChannelListArrays = 1
LineSamplerAtts.channelListToroidalArrayAngle = 5
LineSamplerAtts.channelListToroidalAngle = 0
SetOperatorOptions(LineSamplerAtts, 1)
DrawPlots()
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "./ReScaleRun 7-16-13/nB"
SaveWindowAtts.fileName = "nB(6.08864, 1.132, 0, 192.718, 0.1)TI"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.CURVE  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1024
SaveWindowAtts.height = 1024
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
DeleteWindow()
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (0, 1, 0, 1)
View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
# End spontaneous state

