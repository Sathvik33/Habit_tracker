document.getElementById("app").innerText = "Welcome to Habit Tracker";
function loadHabits() {
    fetch("/habits")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("habitList");
            list.innerHTML = "";

            for (let habit in data) {
                const li = document.createElement("li");
                li.innerText = habit + (data[habit] ? " ✅" : "");
                li.onclick = () => completeHabit(habit);
                list.appendChild(li);
            }
        });
}

function addHabit() {
    const input = document.getElementById("habitInput");
    const habit = input.value.trim();
    if (!habit) return;

    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: habit })
    }).then(() => {
        input.value = "";
        loadHabits();   // 🔥 THIS WAS MISSING OR WRONG
    });
}

function completeHabit(name) {
    fetch("/complete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name })
    }).then(loadHabits);
}

loadHabits();

