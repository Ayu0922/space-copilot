// API URL
const API_URL = "http://127.0.0.1:8000/api/chat";

// Generate one session per browser
let sessionId = localStorage.getItem("session_id");

if (!sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem("session_id", sessionId);
}

// Elements
const chatWindow = document.getElementById("chatWindow");
const sendBtn = document.getElementById("sendBtn");
const queryInput = document.getElementById("query");
const typingIndicator = document.getElementById("typingIndicator");

// Send button
sendBtn.addEventListener("click", sendMessage);

// Press Enter to send
queryInput.addEventListener("keydown", function (e) {

    if (e.key === "Enter" && !e.shiftKey) {

        e.preventDefault();

        sendMessage();

    }

});

// -----------------------------

async function sendMessage() {

    const query = queryInput.value.trim();

    if (query === "") return;

    addUserMessage(query);

    queryInput.value = "";

    showTyping();

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                query: query,

                session_id: sessionId

            })

        });

        if (!response.ok) {

            throw new Error("Server Error");

        }

        const data = await response.json();

        hideTyping();

        addBotMessage(data.answer, data.sources);

    }

    catch (error) {

        hideTyping();

        addBotMessage(

            "Unable to connect to the backend.",

            []

        );

        console.error(error);

    }

}

// -----------------------------

function addUserMessage(text) {

    const html = `

        <div class="user-message mt-4">

            <div class="message-icon">

                <i class="fas fa-user"></i>

            </div>

            <div class="message-content">

                ${escapeHtml(text)}

            </div>

        </div>

    `;

    chatWindow.insertAdjacentHTML("beforeend", html);

    scrollBottom();

}

// -----------------------------

function addBotMessage(answer, sources) {

    let sourceHTML = "";

    if (sources && sources.length > 0) {

        sourceHTML += `

            <div class="mt-3">

                <h6>

                    <i class="fas fa-book me-2"></i>

                    Sources

                </h6>

        `;

        sources.forEach(source => {

            sourceHTML += `

                <div class="card source-card mt-2">

                    <div class="card-body p-2">

                        <strong>

                            ${source.document}

                        </strong>

                        <br>

                        <small>

                            Page: ${source.page}

                        </small>

                        <br>

                        <small>

                            Similarity:

                            ${(source.score * 100).toFixed(1)}%

                        </small>

                    </div>

                </div>

            `;

        });

        sourceHTML += "</div>";

    }

    const html = `

        <div class="bot-message mt-4">

            <div class="message-icon">

                <i class="fas fa-robot"></i>

            </div>

            <div class="message-content">

                ${formatAnswer(answer)}

                ${sourceHTML}

            </div>

        </div>

    `;

    chatWindow.insertAdjacentHTML("beforeend", html);

    scrollBottom();

}

// -----------------------------

function showTyping() {

    typingIndicator.classList.remove("d-none");

    scrollBottom();

}

// -----------------------------

function hideTyping() {

    typingIndicator.classList.add("d-none");

}

// -----------------------------

function scrollBottom() {

    chatWindow.scrollTop = chatWindow.scrollHeight;

}

// -----------------------------

function escapeHtml(text) {

    return text

        .replace(/&/g, "&amp;")

        .replace(/</g, "&lt;")

        .replace(/>/g, "&gt;");

}

// -----------------------------

function formatAnswer(text) {

    return text

        .replace(/\n/g, "<br>");

}