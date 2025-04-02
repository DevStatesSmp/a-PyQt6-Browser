function handleSearch() {
    // Get the input value and trim whitespace
    var input = document.getElementById('searchInput').value.trim();
    if (input === '') {
        alert('Please enter a search query or URL.');
        return;
    }

    // Check if the input is a URL or a search query
    var url;
    var urlPattern = /^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}/;
    if (input.startsWith('http://') || input.startsWith('https://')) {
        url = input;
    } else if (urlPattern.test(input)) {
        url = 'http://' + input;
    } else {
        url = 'https://www.google.com/search?q=' + encodeURIComponent(input);
    }

    // Save the URL to browsing history
    let history = JSON.parse(localStorage.getItem('browsingHistory')) || [];
    history.unshift(url); // Add the newest page at the top
    localStorage.setItem('browsingHistory', JSON.stringify(history));

    // Redirect to the URL
    window.location.href = url;
    window.open(url, '_blank')
}