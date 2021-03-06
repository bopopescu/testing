# -*- coding: utf-8 -*-
"""
Created on Mon Jun  16 06:50:30 2014
Mantainer: José Beltrán [email](<beltran.data@gmail.com>)
Last update: 2014-06-16 Version: 1.0


**Subset and reproject from WGS84 to UTM33WGS84**
MEGS8.1 (ODESA1.2.4) MERIS FR datasets.
"""

"""The module gpt_config has the configuration paths for using the 
BEAM gpt processor (v5.0) localy."""


import os
#from os.path import exists

import gpt_config as beam

def gpt_graph(outputfilename):    
    '''
    Builds an graph XML request that subsets to Himmerjarden area and
    reproject from WGS84 to UTM33WGS84
    To be used with ODESA/MEGS8.1 datasets.
    outputfilename:     ouput path/filename for processing
    '''
   
    requestSkeleton =   '<graph id=\"SUProcess\">\n<version>1.0</version>\n'
    requestSkeleton +=  '   <node id=\"Reprojected">\n'
    requestSkeleton +=  '       <operator>Reproject</operator>\n'
    requestSkeleton +=  '       <sources>\n'
    requestSkeleton +=  '           <source>${source}</source>\n'
    requestSkeleton +=  '       </sources>\n'
    requestSkeleton +=  '       <parameters>\n'
    requestSkeleton +=  '         <crs>PROJCS["WGS 84 / UTM zone 33N",\n'
    requestSkeleton +=  '             GEOGCS["WGS 84",\n'
    requestSkeleton +=  '             DATUM["World Geodetic System 1984",\n'
    requestSkeleton +=  '               SPHEROID["WGS 84", 6378137.0, 298.257223563, AUTHORITY["EPSG","7030"]],\n'
    requestSkeleton +=  '               AUTHORITY["EPSG","6326"]],\n'
    requestSkeleton +=  '               PRIMEM["Greenwich", 0.0, AUTHORITY["EPSG","8901"]],\n'
    requestSkeleton +=  '               UNIT["degree", 0.017453292519943295],\n'
    requestSkeleton +=  '               AXIS["Geodetic longitude", EAST],\n'
    requestSkeleton +=  '               AXIS["Geodetic latitude", NORTH],\n'
    requestSkeleton +=  '               AUTHORITY["EPSG","4326"]],\n'
    requestSkeleton +=  '               PROJECTION["Transverse_Mercator", AUTHORITY["EPSG","9807"]],\n'
    requestSkeleton +=  '               PARAMETER["central_meridian", 15.0],\n'
    requestSkeleton +=  '               PARAMETER["latitude_of_origin", 0.0],\n'
    requestSkeleton +=  '               PARAMETER["scale_factor", 0.9996], \n'
    requestSkeleton +=  '               PARAMETER["false_easting", 500000.0],\n'
    requestSkeleton +=  '               PARAMETER["false_northing", 0.0],\n'
    requestSkeleton +=  '               UNIT["m", 1.0],\n'
    requestSkeleton +=  '               AXIS["Easting", EAST],\n'
    requestSkeleton +=  '               AXIS["Northing", NORTH],\n'
    requestSkeleton +=  '               AUTHORITY["EPSG","32633"]]</crs>\n'
    requestSkeleton +=  '           <resampling>Nearest</resampling>\n'
    requestSkeleton +=  '           <orthorectify>false</orthorectify>\n'
    requestSkeleton +=  '           <noDataValue>NaN</noDataValue>\n'
    requestSkeleton +=  '           <includeTiePointGrids>true</includeTiePointGrids>\n'
    requestSkeleton +=  '           <addDeltaBands>false</addDeltaBands>\n'
    requestSkeleton +=  '       </parameters>\n'
    requestSkeleton +=  '   </node>\n'
    requestSkeleton +=  '   <node id=\"writeFile\">\n'
    requestSkeleton +=  '       <operator>Write</operator>\n'
    requestSkeleton +=  '       <sources>\n'
    requestSkeleton +=  '           <source>Reprojected</source>\n'
    requestSkeleton +=  '       </sources>\n'
    requestSkeleton +=  '       <parameters>\n'
    requestSkeleton +=  '           <file>'+ outputfilename +'</file>\n'
    #requestSkeleton +=  '           <formatName>BEAM-DIMAP</formatName>\n'
    requestSkeleton +=  '           <formatName>TIFF</formatName>\n'
    #requestSkeleton +=  '           <formatName>NetCDF-BEAM</formatName>\n'
    requestSkeleton +=  '       </parameters>\n'
    requestSkeleton +=  '   </node>\n'        
    requestSkeleton +=  '</graph>\n'
    return requestSkeleton
    
    #requestSkeleton +=  '           <formatName>NetCDF-BEAM</formatName>\n'
        #requestSkeleton +=  '           <formatName>NetCDF-BEAM</formatName>\n'
##########
    
destDir = '/home/jobel/testing/FUB_reprojected/'
srcDir  = '/home/jobel/testing/' # gpt_configuration.srcDirs['CCL1P_out']

xmlrequest = '/media/jobel/SeagateDrive/eodata2014/level2/test/gpt_graph.xml'
#
def exit_on_empty_list(list):
    _size = len(list)
    if _size == 0:
        print("Nothing to do here. Now quitting.")
        exit(1)
    else:
        return _size



#
srcList = list()
# Adding recursive walk for directories
for dirpath, dirnames, files in os.walk(srcDir):
    for file in files: # files is a list of files in the current directory
        if file.lower().endswith(".nc"): #".nc"
            #fullpath = #os.path.join(root, file)
            currentFilepath = dirpath
            srcList.append(os.path.join(currentFilepath, file))
        #else:
         #   print("File format not recognized")
srcList.sort()
print("file list to process ready")

"""merisFile contains the path and name of the MERIS dataset to process"""


#            0123456790123456789012
merisFileName = "MER_FSG_2PNMAP20100515_091100_000000362089_00265_42904_0001.N1"
#"         10        20        30        40        50        60        70        80        90
#"0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
#"/media/jobel/SeagateDrive/eodata2014/level2/MEGS/20120405_092930/output/MER_FSG_2PNMAP20120405_092930_000000393113_00223_52823_0001.nc"

filterList = list()
'''
for merisFile in srcList:
    merisFileName = os.path.basename(merisFile) # MERIS filename extraction
    merisYear = merisFileName[14:18]
    if (merisYear in ["2008","2010","2011"]):
        filterList.append(merisFile)
        print("Keep in this one")
'''    
 
for merisFile in srcList:
    
    merisFileName = os.path.basename(merisFile) # MERIS filename extraction
    inputFileName = merisFile # Keep the full path and current MERIS filename
    newFileName = merisFileName[:-3] +".dim"
    outputFile = destDir +'UTM33_WGS84_' +newFileName # New filename
    request = gpt_graph(outputFile) # adds the new filename to the graph
    # Delete previous graph settings, i.e.file should not exist 
    if os.path.exists(xmlrequest):
        os.remove(xmlrequest)
    # New graph is generated with the current settings
    requestFile = open(xmlrequest, 'a')
    requestFile.write(request)
    requestFile.close()     
     
    print("Processing: Processing file " + merisFile + " ...")
    
    ExCommand = beam.gptProcessor + " " + xmlrequest  + " -Ssource=" + inputFileName + ' -f dim -t ' + outputFile 
    print(ExCommand+'\\')    
 
    os.system(ExCommand)

print('done')

