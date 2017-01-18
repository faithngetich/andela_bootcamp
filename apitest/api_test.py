import urllib3, json
urllib3.disable_warnings()

def get_links():
	collected_data = []
	http = urllib3.PoolManager()
	url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyCAzxR-Ai8lwQtbBNjT-kGrDIO59aCRT94&cx=005879488033716101213:abkahazp0sk&q="
	r = http.request('GET', url)
	return json.loads(r.data)

print (get_links())