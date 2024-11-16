// Handle form submission for adding new todos
document.getElementById("addTodoForm").addEventListener("submit", addNewTodo);

async function addNewTodo(e) {
    e.preventDefault();
    const form = e.target;
    const submitButton = form.querySelector("button");
    const contentInput = document.getElementById("todoContent");
    const content = contentInput.value;

    // Show loading state
    submitButton.disabled = true;
    contentInput.disabled = true;
    const originalButtonText = submitButton.innerHTML;
    submitButton.innerHTML =
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Adding...';

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
        // Reset loading state if page doesn't reload
        submitButton.disabled = false;
        contentInput.disabled = false;
        submitButton.innerHTML = originalButtonText;
        contentInput.value = "";
    }
}

const checkBoxID = ".todo-checkbox";

// Handle checkbox toggles
function disableAllCheckboxes() {
    let allBoxes = document.querySelectorAll(checkBoxID);
    for (let box in allBoxes) {
        box.disabled = true;
    }
}

function enableAllCheckboxes() {
    let allBoxes = document.querySelectorAll(checkBoxID);
    for (let box in allBoxes) {
        box.disabled = false;
    }
}

async function toggleStatus(e, itemId, isChecked) {
    const checkbox = e.target;
    disableAllCheckboxes();
    const todoItem = checkbox.closest(".list-group-item");
    const todoText = todoItem.querySelector(".todo-text"); // Get the specific text element for this item

    // Show loading state
    const loadingSpinner = document.createElement("span");
    loadingSpinner.className = "spinner-border spinner-border-sm ms-2";
    loadingSpinner.setAttribute("role", "status");
    loadingSpinner.setAttribute("aria-hidden", "true");
    todoText.after(loadingSpinner);

    try {
        const response = await fetch(`/update?item_id=${itemId}&status=${isChecked}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
        }
        );
        if (response.ok) {
            window.location.reload();
        } else {
            alert("Failed to toggle todo item");
        }
        enableAllCheckboxes();
    } catch (error) {
        console.error("Error toggling item:", error);
        alert("Failed to toggle todo item");
        // Reset checkbox state
        checkbox.checked = !checkbox.checked;
    } finally {
        // Reset loading state if page doesn't reload
        loadingSpinner.remove();
    }
}

// Handle todo deletion
async function deleteTodo(e, itemId) {
    e.preventDefault();
    const deleteButton = e.target;
    const todoItem = deleteButton.closest(".list-group-item");

    // Show loading state
    deleteButton.disabled = true;
    todoItem.style.opacity = "0.5";
    const loadingSpinner = document.createElement("span");
    loadingSpinner.className = "spinner-border spinner-border-sm ms-2";
    loadingSpinner.setAttribute("role", "status");
    loadingSpinner.setAttribute("aria-hidden", "true");
    deleteButton.before(loadingSpinner);

    try {
        const response = await fetch(`/item/?item_id=${itemId}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (response.ok) {
            window.location.reload();
        } else {
            const errorData = await response.json();
            alert(errorData.message || "Failed to delete todo item");
        }
    } catch (error) {
        console.error("Error deleting todo:", error);
        alert("Failed to delete todo item");
    } finally {
        // Reset loading state if page doesn't reload
        deleteButton.disabled = false;
        todoItem.style.opacity = "1";
        loadingSpinner.remove();
    }
}
