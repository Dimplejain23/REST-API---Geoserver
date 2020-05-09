# RESTAPI- Geoserver
GeoServer provides a RESTful interface through which clients can retrieve information about an instance and make configuration changes.
 
# to get the code
Repository named as localgeoserver_restapi
restapi.py
create_style.py
ndvi.sld
# Getting started
The first step is to install the importer plugin. It supports batch operations, creates unique styles. Instructions to download given on the GeoServer documentation - https://docs.geoserver.org/stable/en/user/extensions/importer/installing.html.
The filename should be in this format to follow this restapi code- example (bangalore_20200509.tif) in this way bangalore is the workspace name and the store name is the full filename.
 
To be able to load the data on GeoServer you must get a GeoServer running in the URL http://localhost:8080.
The GeoServer version used was 2.16.2 - stable version

The restapi.py file will do all the following process:-
  #Check the existing workspaces: if already exist as per the requirement then it will not create the workspace.
  #Create the workspace: workspace will create as per the starting name of the .tif file that you want to save in GeoServer.
  #Check the existing Stores:-  if your file already exists then it will not create the store.
  #Create the store:- Store will create with the same filename.
  #Load the style:- Set the style for raster.





