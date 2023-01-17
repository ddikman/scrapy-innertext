import subprocess

# host the file on http
server_process = subprocess.Popen(["pipenv", "run", "python", "host.py"])

# run the scraper
subprocess.call(["scrapy", "crawl", "test"])

# close the server
server_process.terminate()
