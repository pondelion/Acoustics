from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.util import (
    get_ESC50_tags,
    get_ESC50_wavfile,
    get_ESC50_wavfile_by_tag,
    get_mfcc_feat_names,
    load_wav,
)
from feature_extraction.mfcc import extract_mfcc


app = Flask(__name__)
CORS(app)

@app.route('/mfcc_feat_names', methods=['GET', 'POST'])
def mfcc_feat_names():
    return jsonify({'mfcc_feat_names': get_mfcc_feat_names()})


@app.route('/esc_50_tags', methods=['GET', 'POST'])
def esc50_tags():
    return jsonify({'esc_50_tags': list(get_ESC50_tags().keys())})


@app.route('/esc_50_wavfiles', methods=['GET', 'POST'])
def esc50_wavfiles():
    return jsonify({'esc_50_wavfiles': get_ESC50_wavfile()})


@app.route('/esc_50_wavfiles/<tag>', methods=['GET', 'POST'])
def esc50_wavfiles_tag(tag):
    return jsonify({tag: get_ESC50_wavfile_by_tag(tag)})


@app.route('/mfcc_feat', methods=['POST'])
def mfcc_feat():
    if request.method == 'POST':
        print(request.json)
        filepath = request.json['filepath']
    signal, _ = load_wav(filepath)
    feat, f_names = extract_mfcc(signal)
    return jsonify({
        'mfcc_feat': feat.tolist(),
        'feat_names': f_names
    })


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
