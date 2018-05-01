let socreText = null
let socreNice = null
let questionTotle = null
let mouseClicksNumber = 0;
let sendData ={}



setTimeout(() => {
    let tipsIfram = document.getElementById("tips-iframe");


    var clickIframe = window.setInterval(checkFocus, 100);

    function checkFocus() {
        if (document.activeElement == document.getElementById("tips-iframe")) {
            console.log("clicked " + (++mouseClicksNumber));
            window.focus();
        }
    }
}, 3000);

// 所有答题框填入1
function allFillone() {
    document.querySelectorAll('input').forEach((e) => e.value = 1)
}

function sendToServer() {    
    console.log('sendToServer')
    fetch("http://23.83.246.248:8080/exams/add-quize/", {
        method: "POST",
        body: JSON.stringify(sendData)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}

setTimeout(() => {
    document.getElementById('endBtn').onclick = endExam;
    document.querySelector('button.btn.btn-danger.navbar-btn').addEventListener('click', endExam)
    document.querySelectorAll('button.ok.btn.btn-primary')[1].addEventListener('click',sendToServer)
    // document.querySelectorAll('button.ok.btn.btn-primary')[1].addEventListener('click',function () {
    //     console.log('send!')
    // })
}, 1000);


function changeSendData(data){
    sendData= data;
    console.log(sendData)
}


function endExam() {
    console.log('end btn clicked')
    let getSocre = document.querySelectorAll('.examScore.fake-nav-link')[0].querySelector('.pull-right').textContent.split('/')
    socreText = document.querySelectorAll('.examScore.fake-nav-link')[0].querySelector('.pull-right').textContent;
    socreNice = socreText.split('/')[0]
    questionTotle = socreText.split('/')[1]
    changeSendData({
        first_name: localStorage.getItem('mloginFname'),
        last_name: localStorage.getItem('mloginlname'),
        student_id: localStorage.getItem('mloginId'),
        quiz_type: 'pre',
        quiz_name: 'pre-test',
        correct_questions: getSocre[0],
        total_questions: questionTotle,
        got_socre: socreNice,
        total_socre: getSocre[1],
        mouse_clicks:0
    })
}