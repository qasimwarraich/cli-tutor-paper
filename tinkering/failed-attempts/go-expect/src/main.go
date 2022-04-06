package main

import (
	"log"
	"os"
	"os/exec"

	"github.com/Netflix/go-expect"
)

func main() {
    

	c, err := expect.NewConsole(expect.WithStdout(os.Stdout), expect.WithStdin(os.Stdin))
	if err != nil {
		log.Fatal(err)
	}
	defer c.Close()

	cmd := exec.Command("bash")
	cmd.Stdin = c.Tty()
	cmd.Stdout = c.Tty()
	cmd.Stderr = c.Tty()

	go func() {
		c.ExpectEOF()
	}()

	err = cmd.Start()
	if err != nil {
		log.Fatal(err)
	}


	err = cmd.Wait()
	if err != nil {
		log.Fatal(err)
	}

    c.SendLine("Loooool")

    
}
