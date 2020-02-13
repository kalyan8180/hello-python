
#Note: if you edit this file on Windows OS, please be sure to use
#UNIX style new line code, i mean 0xA (LF). Do not save 0xD 0xA!

log() {
    echo $* >&2
}

touch "user_opt_quit.flag"
