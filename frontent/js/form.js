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