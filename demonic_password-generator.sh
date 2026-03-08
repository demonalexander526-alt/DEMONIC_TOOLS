#!/bin/bash

# ============ цвет ============
RED="\e[31m"
GREEN="\e[32m"
CYAN="\e[36m"
MAGENTA="\e[35m"
RESET="\e[0m"


LENGTH=20
CHARS='A-Za-z0-9@#%+=!?$&*'

PASSWORD=$(tr -dc "$CHARS" </dev/urandom | head -c $LENGTH)


echo -e "${MAGENTA}========================================${RESET}"
echo -e "${GREEN}DEMONIC DIRECTORY ACTIVE :${RESET} ${CYAN}${PASSWORD}${RESET}"
echo -e "${MAGENTA}========================================${RESET}"


if command -v termux-clipboard-set &>/dev/null; then
    echo -n "$PASSWORD" | termux-clipboard-set
    echo -e "${GREEN}[✓] Password copied to clipboard${RESET}"
elif command -v xclip &>/dev/null; then
    echo -n "$PASSWORD" | xclip -selection clipboard
    echo -e "${GREEN}[✓] Password copied to clipboard${RESET}"
fi

