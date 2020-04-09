```sql
students_info: -- Подробная нформация обо всех студентах в группе
    student_id integer not null primary key;
    tg_id bigint not null unique check tg_id > 0;
    first_name varchar(50) not null;
    last_name  varchar(50) not null;
    group_num smallint not null;
    subgroup_num smallint not null;
    academic_status smallint not null check academic_status >= 0 and academic_status <= 5;

users: -- Краткая информация о каждом пользователе бота. (Пользователь != студент и студент != пользователь)
    user_id serial primary key;
    tg_id bigint not null unique check tg_id > 0;

sessions: -- Хранилище настроек пользователей (prob. storages?)
    tg_id bigint not null unique primary key check tg_id > 0;
    state varchar(35) not null default "main"
    current_chat bigint;
    names_usage boolean;
    financial_category: integer;
    donate_id: integer;
    current_mailing: integer;

calls_storage: -- Хранилище Призыва
    tg_id bigint not null unique primary key check tg_id > 0;
    selected_ids text;
    call_text text;
    call_attaches: text;

mailings_storage: -- Хранилище Рассылок
    tg_id bigint not null unique primary key check tg_id > 0;
    mailing_text text;
    mailing_attach text;

mailings: -- Перечень доступных Рассылок
    mailing_id serial primary key;
    mailing_name varchar(60) not null;

subscriptions: -- Информация о подписчиках Рассылок
    user_id integer not null;
    mailing_id smallint not null foreign key mailings.mailing_id on delete cascade;
    subscribe_status boolean not null;    

financial_categories: -- Перечень доступных категорий расходов
    category_id serial primary key;
    category_name varchar(60) not null;
    category_summ integer not null

financial_donates: -- Список взносов
    donate_id serial primary key;
    student_id integer not null;
    category_id integer not null foreign key financial_categories.category_id on delete cascade;
    donate_summ integer not null;
    create_date date not null default CURRENT_DATE;
    update_date date;

financial_expenses: -- Список расходов
    expense_id serial primary key;
    category_id integer not null foreign key financial_categories.category_id on delete cascade;
    expense_summ integer not null;
    create_date date not null default CURRENT_DATE;
```