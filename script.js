const inputtext1 = document.querySelector("#newt1");
const targettext1 = document.querySelector("#newt2");
const enterbtn = document.querySelector(".enter");
const linenos = document.querySelector(".linenos");
let counting = 1;

inputtext1.focus();



enterbtn.addEventListener("click", async (e) => {
    const it = inputtext1.value;
    const tt = targettext1.value;

    const data = {
        inp: `${it}`,
        tar: `${tt}`
    }
    const result = await wordcounterAPI(data)

    const storeres = document.createElement("div");
    storeres.className = "alllineno";
    storeres.innerHTML="";

    if(counting>1){
        linenos.innerHTML = `<p class="linenop">Your target word is present in line no.</p>`;
    }

    counting = 1;
    
    
    for(let res of result){
        const storevalue = document.createElement("button");
        storevalue.className="lineno";
        console.log(res);
        storevalue.innerText = `${counting}). ${res}`;
        storeres.appendChild(storevalue);
        counting++;
    };

    linenos.appendChild(storeres);
    linenos.style.display = "flex";
});


async function wordcounterAPI(Data){
    const result = await fetch("https://word-appreance-counter.onrender.com/word_counter", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(Data)
    }
    );
    const r = await result.json();
    return r
}