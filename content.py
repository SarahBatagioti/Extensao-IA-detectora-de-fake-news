import browser

# O código abaixo será executado assim que a página do Chrome for carregada
def main():
    # Lê o texto da página e armazena em uma variável
    page_text = browser.document.body.innerText

    # Essa linha obtém o texto contido na tag "body" da página atual e o armazena na variável "page_text". 
    # A propriedade "innerText" é usada para obter o texto dentro da tag, sem as tags HTML. 
    
    # Exibe o texto na console do Chrome
    # print(page_text) 
    browser.console.log(page_text)

    # Exemplo de como enviar os dados para outra extensão
    browser.window.postMessage(page_text, '*')

# Registra a função 'main' para ser executada assim que a página for carregada
browser.document <= browser.html("""
    <script>
        window.onload = function() {
            Brython(0, [], function() {
                py_import('main').main();
            });
        };
    </script>
""")

# Essa linha registra uma função para ser executada quando a página é carregada. 
# A função usa o Brython para carregar e executar o código Python na página. 
# Quando a página é carregada, o Brython é iniciado e a função "main" é executada, conforme definido anteriormente.

# Portanto, no geral, o código lê o texto da página atual e o exibe no console do navegador. 
# Também envia o conteúdo da página como uma mensagem para outras extensões que estiverem 
# ouvindo no evento "message". O código é executado quando a página é carregada usando o Brython.
