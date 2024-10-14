import string

#  константы проекта
ALLOWED_CHARS_SHORT_LINK = string.ascii_letters + string.digits
LENGTH_SHORT_LINK_AUTO = 6
LENGTH_SHORT_LINK_USER = 16
LENGTH_LINK = 256
REGEXP_SHORT_VALIDATOR = f'^[{ALLOWED_CHARS_SHORT_LINK}]*$'


# форма
PLACEHOLDER_ORIGINAL_LINK = 'Длинная ссылка'
PLACEHOLDER_SHORT_LINK = 'Ваш вариант короткой ссылки'
PLACEHOLDER_SUBMIT_BUTTON = 'Создать'
DATA_REQUIRED_VALIDATOR = 'Обязательное поле'
URL_VALIDATOR = 'Пожалуйста, введите корректный URL'


# ошибки
class Errors:
    SHORT_LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
    TOO_LONG_SHORT_LINK = 'Максимальная длина короткой ссылки 16 символов'
    TOO_LONG_LINK = 'Максимальная длина ссылки 256 символов.'
    WRONG_FORMAT_SHORT_LINK = 'Указано недопустимое имя для короткой ссылки'
    TIME_OUT_ERROR = 'Что то пошло не так, попробуйте ещё раз.'
    EMPTY_REQUEST = 'Отсутствует тело запроса'
    EMPTY_URL = '"url" является обязательным полем!'
    EMPTY_SHORT_LINK = 'Указанный id не найден'
