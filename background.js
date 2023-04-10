let lerBotao = document.getElementById('ler');
let pararBotao = document.getElementById('parar');
let textoTextarea = document.getElementById('texto');

let obterTexto = () => {
  fetch('http://127.0.0.1:5000/texto')
    .then(response => response.json())
    .then(data => {
      textoTextarea.value = data.texto;
    });
};

lerBotao.addEventListener('click', obterTexto);
pararBotao.addEventListener('click', () => {
  textoTextarea.value = '';
});
