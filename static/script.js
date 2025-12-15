document.getElementById("app").innerText = "Welcome to Habit Tracker";
function addHabit() {
    const name = document.getElementById("habit").value;
    fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name})
    });
}

function completeHabit(name) {
    fetch("/complete", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name})
    });
}
