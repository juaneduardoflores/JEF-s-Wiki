let simpleShader;

function preload(){
  // a shader is composed of two parts, a vertex shader, and a fragment shader
  // the vertex shader prepares the vertices and geometry to be drawn
  // the fragment shader renders the actual pixel colors
  // loadShader() is asynchronous so it needs to be in preload
  // loadShader() first takes the filename of a vertex shader, and then a frag shader
  // these file types are usually .vert and .frag, but you can actually use anything. .glsl is another common one
  simpleShader = loadShader('./Blog/basic.vert', './Blog/basic.frag');
}

function setup() {
  // shaders require WEBGL mode to work
  createCanvas(windowWidth, windowHeight, WEBGL);
  noStroke();
  print("hey")
}

function draw() {  
  // shader() sets the active shader with our shader
    // send resolution of sketch into shader
  simpleShader.setUniform('u_resolution', [width, windowHeight]);
  simpleShader.setUniform("u_time", millis() / 1000.0); // we divide millis by 1000 to convert it to seconds
  simpleShader.setUniform("u_mouse", [mouseX, map(mouseY, 0, height, height, 0)]);
  shader(simpleShader);

  // rect gives us some geometry on the screen
  rect(0,0,width, height);
}

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}
