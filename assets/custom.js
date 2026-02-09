document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.querySelectorAll("button");
    buttons.forEach(btn => {
        btn.addEventListener("click", function() {
            this.innerHTML = "Working...";
            setTimeout(() => {
                this.innerHTML = "Submit";
            }, 1500);
        });
    });
});
