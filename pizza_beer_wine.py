import os

STARS = 40


cake = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⢰⡆⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡞⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣥⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⠡⡄⠙⢦⠀⠀⠀⠀⠀⢠⣆⠀⠀⢸⡏⠉⠋⠉⢸⠀⠀⢀⣦⠀⠀⠀⢀⢰⠃⢠⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠻⣥⣽⣦⡼⠁⠀⠀⠀⠀⡞⠙⣆⠀⠈⢷⣀⡇⠀⣯⠀⠀⡼⠈⢷⡀⠀⠈⢻⣄⣾⣦⢞⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡶⣿⣿⠿⢿⠇⠀⠀⠀⣰⠃⢠⠈⢳⡤⢾⡿⣇⠀⢸⠦⢼⡇⢰⡀⠹⣄⠀⢈⣿⠿⠿⠿⢻⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣇⠀⣀⠀⣾⡤⠔⠒⠋⠹⣦⣼⣶⣼⡃⠀⣿⠸⣆⣼⡆⢈⣳⣤⣷⣼⣋⠓⠺⣧⢠⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣹⡆⣻⠀⣿⠀⠀⠀⢀⡶⠿⠿⠿⠛⡇⠀⠈⠛⢛⠉⠀⣼⠛⣛⠛⠋⣹⢦⡀⠹⡿⡀⠀⢸⢦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⡼⠋⡇⠈⢷⢿⡀⡆⠀⠘⣧⢠⠀⠀⢸⠁⠀⠀⢠⠇⢰⠀⠸⡄⢸⠀⠠⡇⠀⢳⡀⢹⡇⠀⠸⡄⠈⠳⣄⠀⠀⠀
⠀⠀⣸⠁⠀⠷⣤⠤⠞⠃⡇⠀⠀⠸⣿⡄⠀⢸⠀⠀⠀⠸⡀⠘⢦⡀⢹⠈⡇⠀⡇⠀⠀⠇⠹⠦⠤⠔⠋⣇⠀⢸⡆⠀⠀
⠀⠀⡇⠀⠀⠀⠱⣄⠀⠀⠙⠲⢤⠀⣿⢳⡄⠈⣇⠀⠀⠀⣹⠀⠀⠃⢸⡄⠁⠀⣹⠀⠀⠀⠀⠀⠀⣀⡤⠿⠀⣸⠃⠀⠀
⠀⠀⠙⣶⠲⡄⠀⠘⢦⣀⣀⣀⣸⠁⢛⠦⠤⠞⠃⠀⠀⠘⠁⠀⠀⠀⠀⠛⠒⠒⠋⣀⣀⡤⠤⠚⠉⠁⠀⢀⡴⣯⠀⠀⠀
⠀⠀⠀⢸⠀⣇⠀⠀⣠⠷⣄⠀⠀⠀⠀⠙⠢⣄⣀⣀⠤⠖⠦⠤⣀⣀⣀⣀⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀⢾⠉⠨⣿⠀⠀⠀
⠀⠀⠀⣸⠀⠙⢦⠼⠁⠀⢸⡀⢠⠖⠋⠉⠒⠢⣄⠀⠀⠀⠀⣀⣀⣤⠾⢦⡀⠀⠀⣰⠊⠉⠓⠦⠤⣤⣞⣥⠾⢻⠆⠀⠀
⠀⠀⢸⠉⠉⠓⠦⣄⡀⠀⠈⣧⠼⠁⠀⠀⠀⠀⠈⢧⡀⠈⠉⢡⠞⠁⠀⠀⠙⠦⠞⠁⠀⢀⣠⠤⠞⠋⠁⠀⢀⡼⠀⠀⠀
⠀⢠⡇⠀⠀⠀⣀⠀⠉⠑⠒⠦⠤⢄⣀⣀⡀⠀⠀⠀⠙⠲⠖⠋⠀⠀⠀⣀⣠⠤⠔⠒⠋⠁⠀⠀⠀⠀⣀⣀⡼⣿⡀⠀⠀
⢀⡼⠳⢶⠞⠉⠉⠙⢦⡀⠀⠀⠀⠂⠒⠚⠿⢍⣙⣶⢶⣶⣶⣶⣖⣋⣉⣁⣠⠄⠀⠀⠀⢀⡴⠦⠤⠞⠁⠀⠀⡇⠙⢧⠀
⣿⡇⠀⠈⢧⡀⠀⠀⠀⠙⢦⡤⠴⠒⠒⠲⠤⣄⡀⠀⠀⠀⢀⡽⠛⠯⣍⡉⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⢀⡴⠃⠀⢸⡇
⠈⢧⠀⠀⠀⠙⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢤⡤⠞⠀⠀⠀⠈⠉⠓⠒⠒⠋⠁⠀⠀⠀⣀⡤⠞⠁⠀⠀⢀⡾⠁
⠀⠈⠑⠦⣀⠀⠀⠀⠉⠓⠲⠤⢄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡤⠴⠒⠋⠁⠀⠀⢀⣠⠖⠋⠀⠀
⠀⠀⠀⠀⠀⠉⠓⠲⠤⣄⣀⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⢀⣀⣠⠤⠖⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠒⠒⠒⠒⠦⠤⠤⠤⠤⠤⠤⠤⠖⠒⠒⠒⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
cake_counter = 0
cake_price = 2.5
cake_total_price = cake_counter * cake_price

