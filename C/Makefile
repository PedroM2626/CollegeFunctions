# Makefile para compilar C e C++

CC=gcc
CXX=g++
CFLAGS=-Wall -Wextra -O2
CXXFLAGS=-Wall -Wextra -O2
SRC_C=$(wildcard *.c)
SRC_CPP=$(wildcard *.cpp)
OBJ_C=$(SRC_C:.c=.o)
OBJ_CPP=$(SRC_CPP:.cpp=.o)
EXEC_C=main_c.exe
EXEC_CPP=main_cpp.exe

all: $(EXEC_C) $(EXEC_CPP)

$(EXEC_C): $(OBJ_C)
	$(CC) $(CFLAGS) -o $@ $^

$(EXEC_CPP): $(OBJ_CPP)
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f *.o *.exe *.out

test:
	@echo "(Adicione comandos de teste aqui)"
