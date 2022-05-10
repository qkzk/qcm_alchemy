/// Make the upload button visible when a file is selected
source = document.getElementById('source');
label = document.getElementById('label');
submit = document.getElementById('submit');
source.onchange = function () {
  label.textContent = 'Fichier choisi: ' + this.value;
  submit.style.visibility = "visible";
};

