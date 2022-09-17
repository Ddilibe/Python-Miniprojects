from table import cookies, connection


ins = cookies.insert().values(
                  cookie_name="chocolate chip",
                  cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
                  cookie_sku="CC01",
                  quantity="12",
                  unit_cost="0.50"
			)
ins = cookies.insert()
result = connection.execute(
            ins,
            cookie_name="dark chocolate chip",
            cookie_recipe_url="http://some.aweso.me/cookies/recipe_dark.html",
            cookie_sku='CC02',
            quantity='1',
            unit_cost='0.75'
        )
print(result.inserted_primary_key)
