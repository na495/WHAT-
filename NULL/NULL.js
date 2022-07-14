let btn1 = false;
let btn2 = false;
let btn3 = false;

function button1() {
    document.getElementById('1').style.color = 'rgb(29, 214, 169)';
    if (btn1 == false)
        btn1 = true;
    else {
        btn1 = false;
        document.getElementById('1').style.color = 'rgb(164, 164, 164)';
    }
}

function button2() {
    document.getElementById('2').style.color = 'rgb(29, 214, 169)';
    if (btn2 == false)
        btn2 = true;
    else {
        btn2 = false;
        document.getElementById('2').style.color = 'rgb(164, 164, 164)';
    }
}

function button3() {
    document.getElementById('3').style.color = 'rgb(29, 214, 169)';
    if (btn3 == false)
        btn3 = true;
    else {
        btn3 = false;
        document.getElementById('3').style.color = 'rgb(164, 164, 164)';
    }
}

function done() {
    if (btn1 == 1 && btn2 == 1, btn3 == 1) {
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

        document.querySelector('#result').innerHTML = (hours + minutes + seconds + milliseconds);
        document.querySelector('#reset').style.display = 'block';
    } else {
        alert('모든 항목에 동의해주세요');
    }
}

function reset() {
    btn1 = false;
    btn2 = false;
    btn3 = false;
    document.querySelector('#result').innerHTML = '';
    document.querySelector('#reset').style.display = 'none';

}