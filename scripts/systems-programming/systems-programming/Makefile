CC = gcc
CFLAGS = -Wall -Wextra -Werror -pthread
SRCS = main.c
OBJS = $(SRCS:.c=.o)
EXEC = threaded-sort

all: $(EXEC)

$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) -o $(EXEC) $(OBJS)

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS)

clean:
	rm -f $(OBJS) $(EXEC)

.PHONY: clean