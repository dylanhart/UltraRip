import os
import urllib.parse
import json
from io import BytesIO

from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
base_url = 'https://ultra-rip.herokuapp.com/'
font = ImageFont.truetype("Slackey/Slackey-Regular.ttf", 15)

@app.route('/rip', methods=['POST'])
def rip_cmd():
	img_query = urllib.parse.urlencode({'text': request.form['text']})
	return json.dumps({
		'response_type': 'in_channel',
		'text': 'rip...',
		'attachments': [
			{
				'image_url': '{}/gen_img?{}'.format(base_url, img_query),
			}
		]
	})

@app.route('/gen_img', methods=['GET'])
def gen_img():
	rip_img = Image.open('rip.png')

	canvas = ImageDraw.Draw(rip_img)
	canvas.text((150, 350), request.args.get('text', 'they died...'), 'black')
	del canvas

	img_io = BytesIO()
	rip_img.save(img_io, 'PNG', quality=70)
	img_io.seek(0)
	return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
