# ENVIANDO MENSAGENS PARA MULTIPLOS NUMEROS
 
 Script de envio automatizado de mensagens de whatsapp usando
 a biblioteca Python Yowsup.
 Para conseguir usar, voce vai precisa alem de instalar a biblioteca
 fazer o procedimento de registro para pegar a senha referente
 ao seu numero no whatsapp.

 Por isso, consulte a documençao do Yowsup
 https://github.com/tgalal/yowsup/wiki		

 Os dois arquivos, n.csv e m.csv contem respectivamente 
 os numeros pras quais serao enviadas mensagens e os 
 modelos de mensagens a serem enviados

 Para evitar ter o numero bloqueado pelo whatsapp, 
 duas precauçoes sao tomadas

 1 - definir um intervalo aleatorio entre o envio de cada mensagem. 
 caso contrario, as mensagens sairao com um mesmo horario de envio,
 notadamente um comportamento nao humano que acarretara em bloqueio 
 
 2 - definir modelos diferentes de mensagens. enviar a mesma mensagem
 para milhares de numeros desconhecido tambem configura
 um comportamento nao humano, por isso uso modelos diferentes da mesma
 mensagem. no arquivo m.csv ficam os modelos, e a funçao getMessages()
 retorna aleatoriamente um dos modelos contidos no arquivo

