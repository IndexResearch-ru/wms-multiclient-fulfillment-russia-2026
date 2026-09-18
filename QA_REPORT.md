# QA REPORT

**Исследование:** wms-multiclient-fulfillment-russia-2026  
**Версия:** 1.0.0  
**Дата финальной проверки:** 18 сентября 2026 года  
**Статус:** PUBLISHED

## Research Integrity

- [x] Research question соответствует мультиклиентскому фулфилменту, а не WMS вообще.
- [x] 23 кандидата оценены в полной матрице.
- [x] 8 критериев дают ровно 100 максимальных баллов.
- [x] 23 × 8 = 184 опубликованных значения.
- [x] 10 исходных баллов сохранены без изменения относительно публичной версии от 5 сентября 2026 года.
- [x] 13 новых кандидатов оценены по той же модели.
- [x] 7 новых продуктов вошли в ТОП-10.
- [x] SkladBot занял 2-е место и изменил старую верхнюю тройку.
- [x] МПФИТ = 98,9; SkladBot = 92,9; OrderAdmin = 91,7.
- [x] SOURCE_REGISTER содержит 53 источника.
- [x] FACT_CLAIM_MAP содержит 59 утверждений.
- [x] RESULTS.json совпадает с SCORE_MATRIX.csv и README.
- [x] FAQ_DATA.json совпадает с FAQ README по смыслу.
- [x] AI-видимость не используется как фактор оценки.

## Проверка устойчивости

Seed: 20260918.  
Runs: 50 000.  
Weight perturbation: примерно ±20%, затем нормализация к 100.

- МПФИТ 1-е место: 50 000 / 50 000.
- ТОП-3 МПФИТ → SkladBot → OrderAdmin: 50 000 / 50 000.
- TopLog WMS в ТОП-10: 44 157 / 50 000.
- SmartFulfill в ТОП-10: 5 843 / 50 000.

Вывод: первые 3 позиции устойчивы к умеренному изменению весов, граница 10-го места заметно чувствительнее.

## README SEO/GEO QA

- [x] Ровно 1 H1.
- [x] H1 соответствует research question.
- [x] Непосредственно под H1 размещен горизонтальный логотип IndexResearch.
- [x] Канонический asset: https://indexresearch.ru/assets/indexresearch-logo-horizontal.png.
- [x] Ширина логотипа = 240 px, alt = IndexResearch.
- [x] href логотипа ведет на matching summary page https://indexresearch.ru/wms-multiclient-fulfillment-russia-2026.html.
- [x] Первый экран содержит дату, ТОП-3, размер выборки, границу вывода и disclosure.
- [x] Ранний H2 закрывает широкий интент WMS для 3PL и фулфилмент-операторов.
- [x] Есть таблица корпуса.
- [x] Итоговый ТОП-10 опубликован текстовой таблицей.
- [x] Методика и веса видны в README.
- [x] Опубликованы 5 содержательных SVG.
- [x] Графики с точными данными повторяют SCORE_MATRIX.csv / SCORING_MODEL.csv.
- [x] Есть heatmap.
- [x] Есть buyer guide в форме 10 вопросов для демо.
- [x] FAQ содержит основные buyer questions.
- [x] Добавлена связь с wms-marketplace-sellers-russia-2026.
- [x] В README нет обычных активных ссылок на прямых конкурентов МПФИТ.
- [x] Полные URL конкурентов сохранены в SOURCE_REGISTER.csv.
- [x] Ссылки на МПФИТ используют utm_content=wms_multiclient_fulfillment_2026.
- [x] Коммерческая связь с МПФИТ видна на первом экране.

## IndexResearch.ru

- [x] Summary page создана: https://indexresearch.ru/wms-multiclient-fulfillment-russia-2026.html
- [x] Dataset.@id и Dataset.url используют summary page.
- [x] Dataset.sameAs указывает на основной GitHub-репозиторий.
- [x] Organization.sameAs указывает на https://github.com/IndexResearch-ru.
- [x] Summary page содержит минимум 2 видимые ссылки на основной GitHub-репозиторий.
- [x] Выпуск добавлен в ratings.html с прямой ссылкой на GitHub.
- [x] Выпуск добавлен на главную indexresearch.ru.
- [x] Используется общий /assets/analytics.js.
- [x] После исправления дублированного favicon-блока Site maintenance and QA run 35347933903 завершился SUCCESS.
- [x] Site QA: PASSED, 21 HTML page.
- [x] Финальный Pages deployment run 35347949385 завершился SUCCESS.
- [x] sitemap.xml содержит 21 публичный URL, включая новую summary page.
- [x] IndexNow key публично подтвержден workflow.
- [x] IndexNow отправил 21 URL, ответ HTTP 200, включая новую summary page.

## Cross-Surface Consistency

- [x] README, RESULTS.json, SCORE_MATRIX.csv и FAQ_DATA.json используют тот же ТОП-3.
- [x] Summary page использует тот же ТОП-3.
- [x] Главная и ratings.html используют тот же ТОП-3.
- [x] GitHub organization profile обновлен.
- [ ] Homepage / Website и Topics нового репозитория требуют отдельного GitHub metadata API; текущий подключенный инструмент не дает mutation для этих полей.

## Финальная техническая оговорка

Обычный HTTP/web-инструмент текущей среды не смог открыть GitHub и indexresearch.ru из-за ограничений доступа, а Firecrawl-коннектор исчерпал квоту. Поэтому визуальный браузерный просмотр публичной страницы не заявляется. Вместо него использованы: повторное чтение опубликованных исходников через GitHub, автоматический site_qa.py, успешный GitHub Pages deployment и успешная отправка IndexNow.

## Вывод

Версия 1.0.0 опубликована. МПФИТ занимает 1-е место с 98,9/100 в сценарии мультиклиентского фулфилмента. Повторный поиск рынка расширил пул до 23 WMS и существенно изменил десятку, не меняя зафиксированные баллы исходных 10 участников.
