// Hamburger menu toggle
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const main = document.querySelector(".main");
    const btn = document.getElementById("menuBtn");

    sidebar.classList.toggle("active");
    main.classList.toggle("shift");

    // Change icon ☰ <-> ✕
    btn.innerHTML = sidebar.classList.contains("active") ? "✕" : "☰";
}

// Animate progress bars on page
const passwordInput = document.querySelector('input[name="password"]');
const registerForm = document.querySelector('form');

registerForm.addEventListener('submit', function(e){
    const password = passwordInput.value;
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
    if(!regex.test(password)){
        e.preventDefault();
        alert("Password too weak! Use at least 8 characters with uppercase, lowercase, and a number.");
    }
});


