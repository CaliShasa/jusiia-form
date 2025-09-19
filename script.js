const steps = document.querySelectorAll(".form-step");
let currentStep = 0;

// Mostra lo step iniziale
steps[currentStep].classList.add("active");

// Pulsanti "Avanti"
document.querySelectorAll(".next-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    if (currentStep < steps.length - 1) {
      steps[currentStep].classList.remove("active");
      currentStep++;
      steps[currentStep].classList.add("active");
    }
  });
});

// Pulsanti "Indietro"
document.querySelectorAll(".prev-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    if (currentStep > 0) {
      steps[currentStep].classList.remove("active");
      currentStep--;
      steps[currentStep].classList.add("active");
    }
  });
});

// Invio finale con debugger7test
document.getElementById("jusiiaForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const formData = new FormData(this);

  // 🔍 debugger7test: stampa tutti i campi
  console.log("🧪 debugger7test: dati inviati al server");
  for (let [key, value] of formData.entries()) {
    console.log(`${key}: ${value}`);
  }

 fetch("https://script.google.com/macros/s/AKfycbzv87YF7psggNZknKxFnXwXbMb-WsVRUGbS7Awcc-V51Nvzg7n5sRXgG7VTZ6h0njPv/exec", {
  method: "POST",
  body: formData,
  mode: "no-cors"
})
.then(() => {
  // non possiamo leggere la risposta, assumiamo che sia andato bene
  alert("✅ Risposte inviate con successo!");
  this.reset();
  steps[currentStep].classList.remove("active");
  currentStep = 0;
  steps[currentStep].classList.add("active");
})
.catch(error => {
  console.error("❌ debugger7test: errore inatteso", error);
  alert("❌ Errore tecnico. Riprova o contatta il team.");
});

});
