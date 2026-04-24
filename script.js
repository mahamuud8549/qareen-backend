document.querySelector('.booking-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        magaca: document.getElementById('magaca').value,
        nooca: document.getElementById('dacwadda').value,
        farriinta: document.getElementById('farriinta').value
    };

    try {
        // Hubi in IP-ga iyo Port-ka (5000) ay sax yihiin
        const response = await fetch('http://127.0.0.1:5000/send-booking', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        if (result.status === "success") {
            alert("Guul: Codsigaaga waa la keydiyey!");
            e.target.reset();
        } else {
            alert("Cillad Server: " + result.message);
        }
    } catch (error) {
        console.error("Cilladda dhacday:", error);
        alert("Xiriir ma jiro! Hubi in Terminal-ka Python uu shidan yahay.");
    }
});