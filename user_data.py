from collections import defaultdict

# In-memory хранилище избранных городов (user_id -> set городов)
user_fav_cities = defaultdict(set)

# In-memory хранилище истории запросов (user_id -> list городов)
user_history = defaultdict(list)

# Добавить город в избранные
def add_fav_city(user_id: int, city: str):
    user_fav_cities[user_id].add(city)

# Удалить город из избранных
def remove_fav_city(user_id: int, city: str):
    user_fav_cities[user_id].discard(city)

# Получить избранные города
def get_fav_cities(user_id: int):
    return list(user_fav_cities[user_id])

# Добавить город в историю
def add_to_history(user_id: int, city: str):
    history = user_history[user_id]
    if city in history:
        history.remove(city)
    history.insert(0, city)
    if len(history) > 5:
        history.pop()

# Получить историю запросов
def get_history(user_id: int):
    return list(user_history[user_id])
