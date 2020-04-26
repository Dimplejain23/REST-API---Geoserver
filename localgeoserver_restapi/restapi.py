import glob
import os
import json
from subprocess import Popen,PIPE


file = "abohar_20200106_pre.tif"

def workspace():
    tif = os.path.basename(file)[0:-4]
    city = tif.split("_")
    print(city[0])
    ## List all the workspace
    workspaces =Popen('curl -v -u admin:geoserver -X GET http://localhost:8080/geoserver/rest/workspaces -H  "accept: application/json" -H  "content-type: application/json"', shell=True, stdout=PIPE)       
    output=workspaces.communicate()[0]
    y = json.loads(str(output)[2:-1])
    x= y["workspaces"]["workspace"]
    space = []
    for i in range (len(x)):
        space.append(x[i]["name"])
    print(space)
    ## workspace create
    if not city[0] in space:
        print("workspace create")
        os.system('curl -v -u admin:geoserver -XPOST -H "Content-type: text/xml" -d "<workspace><name>%s</name></workspace>" \
                                                            http://localhost:8080/geoserver/rest/workspaces'%(city[0]))           
    else:
        print("workspace already exist")
    
    return city[0],city[1]

def cr_store():
    tif = os.path.basename(file)[0:-4]
    city,data = workspace()
    header = "Content-type: application/json"
    jsn = '{"import": {"targetWorkspace": {"workspace": {"name": "%s"}}}}'%(city)
    url = "http://localhost:8080/geoserver/rest/imports"
    var ="curl -u admin:geoserver -XPOST -H '%s' --data '%s' '%s'"%(header,jsn,url)
    ## Get the task ID for storing data
    proc=Popen("curl -u admin:geoserver -XPOST -H '%s' --data '%s' '%s'"%(header,jsn,url), shell=True, stdout=PIPE)    
    output=proc.communicate()[0]
    js = str(output)[2:-1]
    y = json.loads(js)
    ids= y["import"]["id"]
    os.system('curl -u admin:geoserver -F name=%s -F filedata=@%s "http://localhost:8080/geoserver/rest/imports/%s/tasks"'%(city,file,ids))
    
    os.system('curl -u url -u admin:geoserver -XPOST "http://localhost:8080/geoserver/rest/imports/%s"'%(ids))
    
    os.system('curl -u admin:geoserver -XPUT -H "Content-type: text/xml" -d "<layer><defaultStyle><name>ndvi_style</name></defaultStyle><enabled>true</enabled></layer>" \
                                                                                            http://localhost:8080/geoserver/rest/layers/%s:%s'%(city,tif))
    
    
def store():
    tif = os.path.basename(file)[0:-4]
    city,data = workspace()
    print(city)
    ## List all the stores
    coverages =Popen('curl -u admin:geoserver -X GET "http://localhost:8080/geoserver/rest/workspaces/%s/coverages" -H  "accept: application/json" \
                                                                                        -H  "content-type: application/json"'%(city), shell=True, stdout=PIPE)       
    print(coverages)
    output=coverages.communicate()[0]
    y = json.loads(str(output)[2:-1])
    x= y["coverages"]
    
    if len(x) == 0:
        cr_store()
    else:
        x= y["coverages"]["coverage"]
        space = []
        for i in range (len(x)):
            space.append(x[i]["name"])
        print(space)
        if not tif in space:
            print("create store")
            cr_store()
        else:
            print("store already exist")

store()














    
