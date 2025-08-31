# CollegeFunctions - C Project

Este é um projeto C que implementa funções matemáticas úteis para conversão de bases e operações binárias.

## Funcionalidades

- **Conversão de Bases**: Conversão entre diferentes sistemas numéricos (binário, decimal, hexadecimal)
- **Operações Binárias**: Soma e subtração de números binários
- **Verificação**: Validação se uma string representa um número binário válido

## Estrutura do Projeto

```
C/
├── main.c          # Arquivo principal com todas as funções
├── Makefile        # Arquivo de compilação para MinGW (Windows)
├── README.md       # Este arquivo
└── .gitignore      # Arquivo de exclusão do Git
```

## Requisitos

- **Windows** com Qt MinGW instalado
- **GCC** via Qt MinGW (versão 13.1.0 ou superior)
- **mingw32-make** incluído no Qt MinGW

## Instalação

1. Certifique-se de ter o Qt instalado com MinGW
2. O caminho padrão é: `C:\Qt\Tools\mingw1310_64\bin`

## Compilação

### Usando o Makefile (Recomendado)

```bash
# Limpar arquivos de compilação anteriores
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe clean

# Compilar em modo debug (com símbolos de debug)
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe debug

# Compilar em modo release (otimizado)
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe release

# Compilar e executar
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe run

# Executar testes
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe test

# Mostrar ajuda
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe help
```

### Compilação Manual

```bash
# Configurar o ambiente
set PATH=C:\Qt\Tools\mingw1310_64\bin;%PATH%

# Compilar
gcc -Wall -Wextra -O2 -std=c11 -o main.exe main.c

# Executar
main.exe
```

## Funções Disponíveis

### `bool isBinary(const char *str)`
Verifica se uma string contém apenas '0' e '1'.

### `int sumBinary(int number, int number2, bool c2)`
Soma dois números binários de 8 bits.

### `int subtractbinary(int number, int number2, int c)`
Subtrai dois números binários com opções de complemento.

### `int tobase(int number, int base)`
Converte um número decimal para qualquer base (2-36).

### `int toBinary(int number)`
Converte um número decimal para binário.

### `int convertBase(int number, int base, int baseto)`
Converte entre diferentes bases usando decimal como intermediário.

## Exemplo de Uso

O programa principal (`main.c`) já inclui um exemplo básico que imprime:
```
CODE STARTED
Hello, my friends!!!!
```

## Solução de Problemas

### Erro: "gcc: fatal error: cannot execute 'cc1'"
Este erro ocorre quando o MinGW não está corretamente configurado no PATH. Use:
```bash
set PATH=C:\Qt\Tools\mingw1310_64\bin;%PATH%
```

### Erro: "mingw32-make.exe não é reconhecido"
Use o caminho completo para o executável:
```bash
C:\Qt\Tools\mingw1310_64\bin\mingw32-make.exe
```

## Comandos do Makefile

- `make clean`: Remove arquivos temporários (*.o, *.exe, *.out)
- `make debug`: Compila com símbolos de debug
- `make release`: Compila com otimizações
- `make run`: Compila e executa o programa
- `make test`: Executa testes básicos
- `make help`: Mostra todos os comandos disponíveis

## Status do Projeto

✅ **COMPILAÇÃO FUNCIONAL** - O projeto compila com sucesso usando MinGW
✅ **EXECUÇÃO FUNCIONAL** - O programa executa corretamente
✅ **MAKEFILE FUNCIONAL** - Todas as opções do Makefile funcionam
✅ **DOCUMENTAÇÃO ATUALIZADA** - README.md completo e atualizado

## Autor
- **Pedro Morato Lahoz**

## Licença
Este projeto é para fins educacionais.