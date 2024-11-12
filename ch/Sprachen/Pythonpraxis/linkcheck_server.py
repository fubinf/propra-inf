"""A super-specialized single-threaded HTTP server, only made for testing linkcheck.py and nothing else."""
import http.server
import re


def listitems(items: list[str]) -> str:
    result = ["<ol>"]
    for item in items:
        inner = f"<img src='{item}'>" if item.endswith(".jpg") else f"<a href='{item}'>{item}</a>"
        result.append(f"<li>{inner}</li>")
    result.append("</ol>")
    return "\n".join(result)


page_template = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="missing.css">
    <script src="script.js"></script>
  </head>
  <body>
    <h1>{title}</h1>
    {body}
  </body>
</html>
"""
port = 8031
base1 = f'http://localhost:{port}'
base2 = f'http://127.0.0.1:{port}'
page1 = page_template.format(
    title="page1",
    body=listitems(["/page2", f"{base1}/page2", "page3", "image.jpg", "application_json"]))
page2 = page_template.format(
    title="page2",
    body=listitems(["missing.html", "error400", "error500", "error403"]))
page3 = page_template.format(
    title="page3",
    body=listitems([f"{base2}/page2", f"{base2}/image.jpg", f"{base2}/application_json", "http://no.where.xyz"]))
pseudopage = page_template.format(
    title="this is not an HTML page!",
    body=listitems(["must_never_be_checked"]))


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Handles requests to 'http://localhost' (default use) and to 'http://127.0.0.1' (alternative use).
    Knows about /page1, /page2, /page3, /style.css, /script.js, /image.jpg,
    <t1>_<t2> (e.g. application_json; will return HTML content with Content-Type: application/json), and 
    error<number> (e.g. error500; will return a status 500 response with a link-free HTML body). 
    Responds to anything else with status 404. Supports GET and HEAD.
    """

    def do_GET(self):
        self.do_respond(with_body=True)

    def do_HEAD(self):
        self.do_respond(with_body=False)

    def do_respond(self, with_body: bool):
        if self.path == "/":
            self.send_stuff("", with_body)  # empty homepage
        elif mm := re.fullmatch(r"/(page[123])", self.path):
            pagename = globals()[mm.group(1)]
            self.send_stuff(...)
        elif mm := re.fullmatch(r"/(style\.css)", self.path):
            self.send_stuff(pseudopage, with_body, "text/css; charset=utf-8")
        elif mm := re.fullmatch(r"/(script\.js)", self.path):
            self.send_stuff(pseudopage, with_body, "text/javascript; charset=utf-8")
        elif mm := re.fullmatch(r"/(image\.jpg)", self.path):
            self.send_stuff(pseudopage, with_body, "image/jpg")
        elif mm := re.fullmatch(r"/([a-z]+)/([a-z]+)", self.path):
            self.send_stuff(pseudopage, with_body, f"{mm.group(1)}/{mm.group(2)}; charset=utf-8")
        elif mm := re.fullmatch(r"/error(\d+)", self.path):
            self.send_error(..., f"path '{self.path}'")
        else:
            self.send_error(404, f"path '{self.path}' does not exist")

    def send_stuff(self, body: str, with_body: bool, content_type="text/html; charset=utf-8"):
        self.send_response(200)  # begin response
        content = body.encode('utf-8')
        self.send_header("Content-Type", content_type)
        if with_body:
            self.send_header("Content-Length", len(content))
            self.end_headers()
            ...  # write body
        else:
            self.end_headers()


def main(port: int):
    print(f"server for testing 'linkcheck' started. Stop with Ctrl-C. Now visit http://localhost:{port}/page1")
    httpd = http.server.HTTPServer(('127.0.0.1', port), RequestHandler)
    ...  # the infinite server loop


if __name__ == '__main__':
    main(port)
