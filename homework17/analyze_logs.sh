#!/bin/bash

# путь к файлу
path_file="access.log"
# путь к файлу отчета
path_report="report.txt"

# Общее кол-во запросов
num_requests=$(cat $path_file | wc -l)

# Кол-во уникальных ip-адресов
num_uniq_ip=$(cat access.log | awk '{ ip[$1]+=1 } END{ for (i in ip){n++};print n  }')

# Кол-во запросов по методам
num_request_method=$(cat access.log | awk '{ count[$6]++ } END { for (request in count) print count[request], substr(request, 2) }')

# Популярный URL
most_popular_url=$(cat access.log | awk '{ count[$7]++ } END {max_i=0; max_v=""; for (url in count) if(count[url]>max_i) {max_i = count[url]; max_v=url}  print max_i, max_v }')

# Формировние отчета
echo "Отчет о логе веб-сервера" > $path_report
echo "========================" >> $path_report
echo -e "Общее количество запросов:\t $num_requests" >> $path_report
echo -e "Количество уникальных IP-адресов:\t $num_uniq_ip" >> $path_report
echo -e "\n" >> $path_report

echo "Количество запросов по методам:" >> $path_report
IFS=$'\n' read -rd '' -a array <<< $num_request_method
for i in "${array[@]}"
do
	echo "  $i" >> $path_report
done
echo -e "\n" >> $path_report

echo -e "Самый популярный URL:\t $most_popular_url" >> $path_report

echo "Отчет сохранен в файл $path_report"
