/* eslint-disable no-undef, no-unused-vars */

let num = 100;
let range = 500;

let x_points = [];
let y_points = [];

index = 0;

yoffset = 100;

function setup() {
  canvas = createCanvas(windowWidth, windowHeight);
  canvas.position(0, 0);
  canvas.style("z-index", "-1");
  canvas.style("style", "block");
  canvas.parent("sketch");
  frameRate(30);
  windowResized();
}

function draw() {
  background(255);

  // Shift all elements 1 place to the left
  for (let i = 1; i < num; i++) {
    x_points[i - 1] = x_points[i];
    y_points[i - 1] = y_points[i];
  }

  x_points[index] = index + (windowWidth / num) * index + random(range, -range);
  y_points[index] = index + (windowWidth / num) * index * 0.8 + yoffset;
  x_points[index] += random(-range, range);
  y_points[index] += random(-range, range);
  index += 1;

  if (index > num) {
    index = 0;
  }

  // Draw a point
  for (let i = 0; i < num; i++) {
    strokeWeight(10);
    point(x_points[i], y_points[i]);
  }

  // Draw a line connecting the points
  invert = false;
  for (let i = 1; i < num; i++) {
    // calculate value
    let val = (1 - i / num) * 204.0 + 51;
    if (i % (num / 2) == 0) {
      invert = true;
    }
    if (invert == true) {
      val = (i / num) * 204.0 + 51;
    }
    strokeWeight(1);
    stroke(val);
    // draw lines between Points
    line(x_points[i - 1], y_points[i - 1], x_points[i], y_points[i]);
  }
}

function windowResized() {
  setTimeout(function () {
    var body = document.body,
      html = document.documentElement;

    let h = Math.max(
      body.scrollHeight,
      body.offsetHeight,
      html.clientHeight,
      html.scrollHeight,
      html.offsetHeight
    );

    resizeCanvas(windowWidth, h);
  }, 2000);
}
