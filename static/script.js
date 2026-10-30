function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value;

    if (message === "") {
        return;
    }

    const chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `
        <p><b>You:</b> ${message}</p>
    `;

    input.value = "";
}