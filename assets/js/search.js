async function handleSearch() {
  console.log("Search clicked");

  const query = document.getElementById("searchInput").value.trim();

  if (!query) {
    alert("Please enter a book name or genre");
    return;
  }

  try {
    const response = await fetch(
      `http://127.0.0.1:8001/recommend?title=${encodeURIComponent(query)}`
    );

    if (!response.ok) {
      throw new Error("API error");
    }

    const data = await response.json();
    renderBooks(data);

    document
      .getElementById("book-carousel")
      .scrollIntoView({ behavior: "smooth" });

  } catch (error) {
    console.error(error);
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

    const imageSrc = book.thumbnail || "images/default-book.jpg";

    article.innerHTML = `
      <a href="#" class="image featured">
        <img src="${imageSrc}" alt="${book.title}" />
      </a>
      <header>
        <h3>${book.title}</h3>
      </header>
      <p>
        <strong>Author:</strong> ${book.author}<br>
        <strong>Rating:</strong> ${book.rating ?? "N/A"}
        <strong>Rating:</strong> ${book.avg_rating ?? "N/A"}
      </p>
    `;

    reel.appendChild(article);
  });
}