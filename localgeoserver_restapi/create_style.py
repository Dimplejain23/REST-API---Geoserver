import os

## In the same folder file named as ndvi.sld used to create style on geoserver
createdincatalog = os.system('curl -v -u admin:geoserver -XPOST -H "Content-type: text/xml" -d "<style><name>ndvi_style</name><filename>ndvi.sld</filename></style>" \
                                                                                                 http://localhost:8080/geoserver/rest/styles')
print(createdincatalog)

uploaded = os.system('curl -v -u admin:geoserver -XPUT -H "Content-type: application/vnd.ogc.sld+xml" -d @ndvi.sld \
                                                                                        http://localhost:8080/geoserver/rest/styles/ndvi_style')
print(uploaded)
