﻿## Análise Exploratória:
Durante a pesquisa inicial, descobrimos que a banda possui 6 álbuns gravados em estúdio, uma coletânea, um álbum ao vivo, alguns singles e alguns EPs. O álbum ao vivo não traz nenhuma música inédita. Da mesma forma, os singles e EPs advêm dos álbuns gravados em estúdio. Isto é, o único material realmente inédito são os álbuns de estúdio. Assim, escolhemos considerar apenas os álbuns:
	
<ol>
	<li>Appetite for Destruction;</li>
	<li>G N' R Lies;</li>
	<li>Use Your Illusion I;</li>
	<li>Use Your Illusion II;</li>
	<li>"The Spaghetti Incident?";</li>
	<li>Chinese Democracy.</li>
</ol>

Para o grupo 3 de perguntas, escolhemos as seguintes:
<ol>
	<li>Compositores mais comuns;</li>
	<li>Música mais popular por compositor;</li>
	<li>Ano em que a banda recebeu mais prêmios.</li>
</ol>

<br>

## Planejamento dos Dataframes:
Sabendo as perguntas que deveriam ser respondidas, listamos as informações que precisaríamos coletar e as organizamos no Diagrama Entidade-Relacionamento (Figura 1). A partir deste, criou-se o Diagrama do Modelo Relacional (Figura 2), que norteou a produção dos dataframes. Ambos diagramas foram elaborados com a ferramenta <a href="https://erdplus.com/">ERDPlus</a>.

![Ops! Imagem não encontrada.](Figuras/Figura%201%20-%20Diagrama%20Entidade-Relacionamento.png "Figura 1 - Diagrama Entidade-Relacionamento")
*Figura 1 - Diagrama Entidade-Relacionamento*

<br>

![Ops! Imagem não encontrada.](Figuras/Figura%202%20-%20Diagrama%20do%20Modelo%20Relacional.png "Figura 2 - Diagrama do Modelo Relacional")
*Figura 2 - Diagrama do Modelo Relacional*

<br>

É importante notar que, embora uma mesma música possa estar em vários álbuns, cada nova versão pressupõe mudanças na performance. A intonação, o tempo, as intervenções durantes as pausas, enfim, a emoção transmitida muda a cada regravação. Por exemplo, You're Crazy de Appetite for Destruction é consideravelmente mais acelerada e agressiva que a sua versão em G N' R Lies. O próprio timbre do Axl Rose é mais grave no segundo álbum. Por isso, decidimos considerar versões diferentes da mesma música como músicas diferentes.