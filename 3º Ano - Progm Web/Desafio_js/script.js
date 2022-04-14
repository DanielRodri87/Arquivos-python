var user_pesquisa = document.getElementById("pesquisa");
var api_pesquisa = `http://www.omdbapi.com/?t=${user_pesquisa}&apikey=790af7bc`;    // API do OMDB

function buscarFilme() {
    const filme = document.getElementById("busca").value;
    const api_pesquisa = `http://www.omdbapi.com/?t=${filme}&apikey=790af7bc`;
    fetch(api_pesquisa)

        .then(function (response) {
            return response.json();
        }
        )
        .then(function (data) {
            console.log(data);
            document.getElementById("titulo").innerHTML = data.Title;
            document.getElementById("sinopse").innerHTML = data.Plot;
            document.getElementById("duracao").innerHTML = data.Runtime;
            document.getElementById("tipo").innerHTML = data.Type;
            document.getElementById("ano").innerHTML = data.Year;
            document.getElementById("diretor").innerHTML = "<strong>Dirigido por:</strong>"+` ${data.Director}`;
            document.getElementById("escritor").innerHTML = "<strong>Escrito por:</strong>"+` ${data.Writer}`;
            document.getElementById("nota").innerHTML = data.imdbRating;
            document.getElementById("banner").style.backgroundImage = `url(${data.Poster})`;
        }
        )
}

function substituirValores() {
    document.getElementById("titulo").innerHTML = "Titulo";
    document.getElementById("sinopse").innerHTML = "Sinopse";
    document.getElementById("duracao").innerHTML = "Duração";
    document.getElementById("tipo").innerHTML = "Tipo";
    document.getElementById("ano").innerHTML = "Ano";
    document.getElementById("nota").innerHTML = "Nota";
    document.getElementById("banner").style.backgroundImage = "url(https://www.pngitem.com/pimgs/m/9-948892_no-image-available-icon-png-transparent-png.png)";
    document.getElementById("diretor").innerHTML = "diretor";
    document.getElementById("escritor").innerHTML = "escritor";
}
