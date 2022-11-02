#!/bin/bash
exec 2> log_error_auto
auth=1

echo -n "Введите логин: "
read login

while read line
do
    user=($line)
    if [[ ${user[0]} == $login ]]
    then
        for ((try=0;try<4;try++))
        do
            if [[ $try == 3 ]]
            then
                echo упс, кажется Вас нет в системе
                dt=$(date)
                echo "$dt $user :(" >> failed_auth
                exit
            fi
            echo "Введите ваш пароль:"
            read -s -t 10 pass <&1
            input=$(echo -n $pass | sha512sum)
            pass=($input)
            password="${pass[0]}"
            if [[ $password == ${user[1]} ]]   
            then
                echo "Авторизация успешна"
                exit
            else
                echo Неверный пароль. Осталось попыток $((3-($try+1)))
            fi
        done 
    else
        auth=1
    fi
done < database.txt
if [[ $auth == 1 ]]
then
    echo Логин не найден
    exit
fi