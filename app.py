import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from templates.forms import CreateAdvertisementForm

app = Flask(__name__)
app.secret_key = 'sU5erS3cR3T!'
hostname = "foolen.dev"


@app.route('/', methods=["GET", "POST"])
def home():
    form = CreateAdvertisementForm()

    if request.method == 'POST' and form.validate():
        data = {
            'advertisements': {
                'left': {
                    'url': form.left_advertisement_url.data,
                    'image': form.left_advertisement_image.data
                },
                'right': {
                    'url': form.right_advertisement_url.data,
                    'image': form.right_advertisement_image.data
                }
            }
        }

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

        return redirect(url_for('submitted'))

    return render_template('index.html', form=form)


@app.route('/submitted', methods=["GET"])
def submitted():
    return render_template('submitted.html')


@app.route('/api/data', methods=["GET"])
def data():
    try:
        with open('data.json') as json_file:
            return jsonify(json.load(json_file))
    except FileNotFoundError:
        return jsonify({
            'advertisements': {
                'left': {
                    'url': "https://" + hostname,
                    'image': "https://" + hostname + "/static/images/post-left.png"
                },
                'right': {
                    'url': "https://" + hostname,
                    'image': "https://" + hostname + "/static/images/post-right.png"
                }
            }
        })
