## API para encriptcao
Aqui foi desenvolvido uma API utilizando Flask.

Ao enviar uma mensagem, ela será retornada na forma encriptada, onde os métodos de encriptacao sao os seguintes:


<details>
  <summary markdown="span">Informacoes de alto risco!</summary>
### Informacão de como a  mensagem é "encriptada"
* converte toda mensagem pra lower case
* Converte as vogais para números pares, sendo eles
 * a -> 0 (talvez a seja mapeada para 3 ou 5 para gerar ruído)
 * e -> substituir por & ou $
 * i -> 4
 * u -> 6
 * o -> 8
 * Ç -> @
* As outras letras serão modificidas pela próxima somada  7 posicões no alfabeto, e as últimas evidentemente voltão para o comeco, assim as vogais vão voltar a aparecer, mas só quem sabes do passo 1 pode deduzir que algumas vogais foram substituidas.
* as letras `aemptr` tornam-se maisculas pq sim
* Vírgulas são substituidas por #, e é adicionado #  e fim da frase para gerar ruído
</details>


* O desenvolvimento foi inspirado em um livro do Moriarty, aka arqui inimigo do Sherlock Holmes.
  
<p align="center"><img align="center" src="https://moriarty-the-patriot.fandom.com/fr/wiki/William_Moriarty" height="310px" width="690"/></p>
