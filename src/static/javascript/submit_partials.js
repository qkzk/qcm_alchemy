/*
* Open and send an AJAX request to a give URL
* We make sure to insert the CSRF token (for flask validation)
* 
* partials: (object) will be send as JSON
* url: (string) the destination url
* csrf_token: (string) the csrf_token attached to the sending form
*/
function send_xhr(partials, url, csrf_token) {
    // Creating a XHR object
    let xhr = new XMLHttpRequest();
    // open a connection
    xhr.open("POST", url, true);
    // insert CSRF token to avoid 400(bad request) response from Flask
    xhr.setRequestHeader("X-CSRFToken", csrf_token);
    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");
    // Converting JSON data to string
    let data = JSON.stringify(partials);
    // Sending data with the request
    xhr.send(data);
}
