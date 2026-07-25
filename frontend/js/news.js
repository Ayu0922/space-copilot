const API_URL = "http://127.0.0.1:8000/api/news?limit=10";

const newsContainer = document.getElementById("newsContainer");
const loading = document.getElementById("loading");

window.onload = loadNews;

async function loadNews() {

    loading.style.display = "block";
    newsContainer.innerHTML = "";

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {

            throw new Error("Failed to fetch news");

        }

        const data = await response.json();

        loading.style.display = "none";

        if (!data.articles || data.articles.length === 0) {

            newsContainer.innerHTML = `

                <div class="col-12">

                    <div class="alert alert-warning">

                        No space news found.

                    </div>

                </div>

            `;

            return;

        }

        data.articles.forEach(article => {

            const image = article.image_url || "https://via.placeholder.com/600x300?text=Space+News";

            const summary = article.summary
                ? article.summary.substring(0, 180) + "..."
                : "No summary available.";

            const date = article.published_at
                ? new Date(article.published_at).toLocaleString()
                : "Unknown";

            newsContainer.innerHTML += `

            <div class="col-lg-6 col-xl-4">

                <div class="card h-100 shadow">

                    <img
                        src="${image}"
                        class="card-img-top"
                        style="height:220px;object-fit:cover;"
                  onerror="this.onerror=null; this.src='assets/images/no-image-space.png';"
                   >

                    <div class="card-body">

                        <span class="badge bg-primary mb-2">

                            ${article.news_site}

                        </span>

                        <h5 class="card-title">

                            ${article.title}

                        </h5>

                        <p class="card-text">

                            ${summary}

                        </p>

                    </div>

                    <div class="card-footer bg-white">

                        <div class="d-flex justify-content-between align-items-center">

                            <small class="text-muted">

                                <i class="far fa-clock"></i>

                                ${date}

                            </small>

                            <a
                                href="${article.url}"
                                target="_blank"
                                class="btn btn-primary btn-sm"
                            >

                                Read More

                                <i class="fas fa-arrow-up-right-from-square"></i>

                            </a>

                        </div>

                    </div>

                </div>

            </div>

            `;

        });

    }

    catch (error) {

        console.error(error);

        loading.style.display = "none";

        newsContainer.innerHTML = `

            <div class="col-12">

                <div class="alert alert-danger">

                    <i class="fas fa-circle-exclamation"></i>

                    Unable to load news.

                </div>

            </div>

        `;

    }

}