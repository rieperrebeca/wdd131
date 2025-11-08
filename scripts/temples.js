// Display the current year
const currentYear = new Date().getFullYear();
document.getElementById("currentyear").textContent = currentYear;

// Display the last modified date
document.getElementById("lastModified").textContent = `Last Modification: ${document.lastModified}`;
