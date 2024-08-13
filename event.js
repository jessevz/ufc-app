const apiUrl = 'http://127.0.0.1:5000';
const eventEndpoint = `${apiUrl}/events`
// const pastEventEndpoint = `${apiUrl}/past_events`
let filteredEvents = [];
const oneDayInSeconds = 24 * 60 * 60; // 24 hours in seconds
events = [];

fetch(eventEndpoint)
    .then((response) => response.json())
    .then((data) => {
        events = data
        filterEvents(false);
        displayUFCEvents(filteredEvents);
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

function filterEvents(upcoming) {
    const currentTimePlusOneDay = Math.floor(Date.now() / 1000) + oneDayInSeconds;
    if (upcoming) {
        filteredEvents = events.filter(event => event.date >= currentTimePlusOneDay);
    } else {
        filteredEvents = events.filter(event => event.date < currentTimePlusOneDay);
    }
}

document.getElementById('upcomingBtn').addEventListener('click', () => {
    filterEvents(true);
    displayUFCEvents(filteredEvents);
    updateActiveButton('upcoming');
});

document.getElementById('pastBtn').addEventListener('click', () => {
    filterEvents(false);
    displayUFCEvents(filteredEvents);
    updateActiveButton('past');
});

function updateActiveButton(type) {
    const upcomingBtn = document.getElementById('upcomingBtn');
    const pastBtn = document.getElementById('pastBtn');

    if (type === 'upcoming') {
        upcomingBtn.classList.add('active');
        pastBtn.classList.remove('active');
    } else {
        upcomingBtn.classList.remove('active');
        pastBtn.classList.add('active');
    }
}

window.onload = displayUFCEvents(events);
