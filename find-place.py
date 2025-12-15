<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Place Finder</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      margin: 0;
      padding: 0;
    }
    header {
      background: #2563eb;
      color: white;
      padding: 1rem;
      text-align: center;
    }
    .container {
      max-width: 800px;
      margin: 2rem auto;
      background: white;
      padding: 1.5rem;
      border-radius: 8px;
    }
    input {
      width: 100%;
      padding: 0.7rem;
      margin-bottom: 1rem;
      font-size: 1rem;
    }
    .place {
      border-bottom: 1px solid #ddd;
      padding: 0.5rem 0;
    }
    .place:last-child {
      border-bottom: none;
    }
  </style>
</head>
<body>
  <header>
    <h1>🌍 Simple Place Finder</h1>
    <p>Find places easily</p>
  </header>

  <div class="container">
    <input type="text" id="search" placeholder="Search for a place..." />
    <div id="places"></div>
  </div>

  <script>
    const places = [
      { name: "Nairobi", description: "Capital city of Kenya" },
      { name: "Mombasa", description: "Coastal city with beaches" },
      { name: "Kisumu", description: "City near Lake Victoria" },
      { name: "Eldoret", description: "Known for athletics" },
      { name: "Nakuru", description: "Near Lake Nakuru National Park" }
    ];

    const searchInput = document.getElementById("search");
    const placesDiv = document.getElementById("places");

    function displayPlaces(list) {
      placesDiv.innerHTML = "";
      list.forEach(place => {
        const div = document.createElement("div");
        div.className = "place";
        div.innerHTML = `<strong>${place.name}</strong><br>${place.description}`;
        placesDiv.appendChild(div);
      });
    }

    searchInput.addEventListener("input", () => {
      const value = searchInput.value.toLowerCase();
      const filtered = places.filter(p => p.name.toLowerCase().includes(value));
      displayPlaces(filtered);
    });

    displayPlaces(places);
  </script>
</body>
</html>
