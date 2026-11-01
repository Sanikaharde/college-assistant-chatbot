async function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value;

    if (message === "") {
        return;
    }

    const chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `
    <div class="message user">
        ${message}
    </div>
`;

input.value = "";

    try {

        console.log("Sending request to Flask...");

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        console.log("Response received:", response);

        const data = await response.json();

        console.log("Data received:", data);

        chatbox.innerHTML += `
            <div class="message bot">
                ${data.response}
            </div>
        `;

    } catch (error) {

        console.log("ERROR:", error);

        chatbox.innerHTML += `
            <div class="message bot">
                Error connecting to server.
            </div>
        `;
    }

    input.value = "";
}

document.getElementById("message")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});