async function scrape() {
    const url = document.getElementById("postUrl").value;
    const scrapeType = document.getElementById("scrapeType").value;
  
    if (!url) {
      alert("Please enter a valid URL!");
      return;
    }
  
    try {
      const response = await fetch("http://localhost:5000/scrape", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, scrapeType }),
      });
  
      if (!response.ok) throw new Error("Failed to scrape the data.");
  
      const data = await response.json();
      const tableBody = document.querySelector("#resultsTable tbody");
      tableBody.innerHTML = "";
  
      data.results.forEach((item) => {
        const row = `<tr>
          <td>${item.username}</td>
          <td>${item.comment || "N/A"}</td>
        </tr>`;
        tableBody.innerHTML += row;
      });
    } catch (error) {
      alert("Error: " + error.message);
    }
  }
  