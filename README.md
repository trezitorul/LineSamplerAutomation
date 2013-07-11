LineSamplerAutomation
=====================
THIS SCRIPT IS IN STASIS AND DEVELOPMENT WILL BE HALTED FOR THE TIME BEING

This is the repository for the automated linesampler script that I have created for the Plasma Science and Fusion Center.

This script executes the linesampler script over an array of chords and outputs toroidal samples and toroidal integrals and outputs the results for each channel in ascii files.

Requirements for Running:

visIt Must be installed

Running Instructions:

To start the script in commandline only mode run:

visit -cli -s autoLineSampler.py

To start the script in graphical visit mode run:

visit -s autoLineSampler.py

(Not particularly useful since the script deletes the plots shortly after creating them, however, it does leave the variables intact 
which is useful for testing)


