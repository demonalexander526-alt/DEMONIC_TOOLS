# ====== HACKER-STYLE TERMUX HEADER  ======
# ==== DEMON ALEX ===
clear


RED="\e[31m"
GREEN="\e[32m"
CYAN="\e[36m"
RESET="\e[0m"


figlet -f slant "LUKE REMON T" | lolcat
echo -e "${GREEN}Welcome $(whoami) to DEMON SYSTEM${RESET}"
echo -e "${CYAN}======================================${RESET}"


echo "Initializing all modules..." | pv -qL 10
sleep 0.5
echo "Loading cyber protocols..." | pv -qL 10
sleep 0.5
echo "System secure. Ready for action." | pv -qL 10
echo -e "${CYAN}======================================${RESET}"


echo -e "${GREEN}Entering Matrix mode... Press Ctrl+C to exit.${RESET}"
sleep 1
cmatrix -b