wine = '''
⠀⠀⠀⠀⢀⡤⣶⣿⠿⠿⠿⠿⠿⠿⣾⣶⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣥⣀⡀⠀⠀⠀⠀⢀⣀⣠⣿⣿⣄⠀⠀⠀
⠀⠀⢀⣿⡟⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠛⠉⠹⣿⣄⠀⠀
⠀⠀⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀
⠀⣸⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄
⢸⣿⠃⢀⣠⣶⣶⣶⣷⣶⣤⣄⣀⡀⠀⠀⠀⣀⡄⠀⣿⡇
⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣧
⢸⣿⡄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣿⡇
⠀⣿⣷⡀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣼⣿⠁
⠀⠈⠻⣷⣄⡀⠙⠻⠿⣿⣿⣿⣿⡿⠟⠋⠁⣠⣾⡿⠁⠀
⠀⠀⠀⠈⠛⢿⣷⣦⣤⣄⣀⣀⣤⣤⣤⣶⡿⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⣿⣿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣾⡿⠟⠋⠀⠈⠻⢿⣷⣦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠿⠿⢿⣷⣾⣿⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀
'''
wine_counter = 0
wine_price = 3.5
wine_total_price = wine_counter * wine_price

pizza = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀
⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
pizza_counter = 0
pizza_price = 5.0
pizza_total_price = pizza_counter * pizza_price

