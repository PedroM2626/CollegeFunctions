# CollegeFunctions

## Descrição
Este repositório contém uma coleção de funções em C desenvolvidas durante o curso de faculdade. O projeto serve como um espaço para praticar e implementar diversos algoritmos e operações matemáticas, especialmente focados em operações com números binários e conversão entre bases numéricas.

## Funcionalidades

O projeto inclui as seguintes funções:
- **isBinary**: Verifica se uma string contém apenas caracteres '0' e '1' (binários).
- **sumBinary**: Realiza a soma de dois números binários de 8 bits.
- **subtractbinary**: Subtrai dois números binários usando complemento a 1 ou complemento a 2.
- **tobase**: Converte um número decimal para uma base específica.
- **toBinary**: Converte um número decimal para binário.
- **convertBase**: Converte um número de uma base para outra (suporta bases 2, 10 e 16).

## Estrutura do Projeto

```
CollegeFunctions/
├── C/
│   ├── main.c
│   ├── main.exe
│   ├── Makefile
│   ├── .gitignore
│   ├── .env
│   ├── .env.example
│   └── README.md
└── README.md
```

## Linguagens e Expansão
Este repositório será expandido para incluir implementações em outras linguagens de programação além de C.
- As pastas serão organizadas por linguagem (por exemplo: C/, Python/, Java/, JavaScript/, C++/).
- Repositório no GitHub: https://github.com/PedroM2626/CollegeFunctions

## Como Usar

### 1. Clone este repositório:
```bash
git clone https://github.com/PedroM2626/CollegeFunctions.git
```

### 2. Navegue até a pasta do projeto:
```bash
cd CollegeFunctions/C
```

### 3. Configure variáveis de ambiente (opcional):
Crie um arquivo `.env` baseado no `.env.example` se necessário.

### 4. Compile o código (C e C++):
Utilize o Makefile para compilar todos os arquivos C e C++ automaticamente:
```bash
make
```
Isso irá gerar os executáveis `main_c.exe` (para C) e `main_cpp.exe` (para C++ se houver arquivos .cpp).

### 5. Execute o programa:
Para rodar o executável C:
```bash
./main_c.exe
```
Para rodar o executável C++ (se existir):
```bash
./main_cpp.exe
```

### 6. Limpe arquivos de build:
```bash
make clean
```

### 7. Testes
O alvo `make test` está disponível para rodar testes (adapte conforme necessário).

## Variáveis de Ambiente
- Utilize o arquivo `.env.example` como base para criar seu `.env`.
- Exemplo:
```
API_KEY=sua_chave_aqui
```

## Desenvolvimento
Este projeto está em constante desenvolvimento, com novas funções sendo adicionadas conforme necessário para os estudos acadêmicos. Algumas funções ainda estão incompletas ou em processo de implementação.

## Autor
- **Pedro Morato Lahoz**

## Licença
Este projeto é de uso livre para fins educacionais.