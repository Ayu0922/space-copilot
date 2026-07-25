const API_URL = "http://127.0.0.1:8000/api/upload";

const browseBtn = document.getElementById("browseBtn");
const pdfFile = document.getElementById("pdfFile");
const uploadBtn = document.getElementById("uploadBtn");
const loader = document.getElementById("loader");
const result = document.getElementById("result");
const dropArea = document.getElementById("dropArea");

let selectedFile = null;

// Browse

browseBtn.onclick = () => {

    pdfFile.click();

};

// Select file

pdfFile.onchange = (e) => {

    selectedFile = e.target.files[0];

    showSelected();

};

// Drag events

dropArea.addEventListener("dragover", e => {

    e.preventDefault();

    dropArea.classList.add("drag-active");

});

dropArea.addEventListener("dragleave", () => {

    dropArea.classList.remove("drag-active");

});

dropArea.addEventListener("drop", e => {

    e.preventDefault();

    dropArea.classList.remove("drag-active");

    selectedFile = e.dataTransfer.files[0];

    showSelected();

});

// Upload button

uploadBtn.onclick = async () => {

    if (!selectedFile) {

        showAlert("Please select a PDF first.", "danger");

        return;

    }

    const formData = new FormData();

    formData.append("file", selectedFile);

    loader.classList.remove("d-none");

    result.innerHTML = "";

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        loader.classList.add("d-none");

        if (response.ok) {

            showAlert(

                `
                <h5>Upload Successful</h5>

                <strong>${data.filename}</strong>

                <hr>

                Pages Processed : ${data.pages_processed}<br>

                Chunks Stored : ${data.chunks_stored}
                `,

                "success"

            );

        }

        else {

            showAlert(data.detail, "danger");

        }

    }

    catch (err) {

        loader.classList.add("d-none");

        showAlert("Cannot connect to backend.", "danger");

        console.error(err);

    }

};

// Show selected file

function showSelected() {

    result.innerHTML = `

        <div class="alert alert-info">

            <i class="fas fa-file-pdf me-2"></i>

            ${selectedFile.name}

        </div>

    `;

}

// Alert

function showAlert(message, type) {

    result.innerHTML = `

        <div class="alert alert-${type}">

            ${message}

        </div>

    `;

}