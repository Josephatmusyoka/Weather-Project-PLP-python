// Initialize the current forecast index
let currentDayIndex = 0;

// Function to render the forecast for the given index
function renderForecast() {
    const forecastContainer = document.querySelector('.forecast-container');
    const forecastData = weatherData.forecast[currentDayIndex]; // Get forecast for the current day

    // Clear previous forecast
    forecastContainer.innerHTML = '';

    // Render the forecast data for the current day
    const forecastHTML = `
        <p><strong>Date:</strong> ${new Date(forecastData.date).toLocaleDateString()}</p>
        <p><strong>Time:</strong> ${new Date(forecastData.date).toLocaleTimeString()}</p>
        <p><strong>Temperature:</strong> ${forecastData.temperature}°C</p>
        <p><strong>Weather:</strong> ${forecastData.description}</p>
        <p><strong>Wind Speed:</strong> ${forecastData.wind_speed} m/s</p>
        <img src="http://openweathermap.org/img/wn/${forecastData.icon}@2x.png" alt="Weather Icon">
    `;
    forecastContainer.innerHTML = forecastHTML;
}

// Event listeners for the "Previous" and "Next" buttons
document.getElementById('prevDay').addEventListener('click', () => {
    if (currentDayIndex > 0) {
        currentDayIndex--;  // Move to the previous day
        renderForecast();  // Re-render the forecast for the previous day
    }
});

document.getElementById('nextDay').addEventListener('click', () => {
    if (currentDayIndex < weatherData.forecast.length - 1) {
        currentDayIndex++;  // Move to the next day
        renderForecast();  // Re-render the forecast for the next day
    }
});

// Initial render of the forecast
renderForecast();