beer = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⢤⡤⢤⣴⠞⠓⠶⠒⠒⣆⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠛⠉⠀⡴⠒⠋⠁⠉⠉⠦⠤⠴⣀⠀⠙⠒⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⢀⣀⣋⣀⣀⣤⣤⣤⣤⣤⣤⣄⣀⣀⠀⠈⢷⠀
⠀⠀⠀⠀⢀⣀⣀⣀⣹⣦⡴⠛⣿⠉⠉⠁⠀⠀⢸⡇⡇⠀⠀⠀⠉⠉⣿⡆⠈⡧
⠀⠀⠀⡴⡋⡠⠀⡈⢿⡏⡇⠀⣿⠀⠀⠀⠀⠀⠀⡇⡇⠀⠀⠀⠀⠀⡟⢣⠀⢳
⠀⠀⡞⢁⠇⡞⠛⢮⣾⢡⣧⡄⡟⠒⢻⠛⠓⠒⢶⡇⣷⢤⣤⠤⠤⠤⠤⢼⣤⠞
⠀⢰⢧⣾⢸⠃⠀⠈⣿⢸⣿⠇⡇⠐⡏⠀⠀⠀⢸⡇⢸⠀⡇⠀⠀⠀⠀⡀⣇⠀
⠀⣾⣸⡇⡿⠀⠀⠀⣿⢸⠸⠀⡇⢠⠀⠀⠀⠀⢸⣷⢸⠀⢻⠀⠀⠀⡇⡇⢻⠀
⢠⡇⣿⢱⡇⠀⠀⢸⡇⣸⢀⠀⠀⠈⡄⠀⠀⠀⠸⢻⢸⡀⠀⠀⠀⠀⡆⢧⢸⡀
⣸⠈⡟⢸⠀⠀⠀⢸⡇⣿⢸⠀⢰⠘⡀⠀⠀⠀⠀⢸⠈⠃⠀⠀⠀⠈⠁⢸⠘⡇
⢻⡀⢣⠸⣄⣀⣀⣼⡇⣿⠸⠀⢸⠦⠃⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢸⡀⡇
⠈⢧⡀⢠⣬⣭⣿⣿⠀⣿⡄⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⡇
⠀⠀⠉⠙⠒⠿⠟⣿⠀⠹⡇⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⢀⡀⠁⠈⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠟⡿
⠀⠀⠀⠀⠀⠀⠀⠘⣎⢿⡟⠋⠁⠀⠐⠒⠒⢒⣒⣒⣒⣂⣀⣀⣤⣭⣤⣤⣤⠇
⠀⠀⠀⠀⠀⠀⠀⠀⢹⡘⠷⠦⢤⣀⣈⣉⣉⣛⣉⣩⣭⣭⣭⣾⣿⠿⣿⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠲⠶⠶⠤⠤⠤⣤⣤⣤⣤⣤⣭⣭⡭⠭⠴⠃⠀⠀⠀
'''
beer_counter = 0
beer_price = 2.75
beer_total_price = beer_counter * beer_price

pint = '''
⠀⣾⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣏⢿⣿⣿⣿⣿⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢦⠹⣿⣿⣿⠀⠹⡄⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣶⣷⣌⠻⣇⠀⢀⡇⣀⠴⠚⠉⠀⠀⠀⠀⠈⠑⠋⠀⠈⠂⢀⠀⠀⠀
⠀⠀⠀⣨⡿⠙⣿⣷⠦⣽⡿⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠱⠀⠀
⠀⣠⠞⣿⣤⣶⣯⣝⣶⡟⠛⠒⠻⠿⠦⠤⠤⠤⠶⠤⠤⠞⠃⡁⠀⠀⠀⠀⡇⠀
⢰⠃⣰⡿⠟⠋⠉⠻⣿⠇⣿⡇⢰⣶⣶⠀⣶⣶⣶⠀⣶⣶⡎⠀⠀⠀⠀⠀⠃⠀
⡏⢀⣿⠁⠀⠀⠀⠀⢸⢠⣿⡇⢸⣿⣿⠀⣿⣿⣿⠀⣿⣿⣷⠀⠀⠀⠀⠀⠀⢡
⡇⢸⣿⠀⠀⠀⠀⠀⣸⢸⣿⡇⢸⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠇⠀⠀⠀⠀⠀⡆
⢹⠈⣿⣇⠀⠀⠀⠀⡏⢸⣿⡇⢸⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⢀⣀⠀⠀⠀⠀
⠈⣧⠘⣿⣆⠀⠀⠀⡇⣸⣿⠇⣸⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠒⣿⣿⢡⠀⢸⠀
⠀⠘⣧⠘⢿⣦⠀⢰⡇⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⡄⡇⠊⠀
⠀⠀⠈⢳⡈⢻⣷⣸⠁⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⡇⡇⠀⠀
⠀⠀⠀⠀⠙⣄⢻⣿⢰⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⡇⣿⣿⡇⢹⠀⠀
⠀⠀⠀⠀⣠⠟⢸⣿⢸⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⡇⢹⣿⣷⢸⠀⠀
⠀⠀⠀⢸⣧⣤⡿⡇⢸⣿⡟⠀⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⣾⣿⡇⠀⣿⣿⡏⠀⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡈⡇⠀
⠀⠀⠀⠀⠀⠀⢸⡃⠙⠻⠇⠸⣿⣿⡇⠀⣿⣿⣿⠀⣿⣿⣿⡇⢸⡿⠿⠃⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠒⠶⠤⠤⢤⣤⣤⣤⣄⣀⣠⣤⣤⠤⠤⠴⠖⠒⠛⠁⠀
''' # iskljucivo bezalkoholno
pint_counter = 0
pint_price = 3.25
pint_total_price = pint_counter * pint_price

total_price = cake_total_price + wine_total_price + pizza_total_price + beer_total_price + pint_total_price


while True:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    # Za one koji zele znati vise - if uvjet u jednoj liniji:
    # os.system('cls' if os.name == 'nt' else 'clear')

    # Izbornik
    print('\t\tMENU')
    print('*'*STARS)
    print('1. Pizza')
    print('2. Pivo')
    print('3. Pinta')
    print('4. Vino')
    print('5. Kolac')
    print('0. Izlaz')
    print('*'*STARS)

    print()
    print('-'*STARS)
    print()

    print('Narucili ste:')
    print('-'*STARS)
    if cake_counter > 0:
        print(f'{cake_counter} x Cake ({cake_total_price} EUR)')
    if wine_counter > 0:
        print(f'{wine_counter} x Wine ({wine_total_price} EUR)')
    if pizza_counter > 0:
        print(f'{pizza_counter} x Pizza ({pizza_total_price} EUR)')
    if beer_counter > 0:
        print(f'{beer_counter} x Beer ({beer_total_price} EUR)')
    if pint_counter > 0:
        print(f'{pint_counter} x Pint ({pint_total_price} EUR)')

    if (cake_counter == 0 and
        wine_counter == 0 and
        pizza_counter == 0 and
        beer_counter == 0 and
        pint_counter == 0):
        print()
        print('Nemate nista naruceno!')
        print()
    else:
        print('-'*STARS)
        print(f'UKUPNO: {total_price} EUR)')

    print()
    print('-'*STARS)
    print()

    menu_choice = input('Selektirajte broj ispred narudzbe: ')

    match menu_choice:
        case '1':
            pizza_counter = pizza_counter + 1
            pizza_total_price = pizza_price * pizza_counter
            total_price = cake_total_price + wine_total_price + pizza_total_price + beer_total_price + pint_total_price
            print(f'CIJENA PIZZAe: {pizza_price} EUR')
            print(pizza)
        case '2':
            beer_counter += 1
            beer_total_price = beer_price * beer_counter
            total_price = cake_total_price + wine_total_price + pizza_total_price + beer_total_price + pint_total_price
            print(f'CIJENA PIVA: {beer_price} EUR')
            print(beer)
        case '3':
            pint_counter += 1
            pint_total_price = pint_price * pint_counter
            total_price = cake_total_price + wine_total_price + pizza_total_price + beer_total_price + pint_total_price
            print(f'CIJENA PINTe: {pint_price} EUR')
            print(pint)
        case '4':
            wine_counter += 1
            wine_total_price = wine_price * wine_counter
            total_price = cake_total_price + wine_total_price + pizza_total_price + beer_total_price + pint_total_price
            print(f'CIJENA VINA: {wine_price} EUR')
            print(wine)
        case '5':
            cake_counter += 1
            cake_total_price = cake_price * cake_counter
            total_price = cake_total_price + wine_total_price + pizza_total_price + beer_total_price + pint_total_price
            print(f'CIJENA KOLACA: {cake_price} EUR')
            print(cake)
        case '0':
            break
        case _:
            print('Na zalost taj izbor nemamo u ponudi! Izaberite nesto drugo.')


    order_next = input('Zelite li uzeti jos nesto? (da/ne): ')
    if order_next.lower() != 'da':
        break

# Pozdravna poruka
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
# Za one koji zele znati vise - if uvjet u jednoj liniji:
# os.system('cls' if os.name == 'nt' else 'clear')

print()
print('*'*STARS)
print()
print()
print('-'*STARS)
print()

print('Narucili ste:')
print('-'*STARS)
if cake_counter > 0:
    print(f'{cake_counter} x Cake ({cake_total_price} EUR)')
if wine_counter > 0:
    print(f'{wine_counter} x Wine ({wine_total_price} EUR)')
if pizza_counter > 0:
    print(f'{pizza_counter} x Pizza ({pizza_total_price} EUR)')
if beer_counter > 0:
    print(f'{beer_counter} x Beer ({beer_total_price} EUR)')
if pint_counter > 0:
    print(f'{pint_counter} x Pint ({pint_total_price} EUR)')

if (cake_counter == 0 and
    wine_counter == 0 and
    pizza_counter == 0 and
    beer_counter == 0 and
    pint_counter == 0):
    print()
    print('Nemate nista naruceno!')
    print()
else:
    print('-'*STARS)
    print(f'UKUPNO: {total_price} EUR)')

print()
print('-'*STARS)
print()

print('Hvala na posjeti, dodite nam opet!')
print()
print('*'*STARS)
print()
