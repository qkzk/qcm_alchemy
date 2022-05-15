window.oncontextmenu = function(event) {
     event.preventDefault();
     event.stopPropagation();
     return false;
};

window.onblur = function() {
    let elt = document.getElementById("qcm_form")
    if (elt !== null) {
        elt.submit();
    }
   }
