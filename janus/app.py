from sanic import Sanic
from sanic.response import json

APP = Sanic()


@APP.route("/", methods=["POST"])
async def test(request):
    msg = request.json
    return json({"hello": "world"})


if __name__ == "__main__":
    APP.run(host="127.0.0.1", port=3000)
