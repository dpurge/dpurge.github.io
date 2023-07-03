# CGI

## Simple CGI app

```go
package main

import (
    "bytes"
    "fmt"
    "os"
    "time"
)

func main() {
    var buf bytes.Buffer

    fmt.Fprintf(&buf, "Time at %s: %s\n",
        os.Getenv("SERVER_NAME"),
        time.Now().Format(time.RFC1123))
        
    fmt.Println("Content-type: text/plain")
    fmt.Printf("Content-Length: %d\n\n", buf.Len())
    buf.WriteTo(os.Stdout)
}
```