let selectedGenres = [];

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".genre-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const genre = btn.dataset.genre;

            if (selectedGenres.includes(genre)) {
                selectedGenres = selectedGenres.filter(g => g !== genre);
                btn.classList.remove("active");
            } else {
                selectedGenres.push(genre);
                btn.classList.add("active");
            }
        });
    });

});

function getRecommendations() {
    const title = document.getElementById("searchInput").value;
    const container = document.getElementById("results");
    const template = document.getElementById("card-template");

    let url = "http://127.0.0.1:8000/recommend?";
    if (title) url += "title=" + encodeURIComponent(title);
    if (selectedGenres.length > 0) {
        url += "&genres=" + encodeURIComponent(selectedGenres.join(","));
    }

    fetch(url)
        .then(res => res.json())
        .then(data => {

            container.querySelectorAll(".card:not(#card-template)")
                .forEach(card => card.remove());

            if (!data.recommendations || data.recommendations.length === 0) {
                alert("No recommendations found");
                return;
            }

            data.recommendations.forEach(book => {
                const card = template.cloneNode(true);
                card.style.display = "block";
                card.removeAttribute("id");

                card.querySelector("h3 a").textContent = book.title;
                card.querySelector("p").textContent =
                    book.description || "No description available.";

                if (book.image) {
                    card.querySelector("img").src = book.image;
                }

                container.appendChild(card);
            });
        })
        .catch(err => {
            console.error(err);
            alert("Failed to fetch recommendations");
        });
}