# flask_quiz
В сервисе реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.


После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1


указанное в полученном запросе количество вопросов(максимум 100 за раз)


полученные ответы сохраняются в базе данных ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса.


В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняется дополнительный запрос


Ответом на запрос является предыдущей сохранённый вопрос для викторины.


инструкция к сборке докера;
chmod +x services/web/entrypoint.sh -- on linux


icacls services/web/entrypoint.sh --on windows


docker-compose build
docker-compose up -d 