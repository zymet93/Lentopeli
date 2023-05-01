document.cookie = "fgplayercookie=;expires=Thu, 01 Jan 1970 00:00:01 GMT";
document.cookie = "fgworkcookie=;expires=Thu, 01 Jan 1970 00:00:01 GMT";

async function funcfunc() {
    try {
        const response = await fetch("http://127.0.0.1:3000/highscore/get");
        const data = await response.json();

        const list = document.getElementById("topfive");
        let listmember;

        for (let i = 0; i < data.length; i++) {
            console.log(i);
            listmember = document.createElement("li");

            listmember.innerHTML = data[i].p_name + ": " + data[i].currency;

            list.appendChild(listmember);
        }
    } catch (error) {
        console.log(error.message);
    }
}

funcfunc();
