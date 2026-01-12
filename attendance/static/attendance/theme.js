document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("themeToggle");
    const body = document.body;

    // Load saved theme
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark");
        toggleBtn.innerText = "☀️ Light Mode";
    }

    toggleBtn.addEventListener("click", function () {
        body.classList.toggle("dark");

        if (body.classList.contains("dark")) {
            localStorage.setItem("theme", "dark");
            toggleBtn.innerText = "☀️ Light Mode";
        } else {
            localStorage.setItem("theme", "light");
            toggleBtn.innerText = "🌙 Dark Mode";
        }
    });
});

