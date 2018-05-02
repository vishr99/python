# from watson_developer_cloud import VisualRecognitionV3 as vr
# import pprint
#
# instance = vr(api_key='e16a3ff04ffc169ff2cfdf823f4143880686d7cf',version='2016-05-20')
# img = instance.classify(images_url='https://img.huffingtonpost.com/asset/586ead8d1b00002c006e5bfa.jpeg?ops=scalefit_720_noupscale')
# output = pprint.pprint(img['images'][0]['classifiers'][0]['classes'])
# print(output)
from watson_developer_cloud import VisualRecognitionV3 as vr
import pprint
import json

test_url = 'https://img.etimg.com/thumb/msid-62897992,width-643,imgsize-117551,resizemode-4/women-should-be-judged-on-their-work-not-gender-ginni-rometty-ibm-ceo.jpg'
instance = vr(api_key='e16a3ff04ffc169ff2cfdf823f4143880686d7cf',version='2016-05-20')
url_result = instance.classify(parameters=json.dumps({'url': test_url}))
url_result1 =instance.detect_faces(parameters=json.dumps({'url': test_url}))
#print(json.dumps(url_result, indent=2))
output = (json.dumps(url_result))
#print(output)
#print(type(output))
print('--------------------------------------------------')
dict_output = json.loads(output)
#print(dict_output)
#print(type(dict_output))
print(dict_output['images'][0]['classifiers'][0]['classes'][0])
# print(dict_output['images'][0]['classifiers'][0]['classes'][1])
# print(dict_output['images'][0]['classifiers'][0]['classes'][2])
# print(dict_output['images'][0]['classifiers'][0]['classes'][3])
a = {}
#pprint.pprint(url_result['images'][0]['classifiers'][0]['classes'])
#print(json.dumps(url_result1, indent=2))
#pprint.pprint(url_result1['images'][0]['faces'][0])

# a = str(pprint.pprint(url_result['images'][0]['classifiers'][0]['classes']))
# print(a.replace("'class'",""))


