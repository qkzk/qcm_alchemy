// Allow a teacher to click on the QCM-ID part :
// maximize the font-size for easier readbility on projectors
// blur the rest of the screen
const id_qcm = document.getElementById("qcm-id");
const id_qcm_title = document.getElementById("qcm-id-title");
const qcm_url = document.getElementById("qcm-url");
const teacher_consign = document.getElementById("teacher-consign")

id_qcm.addEventListener("click", function() {
    const parts = document.getElementsByClassName("part");
    Array.from(parts).forEach(part => {
        part.classList.toggle("blur");
    });
    id_qcm.classList.toggle("not-blured");
    id_qcm_title.classList.toggle("enormous-text");
    qcm_url.classList.toggle("not-visible");
    teacher_consign.classList.toggle("not-visible");
});

