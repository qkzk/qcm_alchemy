// Style the input-radio (answers) elements.
// When checked:        background orange,  color black
// When not checked:    background dark,    color light
// Will break if the .answer.firstChild isn't a <input type="radio">

var body = document.body;
var radios = document.getElementsByClassName("radio");

for(var i = 0, max = radios.length; i < max; i++) {
    radios[i].onclick = function() {
        let body_style = getComputedStyle(body);
        let bg_color = body_style.getPropertyValue("--main-bg-color");
        let chosen_color = body_style.getPropertyValue("--main-chosen-color");
        let answers = document.getElementsByClassName("answer");

        for (let i = 0; i < answers.length; i++) {
                let answer = answers[i];
                if (!answer.childNodes[1].checked) {
                    answer.style.background = bg_color;
                }
            }

        let parent_div = document.getElementById('answer_' + this.id);
        parent_div.style.background = chosen_color;
    }
    
}
