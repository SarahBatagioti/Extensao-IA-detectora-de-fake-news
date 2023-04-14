// Recebe as informações enviadas pela extensão em Python
window.addEventListener('message', function(event) {
  if (event.source != window) return;

  // Exibe as informações na console do Chrome
  console.log(event.data);
});

//exibir o texto na console do Chrome
console.log("TESTE");

// Adiciona um ouvinte de mensagem para receber as informações coletadas do Python
window.addEventListener('message', function (event) {
    // Verifica se o texto é falso
    if (!event.data.texto) {
        // Abre o pop-up
        chrome.windows.create({
            url: chrome.runtime.getURL('popup.html'),
            type: 'popup',
            width: 200,
            height: 100
        });
    }
});
