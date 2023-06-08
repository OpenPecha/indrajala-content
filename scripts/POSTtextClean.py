import urllib
import urllib.error
from urllib.error import URLError, HTTPError
import urllib.parse
import urllib.request
import json

text = {
	"versionTitle": "chineseDemo",
	"versionSource": "chineseDemo",
	"language": "en",
	"text": [
		"天竺語曰毗奈耶",
		"禮敬三寶",
		"།禮敬斷煩惱摧魔正覺者"
	]
}

def post_text(ref, text):
	textJSON = json.dumps(text)
	ref = ref.replace(" ", "_")
	url = 'http://localhost:8000/api/texts/%s' % ref
	values = {'json': textJSON, 'apikey': 'apikey'}
	data = urllib.parse.urlencode(values)
	binary_data = data.encode('ascii')
	req = urllib.request.Request(url, binary_data)
	try:
		response = urllib.request.urlopen(req)
		print(response.read())
	except (HTTPError):
		print("error")
		print('Error code: ', e.code)
		print(e.read())

post_text("Chapters on Monastic Discipline 1", text)