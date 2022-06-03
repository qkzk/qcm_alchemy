let curr_chart_mark = localStorage.getItem("mark_chart");
const qcm_chart_elm = document.getElementById("qcm-chart");
const qcm_mark_elm = document.getElementById("qcm-marks");
if (curr_chart_mark === "chart") {
    qcm_chart_elm.style.display = "block";
    qcm_mark_elm.style.display = "none";
} else {
    qcm_chart_elm.style.display = "none";
    qcm_mark_elm.style.display = "block";
}

