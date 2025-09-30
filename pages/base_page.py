from playwright.sync_api import Page


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод для открытия ссылок
        self.page.goto(url, wait_until='networkidle')
        '''networkidle - чтобы дождаться завершения загрузки всех сетевых запросов перед выполнением последующих шагов.
        Но некоторые страницы могут продолжать периодически отправлять фоновые запросы (например, polling или аналитика), 
        из-за чего networkidle никогда не сработает. 
        networkidle может быть полезным как дополнительный шаг, чтобы минимизировать лишние ожидания.
        Но основная гарантия готовности страницы в тестах — это web assertions: проверка наличия, видимости,
        интерактивности нужных элементов - to_be_visible
        '''

    def reload(self):  # Метод для перезагрузки страницы
        self.page.reload(wait_until='domcontentloaded')