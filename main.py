import pathlib

from robyn import Robyn, jsonify, Request
from robyn.templating import JinjaTemplate

app = Robyn(__file__)
current_file_path = pathlib.Path(__file__).parent.absolute()
TEMPLATES = JinjaTemplate(current_file_path / "templates")

@app.get("/")
async def h(request):
    return jsonify({"msg": "hello world!", "version": "0.0.2"})

@app.get("/logger")
async def logger(request: Request):
    context = { "id": request.ip_addr }
    return TEMPLATES.render_template(template_name="index.html", **context)

app.start(port=8080)
