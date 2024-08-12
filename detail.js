let eventId = null;
let eventDetailEndpoint = "http://127.0.0.1:5000/event/"

document.addEventListener("DOMContentLoaded", () => {
    const eventId = new URLSearchParams(window.location.search).get("id");
    const id = parseInt(eventId, 10);
    loadEvent(id);
    applySpoilerMode();
})

async function loadEvent(id) {
    endpoint = `${eventDetailEndpoint}${id}`
    try {
    const response = await fetch(endpoint);
    const event = await response.json();

        // Populate event details
        document.getElementById('eventTitle').textContent = event.name;
        const date = new Date(event.date * 1000);
        document.getElementById('eventDate').textContent = date.toDateString();
        document.getElementById('eventLocation').textContent = event.location;

        // Populate fights table
        const tbody = document.querySelector('#fights-table tbody');
        tbody.innerHTML = '';

        event.fights.forEach((fight, index) => {
            let winner = "";
            switch (fight.fighter1_won) {
                case 0:
                    winner = fight.fighter2
                case 1:
                    winner = fight.fighter1;
                    break;
                case null:
                    winner = "N/A"
            }
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${fight.fighter1}</td>
                <td>${fight.fighter2}</td>
                <td class="winner">${winner}</td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching event details:', error);
    }
    applySpoilerMode();
}
// Function to toggle spoiler mode
function applySpoilerMode() {
    const spoilerOn = document.getElementById('spoilerToggle').checked;
    const winnerCells = document.querySelectorAll('.winner');
    winnerCells.forEach(cell => {
        if (spoilerOn) {
            // cell.textContent = 'Hidden';
            cell.style.color = "white";
            cell.classList.add('spoiler-hidden');
        } else {
            // const event = fights[parseInt(cell.parentElement.firstElementChild.textContent) - 1];
            // cell.textContent = event.winner ? event.winner : 'N/A';
            cell.style.color = "black";
            cell.classList.remove('spoiler-hidden');
        }
    });

    // Update spoiler status text
    const spoilerStatus = document.getElementById('spoilerStatus');
    spoilerStatus.textContent = spoilerOn ? 'On' : 'Off';
    spoilerStatus.style.color = spoilerOn ? 'green' : 'red';
}

// Event listener for spoiler toggle
document.getElementById('spoilerToggle').addEventListener('change', applySpoilerMode);
