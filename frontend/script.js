const API_URL = "http://127.0.0.1:8000";  // Ikkalasi ham ishlashi uchun HTTP, ammo HTTPS muammo bo'lsa

async function loadTracks() {
    const response = await fetch(`${API_URL}/tracks`);
    const data = await response.json();
    const trackList = document.getElementById("trackList");

    data.tracks.forEach(track => {
        const li = document.createElement("li");
        li.textContent = track;
        li.onclick = () => playTrack(track);
        trackList.appendChild(li);
    });
}

function playTrack(filename) {
    const player = document.getElementById("audioPlayer");
    const trackName = document.getElementById("currentTrackName");

    player.src = `${API_URL}/track/${filename}`;
    trackName.textContent = `Now Playing: ${filename}`;
    player.play();
}

window.onload = loadTracks;
