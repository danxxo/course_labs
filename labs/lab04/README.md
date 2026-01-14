<div align="center">
<h1><a id="intro">Лабораторная работа №4</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>


## Вводные

Компания зарегистрирована в Евросоюзе и должна соответствовать законодательству ЕС. Работая в данной компании занимаетесь обеспечением ИБ. 

Вы обнаруживаете админскую консоль веб-сайта своей компании, которая доступна неограниченному кругу лиц в сети Интернет, так как публикация торчит во внешний сегмент сети
> - С помощью её интерфейса доступны на просмотр записи с запросами о приобретении продукции компании, которые содержат персональные данные, а также коммерческие предложения (что, в каком объёме, за сколько, специальный условия и т.д.). 
> - Аналогично доступны логи, в которых видны ip-адреса администраторов, которые попадали в нее. 


## Анализ возможности взлома, утечки, доступности информации и ее категории значимости для компании

Проблема: Админ-консоль, содержащая конфиденциальную информацию, ПДн, логи входов администраторов, торчит наружу.

### 1. Возможность взлома

#### 1.1 Описание
Публичная доступность консоли создает прямой вектор для взлома. Злоумышленники могут использовать автоматизированные инструменты для обнаружения (Shodan для поиска открытых админ-панелей) и эксплуатации. 

Отсутствие сегментации сети позволяет переход к внутренним ресурсам.

#### 1.2 Возможные действия злоумышленника
- Прямой доступ к интерфейсу и просмотр / скачивание всех доступных данных
- Поиск и эксплуатация уязвимостей в самой консоли (SQL-инъекции, командные инъекции, path traversal)
- Использование раскрытых IP-адресов и имён учётных записей для целевых атак на администраторов/сотрудников, а также для lateral movement и внутренней разведки

#### 1.3 Последствия
- Компрометация системы 
- Утечка клиентских и коммерческих данных 
- Необходимость дорогостоящего восстановления и расследования.
- Штрафы от регуляторов

#### 1.4 Пример сценария
- Shodan -> admin panel -> admin logs -> phishing -> ransomware

- Shodan -> admin panel -> SQLi -> RCE -> ...

#### 1.5 Оценка
Критическая

#### 2. Возможность утечки

#### 2.1 Описание
Все содержащиеся в консоли данные доступны любому интернет-пользователю. При отсутстсвии двухфакторной аутентификации после брутфорса происходит утечка

#### 2.2 Возможные действия злоумышленника
- Массовый сбор данных с помощью скриптов (web scraping)
- Скачивание и продажа персональных данных на теневых площадках
- Использование коммерческих предложений для конкурентного шпионажа и подрыва текущих сделок
- Сбор IP-адресов и временных меток для подготовки целевых атак на сотрудников
- Публикация части данных в открытом доступе с целью репутационного ущерба

#### 2.3 Последствия
- Массовое разглашение персональных данных клиентов
- утрата коммерческой тайны
- подрыв доверия со стороны партнёров и клиентов
- репутационные потери

#### 2.4 Пример сценария
- Эксфильтрация данных -> публикация данных на теневых форумах

#### 2.5 Оценка
Критическая

#### 3. Доступность информации

#### 3.1 Описание
Публичный интерфейс консоли уязвим к перегрузке и может быть использован для нарушения нормальной работы административного персонала.

#### 3.2 Возможные действия злоумышленника
- Массовые запросы к странице с целью исчерпания ресурсов сервера
- Использование консоли как отвлекающего фактора во время основной атаки на другие системы
- Целенаправленная блокировка доступа администраторов к необходимой информации

#### 3.3 Последствия
- Отказ функционирования критических сервисов

#### 3.4 Пример сценария
- Распределенное выполнение больших запросов к консоли (DDOS) -> нагрузка на критичный сервис

#### 3.5 Оценка
Высокая

## Compliance-анализ

### Регуляторы

#### GDPR

Нарушение защиты персональных данных грозит штрафом до **€20 млн** или **4% годового оборота**. Регламент требует уведомлять надзорный орган о нарушениях не позднее 72 часов (ст. 33).

#### NIS2 Directive

С октября 2024 года вступила в силу директива NIS2, расширяющая требования к кибербезопасности для организаций в ЕС. Директива требует:

- Внедрения мер управления рисками кибербезопасности (ст. 21)
- Уведомления о значительных инцидентах в течение 24 часов (ст. 23)
- Штрафы до **€10 млн** или **2% годового оборота** для существенных организаций

#### 152-ФЗ «О персональных данных»

Поскольку обрабатываются данные граждан РФ, применяются требования российского законодательства:

- Запрет на хранение ПДн россиян на серверах за рубежом без соблюдения условий трансграничной передачи
- Штраф от **1 до 6 млн руб** за первое нарушение, до **18 млн руб** за повторное

### Риски

