// -------------------- SEARCH UI --------------------
let query = "";
const searchUI = document.getElementById("searchui");
const charsWrap = document.getElementById("chars");
const ph = document.getElementById("ph");
const clearBtn = document.getElementById("clearbtn");
let focused = false;

function appendChar(c) { ph.style.display = "none"; const span = document.createElement("span"); span.className = "char"; span.textContent = c; charsWrap.appendChild(span); }
function removeChar() { const last = charsWrap.querySelector(".char:last-child"); if(last) last.remove(); if(!charsWrap.querySelector(".char")) ph.style.display = "block"; }
function clearAll() { query=""; charsWrap.innerHTML=""; ph.style.display="block"; }

searchUI.addEventListener("click", () => { focused = true; ph.style.display="none"; });
document.addEventListener("keydown", e => {
    if(!focused) return;
    const key = e.key;
    if(key.length===1 && !e.ctrlKey && !e.metaKey) { query+=key; appendChar(key); renderClassList(query); e.preventDefault(); }
    else if(key==="Backspace" && query.length){ query=query.slice(0,-1); removeChar(); renderClassList(query); e.preventDefault(); }
    else if(key==="Enter"){ const active = document.querySelector(".class-item.active") || document.querySelector(".class-item"); active?.click(); e.preventDefault(); }
    else if(key==="Escape"){ query=""; clearAll(); renderClassList(query); e.preventDefault(); }
});
clearBtn.addEventListener("click", () => { clearAll(); renderClassList(query); });

// -------------------- CUSTOM CURSOR --------------------
const cursor = document.getElementById("cursor");
document.addEventListener("mousemove", e => { cursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`; });


// -------------------- INITIALIZE --------------------
fetchData();
