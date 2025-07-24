import aiohttp
from translations import translate_weather_desc, get_weather_emoji

async def get_weather(city: str) -> str:
    url = f'https://wttr.in/{city}?format=j1'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return '❗️ Не удалось получить погоду. Проверьте название города или попробуйте позже.'
                data = await resp.json()
                current = data['current_condition'][0]
                temp = current['temp_C']
                feels = current['FeelsLikeC']
                desc = translate_weather_desc(current['weatherDesc'][0]['value'])
                humidity = current['humidity']
                wind = current['windspeedKmph']
                emoji = get_weather_emoji(desc)
                return (
                    f'<b>Погода в городе {city}:</b> {emoji}\n'
                    f'<b>{desc}</b>\n'
                    f'🌡 Температура: <b>{temp}°C</b> (ощущается как {feels}°C)\n'
                    f'💧 Влажность: <b>{humidity}%</b>\n'
                    f'💨 Ветер: <b>{wind} км/ч</b>'
                )
        except Exception as e:
            return f'❗️ Ошибка при получении погоды: {e}'

async def get_day_parts_weather(city: str) -> str:
    url = f'https://wttr.in/{city}?format=j1'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return '❗️ Не удалось получить погоду. Проверьте название города или попробуйте позже.'
                data = await resp.json()
                today = data['weather'][0]['hourly']
                parts = {
                    'Ночь': today[0],   # 00:00
                    'Утро': today[2],   # 06:00
                    'День': today[4],   # 12:00
                    'Вечер': today[6],  # 18:00
                }
                result = f'<b>Погода в городе {city} по времени суток:</b>\n'
                for part, info in parts.items():
                    temp = info['tempC']
                    desc = translate_weather_desc(info['weatherDesc'][0]['value'])
                    emoji = get_weather_emoji(desc)
                    result += f'<b>{part}:</b> {temp}°C, {desc} {emoji}\n'
                return result
        except Exception as e:
            return f'❗️ Ошибка при получении погоды: {e}'

async def get_day_parts_weather_3days(city: str) -> str:
    url = f'https://wttr.in/{city}?format=j1'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return '❗️ Не удалось получить погоду. Проверьте название города или попробуйте позже.'
                data = await resp.json()
                weather_days = data['weather'][:3]
                result = f'<b>Погода в городе {city} по времени суток на 3 дня:</b>\n'
                day_names = ['Сегодня', 'Завтра', 'Послезавтра']
                for i, day in enumerate(weather_days):
                    hourly = day['hourly']
                    parts = {
                        'Ночь': hourly[0],   # 00:00
                        'Утро': hourly[2],   # 06:00
                        'День': hourly[4],   # 12:00
                        'Вечер': hourly[6],  # 18:00
                    }
                    result += f'\n<b>{day_names[i]}:</b>\n'
                    for part, info in parts.items():
                        temp = info['tempC']
                        desc = translate_weather_desc(info['weatherDesc'][0]['value'])
                        emoji = get_weather_emoji(desc)
                        result += f'<b>{part}:</b> {temp}°C, {desc} {emoji}\n'
                return result
        except Exception as e:
            return f'❗️ Ошибка при получении погоды: {e}'
