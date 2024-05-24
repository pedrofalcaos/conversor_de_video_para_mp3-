Conversor MP4 para MP3 🎵
Este é um programa simples que converte arquivos MP4 para MP3 usando uma interface gráfica amigável. Ele foi desenvolvido em Python e utiliza as bibliotecas tkinter e moviepy.

Funcionalidades
Seleção de arquivos MP4 de entrada.
Seleção do local e nome do arquivo MP3 de saída.
Conversão de MP4 para MP3.
Mensagens de confirmação com emojis.
Opção para realizar outra conversão ou encerrar o programa.
Pré-requisitos
Python 3.x instalado.
moviepy e tkinter bibliotecas instaladas.
ffmpeg instalado e configurado no PATH do sistema.
Instalação
Passo 1: Instale o Python
Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode baixar o instalador do Python em python.org.

Passo 2: Instale as bibliotecas necessárias
Use o pip para instalar as bibliotecas necessárias:

sh
Copiar código
pip install moviepy
pip install imageio[ffmpeg]
Passo 3: Instale o ffmpeg
Baixe o ffmpeg do site oficial.
Extraia o conteúdo do arquivo baixado para uma pasta, por exemplo, C:\ffmpeg.
Adicione o caminho da pasta bin do ffmpeg ao PATH do sistema:
Abra o Painel de Controle e vá para Sistema e Segurança > Sistema > Configurações avançadas do sistema.
Clique no botão Variáveis de Ambiente.
Em Variáveis do sistema, encontre a variável Path e edite-a.
Adicione o caminho da pasta bin do ffmpeg, por exemplo, C:\ffmpeg\bin.
Uso
Clone ou baixe este repositório.
Execute o script convert_mp4_to_mp3.py:
sh
Copiar código
python convert_mp4_to_mp3.py
Use a interface gráfica para selecionar o arquivo MP4 de entrada e o local de saída do arquivo MP3.
Clique no botão "Converter 🎶" para iniciar a conversão.
Após a conversão, uma mensagem de confirmação será exibida mostrando o local onde o arquivo MP3 foi salvo.
Você será perguntado se deseja realizar outra conversão. Se optar por "Sim", os campos de entrada serão limpos. Se optar por "Não", o programa será encerrado.
