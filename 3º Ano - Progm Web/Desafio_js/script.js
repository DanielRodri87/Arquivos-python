function buscarFilme() {
    const filme = document.getElementById("busca").value;
    const api_pesquisa = `http://www.omdbapi.com/?t=${filme}&apikey=790af7bc`;
    fetch(api_pesquisa)

        .then(function (response) {
            return response.json();
        }
        )
        .then(function (data) {
            if(data.Response == 'False'){
                console.log(data);
                document.getElementById("descricao").innerHTML = "Filme não encontrado! Digite novamente";
                document.getElementById("titulo").innerHTML = "";
                document.getElementById("sinopse").innerHTML = "";
                document.getElementById("duracao").innerHTML = "";
                document.getElementById("tipo").innerHTML = "";
                document.getElementById("ano").innerHTML = "";
                document.getElementById("diretor").innerHTML = "";
                document.getElementById("escritor").innerHTML = "";
                document.getElementById("nota").innerHTML = "";
                document.getElementById("banner").style.backgroundImage = `url(choro.png)`;


        }   else{
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
        }}
        )
}