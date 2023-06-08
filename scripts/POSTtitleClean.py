import urllib
import urllib.error
from urllib.error import URLError, HTTPError
import urllib.parse
import urllib.request
import json

index = {
	"title": "Chapters on Monastic Discipline",
	"heTitle": "Chapters on Monastic Discipline_",
	"titleVariants": ["Vinayavastu"],
	"sectionNames": ["Chapter", "Paragraph"],
	"categories": ["Kangyur", "Discipline"],
}

def post_index(index):
	url = 'http://127.0.0.1:8000/api/index/' + index["title"].replace(" ", "_")
	indexJSON = json.dumps(index)
	values = {
		'json': indexJSON, 
		'apikey': "apikey"
	}
	data = urllib.parse.urlencode(values)
	binary_data = data.encode('ascii')
	req = urllib.request.Request(url, binary_data)
	try:
		response = urllib.request.urlopen(req)
	except (HTTPError):
	 	print("error")
	 	print ('Error code: ', e.code)
post_index(index)