import subprocess
import json

# host the file on http
server_process = subprocess.Popen(["pipenv", "run", "python", "host.py"])

# run the scraper
subprocess.call(["scrapy", "crawl", "test"])

# close the server
server_process.terminate()

print("\n\nParsing completed, here is the output of output/test.json:")

# load output/test.json and print the json
with open("output/test.json") as f:
    contents = f.read()
    json_doc = json.loads(contents)
    print(json.dumps(json_doc, indent=4))