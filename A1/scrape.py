import pandas as pd
from bs4 import BeautifulSoup
import requests

def pegar_html(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o html e retorna uma string 
    referente a página dada pela url

	:param url: Link da página da internet que se deseja buscar o html
	:url type: str
	:return: Texto do html do link dado
	:r type: str
	'''

    texto_html = requests.get(url)
    return texto_html.text

def pegar_letra(url: str):
    '''
	A função recebe um url do site lyrics.com, busca a letra da música que está presente
    nesse html e retorna uma string referente a letra dessa música

	:param url: Link da página da música
	:url type: str
	:return: letra da música
	:r type: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    letra = soup.find('pre', id='lyric-body-text')
    
    try:
        return letra.text
    except:
        print('Letra não encontrada')

def pegar_letras_musicas_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca as letras de todas as músicas
    desse album e retorna uma lista com essas músicas

	:param url: Link da página do álbum escolhido
	:url type: str
	:return: Letras das músicas do álbum
	:r type: list
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_letras = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_letra' para pegar a letra de cada uma das músicas
        for a in links:
            letra_album = "https://www.lyrics.com/" + a['href']
            print('procurando letra no link: ', "https://www.lyrics.com/" + a['href'])

            #O site usado dá um erro em momentos aleatórios onde não há conteúdo no link
            #Para resolver esse problema usaremos um while, toda vez que o site estiver
            #Vazio o programa fará a busca novamente, corrigindo o problema.
            verso = None
            while verso == None:
                verso = pegar_letra(letra_album)

            #Removeremos da letra os '\n' '\r' e sinalização de refrão '[Chorus:]' mantendo apenas a letra da música
            lista_letras.append(verso.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))

        return lista_letras

