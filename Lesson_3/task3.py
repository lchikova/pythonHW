from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "20")

mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RB123456789RU"
)

print(
    f"Отправление {mail.track} "
    f"из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} в {mail.to_address.index}, "
    f"{mail.to_address.city}, {mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
