
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
            cell.appendChild(create_image());
            row.appendChild(cell);
        }
        tabla.appendChild(row);
    }

    div_contenedor.appendChild(tabla);

    document.body.insertBefore(div_contenedor, document.getElementById("div1"));
}

function create_image(){
    const image = document.createElement("img");
    image.src = "./images/placeholder.png";

    return image
}