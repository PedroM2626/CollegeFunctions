# Makefile para C - Qt MinGW (Windows)
# Versão funcional e otimizada

CC = gcc
CFLAGS = -Wall -Wextra -O2 -std=c11
SOURCES = main.c
OBJECTS = $(SOURCES:.c=.o)
EXECUTABLE = main.exe

.PHONY: all clean run test help

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXECUTABLE)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	-del /Q *.o *.exe *.out 2>nul

run: $(EXECUTABLE)
	$(EXECUTABLE)

test: $(EXECUTABLE)
	@echo Executando testes...
	$(EXECUTABLE)
	@echo Testes concluidos!

help:
	@echo Comandos disponiveis:
	@echo   make          - Compila o programa
	@echo   make clean    - Remove arquivos temporarios
	@echo   make run      - Compila e executa
	@echo   make test     - Executa testes
	@echo   make help     - Mostra esta ajuda

# Builds especiais
debug: CFLAGS += -g -DDEBUG
debug: $(EXECUTABLE)
	@echo Build debug concluido!

release: CFLAGS += -DNDEBUG -O3
release: $(EXECUTABLE)
	@echo Build release concluido!
