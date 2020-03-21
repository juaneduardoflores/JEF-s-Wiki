var visible = false;

function toggleMenu () {
  var btnmenu = document.getElementById("menu");

  visible = !visible;

  if (visible) {
    btnmenu.style.display = 'block';
  } else {
    btnmenu.style.display = 'none';
  }
}

window.addEventListener("resize", function () {
  if (window.innerWidth < 608) {
    document.getElementById("navbtn").style.display = 'block';
    document.getElementById("navoptions").style.display = 'none';
    document.getElementById("navbtnoptions").style.display = 'block';
    // make menu not show
    document.getElementById("menu").style.display = 'none';
  } else if (window.innerWidth > 607) {
    document.getElementById("navbtn").style.display = 'none';
    document.getElementById("navoptions").style.display = 'block';
    document.getElementById("navbtnoptions").style.display = "none";
  }
});
