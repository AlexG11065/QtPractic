import translators as ts


a = "Добрый день"


params = {
    'query_text': a,
    'from_language': 'ru',
    'to_language': 'ar',
    'update_session': 1,

}
print(params['from_language'])

for value in params.values():
    print(value)

# print(ts.translate_text(**params, translator='bing'))

# import translators as ts
#
# q_text = 'Привет'
# q_html = "Дом"
#
# print(ts.translate_text(q_text))
# print(ts.translate_html(q_html, translator='alibaba'))

