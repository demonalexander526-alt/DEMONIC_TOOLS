#!/bin/bash

# ================= цвет ==================
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
CYAN="\e[36m"
MAGENTA="\e[35m"
RESET="\e[0m"


if ! command -v openssl &>/dev/null; then
    echo -e "${YELLOW}Installing OpenSSL...${RESET}"
    pkg install openssl -y 2>/dev/null || sudo apt install openssl -y
fi
clear
echo -e "${MAGENTA}========================================${RESET}"
echo -e "${MAGENTA}        DEMONIC FILE: (ENCRYPT/DECRYPT) TOOL${RESET}"
echo -e "${MAGENTA}        CREATED BY: DEMON ALEX${RESET}"
echo -e "${MAGENTA}========================================${RESET}"

# ================= Меню ==================
echo -e "${CYAN}1) Encrypt a file${RESET}"
echo -e "${CYAN}2) Decrypt a file${RESET}"
echo -e "${CYAN}0) Exit${RESET}"
echo ""
read -p "Choose option: " opt

case $opt in

1)
    read -p "Enter file path to encrypt: " file

    if [ ! -f "$file" ]; then
        echo -e "${RED}File not found!${RESET}"
        exit 1
    fi

    read -s -p "Enter password: " pass
    echo
    read -s -p "Confirm password: " pass2
    echo

    if [ "$pass" != "$pass2" ]; then
        echo -e "${RED}Passwords do not match!${RESET}"
        exit 1
    fi

    openssl enc -aes-256-cbc -salt -pbkdf2 \
        -in "$file" \
        -out "$file.demonic" \
        -pass pass:"$pass"

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Encryption successful!${RESET}"
        echo -e "${GREEN}Encrypted file:${RESET} $file.demonic"
    else
        echo -e "${RED}Encryption failed!${RESET}"
    fi
    ;;


2)
    read -p "Enter .demonic file to decrypt: " file

    if [ ! -f "$file" ]; then
        echo -e "${RED}File not found!${RESET}"
        exit 1
    fi

    read -s -p "Enter password: " pass
    echo

    out="${file%.demonic}"

    openssl enc -aes-256-cbc -d -pbkdf2 \
        -in "$file" \
        -out "$out" \
        -pass pass:"$pass"

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Decryption successful!${RESET}"
        echo -e "${GREEN}Decrypted file:${RESET} $out"
    else
        echo -e "${RED}Wrong password or corrupted file!${RESET}"
        rm -f "$out"
    fi
    ;;

0)
    exit
    ;;

*)
    echo -e "${RED}Invalid option!${RESET}"
    ;;
esac

