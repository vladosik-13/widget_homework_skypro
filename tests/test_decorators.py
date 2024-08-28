from src.decorators import log

'''Тест декоратора log'''


def test_log_decorator(tmpdir):
    log_info = tmpdir.join('test_log.txt')

    @log(log_info)
    def greet():
        return 'Hello'

    res = greet()

    assert res == 'Hello'

    with open(log_info, 'r', encoding='utf-8') as file:
        content = file.read()
        assert 'Запуск функции: greet ok' in content
        assert 'Функция greet выполнена.' in content
