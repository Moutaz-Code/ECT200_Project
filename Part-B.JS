const bookButton = document.getElementById("BookButton");
const secondBanner = document.querySelector(".banner_2");

bookButton.addEventListener("click", () => {
  secondBanner.style.display = secondBanner.style.display === "none" ? "block" : "none";
});
