const contactForm = document.querySelector(".form");
const submitBtn = document.querySelector(".submit");
const nameInput = document.querySelector("#name");
const emailInput = document.querySelector("#email");
const subjectInput = document.querySelector("#subject");
const messageInput = document.querySelector("#message");
const publicKey = "Sdkt0v9uRTuh23xX0";
const serviceID = "service_65qb424";
const templateID = "template_vro5wsg";

emailjs.init(publicKey);

contactForm.addEventListener("submit", e => {
    e.preventDefault();

    submitBtn.innerText = "Just a Moment...";

    const inputFields = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value
    }

    emailjs.send(serviceID, templateID, inputFields)
    .then(() => {
        submitBtn.innerText = "Message Sent Successfully";

        nameInput.value = "";
        emailInput.value = "";
        subjectInput.value = "";
        messageInput.value = "";
    }, (error) => {

        console.log(error);

        submitBtn.innerText = "Something went wrong";
    });
});