const addBtn = document.querySelector("#add-btn");
const input = document.querySelector("#wrapper-input");
const taskCont = document.querySelector(".content");
const tasksContainer = document.querySelector("#tasks");
const error = document.getElementById("error");
const isEmpty = document.getElementById("emptyList")
const countValue = document.querySelector(".num");

let c = 0;


const displayCount = (c) => {
    countValue.innerText = c;
};

const empty = () => {
    isEmpty.style.display = "none"
    if (c == 0) {
        isEmpty.style.display = "block"
    }
}

const addTask = () => {
    const taskName = input.value.trim();
    error.style.display = "none";
    isEmpty.style.display = "none"
    if (!taskName) {
        setTimeout(() => {
            error.style.display = "block";
        }, 200);
        saveData()
        return;
    }

const task = `<div class = "task">
    <input type = "checkbox" class = "task-check">
    <span class = "taskname"> ${taskName}</span>
    <button class = "edit">
    <i class="fa-solid fa-pen-to-square"></i>
    </button>
    <button class = "delete">
    <i class="fa-solid fa-trash"></i>
    </button>
</div>`;

taskCont.insertAdjacentHTML("afterbegin", task);

addBtn.addEventListener("click", addTask);

const deleteButtons = document.querySelectorAll(".delete");
deleteButtons.forEach((button) => {
    button.onclick = () => {
        button.parentNode.remove();
        c-=1;
        // if(checkBox.checked){
        //     c+=1;
        // }
        displayCount(c);
        if (c == 0) {
            isEmpty.style.display = "block"
            saveData()
        }
    };
});   

const editButtons = document.querySelectorAll(".edit");
editButtons.forEach((editBtn) => {
    editBtn.onclick = (e) => {
        let targetElement = e.target;
        if (!(e.target.className == "edit")) {
            targetElement = e.target.parentElement;
        }
        input.value = targetElement.previousElementSibling?.innerText;
        targetElement.parentNode.remove();
        c -= 1;
        displayCount(c);
        if (c == 0) {
            isEmpty.style.display = "block"
            saveData()
        }
    };
});

const tasksCheck = document.querySelectorAll(".task-check");
tasksCheck.forEach((checkBox) => {
    checkBox.onchange = () => {
        checkBox.nextElementSibling.classList.toggle("completed");
        if (checkBox.checked){
            c -= 1;
        }else {
            c += 1;
        }
        displayCount(c);
        saveData()
    };
});

c += 1;
displayCount(c);
input.value = "";
};

addBtn.addEventListener("click",addTask);

window.onload = () => {
    c = 0;
    displayCount(c);
    input.value = "";
}

// function saveData() {
//     localStorage.setItem("data", taskCont.innerHTML);
// }

// function showTask() {
//     taskCont.innerHTML = localStorage.getItem("data");
// }

// showTask()

