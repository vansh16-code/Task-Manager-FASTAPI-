async function fetchTasks() {
    let response = await fetch('/tasks/');
    let tasks = await response.json();
    document.getElementById("taskList").innerHTML = tasks.map(t => 
        `<li>${t.title} - ${t.description} <button onclick="deleteTask(${t.id})">Delete</button></li>`
    ).join("");
}

async function addTask() {
    let title = document.getElementById("taskTitle").value;
    let description = document.getElementById("taskDescription").value;

    await fetch('/tasks/', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({title, description})
    });

    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: "DELETE" });
    fetchTasks();
}

fetchTasks();
