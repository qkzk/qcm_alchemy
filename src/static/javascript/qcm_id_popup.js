// Allow a teacher to click on the QCM-ID part :
// maximize the font-size for easier readbility on projectors
// blur the rest of the screen
const qcm_id = document.getElementById("qcm-id");
const qcm_id_title = document.getElementById("qcm-id-title");
const qcm_url = document.getElementById("qcm-url");
const teacher_consign = document.getElementById("teacher-consign")

qcm_id.addEventListener("click", function() {
    const parts = document.getElementsByClassName("part");
    Array.from(parts).forEach(part => {
        part.classList.toggle("blur");
    });
    qcm_id.classList.toggle("not-blured");
    qcm_id_title.classList.toggle("enormous-text");
    qcm_url.classList.toggle("not-visible");
    teacher_consign.classList.toggle("not-visible");
});

