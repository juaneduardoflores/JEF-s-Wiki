let isToggled = false;

async function setup2() {
  const patchExportURL2 = 'export/02_patch.export.json';

  // Fetch the exported patcher
  let response, patcher;
  try {
    response = await fetch(patchExportURL2);
    patcher = await response.json();
  } catch (err) {
    const errorContext = {
      error: err,
    };
    if (response && (response.status >= 300 || response.status < 200)) {
      (errorContext.header = `Couldn't load patcher export bundle`),
        (errorContext.description =
          `Check app.js to see what file it's trying to load. Currently it's` +
          ` trying to load "${patchExportURL2}". If that doesn't` +
          ` match the name of the file you exported from RNBO, modify` +
          ` patchExportURL in app.js.`);
    } else {
      throw err;
    }
    return;
  }

  // Create the device
  let device;
  try {
    device = await RNBO.createDevice({ context, patcher });
  } catch (err) {
    if (typeof guardrails === 'function') {
      guardrails({ error: err });
    } else {
      throw err;
    }
    return;
  }

  // Connect the device to the web audio graph
  device.node.connect(outputNode);

  document.body.onclick = () => {
    context.resume();
  };

  makeSliders(device);

  // DSP toggle button
  const toggleButton = document.getElementById('02_ezdac-button');
  const param = device.parametersById.get('toggle');

  toggleButton.addEventListener('click', function () {
    isToggled = !isToggled;
    this.classList.toggle('active');
    // You may also want to trigger other actions based on the value of isToggled
    if (isToggled) {
      param.value = 1;
      document.getElementById('02_ezdac-button').style.backgroundImage = "url('../../resources/ezdac_on.svg')";
    } else {
      param.value = 0;
      document.getElementById('02_ezdac-button').style.backgroundImage = "url('../../resources/ezdac_off.svg')";
    }
  });
}

function makeSliders(device) {
  let pdiv = document.getElementById('02_rnbo-parameter-sliders');

  // This will allow us to ignore parameter update events while dragging the slider.
  let isDraggingSlider = false;
  let uiElements = {};

  device.parameters.forEach((param) => {
    // Subpatchers also have params. If we want to expose top-level
    // params only, the best way to determine if a parameter is top level
    // or not is to exclude parameters with a '/' in them.
    // You can uncomment the following line if you don't want to include subpatcher params

    //if (param.id.includes("/")) return;

    // Create a label, an input slider and a value display
    let label = document.createElement('label');
    let slider = document.createElement('input');
    let text = document.createElement('input');
    let sliderContainer = document.createElement('div');
    sliderContainer.appendChild(label);
    sliderContainer.appendChild(slider);
    sliderContainer.appendChild(text);

    // Add a name for the label
    label.setAttribute('name', param.name);
    label.setAttribute('for', param.name);
    label.setAttribute('class', 'param-label');
    label.textContent = `${param.name}: `;

    // Make each slider reflect its parameter
    slider.setAttribute('type', 'range');
    slider.setAttribute('class', 'param-slider');
    slider.setAttribute('id', param.id);
    slider.setAttribute('name', param.name);
    slider.setAttribute('min', param.min);
    slider.setAttribute('max', param.max);
    if (param.steps > 1) {
      slider.setAttribute('step', (param.max - param.min) / (param.steps - 1));
    } else {
      slider.setAttribute('step', (param.max - param.min) / 1000.0);
    }
    slider.setAttribute('value', param.value);

    // Make a settable text input display for the value
    text.setAttribute('value', param.value.toFixed(1));
    text.setAttribute('type', 'text');

    // Make each slider control its parameter
    slider.addEventListener('pointerdown', () => {
      isDraggingSlider = true;
    });
    slider.addEventListener('pointerup', () => {
      isDraggingSlider = false;
      slider.value = param.value;
      text.value = param.value.toFixed(1);
    });
    slider.addEventListener('input', () => {
      let value = Number.parseFloat(slider.value);
      param.value = value;
    });

    // Make the text box input control the parameter value as well
    text.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter') {
        let newValue = Number.parseFloat(text.value);
        if (isNaN(newValue)) {
          text.value = param.value;
        } else {
          newValue = Math.min(newValue, param.max);
          newValue = Math.max(newValue, param.min);
          text.value = newValue;
          param.value = newValue;
        }
      }
    });

    // Store the slider and text by name so we can access them later
    uiElements[param.id] = { slider, text };

    // Add the slider element
    console.log(param.name);
    if (param.name != 'toggle') {
      pdiv.appendChild(sliderContainer);
    }
  });

  // Listen to parameter changes from the device
  device.parameterChangeEvent.subscribe((param) => {
    if (!isDraggingSlider) uiElements[param.id].slider.value = param.value;
    uiElements[param.id].text.value = param.value.toFixed(1);
  });
}

setup2();
