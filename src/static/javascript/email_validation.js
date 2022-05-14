/// Validate an email before submitting it
const form_element = document.getElementById("form");
form_element.addEventListener('submit', event => {
    event.preventDefault();
    const inputmail_element = document.getElementById("email");
    let submitted_email = inputmail_element.value;
    let mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (submitted_email.match(mailformat)) {
        form_element.submit()
    }
    else {
        alert("Veuillez saisir une adresse email valide");
        inputmail_element.focus();
        console.log(false);
    }

});
