# Projeto Final  Coderhouse - Pipeline de Dados com Python
Este repositório foi criado para entrega do projeto final do curso de Python da Coderhouse. Ele contém um exemplo de código Python que realiza a coleta, transformação e armazenamento de dados de diferentes fontes usando, principalmnte, a biblioteca Pandas e a API do BrasilAPI. O código foi desenvolvido para criar um pipeline de dados que inclui a extração de dados de feriados nacionais, informações de corretoras ativas no Brasil e taxas de juros vigentes no país. Os dados coletados são então transformados e armazenados em um banco de dados SQLite para fácil acesso em etapas posteriores da análise.

# Descrição das Etapas
1. Coleta de Dados
   
    O código utiliza a biblioteca requests para fazer solicitações à API do BrasilAPI. Três conjuntos de dados são coletados:

   . Feriados Nacionais: Dados sobre feriados nacionais em um ano específico (no exemplo, 2023).

    . Corretoras Ativas: Informações sobre corretoras ativas no Brasil, incluindo nome, e-mail, município e telefone.

    . Taxas de Juros Vigentes: Dados sobre as taxas de juros vigentes no Brasil.

3. Transformação de Dados
   
    Cada conjunto de dados é submetido a um processo de limpeza e transformação para garantir que estejam prontos para análise. As etapas de transformação incluem:

    . Alteração de nomes de colunas para facilitar a compreensão.
   
    . Formatação de datas.
   
    . Tradução de valores para português.
   
    . Limpeza de dados nulos.
   
    . Outras transformações específicas para cada conjunto de dados.

5. Armazenamento de Dados.

    Os conjuntos de dados transformados são armazenados em um banco de dados SQLite chamado 'coderhouse.db' usando a biblioteca sqlalchemy. Isso permite que os dados sejam facilmente acessados e consultados em etapas posteriores da análise.

# Requisitos:

   . Python 3.x
   
   . Bibliotecas: Pandas, requests, plyer, sqlalchemy

Como Executar:

Para executar o código e criar o banco de dados, siga os passos abaixo:

. Certifique-se de que o Python e as bibliotecas necessárias estejam instaladas.

. Execute o script Python.
O banco de dados 'coderhouse.db' será criado e conterá as tabelas 'feriados_nacionais', 'corretoras_ativas' e 'taxas' com os dados coletados e transformados.

Este código é um exemplo de pipeline de dados básico e pode ser estendido para incluir mais fontes de dados e transformações específicas ao seu projeto. Certifique-se de entender os dados coletados e adaptar o código conforme necessário.  
