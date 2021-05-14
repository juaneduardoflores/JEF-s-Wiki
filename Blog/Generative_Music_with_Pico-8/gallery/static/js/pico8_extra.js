var autoresize = !1,
  autoplay = !0,
  canvas = document.getElementById("canvas"),
  plate = document.getElementById("plate"),
  Module = {};
function onKeyDown_blocker(e) {
  e = e || window.event;
  var t = document.activeElement;
  (t && t != document.body && "canvas" != t.tagName && "CANVAS" != t.tagName) ||
    (-1 < [9, 32, 37, 38, 39, 40].indexOf(e.keyCode) &&
      e.preventDefault &&
      e.preventDefault());
}
function resizeCanvas() {
  var e = 512,
    t = window.innerWidth,
    n = window.innerHeight,
    a =
      document.fullscreenElement ||
      document.mozFullScreenElement ||
      document.webkitIsFullScreen ||
      document.msFullscreenElement;
  (autoresize || a) &&
    (a || (n -= 32),
    (e = Math.max(
      128,
      Math.min(128 * Math.floor(t / 128), 128 * Math.floor(n / 128))
    ))),
    (plate.style.visibility = "visible"),
    (plate.style.width = e),
    (canvas.style.width = e),
    (canvas.style.height = e),
    window.focus();
}
function toggleFullscreen() {
  var e = document.getElementById("frame");
  document.fullscreenElement ||
  document.mozFullScreenElement ||
  document.webkitIsFullScreen ||
  document.msFullscreenElement
    ? ((e.cancelFullscreen =
        e.cancelFullscreen ||
        e.mozCancelFullScreen ||
        e.webkitCancelFullScreen),
      e.cancelFullscreen())
    : ((e.requestFullscreen =
        e.requestFullscreen ||
        e.mozRequestFullScreen ||
        e.webkitRequestFullScreen),
      e.requestFullscreen());
}
(Module.canvas = canvas),
  document.addEventListener("keydown", onKeyDown_blocker, !1),
  window.addEventListener("load", resizeCanvas, !1),
  window.addEventListener("resize", resizeCanvas, !1),
  window.addEventListener("orientationchange", resizeCanvas, !1),
  window.addEventListener("fullscreenchange", resizeCanvas, !1),
  window.addEventListener("webkitfullscreenchange", resizeCanvas, !1);
var supportedPlayers = 2,
  mapFaceButtons = !0,
  mapShoulderButtons = !0,
  mapTriggerButtons = !1,
  mapStickButtons = !1,
  stickDeadzone = 0.4,
  pico8_buttons = [0, 0, 0, 0, 0, 0, 0, 0];
function updateGamepads() {
  for (
    var e = navigator.getGamepads ? navigator.getGamepads() : [], t = 0;
    t < supportedPlayers;
    t++
  )
    pico8_buttons[t] = 0;
  for (var n = 0; n < e.length; n++) {
    var a = e[n];
    if (a && a.connected) {
      var s = n % supportedPlayers,
        o = 0;
      (o |=
        axis(a, 0) < -stickDeadzone || axis(a, 2) < -stickDeadzone || btn(a, 14)
          ? 1
          : 0),
        (o |=
          axis(a, 0) > +stickDeadzone ||
          axis(a, 2) > +stickDeadzone ||
          btn(a, 15)
            ? 2
            : 0),
        (o |=
          axis(a, 1) < -stickDeadzone ||
          axis(a, 3) < -stickDeadzone ||
          btn(a, 12)
            ? 4
            : 0),
        (o |=
          axis(a, 1) > +stickDeadzone ||
          axis(a, 3) > +stickDeadzone ||
          btn(a, 13)
            ? 8
            : 0),
        (o |=
          (mapFaceButtons && (btn(a, 0) || btn(a, 2))) ||
          (mapShoulderButtons && btn(a, 5)) ||
          (mapTriggerButtons && btn(a, 7)) ||
          (mapStickButtons && btn(a, 11))
            ? 16
            : 0),
        (o |=
          (mapFaceButtons && (btn(a, 1) || btn(a, 3))) ||
          (mapShoulderButtons && btn(a, 4)) ||
          (mapTriggerButtons && btn(a, 6)) ||
          (mapStickButtons && btn(a, 10))
            ? 32
            : 0),
        (pico8_buttons[s] |= o),
        (pico8_buttons[0] |= btn(a, 8) || btn(a, 9) ? 64 : 0);
    }
  }
  requestAnimationFrame(updateGamepads);
}
function axis(e, t) {
  return e.axes[t] || 0;
}
function btn(e, t) {
  return !!e.buttons[t] && e.buttons[t].pressed;
}
navigator.getGamepads && requestAnimationFrame(updateGamepads);
var cartLoaded = !1;
function loadCart() {
  if (!cartLoaded) {
    (document.getElementById("start").style.visibility = "hidden"),
      (document.getElementById("frame").style.visibility = "visible");
    var e = document.createElement("script");
    (e.type = "text/javascript"), (e.async = !0), (e.src = "##js_file##");
    var t = function () {
      (cartLoaded = !0),
        (document.getElementById("menubar").style.visibility = "visible"),
        resizeCanvas();
    };
    (e.onload = t), (e.onreadystatechange = t);
    var n = document.getElementsByTagName("script")[0];
    n.parentNode.insertBefore(e, n);
  }
}
if (autoplay) {
  var context = new AudioContext();
  context.onstatechange = function () {
    "running" == context.state && (loadCart(), context.close());
  };
}

