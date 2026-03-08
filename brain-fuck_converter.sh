#!/bin/bash

RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
WHITE="\e[97m"
RESET="\e[0m"

clear

echo -e "${MAGENTA}"
echo "=============================================="
echo "           DEMON CONVERTER"
echo "           Created by NEXO-TECH"
echo "=============================================="
echo -e "${RESET}"

echo -e "${CYAN}Choose an option:${RESET}"
echo -e "${YELLOW}[A] Convert Text (letters, numbers, symbols) ➜ Brainfuck${RESET}"
echo -e "${YELLOW}[B] Convert Brainfuck ➜ Text${RESET}"
echo ""

read -p "$(echo -e ${GREEN}Enter option A or B:${RESET} ) " option

if [[ "$option" =~ ^[Aa]$ ]]; then
    echo ""
    read -p "$(echo -e ${BLUE}Enter your text:${RESET} ) " input
    output=""
    prev=0
    for (( i=0; i<${#input}; i++ )); do
        char="${input:$i:1}"
        ascii=$(printf "%d" "'$char")
        if (( ascii < 32 || ascii > 126 )); then
            echo -e "${RED}Unsupported character detected!${RESET}"
            exit 1
        fi
        diff=$((ascii - prev))
        if (( diff > 0 )); then
            output+=$(printf "%0.s+" $(seq 1 $diff))
        elif (( diff < 0 )); then
            output+=$(printf "%0.s-" $(seq 1 $((-diff))))
        fi
        output+="."
        prev=$ascii
    done
    echo ""
    echo -e "${GREEN}Brainfuck Output:${RESET}"
    echo -e "${WHITE}$output${RESET}"
fi

if [[ "$option" =~ ^[Bb]$ ]]; then
    echo ""
    read -p "$(echo -e ${BLUE}Enter Brainfuck code:${RESET} ) " bfcode
    cell=0
    output=""
    for (( i=0; i<${#bfcode}; i++ )); do
        cmd="${bfcode:$i:1}"
        case "$cmd" in
            "+") ((cell++)) ;;
            "-") ((cell--)) ;;
            ".")
                if (( cell >= 32 && cell <= 126 )); then
                    output+=$(printf "\\$(printf '%03o' $cell)")
                else
                    output+="?"
                fi
                ;;
        esac
    done
    echo ""
    echo -e "${GREEN}Text Output:${RESET}"
    echo -e "${WHITE}$output${RESET}"
fi

echo ""
echo -e "${MAGENTA}Done. Stay Demonic 😈${RESET}"
echo -e "${CYAN}Powered by DEMON ALEX${RESET}"
