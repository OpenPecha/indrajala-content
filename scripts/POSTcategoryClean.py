import urllib.request, urllib.error, urllib.parse
from urllib.error import URLError, HTTPError
import json

index = {
	"sectionNames": ["Chapter", "Paragraph"],
	"categories": ["Vinaya"],
}

def post_index(index):
	url = 'http://indrajala.com/api/index/' + index["categories"][0].replace(" ", "_")
	indexJSON = json.dumps(index)
	values = {
		'json': indexJSON, 
		'apikey': 'apikey'
	}

	data = urllib.parse.urlencode(values)
	binary_data = data.encode('ascii')
	req = urllib.request.Request(url, binary_data)
# 	print(req)

	try:
		response = urllib.request.urlopen(req)
		print(response.read())
	except HTTPError as e:
		print('Error code: ', e.code)

post_index(index)
