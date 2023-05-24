# Programa de Envio de Notícias via Bot Telegram

Este programa consiste em um código Python que utiliza a biblioteca feedparser para obter notícias de um feed RSS do site OLiberal.com IA. O objetivo do programa é enviar as notícias mais recentes para um chat específico no Telegram, utilizando um bot.

# Como funciona o programa

1 - O programa utiliza a biblioteca feedparser para fazer o parsing do feed RSS do site OLiberal.com IA. A URL do feed RSS é definida na variável rss_url.

2 - O programa faz uso da biblioteca requests para realizar requisições HTTP.

3 - É utilizado o módulo logging para configurar logs de depuração.

4 - O token do bot Telegram é definido na variável bot_token.

5 - O arquivo de notícias postadas é criado com base na data atual e é armazenado na variável file_name.

6 - O programa verifica se o arquivo de notícias postadas existe. Se existir, as notícias já enviadas são carregadas para a lista sent_news.

7 - A função send_message() é definida para enviar mensagens para o chat específico no Telegram. É utilizado o token do bot, o ID do chat e a mensagem como parâmetros.

8 - A função add_to_sent_news() é definida para adicionar o link da nova notícia ao arquivo de notícias postadas.

9 - O ID do chat específico é definido na variável chat_id.

10 - A função send_news() é definida para enviar as notícias mais recentes do feed RSS para o chat específico no Telegram.

- A função faz o parsing do feed RSS utilizando feedparser.
- Para cada notícia, verifica se o link já foi enviado anteriormente. Se não tiver sido, a notícia é enviada para o chat específico 
- utilizando a função send_message() e o link é adicionado ao arquivo de notícias postadas utilizando a função add_to_sent_news().

11 - É definida a periodicidade de envio de notícias utilizando a biblioteca schedule. No exemplo, o programa é configurado para enviar notícias a cada 1 minuto, chamando a função send_news(). O bot_token, chat_id e rss_url são passados como argumentos.

12 - A função create_new_file() é definida para criar um novo arquivo de notícias postadas a cada 15 dias. Ela atualiza o nome do arquivo, cria um novo arquivo vazio e reinicia a lista de notícias enviadas.

13 - É definida a periodicidade de criação de novo arquivo de notícias utilizando a função schedule. No exemplo, o programa é configurado para criar um novo arquivo a cada 15 dias, chamando a função create_new_file().

14 - O programa executa um loop infinito onde verifica e executa as tarefas agendadas pela biblioteca schedule. A função run_pending() é chamada para executar as tarefas agendadas. O programa aguarda 1 segundo entre cada iteração do loop.

# Como usar o programa

1 - Certifique-se de ter o Python instalado em seu ambiente de desenvolvimento.

2 - Clone o repositório contendo o programa ou copie o código para o seu projeto.

3 - Certifique-se de ter um bot Telegram configurado e obtenha o token do bot.

4 - Defina o token do bot na variável bot_token.
