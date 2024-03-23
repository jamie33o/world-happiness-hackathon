'use strict'

let log = console.log.bind(console),
  id = val => document.getElementById(val),
  ul = id('ul'),
  gUMbtn = id('gUMbtn'),
  start = id('start'),
  stop = id('stop'),
  stream,
  recorder,
  counter=1,
  chunks,
  media = {
    tag: 'audio',
    type: 'audio/ogg',
    ext: '.ogg',
    gUM: {audio: true}
  };

  navigator.mediaDevices.getUserMedia(media.gUM).then(_stream => {
    stream = _stream;
    id('btns').style.display = 'inherit';
    start.removeAttribute('disabled');
    recorder = new MediaRecorder(stream);
    recorder.ondataavailable = e => {
      chunks.push(e.data);
      if(recorder.state == 'inactive')  makeLink();
    };
    log('got media successfully');
  }).catch(log);


start.onclick = e => {
  start.disabled = true;
  stop.removeAttribute('disabled');
  chunks=[];
  recorder.start();
}


stop.onclick = e => {
  stop.disabled = true;
  recorder.stop();
  start.removeAttribute('disabled');
}

let formData

function makeLink(){
  let blob = new Blob(chunks, {type: media.type })
    , url = URL.createObjectURL(blob)
    , li = document.createElement('li')
    , mt = document.createElement(media.tag)
    , hf = document.createElement('a')
  ;
  mt.controls = true;
  mt.src = url;
  
   

  hf.href = url;
  hf.download = `${counter++}${media.ext}`;
  hf.innerHTML = `donwload ${hf.download}`;
  li.appendChild(mt);
  li.appendChild(hf);
  ul.appendChild(li);
 


   // Create a File object
   let file = new File([blob], hf.innerHTML);

   // Create a new FormData object and append the File object
    formData = new FormData();
   formData.append('audio_file', file);


}

   
$('.audio-upload').click(function(){
    let url = $(this).data('url')
    let csrf = $(this).data('csrf')
    $.ajax({
        url: url, 
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
     //    headers: {'X-CSRFToken': csrf}, 
        success: function(response) {
            console.log('File uploaded successfully:', response);
            // Handle success response
        },
        error: function(xhr, status, error) {
            console.error('There was a problem with the file upload:', error);
            // Handle error
        }
    });

})