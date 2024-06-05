$(document).ready(function() {
    // Check local storage for consent status
    if (localStorage.getItem('cookiesAccepted') !== 'true') {
        $('#hide-cookies').show();
    }

    // Handle the cookie consent button click
    $('#submit-cookies').click(function () {
        $('#hide-cookies').hide();
        // Save consent status in local storage
        localStorage.setItem('cookiesAccepted', 'true');
    });
});
