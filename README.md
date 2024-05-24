# Conversor MP4 para MP3 🎵

Este é um programa simples que converte arquivos MP4 para MP3 usando uma interface gráfica amigável. Ele foi desenvolvido em Python e utiliza as bibliotecas `tkinter` e `moviepy`.

## Funcionalidades

- Seleção de arquivos MP4 de entrada.
- Seleção do local e nome do arquivo MP3 de saída.
- Conversão de MP4 para MP3.
- Mensagens de confirmação com emojis.
- Opção para realizar outra conversão ou encerrar o programa.

## Pré-requisitos

- Python 3.x instalado.
- `moviepy` e `tkinter` bibliotecas instaladas.
- `ffmpeg` instalado e configurado no PATH do sistema.

## Instalação

### Passo 1: Instale o Python

Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode baixar o instalador do Python em [python.org](https://www.python.org/downloads/).

### Passo 2: Instale as bibliotecas necessárias

Use o `pip` para instalar as bibliotecas necessárias:

```sh
pip install moviepy
pip install imageio[ffmpeg]
