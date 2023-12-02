import os
import json
import pathlib

from robyn import Robyn, jsonify, Request, serve_html
from robyn.templating import JinjaTemplate

try: 
    env = json.load(open(".env.json"))
    for key, value in env.items():
        print(f"Setting environment variable: {key} = ****")
        os.environ[key] = value
except FileNotFoundError:
    print("Error: '.env.json' file not found.")
    pass

app = Robyn(__file__)
current_file_path = pathlib.Path(__file__).parent.absolute()
TEMPLATES = JinjaTemplate(current_file_path / "templates")

@app.get("/")
async def r_h(request: Request):
    if request.query_params.get("format", None) == "json":
        return jsonify({"msg": "hello world!", "version": "0.0.2"})
  
    return serve_html("./templates/index.html")

@app.get("/logger")
async def r_logger(request: Request):
    context = { "id": request.ip_addr }
    return TEMPLATES.render_template(template_name="logging.html", **context)

if __name__ == "__main__":
    print("Starting server...")
    ROBYN_PORT = os.getenv("ROBYN_PORT") or "8080"
    app.start(host="0.0.0.0", port=int(ROBYN_PORT))
