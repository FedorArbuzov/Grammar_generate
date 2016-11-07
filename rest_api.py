from bottle import route, run
import wikipedia
wikipedia.set_lang("en")
@route('/quest/<quest_id:int>')
def quest(quest_id):
    if quest_id == 1:
        arr = {
            "name" : "Мекка Москвы",
            "desc" : "Докажите всем, что вы были в Москве. Посетите Кремль и Москва-сити.",
            "long_desc": "jnfgjbgtjn;juegrijoegrjioegrijogrejnogrejnoregjngrejngre",
            "events":
                [
                    {
                        "lat" : 55.7522,
                        "long": 37.6156 ,
                        "desc":  "Кремль",
                        "dist": 30,
                        "question" : None
                    },
                    {
                        "lat": 55.7480861,
                        "long": 37.5379497,
                        "desc":  "Москва-сити",
                        "dist": 30,
                        "question": None
                    }
                ]
        }
    return arr

run(host='31.135.85.7', port=9583, debug=True)
