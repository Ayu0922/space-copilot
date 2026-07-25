const API_URL = "http://127.0.0.1:8000/api/documents";
const PDF_BASE = "http://127.0.0.1:8000/documents";

const container = document.getElementById("documentsContainer");
const searchBox = document.getElementById("searchInput");
const totalDocs = document.getElementById("totalDocuments");

let documents = [];

// ----------------------
// Image Mapping
// ----------------------

function getImage(filename) {

    const name = filename.toLowerCase();

    if (name.includes("aditya"))
        return "assets/images/Aditya_L1.png";

    if (name.includes("chandrayaan"))
        return "assets/images/Chandrayaan3.png";

    if (name.includes("gaganyaan"))
        return "assets/images/Gaganyaan.png";

    if (name.includes("mars"))
        return "assets/images/mars_orbitor.jpg";

    if (name.includes("pslv"))
        return "assets/images/PSLV_C60.jpg";

    if (name.includes("lvm3") || name.includes("gslv"))
        return "assets/images/LVM3.png";

    return "assets/images/no-image-space.png";

}

// ----------------------
// Load Documents
// ----------------------
async function loadDocuments() {

    try {

        const response = await fetch(API_URL);

        const data = await response.json();

        documents = data.documents;

        totalDocs.textContent = documents.length;

        renderDocuments(documents);

    }

    catch (error) {

        console.error(error);

        container.innerHTML = `

            <div class="col-12">

                <div class="alert alert-danger">

                    Unable to load documents.

                </div>

            </div>

        `;

    }

}

// ----------------------
// Render Cards
// ----------------------

function renderDocuments(list) {

    container.innerHTML = "";

    list.forEach(doc => {

        const image = getImage(doc.filename || doc.name);

        const filename = doc.filename
            ? doc.filename
            : `${doc.name}.pdf`;

        const card = `

        <div class="col-lg-4 col-md-6 mb-4">

            <div class="document-card">

                <img
                    src="${image}"
                    class="document-image"
                    alt="${doc.name}">

                <div class="document-content">

                    <h4>${doc.name}</h4>

                    <p>${doc.pages} Pages</p>

                    <span class="badge bg-success">
                        Indexed
                    </span>

                    <div class="mt-4">

                        <button
                            class="btn btn-outline-info w-100 mb-2 preview-btn"
                            data-file="${filename}">

                            <i class="fas fa-eye me-2"></i>

                            Preview

                        </button>

                        <button
                            class="btn btn-primary w-100 download-btn"
                            data-file="${filename}">

                            <i class="fas fa-download me-2"></i>

                            Download

                        </button>

                    </div>

                </div>

            </div>

        </div>

        `;

        container.innerHTML += card;

    });

    attachEvents();

}

// ----------------------
// Buttons
// ----------------------

function attachEvents() {

    document.querySelectorAll(".preview-btn").forEach(btn => {

        btn.onclick = () => {

            const file = btn.dataset.file;

            window.open(

                `${PDF_BASE}/${encodeURIComponent(file)}`,

                "_blank"

            );

        };

    });

    document.querySelectorAll(".download-btn").forEach(btn => {

        btn.onclick = () => {

            const file = btn.dataset.file;

            const link = document.createElement("a");

            link.href = `${PDF_BASE}/${encodeURIComponent(file)}`;

            link.download = file;

            document.body.appendChild(link);

            link.click();

            document.body.removeChild(link);

        };

    });

}

// ----------------------
// Search
// ----------------------

if (searchBox) {

    searchBox.addEventListener("input", function () {

        const value = this.value.toLowerCase();

        const filtered = documents.filter(doc =>

            doc.name.toLowerCase().includes(value)

        );

        renderDocuments(filtered);

    });

}

// ----------------------

loadDocuments();