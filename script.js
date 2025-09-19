const steps = document.querySelectorAll(".form-step");
let currentStep = 0;

// Mostra lo step iniziale
steps[currentStep].classList.add("active");

// Funzione di validazione di uno step
function validateStep(stepIndex) {
  const currentFormStep = steps[stepIndex];
  const requiredFields = currentFormStep.querySelectorAll("[required]");
  let valid = true;

  requiredFields.forEach(field => {
    if (field.type === "radio" || field.type === "checkbox") {
      const checked = currentFormStep.querySelector(
        `input[name="${field.name}"]:checked`
      );
      if (!checked) valid = false;
    } else if (!field.value.trim()) {
      valid = false;
    }
  });

  return valid;
}

// Pulsanti "Avanti"
document.querySelectorAll(".next-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    if (!validateStep(currentStep)) {
      alert("⚠️ Devi rispondere a tutte le domande in questa sezione prima di continuare.");
      return;
    }
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

// Invio finale
document.getElementById("jusiiaForm").addEventListener("submit", function (e) {
  e.preventDefault();

  // 🚨 Verifica ultimo step
  if (currentStep !== steps.length - 1) {
    console.warn("⚠️ Tentativo di submit non all'ultimo step, ignorato.");
    return;
  }

  // 🚨 Controllo globale su tutto il form
  const allRequired = this.querySelectorAll("[required]");
  let allValid = true;

  allRequired.forEach(field => {
    if (field.type === "radio" || field.type === "checkbox") {
      const checked = this.querySelector(`input[name="${field.name}"]:checked`);
      if (!checked) allValid = false;
    } else if (!field.value.trim()) {
      allValid = false;
    }
  });

  if (!allValid) {
    alert("⚠️ Devi compilare tutte le domande prima di inviare il questionario.");
    return;
  }

  const formData = new FormData(this);
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
