from robyn import Robyn, jsonify

app = Robyn(__file__)

@app.get("/")
async def h(request):
    return jsonify({"msg": "hello world!"})

app.start(port=8080)
