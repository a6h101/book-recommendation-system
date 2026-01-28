async function handleSearch() {
  const query = document.getElementById("searchInput").value.trim();
  const carousel = document.getElementById("book-carousel");

  if (!query) {
    alert("Please enter a book name or genre");
    return;
  }

  // Hide carousel before loading
  carousel.classList.remove("show");

  try {
    const response = await fetch(
      `http://127.0.0.1:8001/recommend?title=${encodeURIComponent(query)}`
    );

    if (!response.ok) throw new Error("API error");

    const data = await response.json();
    renderBooks(data);

    // Force reflow so animation triggers
    carousel.offsetHeight;
    carousel.classList.add("show");

    // Smooth scroll (same style as Explore button)
    $('html, body').animate(
      { scrollTop: $('#book-carousel').offset().top - 100 },
      1400
    );

  } catch (err) {
    console.error(err);
    alert("Failed to fetch recommendations");
  }
}

function renderBooks(books) {
  const reel = document.getElementById("carouselReel");
  reel.innerHTML = "";

  if (!books || books.length === 0) {
    reel.innerHTML = "<p>No recommendations found.</p>";
    return;
  }

  books.forEach(book => {
    const article = document.createElement("article");
    article.classList.add("book-card");

    article.innerHTML = `
      <a href="${book.url}" target="_blank" rel="noopener noreferrer" class="book-link">
      <div class="book-image">
        <img src="${book.thumbnail}" alt="${book.title}"/>
      </div>
        <header>
          <h3>${book.title}</h3>
        </header>

        <p>
          <strong>Author:</strong> ${book.author}<br>
          <strong>Rating:</strong> ${book.avg_rating ?? "N/A"}
        </p>
      </a>
    `;

    reel.appendChild(article);
  });
}