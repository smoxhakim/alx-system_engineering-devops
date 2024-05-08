push() {
    git add .
    git commit -m "$1"
    git push
    echo -e "\n\033[1;32mSuccess\033[0m"
    echo -e "\n"
}
back (){
    arg=$(( $1 + 0 ))
    ((i = 0))

    if [ $# -eq 0 ]; then
        cd ..
        return
    fi
    
    while ((arg > i)); do
        cd ..
        ((i++))
    done
}