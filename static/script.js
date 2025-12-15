console.log("script.js loaded");

function loadHabits() {
    fetch("/habits")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("habitList");
            list.innerHTML = "";

            for (let habit in data) {
                const li = document.createElement("li");

                const checkbox = document.createElement("input");
                checkbox.type = "checkbox";
                checkbox.checked = data[habit];
                checkbox.onchange = () => toggleHabit(habit);

                const text = document.createElement("span");
                text.innerText = " " + habit + " ";

                const delBtn = document.createElement("button");
                delBtn.innerText = "Delete";
                delBtn.onclick = () => deleteHabit(habit);

                li.appendChild(checkbox);
                li.appendChild(text);
                li.appendChild(delBtn);

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
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name: habit})
    }).then(() => {
        input.value = "";
        loadHabits();
    });
}

function toggleHabit(name) {
    fetch("/toggle", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name})
    }).then(loadHabits);
}

function deleteHabit(name) {
    fetch("/delete", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name})
    }).then(loadHabits);
}

loadHabits();
