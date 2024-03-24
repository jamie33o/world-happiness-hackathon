'use strict'

let log = console.log.bind(console),
  id = val => document.getElementById(val),
  ul = id('ul'),
  gUMbtn = id('gUMbtn'),
  start = id('start'),
  stop = id('stop'),
  timer = id('timer'),
  stream,
  recorder,
  timerInterval,  
  running,
  seconds = 0,
  minutes = 0,
  hours = 0,
  counter=1,

  chunks,
  formData,
  media = {
    tag: 'audio',
    type: 'audio/ogg',
    ext: '.ogg',
    gUM: {audio: true},
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
  toggleTimer()
}

stop.onclick = e => {
  stop.disabled = true;
  recorder.stop();
  start.removeAttribute('disabled');
  toggleTimer()
}

function updateTimer() {
  seconds++;
  if (seconds >= 60) {
      seconds = 0;
      minutes++;
      if (minutes >= 60) {
          minutes = 0;
          hours++;
      }
  }
  timer.innerHTML = formatTime(hours) + ":" + formatTime(minutes) + ":" + formatTime(seconds);
}

function formatTime(time) {
  return time < 10 ? "0" + time : time;
}

function toggleTimer() {
  if (running) {
      clearInterval(timerInterval);
      running = false;
      hours = 0;
      minutes = 0;
      seconds = 0;
  } else {
      timerInterval = setInterval(updateTimer, 1000);
      running = true;
  }
}

function makeLink(){
  let blob = new Blob(chunks, {type: media.type })
    , url = URL.createObjectURL(blob)
  ;
 
  $(ul).prepend(`<li class="border p-2 d-flex justify-content-between">
                  <audio controls>
                      <source src="${url}" type="audio/mpeg">
                      Your browser does not support the audio element.
                  </audio>
                  <button data-url="upload_recording/" class="border audio-upload btn-success btn-sm ">Save</button>
                </li>`)

  // Create a File object
  let file = new File([blob], `donwload ${counter++}${media.ext}`);

  // Create a new FormData object and append the File object
  formData = new FormData();
  formData.append('audio_file', file);
}

   
$(document).on('click', '.audio-upload', function(){
  let self = $(this)
    let url = $(this).data('url')
    $.ajax({
        url: url, 
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            self.replaceWith(`<p>Saved</p>`)

        },
        error: function(xhr, status, error) {
            console.error('There was a problem with the file upload:', error);
            // Handle error
        }
    });

})