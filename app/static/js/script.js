/*
Author Name: Patan Musthakheem
Date & Time: 08-04-2025 12:02AM
File: script.js
*/
function sendResponse() {

    const name = document.getElementById("userName").value.trim();
    const email = document.getElementById("userEmail").value.trim();
    const type = document.getElementById("feedbackType").value;
    const msg = document.getElementById("userMessage").value.trim();
    const respMsg = document.getElementById("message");
    const btn = document.getElementById("submit-btn");

    if (name && email && msg && type !== "") {
        respMsg.hidden = true;
        btn.disabled = true;
        fetch("/api/feedback", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, email, type, msg })
        })
        .then(res => res.json())
        .then(data => {
            respMsg.innerText = data.message;
            respMsg.style.color = data.success ? "green" : "red";
            respMsg.hidden = false;
        })
        .catch(() => {
            respMsg.innerText = "Something went wrong!";
            respMsg.style.color = "red";
            respMsg.hidden = false;
        })
        .finally(() => {
            btn.disabled = false;
        });

    } else {
        respMsg.hidden = false;
        respMsg.innerText = "Please fill in all the details!";
        respMsg.style.color = 'red';
    }
}
