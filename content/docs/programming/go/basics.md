# Go Basics

## Project template

Set up:

```sh
mkdir example-project
cd ./example-project
go mod init
```

`./.gitignore`:

```gitignore
```

`./Makefile`:

```make
.PHONY: clean build test

clean:
    echo "Not implemented"

build:
    echo "Not implemented"

test:
    echo "Not implemented"

install:
    echo "Not implemented"
```

`./main.go`:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Run project:

```sh
go run .
```

## Taskfile

- [Task file home](https://taskfile.dev/)
- [Task file repository](https://github.com/go-task/task)