from PyPDF2 import PdfReader
import requests
import os

API_KEY = os.environ.get("API_KEY")
API_URL = "https://api.voicerss.org/"

reader = PdfReader("path/to/pdf")
# select a pagenumber, or get smaller chuncks of data
text = reader.pages[0].extract_text()

response = requests.get(url = API_URL, 
	params = { 					# mandatory parameters
		"key": API_KEY,			# key -- The API KEY
		"src": text,			# src -- Textual content (100KB max)
		"hl": "en-us",			# hl -- Language
		"c": "MP3"				# c -- audio format file
	})
response.raise_for_status()
with open("audio.mp3","wb") as fobj:
	fobj.write(response.content)