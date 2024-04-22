function startOsc() {
  let ctx = createAudioContext();
  let cvs = document.querySelector('.osc');
  console.log('started osc');
  getUserMedia({ audio: true }).then((stream) => {
    // Works with any supported source
    let src = ctx.createMediaStreamSource(stream);
    let osc = new _osc.Oscilloscope(ctx, src, cvs);
    osc.start();
  });
}
// document.querySelector("#01_ezdac-button").addEventListener("click",startOsc);
