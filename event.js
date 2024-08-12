const apiUrl = 'http://127.0.0.1:5000';
const eventEndpoint = `${apiUrl}/events`
events = [];

fetch(eventEndpoint)
    .then((response) => response.json())
    .then((events) => {
        displayUFCEvents(events);
    })

function displayUFCEvents(events) {
  try {
        // Get the table body element
        const tbody = document.querySelector('#ufc-events-table tbody');

        // Clear existing rows
        tbody.innerHTML = '';

        // Populate the table with event data
        events.forEach(event => {
            const row = document.createElement('tr');
            const date = new Date(event.date * 1000);
            const month = date.toLocaleString('default', {month: 'long'});
            const day = date.getDate();
            console.log(day);
            const year = date.getFullYear();

            const formattedDate = `${month}-${day}-${year}`;

            row.innerHTML = `
                <td><a href="detail.html?id=${event.id}">${event.name}</td>
                <td>${date.toDateString()}</td>
                <td>${event.location}</td>
                <td><a href="https://watchmmafull.com/search/${formattedDate}/"target="_blank" class="watch-icon">🎥</a></td>
            `;

            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching UFC events:', error);
    }   
}

window.onload = displayUFCEvents(events);
