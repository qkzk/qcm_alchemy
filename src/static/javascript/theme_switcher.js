
// Theme switcher
// Allows the theme to switch from dark to light back and forth.
// Listen to a click event on the top button.
const btn = document.getElementById("theme-switcher");
// Select the theme preference from localStorage
const currentTheme = localStorage.getItem("theme");
 
// If the current theme in localStorage is "dark"...
if (currentTheme == "dark") {
  // ...then use the .dark-theme class
    document.body.classList.add("dark-theme");
}

btn.addEventListener("click", function() {
    console.log("theme switch !");
    // Toggle the .dark-theme class on the body
    document.body.classList.toggle("dark-theme");


    // Toggle the colors of selected and not selected radio elements in QCM.
    var body = document.body;
    var radios = document.getElementsByClassName("radio");

    for(var i = 0, max = radios.length; i < max; i++) {
        
        let body_style = getComputedStyle(body);
        let bg_color = body_style.getPropertyValue("--main-bg-color");
        let chosen_color = body_style.getPropertyValue("--main-chosen-color");
        let pre_color = body_style.getPropertyValue("--main-pre-color");
        let answers = document.getElementsByClassName("answer");

        for (let i = 0; i < answers.length; i++) {
                let answer = answers[i];
                if (!answer.childNodes[1].checked) {
                    answer.style.background = bg_color;
                }
            }
        let parent_div = document.getElementById('answer_' + this.id);
        if (parent_div !== null) {
                parent_div.style.background = chosen_color;
                parent_div.style.color = pre_color;
        }
    }


    // Let's say the theme is equal to light
    let theme = "light";
    // If the body contains the .dark-theme class...
    if (document.body.classList.contains("dark-theme")) {
        // ...then let's make the theme dark
        theme = "dark";
        btn.innerHTML = "☀️";
    }
    else {
        btn.innerHTML = "🌙"; 
    }
    // Then save the choice in localStorage
    localStorage.setItem("theme", theme);
});
