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

let filename = location.pathname.split("/").at(-1);
if (filename) {
  filename = decodeURIComponent(filename.substr(0, filename.length - 5));
}
const timer = document.getElementsByClassName("breadcrumbs")?.[0]
  ?.parentElement?.appendChild(document.createElement("span"));
if (timer && filename != "glossary") {
  timer.id = "timer";
  let time = 0, start;
  const controls = Object.fromEntries(["time", "copy", "play", "pause", "stop"].map(c => [c, timer.appendChild(document.createElement("span"))]));

  function playPause(play, pause) {
    controls.pause.style.display = play ? "inline" : "none";
    controls.stop.style.display = (play || pause) ? "inline" : "none";
    controls.play.style.display = play ? "none" : "inline";
  }
  function showTime() {
    const quarters = Math.max(time / (60 * 60 * 1000), 1);
    const mins = (quarters % 4) * 25;
    controls.time.textContent = "%" + filename + " " + Math.floor(quarters / 4) + (mins ? ("." + mins) : "") + "h ";
    controls.copy.style.display = "inline";
  }

  Object.entries(controls).forEach(e => e[1].className = e[0])
  controls.copy.style.display = "none";
  controls.pause.style.display = "none";
  controls.stop.style.display = "none";
  playPause(false);
  controls.copy.onclick = () => {
    navigator.clipboard.writeText(controls.time.textContent);
  }
  controls.play.onclick = () => {
    start = new Date();
    playPause(true);
  }
  controls.pause.onclick = () => {
    time += new Date() - start;
    showTime();
    playPause(false, true);
  }
  controls.stop.onclick = () => {
    showTime();
    time = 0;
    playPause(false);
  }
}

function distance(a, b) {
    let m = [], i, j, min = Math.min;

    if (!(a && b)) return (b || a).length;

    for (i = 0; i <= b.length; m[i] = [i++]);
    for (j = 0; j <= a.length; m[0][j] = j++);

    for (i = 1; i <= b.length; i++) {
        for (j = 1; j <= a.length; j++) {
            m[i][j] = b.charAt(i - 1) == a.charAt(j - 1)
                ? m[i - 1][j - 1]
                : m[i][j] = min(
                    m[i - 1][j - 1] + 1, 
                    min(m[i][j - 1] + 1, m[i - 1 ][j] + 1))
        }
    }

    return m[b.length][a.length];
}

const main = document.getElementsByTagName("main")?.[0]?.firstElementChild;
const searchContainer = main?.appendChild?.(document.createElement("div"));
if (searchContainer && filename == "glossary") {
  const terms = Object.fromEntries([...document.getElementsByClassName("glossary-term-block")]
    .flatMap(e => e.getElementsByClassName("glossary-term-heading")[0].innerText.split(" | ").map(h => [h, e.firstElementChild.id])));
  searchContainer.style.float = "right";
  const searchText = document.createElement("input");
  searchText.type = "text";
  searchText.placeholder = "🔍";
  const searchResults = document.createElement("datalist");
  searchResults.id = "searchResults";
  searchText.setAttribute("list", searchResults.id);
  searchText.addEventListener("input", e => {
    searchResults.innerHTML = "";
    const input = e.target.value.toLowerCase();
    Object.keys(terms).map(t => [t, t.toLowerCase()]).filter(t => t[1].includes(input))
      .map(t => [t[0], distance(t[1], input)]).sort((a, b) => a[1] - b[1]).slice(0, 10)
      .forEach(match => { searchResults.appendChild(document.createElement("option")).value = match[0]; });
  });
  searchText.addEventListener("change", e => { location.hash = "#" + terms[e.target.value]; });
  searchContainer.appendChild(searchText);
  searchContainer.appendChild(searchResults);
}
