import csv, json
from fastkml import kml
from geojson import Feature, FeatureCollection, Point, LineString, Polygon
import xml.etree.ElementTree as ET

input_file_name = 'pedbike_risk_exposure_IE_NM_Superior'

input_file = 'data/'+ input_file_name + '.csv'
output_file = 'data/'+ input_file_name + '_GeoJson.json'
output_file_1 = 'data/'+ input_file_name + '_GeoJson_1.json'
output_file_2 = 'data/'+ input_file_name + '_GeoJson_2.json'
features = []

def remove_tags(text):
    extracted_string = ';'.join(ET.fromstring(text).itertext())
    array = extracted_string.split()
    return array

'''csv line''' 
'''
with open(input_file, newline='') as csvlinefile:
    reader = csv.reader(csvlinefile, delimiter=',')
    next(reader)

    for geometry, weight, fips, region, rid, rank in reader:
        extracted_array = remove_tags(geometry)
        line_coords = []
        for coords in extracted_array: 
            if len(coords.split(',')) == 2: 
                longitude,latitude = coords.split(',')
            elif len(coords.split(',')) == 3:
                longitude,latitude, elevation = coords.split(',')
            
            longitude, latitude = map(float, (longitude, latitude))
            line_coords.append((longitude, latitude))
        
        features.append(
            Feature(
                geometry = LineString(line_coords),
                properties = {
                    'weight': weight,
                    'fips'  : fips,
                    'region': region,
                    'rid'   : rid, 
                    'rank'  : rank
                }
            )
        )

collection = FeatureCollection(features)
with open(output_file, "w") as f:
    f.write('%s' % collection)        
'''

'''csv polygon'''
# { 
# "displayFieldName" : "<displayFieldName>",
# "fieldAliases" : {
#   "<fieldName1>" : "<fieldAlias1>",
#   "<fieldName2>" : "<fieldAlias2>"
# },
# "geometryType" : "<geometryType>",
# "hasZ" : <true|false>,  //Added at 10.1
# "hasM" : <true|false>,   //Added at 10.1
# "spatialReference" : <spatialReference>,
# "fields": [
#             {
#                 "name": "<field1>",
#                 "type": "<field1Type>",
#                 "alias": "<field1Alias>"
#             },
#             {
#                 "name": "<field2>",
#                 "type": "<field2Type>",
#                 "alias": "<field2Alias>"
#             }
#         ],
#  "features": [
#             {
#                 "geometry": {
#                     <geometry1>
#                 },
#                 "attributes": {
#                     "<field1>": <value11>,
#                     "<field2>": <value12> 
#                 } 
#             },
#             {
#                 "geometry": {
#                     <geometry2>
#                 },
#                 "attributes": {
#                     "<field1>": <value21>,
#                     "<field2>": <value22> 
#                 } 
#             }
#         ]
# }
with open(input_file, newline='') as csvpolygonfile:
    reader = csv.reader(csvpolygonfile, delimiter=',')
    next(reader)

    for spaz_id, fips, region, Rid, PedCrashCt, Ped_Risk, PRrank, BikeCrashCt, \
        Bike_Risk, BRrank, PedExp, PErank, Pie, PIErank, BikeExp, BErank, Bie, \
        BIErank, NMRisk, NMRrank, NMExp, NMErank, geometry in reader:

        extracted_array = remove_tags(geometry)
        polygon_coords = []
        for coords in extracted_array: 
            if len(coords.split(',')) == 2: 
                longitude,latitude = coords.split(',')
            elif len(coords.split(',')) == 3:
                longitude,latitude, elevation = coords.split(',')
            
            longitude, latitude = map(float, (longitude, latitude))
            polygon_coords.append((longitude, latitude))
        
        features.append(
            Feature(
                geometry = Polygon([polygon_coords]),
                properties = {
                    'spaz_id'     : spaz_id, 
                    'fips'        : fips, 
                    'region'      : region,
                    'Rid'         : Rid, 
                    'PedCrashCt'  : PedCrashCt,
                    'Ped_Risk'    : Ped_Risk, 
                    'PRrank'      : PRrank, 
                    'BikeCrashCt' : BikeCrashCt, 
                    'Bike_Risk'   : Bike_Risk, 
                    'BRrank'      : BRrank, 
                    'PedExp'      : PedExp, 
                    'PErank'      : PErank, 
                    'Pie'         : Pie, 
                    'PIErank'     : PIErank, 
                    'BikeExp'     : BikeExp, 
                    'BErank'      : BErank, 
                    'Bie'         : Bie, 
                    'BIErank'     : BIErank, 
                    'NMRisk'      : NMRisk, 
                    'NMRrank'     : NMRrank, 
                    'NMExp'       : NMExp, 
                    'NMErank'     : NMErank
                }
            )
        )

