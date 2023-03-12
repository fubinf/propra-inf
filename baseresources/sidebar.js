const btn = document.getElementById("toggle");
let btnst = true;
btn.onclick = () => {
  btnst = !btnst;
  if (btnst) {
    document.querySelector('.toggle span').classList.add('toggle');
    document.getElementById('sidebar').classList.remove('sidebarhide');
    document.getElementById('main').classList.remove('mainfull');
  } else {
    document.querySelector('.toggle span').classList.remove('toggle');
    document.getElementById('sidebar').classList.add('sidebarhide');
    document.getElementById('main').classList.add('mainfull');
  }
};
