## API para encriptação
Nesse projeto foi desenvolvido uma API que ao enviar uma mensagem, ela será retornada na forma encriptada, onde os métodos de encriptação sao os seguintes:


<details>
  <summary markdown="span">Informações de alto risco!</summary>
  
### Informação de como a  mensagem é "encriptada"

* Converte toda mensagem pra lower case
* Converte as vogais para números pares, sendo eles
 * a -> 0 
 * e -> substituir por & ou $
 * i -> 4
 * u -> 6
 * o -> 8
 * Ç -> @
* As outras letras serão modificadas pela próxima somada 7 posições no alfabeto, e as últimas evidentemente retornam para o começo, assim as vogais vão voltar a aparecer, mas só quem sabes do passo 1 pode deduzir que algumas vogais foram substituídas.
* as letras `aemptr` tornam-se maiúsculas pq sim
* Vírgulas são substituídas por #, e é adicionado # no fim da frase para gerar ruído

</details>


* O desenvolvimento foi inspirado em um livro do Moriarty, aka arqui inimigo do Sherlock Holmes.
  
<p align="center"><img align="center" src="https://media.tenor.com/LmkFlYBYuC4AAAAC/moriarty-the-patriot-yuukoku-no-moriarty.gif" height="310px" width="690"/></p>


### Como usar

```docker
docker compose build 
docker compose up
``` 