package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"

	"github.com/chzyer/readline"
	"github.com/muesli/termenv"
)

func printer(s string, string_type string) {
	p := termenv.ColorProfile()
	styled := termenv.String(s)
	switch string_type {
	case "welcome":
		fmt.Println(styled.Foreground(p.Color("#FF2FF2")))

	case "error":
		fmt.Println(styled.Foreground(p.Color("#FF0000")))

	case "note":
		fmt.Println(styled.Foreground(p.Color("#FFFF00")))

	default:
		fmt.Println(styled.Foreground(p.Color("#00FF00")))
	}
}

func buildPrompt() string {
    user, _ := exec.Command("whoami").Output()
    userstring := string(user[:len(user)-1])

    host, err := os.LookupEnv("HOST")
    if err {host = "Tutor"}

    cwd, _ := os.Getwd()


    return userstring + "@" + host + "in" + cwd
}

func main() {
    rl, err := readline.New(buildPrompt() + " >")
	if err != nil {
		panic(err)
	}
	defer rl.Close()

	termenv.ClearScreen()

	printer("Welcome to Chistole", "welcome")

	time.Sleep(1 * time.Second)

	printer("This lesson will be about", "")
    printer(`Lorem ipsum dolor sit amet, officia excepteur ex fugiat
    reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse
    exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit
    nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor
    minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure
    elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor
    Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing
    id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua
    reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate
    laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa
    duis.`, "")

	// time.Sleep(4 * time.Second)
    printer("\n\nWhen you are ready press any key to begin", "note")
    fmt.Scanln() // Any key
    
	termenv.ClearScreen()

	printer("Welcome to the shell", "")

    //Readline loop
	for {
		line, err := rl.Readline()
		if err != nil { // io.EOF
			break
		}
		println(line)
	}
}
