function set_theme(theme) {

    localStorage.setItem("theme", theme);
    const btn = document.getElementById("theme-switcher");
    const body = document.body;
    const radios = document.getElementsByClassName("radio");

    if (theme === "dark") {
        body.classList.add("dark-theme");
        btn.innerHTML = "☀️";
        document.querySelectorAll(".codehilite").forEach(function(i) {
            i.classList.remove("codehi-light");
            i.classList.add("codehi-dark");
        });
    } else {
        body.classList.remove("dark-theme");
        btn.innerHTML = "🌙"; 
        document.querySelectorAll(".codehilite").forEach(function(i) {
            i.classList.remove("codehi-dark");
            i.classList.add("codehi-light");
        });
    }

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
}

const btn = document.getElementById("theme-switcher");
let currentTheme = localStorage.getItem("theme");

if (currentTheme === null || currentTheme == "dark") {
    localStorage.setItem("theme", "dark");
    currentTheme = "dark";
    set_theme("dark");
} else {
    set_theme("light");
}

btn.addEventListener("click", function() {
    let theme = localStorage.getItem("theme");
    if (theme === null || theme === "light") {
        theme = "dark";
    } else {
        theme = "light";
    }
    set_theme(theme)
})