<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Риск</th>
            <th>Описание риска</th>
            <th>Уровень критичности</th>
            <th>Вероятность реализации</th>
            <th>Потенциальные последствия для компании</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Массовое разглашение персональных данных (ПДн) клиентов</td>
            <td>ПДн граждан ЕС и РФ доступны любому интернет-пользователю без авторизации</td>
            <td class="critical">Критический</td>
            <td>высокая</td>
            <td>Штрафы регуляторов, массовые жалобы и иски от субъектов данных, утрата доверия клиентов, репутационный ущерб</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Утечка коммерческой тайны и инсайдерской информации</td>
            <td>Полные коммерческие предложения (цены, объёмы, условия, скидки, индивидуальные договорённости) открыты</td>
            <td class="critical">Критический</td>
            <td>высокая</td>
            <td>Подрыв текущих и будущих сделок, демпинг со стороны конкурентов, потеря конкурентных преимуществ, финансовые убытки</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Компрометация инфраструктуры через раскрытие данных администраторов</td>
            <td>IP-адреса, время доступа, иногда имена учётных записей видны всем</td>
            <td class="critical">Критический</td>
            <td>Средняя</td>
            <td>Целевые атаки на ключевых сотрудников (spear-phishing, social engineering), lateral movement, ransomware</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Нарушение требований GDPR, NIS2 и 152-ФЗ одновременно</td>
            <td>Несоблюдение всех трёх регуляций сразу из-за одного и того же инцидента</td>
            <td class="critical">Критический</td>
            <td>Высокая</td>
            <td>Множественные расследования, штрафы от нескольких регуляторов, уголовная ответственность должностных лиц</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Репутационный и клиентский ущерб</td>
            <td>Публикация данных в СМИ / даркнете / соцсетях после обнаружения консоли</td>
            <td class="high">Высокий</td>
            <td>Высокая</td>
            <td>Отток клиентов, потеря партнёров, негатив в прессе, снижение капитализации (если публичная компания)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Операционные сбои и перегрузка консоли</td>
            <td>Публичный интерфейс может быть перегружен или использован для отвлечения внимания</td>
            <td class="medium-high">Высокий</td>
            <td>Высокая</td>
            <td>Задержки в обработке заявок, упущенная выгода, дополнительная нагрузка на ИТ/ИБ-команды</td>
        </tr>
    </tbody>
</table>

### Меры снижения рисков

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif; width: 100%;">
    <thead>
        <tr style="font-weight: bold; text-align: left;">
            <th>№ риска</th>
            <th>Меры снижения</th>
            <th>Необходимость</th>
            <th>Срочность</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1-6</td>
            <td>Изоляция консоли от публичного доступа</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
        </tr>
        <tr>
            <td>1-3</td>
            <td>Доступ через VPN/Jump host</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
        </tr>
        <tr>
            <td>1-3</td>
            <td>Внедрение MFA</td>
            <td style="background-color: #ff8533; color: black; text-align: center; font-weight: bold;">8</td>
            <td style="background-color: #3374ffff; color: black; text-align: center; font-weight: bold;">5</td>
        </tr>
        <tr>
            <td>1,2,4</td>
            <td>Псевдонимизация ПДн</td>
            <td style="background-color: #ff8533; color: black; text-align: center; font-weight: bold;">8</td>
            <td style="background-color: #66cc66; color: black; text-align: center; font-weight: bold;">2</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Фильтрация адресов входа по IP на FW</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Уведомление регуляторов/контрагентов о нарушении</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
            <td style="background-color: #ffae00ff; color: black; text-align: center; font-weight: bold;">7</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Защита логов, перемещение логов в SIEM, скрытие</td>
            <td style="background-color: #ffcc00; color: black; text-align: center; font-weight: bold;">6</td>
            <td style="background-color: #ffcc00; color: black; text-align: center; font-weight: bold;">6</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Проведение расследования</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
            <td style="background-color: #ff4d4d; color: white; text-align: center; font-weight: bold;">10</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Внедрение WAF</td>
            <td style="background-color: #99ccff; color: black; text-align: center; font-weight: bold;">4</td>
            <td style="background-color: #ffcc00; color: black; text-align: center; font-weight: bold;">6</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Аудит Supply Chain на предмет наличия уязвимостей</td>
            <td style="background-color: #99ccff; color: black; text-align: center; font-weight: bold;">4</td>
            <td style="background-color: #ffcc00; color: black; text-align: center; font-weight: bold;">6</td>
        </tr>
    </tbody>
</table>

### Техническое решение (срочное)
- Переместить консоль в частный сегмент сети
- Организовать доступ по VPN
- Реализовать фильтрацию по IP на FW
- Уведомить регулятора
- Провести расследование 

## Links

- [Markdown](https://stackedit.io)
- [Gist](https://gist.github.com)
- [GitHub CLI](https://cli.github.com)
- <a href="https://github.com/geminishkv/course_labs/blob/develop/artifacts/exmpls/Пример_аналитических_отчетов_по_задачам_ИБ.pdf">Пример аналитических отчетов</a>

Copyright (c) 2025 Elijah S Shmakov

![Logo](../../assets/logotype/logo.jpg)