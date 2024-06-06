document.addEventListener("DOMContentLoaded", function() {
    const generateBtn = document.getElementById("generateBtn");
    const readmeForm = document.getElementById("readmeForm");
    const generatedReadme = document.getElementById("generatedReadme");
    const copyBtn = document.getElementById("copyBtn");

    generateBtn.addEventListener("click", function() {
        const formData = {
            text: document.getElementById("readmeText").value,
            use_table: document.getElementById("useTable").value === "true",
            use_icon: document.getElementById("useIcon").value === "true",
            add_license: document.getElementById("addLicense").value === "true",
            add_contribution: document.getElementById("addContribution").value === "true",
            add_author: document.getElementById("addAuthor").value === "true"
        };

        fetch("/generate_readme", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            generatedReadme.textContent = data.readme;
        });
    });

    new ClipboardJS(copyBtn, {
        text: function() {
            return generatedReadme.textContent;
        }
    });

    copyBtn.addEventListener("click", function() {
        alert("README content copied to clipboard!");
    });
});
