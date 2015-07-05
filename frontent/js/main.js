function addElement(container) {
    var count = container.getElementsByClassName("inputField").length;
    var deleteButton = container.getElementsByClassName("button delete");
    var label = document.createElement("label");
    var input = document.createElement("input");
    var inputName, labelName;

    console.log(container.id);
    if (container.id == "containerExpertise") {
        inputName = "expertise";
        labelName = "Lernergebnis";
    }
    if (container.id == "containerUnits") {
        inputName = "assignedUnits";
        labelName = "zugeordnete Units";
    }

    input.type = "text";
    input.className = "inputField spaceLeft";
    input.id = inputName + count;
    label.htmlFor = input.id;
    label.className = "labelTitle";
    label.innerHTML = labelName;
    label.style.visibility = "hidden";


    container.appendChild(label);
    container.appendChild(input);
    container.appendChild(document.createElement("br"));

    deleteButton[0].style.visibility = "visible";

}

function deleteElement (parent) {
    var count = parent.getElementsByClassName("inputField").length;
    //getElementById wirft Fehler bei deletebutton, warum auch immer???
    var deleteButton = parent.getElementsByClassName("button delete");
    if (count > 1) {
        if (count == 2) {
            //delete button ausblenden bevor das letzte Element entfernt wird
            deleteButton[0].style.visibility = "hidden";
        }
        var element = parent.lastChild.previousSibling;

        //delete <br>
        parent.removeChild(element.previousSibling.previousSibling);
        //delete <label>
        parent.removeChild(element.previousSibling);
        //delete <input text>
        parent.removeChild(element);
    }
}
