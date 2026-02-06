const buttons = document.querySelectorAll(".filters button");
const artworks = document.querySelectorAll(".artwork");

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;

    artworks.forEach(art => {
      const tags = art.dataset.tags.split(" ");

      if (filter === "all" || tags.includes(filter)) {
        art.style.display = "flex";
      } else {
        art.style.display = "none";
      }
    });
  });
});
