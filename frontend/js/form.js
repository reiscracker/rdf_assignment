var ausgabeArry = [['key','value']]
var csvRows = [];

function submitForm(form) {

    var allDivs = form.getElementsByClassName("inputDiv");

    for (var i = 0; i < allDivs.length; i++)
    {
        proceedDiv(allDivs[i]);
    }

    exportCSV();
}

function proceedDiv(div) {
    var allElements = div.getElementsByTagName("*");
    for (var i = 0; i < allElements.length; i++)
    {
        if (allElements[i].className == "inputField") {
            if (allElements[i].value != "" && allElements[i].value != null) {
                //replace ersetzt "normale" Leerzeichen, da diese sonst beim Export in CSV verschwunden waren
                ausgabeArry.push([allElements[i-1].innerHTML.replace(/ /g,"\u00A0"), allElements[i].value.replace(/ /g,"\u00A0")]);
            }
        }
    }
}

function exportCSV() {


    for (var i = 0, l = ausgabeArry.length; i < l; ++i) {
        csvRows.push(ausgabeArry[i].join('#'));
    }

    var csvString = csvRows.join("%0A");
    console.log(csvString);
    var a = document.createElement('a');
    a.href = 'data:attachment/csv,' + csvString;
    a.target = '_blank';
    a.download = 'myModul.csv';


    document.body.appendChild(a);
    a.click();
}

function loadFile(files) {
    if (window.FileReader) {
        readFile(files[0]);
    }
    else {
        alert("File API wird nicht unterstützt");
    }

}

function readFile(file) {
    console.log(file);
    var reader = new FileReader();
    reader.readAsText(file);
    reader.onerror = errorHandler;
    reader.onload = processFile;
}

function errorHandler(evt) {
    alert(evt.target.error.name);
}

function processFile(file) {
    var csv = file.target.result;
    processData(csv);
}

function processData(csv) {
    var allTextLines = csv.split(/\r\n|\n/);
    var lines = [];
    var div = document.getElementById("tableContainer");
    var table = document.createElement("table");

    //starten bei i = 1 um anfangszeile key#value zu überspringen
    for (var i = 1; i < allTextLines.length; i++) {
        var data = allTextLines[i].split('#');
        var temp = [];

        var row = document.createElement("tr");
        var col1 = document.createElement("td");
        var col2 = document.createElement("td");
        var notNUll = true;

        for (var j = 0; j < data.length; j++) {
            console.log(data[j].length);
            if (j == 0) {
                if (data[j].length > 0) {
                    //Leerzeichen müssen wieder ersetzt werden, da es sonst zu fehlerhaften Anzeigen in der Tabelle kommt
                    setCol(data[j].replace(/\u00A0/g," "), col1);
                }
                else {
                    notNUll = false;
                }
            }
            else if (j == 1) {
                if (data[j].length > 0) {
                    //Leerzeichen müssen wieder ersetzt werden, da es sonst zu fehlerhaften Anzeigen in der Tabelle kommt
                    setCol(data[j].replace(/\u00A0/g," "), col2);
                }
                else {
                    notNUll = false;
                }
            }

            temp.push(data[j]);
        }


        if (notNUll) {
            row.appendChild(col1);
            row.appendChild(col2);
            table.appendChild(row);
            col1.className = "titleCol";
            col2.className = "dataCol";
            row.className = "row";

            lines.push(temp);
        }

    }

    table.className = "formtable";
    div.appendChild(table);
}

function setCol (data, col) {
    console.log(data);
    var text = document.createTextNode(data);
    col.appendChild(text);
}