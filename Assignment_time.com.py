import http.client
import re
import json

def get_Latest_Stories():
    connection = http.client.HTTPSConnection("time.com")
    connection.request("GET", "/")
    
    response = connection.getresponse()
    html_content = response.read().decode("utf-8")
    connection.close()

    story_pattern = re.compile(
    r'<a href="(/[^"]+)"[^>]*>\s*<h3 class="latest-stories__item-headline">\s*(.*?)\s*</h3>',
    re.DOTALL)


    matches = story_pattern.findall(html_content)

    stories = []
    seen_links = set()
    for link, title in matches:
        full_link = "https://time.com" + link  
        if full_link not in seen_links:
            stories.append({"title": title.strip(), "link": full_link.strip()})
            seen_links.add(full_link)
        if len(stories) == 6: 
            break
    
    return stories

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/getTimeStories":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            stories = get_Latest_Stories()
            self.wfile.write(json.dumps(stories, indent=4).encode("utf-8"))

server = HTTPServer(("localhost", 8000), RequestHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