def pegar_titulo(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o nome da música que está
    presente nesse link o retorna

	:param url: Link da página da música
	:url type: str
	:return: Título da música
	:r type: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    titulo = soup.find('h1', id='lyric-title-text')
    try:
        return titulo.text
    except:
        print('erro')

def pegar_titulos_musicas_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca os títulos de todas as músicas
    desse album e retorna uma lista com esses títulos

	:param url: Link da página do álbum escolhido
	:url type: str
	:return: Títulos das músicas do álbum
	:r type: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_titulos = []

    #semelhante à função 'pegar_letras_musicas_album' dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_titulo' para pegar a letra de cada uma das músicas
        for a in links:
            letra_album = "https://www.lyrics.com/" + a['href']
            print('procurando título no link: ', "https://www.lyrics.com/" + a['href'])

            #Uso do while para evitar o erro da página vazia novamente
            titulos = None
            while titulos == None:
                titulos = pegar_titulo(letra_album)

            lista_titulos.append(titulos.replace('\n', ' ').replace('\r', '').replace('[Chorus:] ', ''))
        return lista_titulos

def pegar_ano(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o ano de lançamento da música que está presente
    nesse html e retorna uma string referente ao seu ano de lançamento
    
	:param url: Link da página da música
	:url type: str
	:return: Ano de lançamento
	:r type: str
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    tempo_ano = soup.findAll('dd', attrs={'class': 'dd-margin'})

    tempo_ano_list = []
    for item in tempo_ano:
        tempo_ano_list.append(item)
    try:
        tempo = tempo_ano_list[0]
    except:
        tempo = None
    
    try:
        return tempo.text
    except:
        return None

def pegar_ano_musicas_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o tempo de todas as músicas
    desse álbum e retorna uma lista com esses tempos

	:param url: Link da página da música
	:url type: str
	:return: Tempo das músicas do álbum
	:r type: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_tempos = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_letra' para pegar a letra de cada uma das músicas
        for a in links:
            tempo_album = "https://www.lyrics.com/" + a['href']
            print('procurando tempo no link: ', "https://www.lyrics.com/" + a['href'])
            
            time = pegar_ano(tempo_album)
            lista_tempos.append(time)

    return lista_tempos
        

def pegar_titulo_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o tempo de todas as músicas
    desse álbum e retorna uma lista com esses tempos

	:param url: Link da página da música
	:url type: str
	:return: Tempo das músicas do álbum
	:r type: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.find('h1')

    titulo_album = album.text
    return titulo_album.replace(' Album', '')

def pegar_compositores(url: str):
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    detalhes = soup.find('div', attrs={'class': 'lyric-credits'})
    
    itens = detalhes.find('p', attrs={'class': False})
    compositores = itens.text
    
    return compositores.replace('Written by: ', '')

def pegar_compositores_musicas_album(url: str):
    '''
	A função recebe um url do site lyrics.com, busca o tempo de todas as músicas
    desse álbum e retorna uma lista com esses tempos

	:param url: Link da página da música
	:url type: str
	:return: Tempo das músicas do álbum
	:r type: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_compositores = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_letra' para pegar a letra de cada uma das músicas
        for a in links:
            compositores_album = "https://www.lyrics.com/" + a['href']
            print('procurando compositores no link: ', "https://www.lyrics.com" + a['href'])
            
            compositores = pegar_compositores(compositores_album)
            lista_compositores.append(compositores)
    return lista_compositores

def pegar_link_youtube(url: str):
    '''
	A função recebe um url do site lyrics.com, busca a letra da música que está presente
    nesse html e retorna uma string referente a letra dessa música

	:param url: Link da página da música
	:url type: str
	:return: letra da música
	:r type: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    views = soup.find('div', class_='youtube-player')['data-id']
    return views

def pegar_visualizacoes(url: str):
    '''
	A função recebe um url do site lyrics.com, busca a letra da música que está presente
    nesse html e retorna uma string referente a letra dessa música

	:param url: Link da página da música
	:url type: str
	:return: letra da música
	:r type: str
	'''

    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    try:
        views = soup.find("meta", itemprop="interactionCount")["content"]
        return views
    except:
        return None

def pegar_visualizacoes_musicas_album(url:str):
    '''
	A função recebe um url do site lyrics.com, busca o tempo de todas as músicas
    desse álbum e retorna uma lista com esses tempos

	:param url: Link da página da música
	:url type: str
	:return: Tempo das músicas do álbum
	:r type: list
	'''
    soup = BeautifulSoup(pegar_html(url), 'html.parser')
    album = soup.findAll('table', attrs={'class': 'table tdata'})

    lista_visualizacoes = []

    #dentro do link do album buscaremos todos os links que levam as suas músicas
    for div in album:
        links = div.find_all('a')
        #Ao pegar todos esses links usaremos a função 'pegar_letra' para pegar a letra de cada uma das músicas
        for a in links:
            links_musicas_album = "https://www.lyrics.com/" + a['href']
            
            link = None
            while link == None:
                link = pegar_link_youtube(links_musicas_album)
                print('Pegando link do youtube: ', link)
            

            visualizacoes = pegar_visualizacoes('http://youtube.com/watch?v='+link)
            print('Pegando views no link ', 'http://youtube.com/watch?v='+link)
            try:
                lista_visualizacoes.append(visualizacoes)
            except:
                lista_visualizacoes.append('None')
    return lista_visualizacoes

def gerar_dataframe_album(url: str):
    '''
    Usando as funções criadas obteremos um dataframe de um álbum dado a partir de
    um url do site lyrics.com
    
	:param url: Link da página da música
	:url type: str
	:return: Dataframe do álbum
	:r type: DataFrame
    '''
    print('O processo pode demorar um pouco dependendo da quantidade de músicas. Aguarde...')
    dados = {'Ano':pegar_ano_musicas_album(url),'Compositores':pegar_compositores_musicas_album(url), 'letra':pegar_letras_musicas_album(url)}
    df = pd.DataFrame(data=dados, index=[pegar_titulos_musicas_album(url)])
    print(df)
    return df

def gerar_dataframe_banda(url_list: list):
    '''
    Usando as funções criadas e recebendo como parâmetro uma lista de links obteremos
    um dataframe de uma banda dado a partir da lista de urls do site lyrics.com
    
	:param url_list: Lista de links dos albuns da banda
	:url_list type: list
	:return: Dataframe da banda
	:r type: DataFrame
    '''
    lista_titulos = []
    lista_letras = []
    lista_anos = []
    lista_compositores = []
    lista_titulo_album = []
    lista_visualizacoes = []
    for album in url_list:
        lista_titulos += pegar_titulos_musicas_album(album)
        lista_letras += pegar_letras_musicas_album(album)
        lista_anos += pegar_ano_musicas_album(album)
        lista_compositores += pegar_compositores_musicas_album(album)
        lista_visualizacoes += pegar_visualizacoes_musicas_album(album)
        numero_faixas = len(pegar_letras_musicas_album(album))
        lista_titulo_album += [pegar_titulo_album(album)]*numero_faixas
    dados = {'Ano':lista_anos, 'compositores':lista_compositores, 'visualizacoes':lista_visualizacoes, 'letra':lista_letras}
    indice = [lista_titulo_album, lista_titulos]
    df = pd.DataFrame(data=dados, index=indice)
    print(df)
    return df