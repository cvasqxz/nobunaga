from flask import current_app as app
from requests import post, exceptions


def RPC(method, params=[]):
	data = '{"jsonrpc":"2.0","id":"nobunaga","method":"%s","params":%s}'
	data = data % (method, params)

	try:
		req = post(app.config["RPC_URL"], data=data)
	except:
		return None

	if req.status_code != 200:
		return None

	req = req.json()

	if req["error"] != None:
		return req["error"]

	if req["id"] != "nobunaga":
		return None

	return req["result"]