const toggle = document.getElementById("toggleProtection");
const status = document.getElementById("status");

// Load saved state
chrome.storage.local.get(["protection"], (result) => {

    // Default: ON
    if (result.protection === undefined) {

        chrome.storage.local.set({
            protection: true
        });

        toggle.checked = true;
        status.innerHTML = "🟢 Protection Enabled";

    } else {

        toggle.checked = result.protection;

        if (result.protection) {

            status.innerHTML = "🟢 Protection Enabled";

        } else {

            status.innerHTML = "🔴 Protection Disabled";

        }

    }

});

// Toggle Protection
toggle.addEventListener("change", () => {

    chrome.storage.local.set({
        protection: toggle.checked
    });

    if (toggle.checked) {

        status.innerHTML = "🟢 Protection Enabled";

    } else {

        status.innerHTML = "🔴 Protection Disabled";

    }

    // Tell background.js to update badge
    chrome.runtime.sendMessage({
        action: "updateBadge"
    });

});

// Open Grafana
document.getElementById("dashboard").onclick = () => {

    chrome.tabs.create({
        url: "http://localhost:3000"
    });

};