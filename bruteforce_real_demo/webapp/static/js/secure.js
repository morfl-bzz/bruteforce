const correctUsernameSecure = "user123";
const correctPasswordSecure = "pass123";
let failedAttempts = 0;
let lockedUntil = 0;

document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const now = Date.now();

  if (now < lockedUntil) {
    window.location.href = "/blocked"; // Redirect to the blocked page
    return;
  }

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === correctUsernameSecure && password === correctPasswordSecure) {
    document.getElementById("message").style.color = "green";
    document.getElementById("message").textContent = "Login erfolgreich!";
    failedAttempts = 0;
  } else {
    failedAttempts++;
    document.getElementById("message").style.color = "red";
    document.getElementById("message").textContent = "Login fehlgeschlagen";

    if (failedAttempts >= 5) {
      lockedUntil = now + 60000;
      window.location.href = "/blocked"; // Redirect to the blocked page
    }
  }
});