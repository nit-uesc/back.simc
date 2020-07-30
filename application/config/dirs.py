"""."""
import os
# import sys
# from subprocess import call


# if not os.path.exists('src/processed_data/corpus'):
#     os.makedirs('src/processed_data/corpus')

# if not os.path.exists('src/processed_data/summary'):
#     os.makedirs('src/processed_data/summary')

if not os.path.exists('public'):
    os.makedirs('public')

if not os.path.exists('public/xml'):
    os.makedirs('public/xml')

if not os.path.exists('public/json'):
    os.makedirs('public/json')

if not os.path.exists('public/photos'):
    os.makedirs('public/photos')

if not os.path.exists('public/thumbnails-70x70'):
    os.makedirs('public/thumbnails-70x70')

if not os.path.exists('public/thumbnails-150x150'):
    os.makedirs('public/thumbnails-150x150')

# print('Coletando curriculos')
# call(["php", "src/1_coleta/coleta_curriculos.php", "cpfs.txt"])

# print('Coletando codigos')
# import coleta_codigo

# print('Coletando fotos')
# import coleta_fotos

# import thumbnail_generator
# print('Gerando thumbnails 70x70')
# thumbnail_generator.generate(70, 'logo', '../public/thumbnails-70x70/')
# thumbnail_generator.generate_folder(70, '../public/fotos/', '../public/thumbnails-70x70/')
# print('Gerando thumbnails 150x150')
# thumbnail_generator.generate(150, 'logo', '../public/thumbnails-150x150/')
# thumbnail_generator.generate_folder(150, '../public/fotos/','../public/thumbnails-150x150/')

# print('Convertendo curriculos para json')
# import converter_curriculos_para_json

# print('Analisando curriculos')
# import extrai_corpus_e_sumarios
