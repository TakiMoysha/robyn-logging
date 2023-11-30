import pathlib

from robyn import Robyn, jsonify, Request, serve_html
from robyn.templating import JinjaTemplate

app = Robyn(__file__)
current_file_path = pathlib.Path(__file__).parent.absolute()
TEMPLATES = JinjaTemplate(current_file_path / "templates")

@app.get("/")
async def h(request):
    return serve_html("./templates/index.html")

@app.get("/json")
async def json(request):
    return jsonify({"msg": "hello world!", "version": "0.0.2"})

@app.get("/logger")
async def logger(request: Request):
    context = { "id": request.ip_addr }
    return TEMPLATES.render_template(template_name="logging.html", **context)

app.start(port=8080)
