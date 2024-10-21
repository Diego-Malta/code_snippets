from translate import Translator

# Configura a tradução
s = Translator(from_lang='en', to_lang='pt-br')

# Traduz texto desejado
res = s.translate("Hey guys")

# Mostra a tradução
print(res)
