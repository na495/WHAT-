function Clock() {
    let today = new Date();

    let hours = "";
    if (today.getHours() > 12) {
        hours += "오후 ";
        hours += (today.getHours() - 12) + "시 ";
    } else {
        hours += "오전 ";
        hours += today.getHours() + "시 ";
    }; // 시
    let minutes = today.getMinutes() + "분 "; // 분
    let seconds = today.getSeconds() + "초 "; // 초
    let milliseconds = (today.getMilliseconds() / 100).toFixed(); // 밀리초


    if (today.getSeconds() > 50) { //정각 1분전부터 빨강색으로 출력
        document.getElementById('time').style.color = "red";
    } else {
        document.getElementById('time').style.color = "black";
    }

    document.getElementById('tl').innerText = (hours);
    document.getElementById('qns').innerText = (minutes);
    document.getElementById('ch').innerText = (seconds);
    document.getElementById('alfflch').innerText = (milliseconds);


    setTimeout(Clock, 100); //0.1초마다 갱신

}

function checkedms() {

    const checkbox = document.getElementById('msonoff');
    const checkedTrue = checkbox.checked;

    if (checkedTrue == true)
        document.getElementById('alfflch').style.display = "none";
    else
        document.getElementById('alfflch').style.display = "inline";

}



function addList() {
    let today = new Date();

    let hours = "";
    if (today.getHours() > 12) {
        hours += "오후 ";
        hours += (today.getHours() - 12) + "시 ";
    } else {
        hours += "오전 ";
        hours += today.getHours() + "시 ";
    }; // 시
    let minutes = today.getMinutes() + "분 "; // 분
    let seconds = today.getSeconds() + "초 "; // 초
    let milliseconds = today.getMilliseconds(); // 밀리초

    const li = document.createElement('li');
    li.setAttribute('onclick', 'liremove()');
    li.innerHTML = (hours + minutes + seconds + milliseconds);
    document.getElementById('List').appendChild(li);
}

function removeList() {
    let List = document.getElementById('List');
    while (List.hasChildNodes()) {
        List.removeChild(List.firstChild);
    }
}