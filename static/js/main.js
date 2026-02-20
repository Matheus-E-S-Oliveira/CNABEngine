document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("file");
  const fileName = document.getElementById("fileName");
  const fileInfo = document.getElementById("fileInfo");
  const removeBtn = document.getElementById("removeFile");
  const submitButton = document.querySelector(".submit-button");
  const clearBtn = document.querySelector(".clear-button");

  if (!fileName.textContent.trim()) {
    submitButton.disabled = true;
  }

  if (!fileInput) return;

  fileInput.addEventListener("change", function () {
    if (this.files.length === 0) {
      resetFile();
      return;
    }

    const file = this.files[0];
    const validExtensions = [".rem", ".ret"];

    const isValid = validExtensions.some((ext) =>
      file.name.toLowerCase().endsWith(ext),
    );

    if (!isValid) {
      fileName.textContent = "Extensão inválida!";
      fileName.style.color = "red";
      submitButton.disabled = true;
      fileInfo.style.display = "flex";
      return;
    }

    fileName.textContent = file.name;
    fileName.style.color = "#fff";
    fileName.style.fontWeight = "bold";
    fileInfo.style.display = "flex";
    submitButton.disabled = false;
  });

  if (removeBtn) {
    removeBtn.addEventListener("click", resetFile);
  }

  function resetFile() {
    fileInput.value = "";
    fileName.textContent = "";
    fileInfo.style.display = "none";
    submitButton.disabled = true;
  }
});
