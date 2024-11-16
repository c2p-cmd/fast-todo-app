document.getElementById("addTodoForm").addEventListener("submit", addNewTodo);

async function addNewTodo(e) {
    e.preventDefault();
    const contentInput = document.getElementById("todoContent");
    const content = contentInput.value;

    try {
        const response = await fetch("/add/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ content: content }),
        });
        if (response.ok) {
            window.location.reload();
        } else {
            alert("Failed to add todo item");
        }
    } catch (error) {
        console.error("Error adding todo:", error);
        alert("Failed to add todo item");
    } finally {
        contentInput.value = "";
    }
}

document.querySelectorAll("input[type=checkbox]").forEach(addListenerToCheckBox);

function addListenerToCheckBox(checkbox) {
    checkbox.addEventListener("change", toggleStatus);
}

async function toggleStatus(e) {
    const checkbox = e.target;
    const itemId = checkbox.dataset.itemId;

    try {
        const response = await fetch(`/toggle/?item_id=${itemId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
        });
        if (response.ok) {
            window.location.reload();
        } else {
            alert("Failed to toggle todo item");
        }
    } catch (error) {
        console.error("Error toggling item:", error);
        alert("Failed to toggle todo item");
    }
}
