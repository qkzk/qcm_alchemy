
window.onblur = function() {
    let elt = document.getElementById("qcm_form")
    if (elt !== null) {
        elt.submit();
    }
   }
