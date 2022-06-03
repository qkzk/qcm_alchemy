const toggle_chart = document.getElementById("toggle_chart");
toggle_chart.addEventListener("click", toogle_details);

function toogle_details() {
    const marks_elm = document.getElementById("qcm-marks");
    const chart_elm = document.getElementById("qcm-chart");
    if (marks_elm.style.display != 'none') {
        marks_elm.style.display = 'none';
        chart_elm.style.display = 'block';
        toggle_chart.innerText = "Notes";
        localStorage.setItem("mark_chart", "chart");
    }
    else {
        marks_elm.style.display = 'block';
        chart_elm.style.display = 'none';
        toggle_chart.innerText = "Graphes";
        localStorage.setItem("mark_chart", "mark");
    }
}

