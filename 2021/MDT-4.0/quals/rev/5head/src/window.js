// Run this function after the page has loaded
$(() => {
  const { dialog } = require('electron').remote

  function encode(data) {
    var out = []
    var cur = data[0]
    var cnt = 1
    for (let i = 1; i < data.length; i++) {
      if ( data[i] == cur) {
        cnt += 1
      } else {
        out.push((cnt << 8) + cur)
        cnt = 1
        cur = data[i]
      }
    }
    out.push((cnt << 8) + cur)
    return out
  }

  Array.prototype.equals = function( array ) {
    return this.length == array.length && 
           this.every( function(this_i,i) { return this_i == array[i] } )  
    }

  navigator.mediaDevices.getUserMedia({video: true})
  .then(mediaStream => {
    document.querySelector('video').srcObject = mediaStream;

    const track = mediaStream.getVideoTracks()[0];
    imageCapture = new ImageCapture(track);
  })
  .catch(error => ChromeSamples.log(error));


  function onGrabFrameButtonClick() {
    imageCapture.grabFrame()
    .then(bitmap => {
      // $('#authenticate-toggle').text("wkwk");
      var canvas = document.getElementById('canvas')
      var context = canvas.getContext('2d');
      context.drawImage(bitmap, 0, 0);
      // $('#authenticate-toggle').text("wkwk");
      var captured = context.getImageData(0, 0, bitmap.width, bitmap.height);

      const compressed = encode(captured.data);
      
      if (compressed.equals(data)) {
        dialog.showMessageBox({
          title: '5Head',
          buttons: ['Dismiss'],
          type: 'info',
          message: 'ACCESS GRANTED',
         });
      } else {
        dialog.showMessageBox({
          title: '3Head',
          buttons: ['Dismiss'],
          type: 'warning',
          message: 'ACCESS DENIED',
         });
      }
      
      // electron.remote.getCurrentWindow().close()
    })
    .catch(error => ChromeSamples.log(error));
  }

  $('#authenticate-toggle').on('click', e => {
    onGrabFrameButtonClick()
  })
})