/// Make the upload button visible when a file is selected
const source = document.getElementById('source');
const submit = document.getElementById('submit');
const chosen_file = document.getElementById('chosen-file');

source.onchange = function () {
  chosen_file.textContent = 'Fichier choisi: ' + this.value;
  submit.style.visibility = "visible";
};

