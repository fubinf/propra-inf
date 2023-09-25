const targets = ["public", "login.html", "some/file", "api/logout", "api/newuser"];
const args = {"irrelevante Argumente": "", "ungültige Session-ID": "", "gültige Session-ID": "", "falscher Benutzername/Passwort": "", "korrekter Benutzername/Passwort": ""};
const headers = {"irrelevantes Cookie": "", "ungültige Session-ID": "", "gültige Session-ID": ""};
const success = {status: 200, body: ""};
const login = {status: 200, body: "login"};
const denied = {status: 401, body: ""};
const expected = [
  new Array(5).fill(new Array(3).fill(success)), //public should always work
  [...new Array(3).fill([login, login, success]), new Array(3).fill(success), [login, login, success]],
  [...new Array(3).fill([denied, denied, success]), new Array(3).fill(success), [denied, denied, success]],
  ... new Array(2).fill([...new Array(3).fill([denied, denied, {}]), new Array(3).fill({}), [denied, denied, {}]])
];

function radio(index, cat, title) {
  if (index == undefined || !title) {
    return title;
  }
  return `<input type="radio" id="${cat + index}" name="${cat}" onclick="select(true);"${index == 0 ? " checked" : ""}/><label for="${cat + index}">${title}</label>`;
}

let stage = 3;
function line(target, arg, header, index) {
  if (typeof target == "number") {
    const url = target > stage ? "" : (targets[target] ?? "");
    return line(url, Object.keys(args)[target] ?? "", Object.keys(headers)[target] ?? "", target);
  }
  const tag = index == undefined ? "th" : "td";
  return `<tr><${tag}>${radio(index, "target", target)}</${tag}><${tag}>${radio(index, "arg", arg)}</${tag}><${tag}>${radio(index, "header", header)}</${tag}></tr>`;
}

const root = document.getElementById("httpauth");
function select(showExpected) {
  const selected = Object.fromEntries([...root.getElementsByTagName("input")].filter(e => e.checked).map(e => e.id.match(/[a-z]+|\d+/g)));
  if (showExpected) {
    document.getElementById("result").innerText = "Erwartet: " + JSON.stringify(expected[selected.target][selected.arg][selected.header]);
  }
  return {target: parseInt(selected.target ?? 0), arg: parseInt(selected.arg ?? 0), header: parseInt(selected.header ?? 0)};
}

const successmsg = "Okay.";
async function send(server, selected) {
  if (server == undefined) {
    return send(document.getElementById("server").value, select());
  }
  const exp = expected[selected.target][selected.arg][selected.header];
  const url = `http://${server}/` + (stage <= 5 ? targets[selected.target] : ".auth");
  const response = await fetch(url).catch(e => ({status: 500}));
  if (response.status == 500) {
    return `Server ${server} antwortet nicht.`;
  }
  const body = await response.blob();
  let e = exp.hasOwnProperty("status") && exp.status != response.status ? "status" : null;
  e = e ?? (exp.hasOwnProperty("body") && exp.body != body ? "body" : null);
  if (e) {
    return `Falscher ${e}. Empfangen ${response[e] ?? body}, erwartet ${exp[e]}.`;
  }
  return successmsg;
}

function groupBy(xs, key, map) {
  return xs.reduce((rv, x) => {
    (rv[key(x)] = rv[key(x)] || []).push((map || (e => e))(x));
    return rv;
  }, {});
}

const cartesian = (...a) => a.reduce((a, b) => a.flatMap(d => b.map(e => [d, e].flat())));
async function sendAll() {
  let available = groupBy([...root.getElementsByTagName("input")].filter(e => e.type == "radio").map(e => e.id.match(/[a-z]+|\d+/g)), l => l[0], l => l[1]);
  available = Object.fromEntries(Object.entries(available).map(e => [e[0], e[1].length]));
  const server = document.getElementById("server").value;
  const counted = Object.entries(available).map(e => new Array(e[1]).fill().map((_, i) => ({[e[0]]: i})));
  const options = cartesian(...counted).map(e => e.reduce((a, b) => Object.assign(a, b), {}));
  const res = await Promise.any(options.map(option => send(server, option).then(result => Promise[result == successmsg ? "reject" : "resolve"]({option, result})))).catch(err => {result: successmsg});
  Object.entries(res.option ?? {}).map(e => e.join("")).forEach(id => {document.getElementById(id).checked = true})
  return res.result;
}

const tablelines = line("Pfad", "Argument", "Header") + Object.keys(new Array(stage).fill()).map(i => line(parseInt(i))).join("");
root.innerHTML = `<table style="padding: 2;">${tablelines}</table><input type="text" id="server" value="127.0.0.1:7979"/><button type="button" onclick="send().then(e => result.innerText = e)">Auswahl senden</button><button type="button" onclick="sendAll().then(e => result.innerText = e)">Alle senden</button><div id="result"></div>`;
const result = document.getElementById("result");
