from pyblinkm import BlinkM
import falcon
import json

class RGBResource:
    def __init__(self):
        self.rgb = (0, 0, 0)
        self.blinkm = BlinkM()
        self.blinkm.reset()

    def _send_reponse(self, resp):
        red, green, blue = self.rgb
        body = {
            "red": self.rgb[0],
            "green": self.rgb[1],
            "blue": self.rgb[2]
        }
        resp.body = json.dumps(body)

    def on_get(self, req, resp):
        self._send_reponse(resp)

    def on_post(self, req, resp):
        body = req.stream.read()
        data = json.loads(body.decode('utf-8'))
        self.rgb = (
            data['red'],
            data['green'],
            data['blue']
        )

        blinkm.fade_to(
            self.rgb[0],
            self.rgb[1],
            self.rgb[2]
        )
        self._send_reponse(resp)

app = falcon.API()

app.add_route('/rgb', RGBResource())