# features_1 = features[:len(features)//2]
# features_2 = features[len(features)//2:]
# collection_1 = FeatureCollection(features_1)
# collection_2 = FeatureCollection(features_2)
# with open(output_file_1, "w") as f1:
#     f1.write('%s' % collection_1)

# with open(output_file_2, "w") as f2:
#     f2.write('%s' % collection_2)

collection = FeatureCollection(features)

with open(output_file, "w") as f:
    f.write('%s' % collection)

# pedbike_risk_exposure_IE_NM_NorthBay_GeoJson_1

# { 
# "displayFieldName" : "<displayFieldName>",
# "fieldAliases" : {
#   "<fieldName1>" : "<fieldAlias1>",
#   "<fieldName2>" : "<fieldAlias2>"
# },
# "geometryType" : "<geometryType>",
# "hasZ" : <true|false>,  //Added at 10.1
# "hasM" : <true|false>,   //Added at 10.1
# "spatialReference" : <spatialReference>,
# "fields": [
#             {
#                 "name": "<field1>",
#                 "type": "<field1Type>",
#                 "alias": "<field1Alias>"
#             },
#             {
#                 "name": "<field2>",
#                 "type": "<field2Type>",
#                 "alias": "<field2Alias>"
#             }
#         ],
#  "features": [
#             {
#                 "geometry": {
#                     <geometry1>
#                 },
#                 "attributes": {
#                     "<field1>": <value11>,
#                     "<field2>": <value12> 
#                 } 
#             },
#             {
#                 "geometry": {
#                     <geometry2>
#                 },
#                 "attributes": {
#                     "<field1>": <value21>,
#                     "<field2>": <value22> 
#                 } 
#             }
#         ]
# }

#{   "type": "FeatureCollection",
#     "features": [
#         {   "type": "Feature",
#             "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
#             "properties": {"prop0": "value0"}
#         },
#         {   "type": "Feature",
#             "geometry": {
#             "type": "LineString",
#             "coordinates": [
#                 [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
#                 ]
#             },
#             "properties": {
#             "prop0": "value0",
#             "prop1": 0.0
#             }
#         },
#         {   "type": "Feature",
#             "geometry": {
#             "type": "Polygon",
#             "coordinates": [
#                 [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
#                 [100.0, 1.0], [100.0, 0.0] ]
#                 ]  
#             },
#             "properties": {
#             "prop0": "value0",
#             "prop1": {"this": "that"}
#             }
#         }
#     ]
# }

# Formatting
# { "type": "FeatureCollection",
#   "features": [
#     { "type": "Feature",
#       "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
#       "properties": {"prop0": "value0"}
#       },
#     { "type": "Feature",
#       "geometry": {
#         "type": "LineString",
#         "coordinates": [
#           [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
#           ]
#         },
#       "properties": {
#         "prop0": "value0",
#         "prop1": 0.0
#         }
#       },
#     { "type": "Feature",
#        "geometry": {
#          "type": "Polygon",
#          "coordinates": [
#            [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
#              [100.0, 1.0], [100.0, 0.0] ]
#            ]
#        },
#        "properties": {
#          "prop0": "value0",
#          "prop1": {"this": "that"}
#          }
#        }
#      ]
#    }