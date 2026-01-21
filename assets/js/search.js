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
      `http://127.0.0.1:8000/recommend?title=${encodeURIComponent(query)}`
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

    const img = book.image_url || "images/default-book.jpg";

    article.innerHTML = `
      <a class="image featured">
        <img src="${img}" alt="${book.title}">
      </a>
      <header>
        <h3>${book.title}</h3>
      </header>
      <p>
        <strong>Author:</strong> ${book.author}<br>
        <strong>Rating:</strong> ${book.rating ?? "N/A"}
      </p>
    `;

    reel.appendChild(article);
  });
}
