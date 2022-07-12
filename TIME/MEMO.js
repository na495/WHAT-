const text = window.localStorage.getItem('maintext');
window.localStorage.setItem('maintext', text);

function onload() {
    const text = window.localStorage.getItem('maintext');
    document.querySelector('textarea').innerHTML = text;
}

function save() {
    const text = document.querySelector('#textbox').value;
    window.localStorage.setItem('maintext', text);
}

function reset() {
    if (window.confirm('삭제하면 영원히 되돌릴 수 없습니다.')) {
        window.localStorage.setItem('maintext', '');
        const text = window.localStorage.getItem('maintext');
        document.querySelector('textarea').innerHTML = text;
    }
}

window.onbeforeunload = function() {
    const orginaltext = window.localStorage.getItem('maintext');
    const nowtext = document.querySelector('#textbox').value;

    if (orginaltext != nowtext)
        return "Do you really want to close?";
};