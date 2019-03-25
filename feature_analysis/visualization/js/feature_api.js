// import config from './config';


SERVER_IP = '192.168.1.109'
PORT = 5000


function requestGet (url, callback) {
  var request = new XMLHttpRequest()
  request.open('GET', url, true)
  request.responseType = 'json'
  request.onload = function () {
    callback(this.response)
  }
  request.send()
  return request
}

function requestPost (url, callback, data) {
  var request = new XMLHttpRequest()
  request.open('POST', url, true)
  request.responseType = 'json'
  request.setRequestHeader( 'Content-Type', 'application/json' )
  request.onload = function () {
    callback(this.response)
  }
  request.send(JSON.stringify(data))
  return request
}

function getMfccFeatNames (callback) {
  requestGet(
    url='http://' + SERVER_IP + ':' + PORT + '/mfcc_feat_names',
    callback=callback
  )
}

function getEsc50Tags (callback) {
  requestGet(
    url='http://' + SERVER_IP + ':' + PORT + '/esc_50_tags',
    callback=callback
  )
}

function getEsc50Wavfiles (callback, tag='') {
  if (tag != '') {
    tag = '/' + tag
  }
  requestGet(
    url='http://' + SERVER_IP + ':' + PORT + '/esc_50_wavfiles' + tag,
    callback=callback
  )
}

function getMfccFeat (callback, filepath) {
  requestPost(
    url='http://' + SERVER_IP + ':' + PORT + '/mfcc_feat',
    callback=callback,
    data={'filepath': filepath}
  )
}
