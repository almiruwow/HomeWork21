from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, capacity, items):
        self._capacity = capacity
        self._items = items

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self._capacity = 100
        self._items = {}

    def add(self, name, quantity):
        if self._items.get(name) is None:
            self._items[name] = int(quantity)
        else:
            self._items[name] += int(quantity)
        self._capacity -= int(quantity)

    def remove(self, name, quantity):
        res = self._items[name] - int(quantity)
        if res > 0:
            self._items[name] = res
        else:
            del self._items[name]

        self._capacity += int(quantity)

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def get_items(self):
        return self._items

    @get_items.setter
    def get_items(self, item):
        self._items = item
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Storage):
    def __init__(self):
        self._capacity = 20
        self._items = {}

    def add(self, name, quantity):
        if self._items.get(name) is None:
            self._items[name] = int(quantity)
        else:
            self._items[name] += int(quantity)
        self._capacity -= int(quantity)

    def remove(self, name, quantity):
        res = self._items[name] - int(quantity)
        if res > 0:
            self._items[name] = res
        else:
            del self._items[name]

        self._capacity += int(quantity)

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._items)


class Request:
    def __init__(self, string):
        self.from_ = self.string_preparation(string)[4]
        self.to_ = self.string_preparation(string)[6]
        self.amount = self.string_preparation(string)[1]
        self.product = self.string_preparation(string)[2]

    @staticmethod
    def string_preparation(string):
        data = string.split(' ')
        return data

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to_}'


def main():
    store.get_items = {'лук': 11, 'чеснок': 4, 'оливка': 7, 'веник': 18, 'хинкали': 1, 'сметана': 13}
    while True:
        user_answer = input('Введите команду: ')

        from_store = None
        from_shop = None

        if user_answer.split(' ')[-1] == 'магазин':
            from_store = True
            from_shop = None
        else:
            from_shop = True
            from_store = None

        if user_answer == 'stop':
            break

        request = Request(user_answer)

        if from_store is not None:

            if request.product not in store.get_items:
                print(f'Нужного товара нет в {request.from_}')
                continue

            if store.get_items[request.product] >= int(request.amount):
                if shop.get_free_space < int(request.amount):
                    print('В магазине нет сводобного места!')
                    continue
                elif shop.get_unique_items_count >= 5:
                    print('К сожалению магазин заполнен!')
                    continue
                print('\nНужное количество есть на складе')
            else:
                print(f"На складе нет нужного количества. На складе {store.get_items[request.product]}")
                continue

            store.remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} со {request.from_}')
            print(f'Курьер везет {request.amount} {request.product} со {request.from_} в {request.to_}')
            print(f'Курьер доставил {request.amount} {request.product}  в {request.to_}\n')
            shop.add(request.product, request.amount)

            for title, item in {'склад':store, 'магазин':shop}.items():
                print(f'В {title} хранится:\n')
                for name, count in item.get_items.items():
                    print(name + ' - ' + str(count) + ' Шт.')

                print('-' * 50)

        elif from_shop is not None:
            if request.product not in shop.get_items:
                print(f'Нужного товара нет в {request.from_}')
                continue

            if store.get_items[request.product] >= int(request.amount):
                if shop.get_free_space < int(request.amount):
                    print('В магазине нет сводобного места!')
                    continue
                print(f'\nНужное количество есть в {request.from_}')
                print(f'Курьер забрал {request.amount} {request.product} из {request.from_}')
            else:
                print(f"На складе нет нужного количества. На складе {store.get_items[request.product]}")
                continue

            shop.remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} из {request.from_}')
            print(f'Курьер везет {request.amount} {request.product} из {request.from_} в {request.to_}')
            print(f'Курьер доставил {request.amount} {request.product}  в {request.to_}\n')
            store.add(request.product, request.amount)

            for title, item in {'склад': store, 'магазин': shop}.items():
                print(f'В {title} хранится:\n')
                for name, count in item.get_items.items():
                    print(name + ' - ' + str(count) + ' Шт.')

                print('-' * 50)


if __name__ == '__main__':
    store = Store()
    shop = Shop()
    main()