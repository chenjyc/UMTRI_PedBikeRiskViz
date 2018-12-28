# UMTRI_PedBikeRiskViz

Functionalities
- Look up areas
- Zoom in and out
- Show highlight and pop-up 
- Display of legend
- Filter by value*
- Display of polygon, line, and point layer data
- Display of polygons by attribute 
	- Display by colored bins* 
	- Display by continuous spectrum

**Note**:

_Filter by value_ and _display by colored bins_ are only available for Bie and Pie attribute.  


# Setting up data in ArcGIS Online 

- Open up ArcGIS Pro 
- You would be prompted to log in with University of Michigan account
- **Note** that login may not get you actually connected to ArcGIS Online portal the first time, you should click "Switch Active Portal" on the top right corner, log in through ArcGIS website (www.arcgis.com) using Enterprise Login, and then do "Switch Active Portal" back again to UM account (umich.maps.arcgis.com), should work then. 
- Start a new project on ArcGIS Pro
- Create a blank new map (Insert -> New Map)
- Drag the shapefiles into the content section of the new map, the data should be displayed on the map if successful 
- Share data to online (have to share each shapefile individually)
	- Right click on the dataset in the content
	- Click "Sharing", then click "Share as web layer"
	- Add name, summary, and tag
	- For "Layer Type", select "Feature"
	- For "Share With", select "Everyone" to make it a public layer
	- Finally click "Analyze" for error checking and then "Publish"


# Javascript reference 
ArcGIS Javascript API site
- [API Reference](https://developers.arcgis.com/javascript/latest/api-reference/index.html)
- [Sample code](https://developers.arcgis.com/javascript/latest/sample-code/index.html)

# To do 
- Files to MBox 