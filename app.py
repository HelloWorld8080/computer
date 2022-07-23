from jinja2 import FileSystemLoader, Environment
from sanic import Sanic, HTTPResponse
import os
import json

app = Sanic(__name__)

templates_dir = 'template'
file_loader = FileSystemLoader([templates_dir])
environment = Environment(loader=file_loader, enable_async=True)

@app.route('/')
async def test(request):
    templates = environment.get_template('index.html')
    result = await templates.render_async()
    return HTTPResponse(result, content_type='text/html')

if __name__ == '__main__':
    app.static('/static', './static')
    app.static('/result', './result')
    app.static('/lib','./lib')
    app.run(host='0.0.0.0', port=7788, access_log=True)
