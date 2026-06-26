// Set badge when extension starts
updateBadge();

chrome.runtime.onStartup.addListener(updateBadge);
chrome.runtime.onInstalled.addListener(updateBadge);

// Listen for popup messages
chrome.runtime.onMessage.addListener((message) => {

    if (message.action === "updateBadge") {

        updateBadge();

    }

});

function updateBadge() {

    chrome.storage.local.get("protection", (data) => {

        if (data.protection === false) {

            chrome.action.setBadgeText({
                text: "OFF"
            });

            chrome.action.setBadgeBackgroundColor({
                color: "#ef4444"
            });

        } else {

            chrome.action.setBadgeText({
                text: "ON"
            });

            chrome.action.setBadgeBackgroundColor({
                color: "#22c55e"
            });

        }

    });

}

// Automatic website scanning
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {

    if (changeInfo.status !== "complete")
        return;

    chrome.storage.local.get("protection", (data) => {

        if (data.protection === false) {

            console.log("Protection OFF");

            return;

        }

        if (!tab.url)
            return;

        console.log("Scanning:", tab.url);

        fetch("http://127.0.0.1:5000/check", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: tab.url
            })

        })
        .then(response => response.json())
        .then(data => {

            console.log("Threat Report:", data);

        })
        .catch(error => {

            console.error(error);

        });

    });

});