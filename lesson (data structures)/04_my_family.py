# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['father', 'mother', 'i']


# список списков приблизителного роста членов вашей семьи
# ['имя', рост]
my_family_height = [
    ['father', 180], ['mother', 170], ['i', 185]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Рост отца -', my_family_height[0][1], 'см')
print('Общий рост моей семьи -', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] , 'см')