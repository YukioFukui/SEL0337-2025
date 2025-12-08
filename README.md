# SEL0337-2025
Alunos: 
  Enzo Yuko Fukui Palumbo - 13689441
  Reynaldo Thierry - 13825985

Logs de atualização se encontram no arquivo historico.txt

Prática 5
  Arquivos .py se encontram na pasta ScriptsPratica5.
Diagrama da montagem:
  <img width="528" height="341" alt="diagrama_montagem_p5" src="https://github.com/user-attachments/assets/df8127e5-a7a0-460f-88ec-ae7257338d6e" />

O código PWMLED.py executa um aumento de brilho cíclico do LED verde para três repetições.
O código blink.py executa um ciclo de liga e desliga do LED vermelho para cinco repetições.
O arquivo PWMLED.service faz com que PWMLED.py é executado ao iniciar a RaspiberryPi por meio do ExecStart. Daí o script então faz o ciclo de PWM três vezes e encerra, o encerramento por sua vez faz com que o script blink.py seja executado para então iniciar seu ciclo de liga/desliga do LED.
Utilizando o comando "sudo systemctl start PWMLED" para simular o início do serviço PWMLED e utilizando-se o comando "sudo systemctl status PWMLED" para ver seu funcionamento resulta na imagem abaixo, a qual indica que o serviço está ativo:
<img width="842" height="238" alt="status_ativo_corte" src="https://github.com/user-attachments/assets/744062d9-ad87-4a1e-84fb-f2232d35da9e" />
Quando o processo do blink.py encerra o serviço finalmente se encerra por completo:
<img width="962" height="319" alt="status_inativo_corte" src="https://github.com/user-attachments/assets/5ddda4e5-4b04-4326-aeb7-8adfa7354d70" />
