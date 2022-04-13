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
            document.getElementById("tipo").innerHTML = data.Type;
            document.getElementById("ano").innerHTML = data.Year;
            document.getElementById("diretor").innerHTML = data.Director;
            document.getElementById("escritor").innerHTML = data.Writer;
            document.getElementById("nota").innerHTML = data.imdbRating;
            document.getElementById("poster").src = data.Poster;
        }
        )
}

function substituirValores() {
    document.getElementById("titulo").innerHTML = "Título";
    document.getElementById("sinopse").innerHTML = "Sinopse";
    document.getElementById("tipo").innerHTML = "Tipo";
    document.getElementById("ano").innerHTML = "Ano";
    document.getElementById("diretor").innerHTML = "Diretor";
    document.getElementById("escritor").innerHTML = "Escritor";
    document.getElementById("nota").innerHTML = "Nota";
    document.getElementById("poster").src = "https://via.placeholder.com/300x450";
}


