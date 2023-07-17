// Email 2 is the verify input
function verifyEmails(emailInputID1, emailInputID2) {
    email1 = document.getElementById(emailInputID1).value
    email2 = document.getElementById(emailInputID2).value
    if (email1 != email2) {
        document.getElementById(emailInputID2).style.borderColor = "red";
    }
    else {
        document.getElementById(emailInputID2).style.borderColor = "none";
    }
}

document.getElementById("id_studentEmail").addEventListener("change", verifyEmails("id_studentEmail", "id_vertifyStudentEmail"))
document.getElementById("id_vertifyStudentEmail").addEventListener("change", verifyEmails("id_studentEmail", "id_vertifyStudentEmail"))

document.getElementById("id_preferredEmail").addEventListener("change", verifyEmails("id_preferredEmail", "id_vertifyPreferredEmail"))
document.getElementById("id_vertifyPreferredEmail").addEventListener("change", verifyEmails("id_preferredEmail", "id_vertifyPreferredEmail"))