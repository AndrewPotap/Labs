from collections import namedtuple

Predmet = namedtuple('Predmet', 'name, value, weight')
items = Predmet('Банан',2, 12), Predmet('Кружка',3, 3), Predmet('Парасоля',1, 20), Predmet('Телефон',5, 15), Predmet('Документи',7, 9)
capacity = 40  # Вмістимсть рюкзака


def best_value(nitems, weight_limit):
    if nitems == 0:  # якщо кількість предметів = 0
        return 0  # то результат - 0
    elif items[nitems - 1].weight > weight_limit:
        # якщо новий предмет важчий за поточну вмістимість
        return best_value(nitems - 1, weight_limit)  # то не складати предмет
    else:
        return max(  # найбільше значення з предметом та без
            best_value(nitems - 1, weight_limit),  # без
            best_value(nitems - 1, weight_limit - items[nitems - 1].weight)
            + items[nitems - 1].value)  # з предметом

result = []
weight_limit = capacity
for i in reversed(range(len(items))):
    if best_value(i + 1, weight_limit) > best_value(i, weight_limit):
        # краще із ітим предметом
        result.append(items[i])  # додати в результат цей предмет
        weight_limit -= items[i].weight
print(result)