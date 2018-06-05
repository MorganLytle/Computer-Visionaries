import base64
import json
import os
import ssl

def apiCall():

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
  image_data = base64.b64encode(open("./testImage.JPG", "rb").read()).decode()
  
  params = json.dumps({"image": image_data})
  conn.request("POST", "/v1/recognition?objectType=licenseplate", params, headers)
  response = conn.getresponse()
  result = response.read()
  
  
  #print("Detection Results = " + str(result) + "\n\n\n")

  apiResult = json.loads(str(result))#converts json to a dictionary
  print(json.dumps(apiResult, indent = 2)+ "\n\n\n") #prints api data
  class apiData:
    def __init__(test, licPlate, conf, reg, regConf):
      test.licPlate = licPlate
      test.conf = conf
      test.reg = reg
      test.regConf = regConf

  test1Plate = str(apiResult['objects'][0]['licenseplateAnnotation']['attributes']['system']['string']['name'])
  test1Conf = float(apiResult['objects'][0]['licenseplateAnnotation']['attributes']['system']['string']['confidence'])
  test1Reg = str(apiResult['objects'][0]['licenseplateAnnotation']['attributes']['system']['region']['name'])
  test1RegConf = float(apiResult['objects'][0]['licenseplateAnnotation']['attributes']['system']['region']['confidence'])
  
  apiData1 = apiData(test1Plate, test1Conf, test1Reg, test1RegConf)
  print(apiData1.licPlate)#prints license plate number

  return apiData1
  
def main():
  apiCall()

if __name__ == "__main__":
  main()
   
