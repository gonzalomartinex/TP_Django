
//var path = require('path');
//var filename = path.basename('/home/alumno/PG3/TP_Django/PaginaDeStreaming/Streaming/static/images/placeholder.png');
//console.log(filename);

function create_table(){
    const div_contenedor = document.createElement("div");
    div_contenedor.classList = "centered black";
    const tabla = document.createElement("table");

    rows = 5;
    cells = 5;

    for (i=0;i<rows;i++){
        row = document.createElement("tr");
        for(e=0;e<cells;e++){
            cell = document.createElement("td");
            cell.appendChild(create_button());
            row.appendChild(cell);
        }
        tabla.appendChild(row);
    }

    div_contenedor.appendChild(tabla);

    document.body.insertBefore(div_contenedor, document.getElementById("div1"));
}

function create_button(){
    const button = document.createElement("button");
    button.appendChild(create_image());

    return button
}

function create_image(){
    const image = document.createElement("img");
    image.src = '/static/images/placeholder.png';

    return image
}