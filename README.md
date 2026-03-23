Opa galera!

Esse é um **projeto teste** que fiz. Como também trabalho com **edição de vídeos**, preciso fazer o download de **áudios em MP3 do YouTube**.

Mesmo existindo sites que fazem esse trabalho, muitos acabam deixando de funcionar com o tempo ou possuem **excesso de anúncios**.

Dessa forma, acabei criando esse **pequeno código em Python** que, pelo menos para mim, funciona perfeitamente.

Esse código é a primeira versão do projeto, talvez eu faça algumas alterações para que não precise de tantas dependências.

---

O que o projeto faz

- Faz o download do áudio de vídeos do YouTube
- Converte automaticamente para **MP3**
- Usa cookies para evitar bloqueios de algumas URLs
- Salva os arquivos em uma pasta local

---
Dependência importante

Este projeto **requer o FFmpeg instalado no sistema**, pois ele é responsável pela conversão do áudio para MP3.

Sem o FFmpeg, o download pode até ocorrer, mas a conversão falhará.

---
Alterações necessária
Na função "def mp3(url)" será necessária a alterações de 2 parâmetros

Serão eles:
"outtmpl": "caminho para onde os audios baixados vão /yt_mp3/audio/%(title)s.%(ext)s"
"cookiefile": "caminho do arquvio cookies.txt /yt_mp3/cookies.txt",

Você precisará informar o caminho para onde seus audios serão exportados, no parâmetro "outtmpl" e também informar no parâmetro "cookiefile", o cookie do seu navegador para que o yt não faça o bloqueio de alguns conteúdos.

---
Biblioteca utilizada

Este projeto utiliza a biblioteca:

- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)


- Além disso, você precisa de uma extensão no seu navegador para fornecer um arquivos de "cookies.txt"



