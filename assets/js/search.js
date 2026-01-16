function handleSearch() {
  const input = document.getElementById("searchInput");
  const query = input.value.trim();

  if (!query) {
    alert("Please enter a book name or genre");
    return;
  }

  console.log("Searching recommendations for:", query);

  // TEMP (later this will call backend / ML API)
  alert("Recommended books for: " + query);
}