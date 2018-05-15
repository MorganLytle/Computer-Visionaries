import base64
import json
import os
import ssl
try:
    import httplib  # Python 2
except:
    import http.client as httplib  # Python 3

headers = {"Content-type": "application/json",
           "X-Access-Token": "McPKA4h9qAYxwwrPHbvvDRY5tM4AJwkxPlrv"}
conn = httplib.HTTPSConnection("dev.sighthoundapi.com", 
       context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

# To use a hosted image uncomment the following line and update the URL
#image_data = "https://dev.sighthoundapi.com/v1/detections?type=face,person&faceOption=landmark,gender"

# To use a local file uncomment the following line and update the path
#image_data = base64.b64encode(open("/path/to/local/image.jpg", "rb").read()).decode()

params = json.dumps({"image": image_data})
conn.request("POST", "/v1/detections?type=face,person&faceOption=landmark,gender", params, headers)
response = conn.getresponse()
result = response.read()
print("Detection Results = " + str(result))

