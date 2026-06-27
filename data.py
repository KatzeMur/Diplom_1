# Тестовые данные для юнит-тестов
BUN_NAME = "Black bun"
BUN_PRICE = 100.0

INGREDIENT_TYPE = "SAUCE"
INGREDIENT_NAME = "Hot sauce"
INGREDIENT_PRICE = 50.0

EXPECTED_RECEIPT = (
    f"(==== {BUN_NAME} ====)\n"
    f"= {INGREDIENT_TYPE.lower()} {INGREDIENT_NAME} =\n"
    f"(==== {BUN_NAME} ====)\n\n"
    f"Price: {BUN_PRICE * 2 + INGREDIENT_PRICE}"
)
