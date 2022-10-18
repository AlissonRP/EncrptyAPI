## API para encriptação
Nesse projeto foi desenvolvido uma API que ao enviar uma mensagem, ela será retornada na forma encriptada, onde os métodos de encriptação são os seguintes:


<details>
  <summary markdown="span">Informações de alto risco!</summary>
  
### Como a  mensagem é "encriptada"

* Converte toda mensagem para lower case
* Converte as subsequentes letras da seguinte maneira:
   * `a -> 0`
   * `e -> substituir por & ou $`
   * `i -> 4`
   * `u -> 6`
   * `o -> 8`
   * `ç -> @`
* As letras restantes serão modificadas pela próxima somada 7 posições no alfabeto, e as últimas evidentemente, retornam para o começo do alfabeto, assim as vogais vão reaparecer, mas só quem sabes do passo 1 pode deduzir que algumas vogais foram substituídas.
* As letras `aemptr` tornam-se maiúsculas pq sim
* Vírgulas são substituídas por `#`, e é adicionado `#` no fim do texto para gerar ruído.


</details>


### Como usar

```docker
docker compose build 
docker compose up
```


<details>
  <summary markdown="span">Breve Exemplo</summary>

Output: `8 4Tws0j0c&s wy8M&zz8y T8y40yAf# c04 z& &uj8uAy0y j8T zo&ys8jR o8sT&z u8 o8A&s 4uc4k40#`

Input: `O implacavel professor Moriarty, vai se encontrar com Sherlock Holmes no Hotel Invidia`

</details>
* O desenvolvimento foi inspirado em um livro de Moriarty, a.k.a arqui-inimigo de Sherlock Holmes.
<p align="center"><img align="center" src="https://media.tenor.com/LmkFlYBYuC4AAAAC/moriarty-the-patriot-yuukoku-no-moriarty.gif" height="210px" width="590"/></p>