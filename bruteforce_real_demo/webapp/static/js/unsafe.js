const correctUsername = "user123";
const correctPassword = "pass123";

document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === correctUsername && password === correctPassword) {
    document.getElementById("message").style.color = "green";
    document.getElementById("message").textContent = "Login erfolgreich!";
    setTimeout(() => {
      window.location.href = "/bank"; // Redirect to the bank page
    }, 1000);
  } else {
    document.getElementById("message").style.color = "red";
    document.getElementById("message").textContent = "Login fehlgeschlagen";
  }
});