

import telebot
from telebot import types

token = "8706132020:AAHsUQN3VSCCW7C7b4fKhQ7o5kWL-XLX28M"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    inline_m = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Andijon", callback_data="andijon")
    btn2 = types.InlineKeyboardButton("Buxoro", callback_data="buxoro")
    btn3 = types.InlineKeyboardButton("Farg'ona", callback_data="fargona")
    btn4 = types.InlineKeyboardButton("Jizzax", callback_data="jizzax")
    btn5 = types.InlineKeyboardButton("Xorazm", callback_data="xorazm")
    btn6 = types.InlineKeyboardButton("Namangan", callback_data="namangan")
    btn7 = types.InlineKeyboardButton("Navoiy", callback_data="navoiy")
    btn8 = types.InlineKeyboardButton("Qashqadaryo", callback_data="qashqadaryo")
    btn9 = types.InlineKeyboardButton("Samarqand", callback_data="samarqand")
    btn10 = types.InlineKeyboardButton("Sirdaryo", callback_data="sirdaryo")
    btn11 = types.InlineKeyboardButton("Surxondaryo", callback_data="surxondaryo")
    btn12 = types.InlineKeyboardButton("Toshkent", callback_data="toshkent")
    inline_m.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)

    bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=inline_m)

@bot.callback_query_handler(func=lambda call: True)
def getCall(call):
    if call.data == "andijon":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Andijon", callback_data="andijon_tuman")
        btn2 = types.InlineKeyboardButton("Asaka", callback_data="asaka")
        btn3 = types.InlineKeyboardButton("Baliqchi", callback_data="baliqchi")
        btn4 = types.InlineKeyboardButton("Bo'z", callback_data="boz")
        btn5 = types.InlineKeyboardButton("Buloqboshi", callback_data="buloqboshi")
        btn6 = types.InlineKeyboardButton("Izboskan", callback_data="izboskan")
        btn7 = types.InlineKeyboardButton("Jalaquduq", callback_data="jalaquduq")
        btn8 = types.InlineKeyboardButton("Marhamat", callback_data="marhamat")
        btn9 = types.InlineKeyboardButton("Oltinko'l", callback_data="oltinkol")
        btn10 = types.InlineKeyboardButton("Paxtaobod", callback_data="paxtaobod")
        btn11 = types.InlineKeyboardButton("Qo'rg'ontepa", callback_data="qorgontepa")
        btn12 = types.InlineKeyboardButton("Ulug'nor", callback_data="ulugnor")
        btn13 = types.InlineKeyboardButton("Xo'jaobod", callback_data="xojaobod")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)
        inline_m.add(btn13)

        bot.send_message(call.message.chat.id, "Andijon tumanlari:", reply_markup=inline_m)

    elif call.data == "andijon_tuman":
        bot.send_message(call.message.chat.id, "Andijon tumani tanlandi")

    elif call.data == "asaka":
        bot.send_message(call.message.chat.id, "Asaka tumani tanlandi")

    elif call.data == "baliqchi":
        bot.send_message(call.message.chat.id, "Baliqchi tumani tanlandi")

    elif call.data == "boz":
        bot.send_message(call.message.chat.id, "Bo'z tumani tanlandi")

    elif call.data == "buloqboshi":
        bot.send_message(call.message.chat.id, "Buloqboshi tumani tanlandi")

    elif call.data == "izboskan":
        bot.send_message(call.message.chat.id, "Izboskan tumani tanlandi")

    elif call.data == "jalaquduq":
        bot.send_message(call.message.chat.id, "Jalaquduq tumani tanlandi")

    elif call.data == "marhamat":
        bot.send_message(call.message.chat.id, "Marhamat tumani tanlandi")

    elif call.data == "oltinkol":
        bot.send_message(call.message.chat.id, "Oltinko'l tumani tanlandi")

    elif call.data == "paxtaobod":
        bot.send_message(call.message.chat.id, "Paxtaobod tumani tanlandi")

    elif call.data == "qorgontepa":
        bot.send_message(call.message.chat.id, "Qo'rg'ontepa tumani tanlandi")

    elif call.data == "ulugnor":
        bot.send_message(call.message.chat.id, "Ulug'nor tumani tanlandi")

    elif call.data == "xojaobod":
        bot.send_message(call.message.chat.id, "Xo'jaobod tumani tanlandi")    



    elif call.data == "buxoro":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Olot", callback_data="olot")
        btn2 = types.InlineKeyboardButton("Buxoro", callback_data="buxoro_tuman")
        btn3 = types.InlineKeyboardButton("G'ijduvon", callback_data="gijduvon")
        btn4 = types.InlineKeyboardButton("Jondor", callback_data="jondor")
        btn5 = types.InlineKeyboardButton("Kogon", callback_data="kogon_tuman")
        btn6 = types.InlineKeyboardButton("Qorako'l", callback_data="qorakol")
        btn7 = types.InlineKeyboardButton("Qorovulbozor", callback_data="qorovulbozor")
        btn8 = types.InlineKeyboardButton("Peshku", callback_data="peshku")
        btn9 = types.InlineKeyboardButton("Romitan", callback_data="romitan")
        btn10 = types.InlineKeyboardButton("Shofirkon", callback_data="shofirkon")
        btn11 = types.InlineKeyboardButton("Vobkent", callback_data="vobkent")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)

        bot.send_message(call.message.chat.id, "Buxoro tumanlari:", reply_markup=inline_m)

    elif call.data == "olot":
        bot.send_message(call.message.chat.id, "Olot tumani tanlandi")

    elif call.data == "buxoro_tuman":
        bot.send_message(call.message.chat.id, "Buxoro tumani tanlandi")

    elif call.data == "gijduvon":
        bot.send_message(call.message.chat.id, "G'ijduvon tumani tanlandi")

    elif call.data == "jondor":
        bot.send_message(call.message.chat.id, "Jondor tumani tanlandi")

    elif call.data == "kogon_tuman":
        bot.send_message(call.message.chat.id, "Kogon tumani tanlandi")

    elif call.data == "qorakol":
        bot.send_message(call.message.chat.id, "Qorako'l tumani tanlandi")

    elif call.data == "qorovulbozor":
        bot.send_message(call.message.chat.id, "Qorovulbozor tumani tanlandi")

    elif call.data == "peshku":
        bot.send_message(call.message.chat.id, "Peshku tumani tanlandi")

    elif call.data == "romitan":
        bot.send_message(call.message.chat.id, "Romitan tumani tanlandi")

    elif call.data == "shofirkon":
        bot.send_message(call.message.chat.id, "Shofirkon tumani tanlandi")

    elif call.data == "vobkent":
        bot.send_message(call.message.chat.id, "Vobkent tumani tanlandi")




    elif call.data == "fargona":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Oltiariq", callback_data="oltiariq")
        btn2 = types.InlineKeyboardButton("Bag'dod", callback_data="bagdod")
        btn3 = types.InlineKeyboardButton("Beshariq", callback_data="beshariq")
        btn4 = types.InlineKeyboardButton("Buvayda", callback_data="buvayda")
        btn5 = types.InlineKeyboardButton("Dang'ara", callback_data="dangara")
        btn6 = types.InlineKeyboardButton("Farg'ona", callback_data="fargona_tuman")
        btn7 = types.InlineKeyboardButton("Furqat", callback_data="furqat")
        btn8 = types.InlineKeyboardButton("Qo'shtepa", callback_data="qoshtepa")
        btn9 = types.InlineKeyboardButton("Quva", callback_data="quva")
        btn10 = types.InlineKeyboardButton("Rishton", callback_data="rishton")
        btn11 = types.InlineKeyboardButton("So'x", callback_data="sox")
        btn12 = types.InlineKeyboardButton("Toshloq", callback_data="toshloq")
        btn13 = types.InlineKeyboardButton("Uchko'prik", callback_data="uchkoprik")
        btn14 = types.InlineKeyboardButton("O'zbekiston", callback_data="ozbekiston")
        btn15 = types.InlineKeyboardButton("Yozyovon", callback_data="yozyovon")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)
        inline_m.add(btn13)
        inline_m.add(btn14)
        inline_m.add(btn15)

        bot.send_message(call.message.chat.id, "Farg'ona tumanlari:", reply_markup=inline_m)

    elif call.data == "oltiariq":
        bot.send_message(call.message.chat.id, "Oltiariq tumani tanlandi")

    elif call.data == "bagdod":
        bot.send_message(call.message.chat.id, "Bag'dod tumani tanlandi")

    elif call.data == "beshariq":
        bot.send_message(call.message.chat.id, "Beshariq tumani tanlandi")

    elif call.data == "buvayda":
        bot.send_message(call.message.chat.id, "Buvayda tumani tanlandi")

    elif call.data == "dangara":
        bot.send_message(call.message.chat.id, "Dang'ara tumani tanlandi")

    elif call.data == "fargona_tuman":
        bot.send_message(call.message.chat.id, "Farg'ona tumani tanlandi")

    elif call.data == "furqat":
        bot.send_message(call.message.chat.id, "Furqat tumani tanlandi")

    elif call.data == "qoshtepa":
        bot.send_message(call.message.chat.id, "Qo'shtepa tumani tanlandi")

    elif call.data == "quva":
        bot.send_message(call.message.chat.id, "Quva tumani tanlandi")

    elif call.data == "rishton":
        bot.send_message(call.message.chat.id, "Rishton tumani tanlandi")

    elif call.data == "sox":
        bot.send_message(call.message.chat.id, "So'x tumani tanlandi")

    elif call.data == "toshloq":
        bot.send_message(call.message.chat.id, "Toshloq tumani tanlandi")

    elif call.data == "uchkoprik":
        bot.send_message(call.message.chat.id, "Uchko'prik tumani tanlandi")

    elif call.data == "ozbekiston":
        bot.send_message(call.message.chat.id, "O'zbekiston tumani tanlandi")

    elif call.data == "yozyovon":
        bot.send_message(call.message.chat.id, "Yozyovon tumani tanlandi")

    elif call.data == "jizzax":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Arnasoy", callback_data="arnasoy")
        btn2 = types.InlineKeyboardButton("Baxmal", callback_data="baxmal")
        btn3 = types.InlineKeyboardButton("Do'stlik", callback_data="dostlik")
        btn4 = types.InlineKeyboardButton("Forish", callback_data="forish")
        btn5 = types.InlineKeyboardButton("G'allaorol", callback_data="gallaorol")
        btn6 = types.InlineKeyboardButton("Sharof Rashidov", callback_data="sharof_rashidov")
        btn7 = types.InlineKeyboardButton("Mirzacho'l", callback_data="mirzachol")
        btn8 = types.InlineKeyboardButton("Paxtakor", callback_data="paxtakor")
        btn9 = types.InlineKeyboardButton("Yangiobod", callback_data="yangiobod")
        btn10 = types.InlineKeyboardButton("Zomin", callback_data="zomin")
        btn11 = types.InlineKeyboardButton("Zafarobod", callback_data="zafarobod")
        btn12 = types.InlineKeyboardButton("Zarbdor", callback_data="zarbdor")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)

        bot.send_message(call.message.chat.id, "Jizzax tumanlari:", reply_markup=inline_m)

    elif call.data == "arnasoy":
        bot.send_message(call.message.chat.id, "Arnasoy tumani tanlandi")

    elif call.data == "baxmal":
        bot.send_message(call.message.chat.id, "Baxmal tumani tanlandi")

    elif call.data == "dostlik":
        bot.send_message(call.message.chat.id, "Do'stlik tumani tanlandi")

    elif call.data == "forish":
        bot.send_message(call.message.chat.id, "Forish tumani tanlandi")

    elif call.data == "gallaorol":
        bot.send_message(call.message.chat.id, "G'allaorol tumani tanlandi")

    elif call.data == "sharof_rashidov":
        bot.send_message(call.message.chat.id, "Sharof Rashidov tumani tanlandi")

    elif call.data == "mirzachol":
        bot.send_message(call.message.chat.id, "Mirzacho'l tumani tanlandi")

    elif call.data == "paxtakor":
        bot.send_message(call.message.chat.id, "Paxtakor tumani tanlandi")

    elif call.data == "yangiobod":
        bot.send_message(call.message.chat.id, "Yangiobod tumani tanlandi")

    elif call.data == "zomin":
        bot.send_message(call.message.chat.id, "Zomin tumani tanlandi")

    elif call.data == "zafarobod":
        bot.send_message(call.message.chat.id, "Zafarobod tumani tanlandi")

    elif call.data == "zarbdor":
        bot.send_message(call.message.chat.id, "Zarbdor tumani tanlandi")


    elif call.data == "xorazm":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Bog'ot", callback_data="bogot")
        btn2 = types.InlineKeyboardButton("Gurlan", callback_data="gurlan")
        btn3 = types.InlineKeyboardButton("Xonqa", callback_data="xonqa")
        btn4 = types.InlineKeyboardButton("Hazorasp", callback_data="hazorasp")
        btn5 = types.InlineKeyboardButton("Xiva", callback_data="xiva_tuman")
        btn6 = types.InlineKeyboardButton("Qo'shko'pir", callback_data="qoshkopir")
        btn7 = types.InlineKeyboardButton("Shovot", callback_data="shovot")
        btn8 = types.InlineKeyboardButton("Urganch", callback_data="urganch_tuman")
        btn9 = types.InlineKeyboardButton("Yangiariq", callback_data="yangiariq")
        btn10 = types.InlineKeyboardButton("Yangibozor", callback_data="yangibozor")
        btn11 = types.InlineKeyboardButton("Tuproqqal'a", callback_data="tuproqqala")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)

        bot.send_message(call.message.chat.id, "Xorazm tumanlari:", reply_markup=inline_m)

    elif call.data == "bogot":
        bot.send_message(call.message.chat.id, "Bog'ot tumani tanlandi")

    elif call.data == "gurlan":
        bot.send_message(call.message.chat.id, "Gurlan tumani tanlandi")

    elif call.data == "xonqa":
        bot.send_message(call.message.chat.id, "Xonqa tumani tanlandi")

    elif call.data == "hazorasp":
        bot.send_message(call.message.chat.id, "Hazorasp tumani tanlandi")

    elif call.data == "xiva_tuman":
        bot.send_message(call.message.chat.id, "Xiva tumani tanlandi")

    elif call.data == "qoshkopir":
        bot.send_message(call.message.chat.id, "Qo'shko'pir tumani tanlandi")

    elif call.data == "shovot":
        bot.send_message(call.message.chat.id, "Shovot tumani tanlandi")

    elif call.data == "urganch_tuman":
        bot.send_message(call.message.chat.id, "Urganch tumani tanlandi")

    elif call.data == "yangiariq":
        bot.send_message(call.message.chat.id, "Yangiariq tumani tanlandi")

    elif call.data == "yangibozor":
        bot.send_message(call.message.chat.id, "Yangibozor tumani tanlandi")

    elif call.data == "tuproqqala":
        bot.send_message(call.message.chat.id, "Tuproqqal'a tumani tanlandi")


    elif call.data == "namangan":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Chortoq", callback_data="chortoq")
        btn2 = types.InlineKeyboardButton("Chust", callback_data="chust")
        btn3 = types.InlineKeyboardButton("Kosonsoy", callback_data="kosonsoy")
        btn4 = types.InlineKeyboardButton("Mingbuloq", callback_data="mingbuloq")
        btn5 = types.InlineKeyboardButton("Namangan", callback_data="namangan_tuman")
        btn6 = types.InlineKeyboardButton("Norin", callback_data="norin")
        btn7 = types.InlineKeyboardButton("Pop", callback_data="pop")
        btn8 = types.InlineKeyboardButton("To'raqo'rg'on", callback_data="toraqorgon")
        btn9 = types.InlineKeyboardButton("Uchqo'rg'on", callback_data="uchqorgon")
        btn10 = types.InlineKeyboardButton("Uychi", callback_data="uychi")
        btn11 = types.InlineKeyboardButton("Yangiqo'rg'on", callback_data="yangiqorgon")
        btn12 = types.InlineKeyboardButton("Yangi Namangan", callback_data="yangi_namangan")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)

        bot.send_message(call.message.chat.id, "Namangan tumanlari:", reply_markup=inline_m)

    elif call.data == "chortoq":
        bot.send_message(call.message.chat.id, "Chortoq tumani tanlandi")

    elif call.data == "chust":
        bot.send_message(call.message.chat.id, "Chust tumani tanlandi")

    elif call.data == "kosonsoy":
        bot.send_message(call.message.chat.id, "Kosonsoy tumani tanlandi")

    elif call.data == "mingbuloq":
        bot.send_message(call.message.chat.id, "Mingbuloq tumani tanlandi")

    elif call.data == "namangan_tuman":
        bot.send_message(call.message.chat.id, "Namangan tumani tanlandi")

    elif call.data == "norin":
        bot.send_message(call.message.chat.id, "Norin tumani tanlandi")

    elif call.data == "pop":
        bot.send_message(call.message.chat.id, "Pop tumani tanlandi")

    elif call.data == "toraqorgon":
        bot.send_message(call.message.chat.id, "To'raqo'rg'on tumani tanlandi")

    elif call.data == "uchqorgon":
        bot.send_message(call.message.chat.id, "Uchqo'rg'on tumani tanlandi")

    elif call.data == "uychi":
        bot.send_message(call.message.chat.id, "Uychi tumani tanlandi")

    elif call.data == "yangiqorgon":
        bot.send_message(call.message.chat.id, "Yangiqo'rg'on tumani tanlandi")

    elif call.data == "yangi_namangan":
        bot.send_message(call.message.chat.id, "Yangi Namangan tumani tanlandi")


    elif call.data == "navoiy":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Konimex", callback_data="konimex")
        btn2 = types.InlineKeyboardButton("Qiziltepa", callback_data="qiziltepa")
        btn3 = types.InlineKeyboardButton("Xatirchi", callback_data="xatirchi")
        btn4 = types.InlineKeyboardButton("Navbahor", callback_data="navbahor")
        btn5 = types.InlineKeyboardButton("Karmana", callback_data="karmana")
        btn6 = types.InlineKeyboardButton("Nurota", callback_data="nurota")
        btn7 = types.InlineKeyboardButton("Tomdi", callback_data="tomdi")
        btn8 = types.InlineKeyboardButton("Uchquduq", callback_data="uchquduq")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)

        bot.send_message(call.message.chat.id, "Navoiy tumanlari:", reply_markup=inline_m)

    elif call.data == "konimex":
        bot.send_message(call.message.chat.id, "Konimex tumani tanlandi")

    elif call.data == "qiziltepa":
        bot.send_message(call.message.chat.id, "Qiziltepa tumani tanlandi")

    elif call.data == "xatirchi":
        bot.send_message(call.message.chat.id, "Xatirchi tumani tanlandi")

    elif call.data == "navbahor":
        bot.send_message(call.message.chat.id, "Navbahor tumani tanlandi")

    elif call.data == "karmana":
        bot.send_message(call.message.chat.id, "Karmana tumani tanlandi")

    elif call.data == "nurota":
        bot.send_message(call.message.chat.id, "Nurota tumani tanlandi")

    elif call.data == "tomdi":
        bot.send_message(call.message.chat.id, "Tomdi tumani tanlandi")

    elif call.data == "uchquduq":
        bot.send_message(call.message.chat.id, "Uchquduq tumani tanlandi")


    elif call.data == "qashqadaryo":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Chiroqchi", callback_data="chiroqchi")
        btn2 = types.InlineKeyboardButton("Dehqonobod", callback_data="dehqonobod")
        btn3 = types.InlineKeyboardButton("G'uzor", callback_data="guzor")
        btn4 = types.InlineKeyboardButton("Qamashi", callback_data="qamashi")
        btn5 = types.InlineKeyboardButton("Qarshi", callback_data="qarshi_tuman")
        btn6 = types.InlineKeyboardButton("Koson", callback_data="koson")
        btn7 = types.InlineKeyboardButton("Kasbi", callback_data="kasbi")
        btn8 = types.InlineKeyboardButton("Kitob", callback_data="kitob")
        btn9 = types.InlineKeyboardButton("Mirishkor", callback_data="mirishkor")
        btn10 = types.InlineKeyboardButton("Muborak", callback_data="muborak")
        btn11 = types.InlineKeyboardButton("Nishon", callback_data="nishon")
        btn12 = types.InlineKeyboardButton("Shahrisabz", callback_data="shahrisabz_tuman")
        btn13 = types.InlineKeyboardButton("Yakkabog'", callback_data="yakkabog")
        btn14 = types.InlineKeyboardButton("Ko'kdala", callback_data="kokdala")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)
        inline_m.add(btn13)
        inline_m.add(btn14)

        bot.send_message(call.message.chat.id, "Qashqadaryo tumanlari:", reply_markup=inline_m)

    elif call.data == "chiroqchi":
        bot.send_message(call.message.chat.id, "Chiroqchi tumani tanlandi")

    elif call.data == "dehqonobod":
        bot.send_message(call.message.chat.id, "Dehqonobod tumani tanlandi")

    elif call.data == "guzor":
        bot.send_message(call.message.chat.id, "G'uzor tumani tanlandi")

    elif call.data == "qamashi":
        bot.send_message(call.message.chat.id, "Qamashi tumani tanlandi")

    elif call.data == "qarshi_tuman":
        bot.send_message(call.message.chat.id, "Qarshi tumani tanlandi")

    elif call.data == "koson":
        bot.send_message(call.message.chat.id, "Koson tumani tanlandi")

    elif call.data == "kasbi":
        bot.send_message(call.message.chat.id, "Kasbi tumani tanlandi")

    elif call.data == "kitob":
        bot.send_message(call.message.chat.id, "Kitob tumani tanlandi")

    elif call.data == "mirishkor":
        bot.send_message(call.message.chat.id, "Mirishkor tumani tanlandi")

    elif call.data == "muborak":
        bot.send_message(call.message.chat.id, "Muborak tumani tanlandi")

    elif call.data == "nishon":
        bot.send_message(call.message.chat.id, "Nishon tumani tanlandi")

    elif call.data == "shahrisabz_tuman":
        bot.send_message(call.message.chat.id, "Shahrisabz tumani tanlandi")

    elif call.data == "yakkabog":
        bot.send_message(call.message.chat.id, "Yakkabog' tumani tanlandi")

    elif call.data == "kokdala":
        bot.send_message(call.message.chat.id, "Ko'kdala tumani tanlandi")


    elif call.data == "samarqand":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Bulung'ur", callback_data="bulungur")
        btn2 = types.InlineKeyboardButton("Ishtixon", callback_data="ishtixon")
        btn3 = types.InlineKeyboardButton("Jomboy", callback_data="jomboy")
        btn4 = types.InlineKeyboardButton("Kattaqo'rg'on", callback_data="kattaqorgon")
        btn5 = types.InlineKeyboardButton("Qo'shrabot", callback_data="qoshrabot")
        btn6 = types.InlineKeyboardButton("Narpay", callback_data="narpay")
        btn7 = types.InlineKeyboardButton("Nurobod", callback_data="nurobod")
        btn8 = types.InlineKeyboardButton("Oqdaryo", callback_data="oqdaryo")
        btn9 = types.InlineKeyboardButton("Paxtachi", callback_data="paxtachi")
        btn10 = types.InlineKeyboardButton("Payariq", callback_data="payariq")
        btn11 = types.InlineKeyboardButton("Pastdarg'om", callback_data="pastdargom")
        btn12 = types.InlineKeyboardButton("Samarqand", callback_data="samarqand_tuman")
        btn13 = types.InlineKeyboardButton("Toyloq", callback_data="toyloq")
        btn14 = types.InlineKeyboardButton("Urgut", callback_data="urgut")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)
        inline_m.add(btn13)
        inline_m.add(btn14)

        bot.send_message(call.message.chat.id, "Samarqand tumanlari:", reply_markup=inline_m)

    elif call.data == "bulungur":
        bot.send_message(call.message.chat.id, "Bulung'ur tumani tanlandi")

    elif call.data == "ishtixon":
        bot.send_message(call.message.chat.id, "Ishtixon tumani tanlandi")

    elif call.data == "jomboy":
        bot.send_message(call.message.chat.id, "Jomboy tumani tanlandi")

    elif call.data == "kattaqorgon":
        bot.send_message(call.message.chat.id, "Kattaqo'rg'on tumani tanlandi")

    elif call.data == "qoshrabot":
        bot.send_message(call.message.chat.id, "Qo'shrabot tumani tanlandi")

    elif call.data == "narpay":
        bot.send_message(call.message.chat.id, "Narpay tumani tanlandi")

    elif call.data == "nurobod":
        bot.send_message(call.message.chat.id, "Nurobod tumani tanlandi")

    elif call.data == "oqdaryo":
        bot.send_message(call.message.chat.id, "Oqdaryo tumani tanlandi")

    elif call.data == "paxtachi":
        bot.send_message(call.message.chat.id, "Paxtachi tumani tanlandi")

    elif call.data == "payariq":
        bot.send_message(call.message.chat.id, "Payariq tumani tanlandi")

    elif call.data == "pastdargom":
        bot.send_message(call.message.chat.id, "Pastdarg'om tumani tanlandi")

    elif call.data == "samarqand_tuman":
        bot.send_message(call.message.chat.id, "Samarqand tumani tanlandi")

    elif call.data == "toyloq":
        bot.send_message(call.message.chat.id, "Toyloq tumani tanlandi")

    elif call.data == "urgut":
        bot.send_message(call.message.chat.id, "Urgut tumani tanlandi")


    elif call.data == "sirdaryo":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Oqoltin", callback_data="oqoltin")
        btn2 = types.InlineKeyboardButton("Boyovut", callback_data="boyovut")
        btn3 = types.InlineKeyboardButton("Guliston", callback_data="guliston_tuman")
        btn4 = types.InlineKeyboardButton("Xovos", callback_data="xovos")
        btn5 = types.InlineKeyboardButton("Mirzaobod", callback_data="mirzaobod")
        btn6 = types.InlineKeyboardButton("Sardoba", callback_data="sardoba")
        btn7 = types.InlineKeyboardButton("Sayxunobod", callback_data="sayxunobod")
        btn8 = types.InlineKeyboardButton("Sirdaryo", callback_data="sirdaryo_tuman")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)

        bot.send_message(call.message.chat.id, "Sirdaryo tumanlari:", reply_markup=inline_m)

    elif call.data == "oqoltin":
        bot.send_message(call.message.chat.id, "Oqoltin tumani tanlandi")

    elif call.data == "boyovut":
        bot.send_message(call.message.chat.id, "Boyovut tumani tanlandi")

    elif call.data == "guliston_tuman":
        bot.send_message(call.message.chat.id, "Guliston tumani tanlandi")

    elif call.data == "xovos":
        bot.send_message(call.message.chat.id, "Xovos tumani tanlandi")

    elif call.data == "mirzaobod":
        bot.send_message(call.message.chat.id, "Mirzaobod tumani tanlandi")

    elif call.data == "sardoba":
        bot.send_message(call.message.chat.id, "Sardoba tumani tanlandi")

    elif call.data == "sayxunobod":
        bot.send_message(call.message.chat.id, "Sayxunobod tumani tanlandi")

    elif call.data == "sirdaryo_tuman":
        bot.send_message(call.message.chat.id, "Sirdaryo tumani tanlandi")


    elif call.data == "surxondaryo":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Angor", callback_data="angor")
        btn2 = types.InlineKeyboardButton("Bandixon", callback_data="bandixon")
        btn3 = types.InlineKeyboardButton("Boysun", callback_data="boysun")
        btn4 = types.InlineKeyboardButton("Denov", callback_data="denov")
        btn5 = types.InlineKeyboardButton("Jarqo'rg'on", callback_data="jarqorgon")
        btn6 = types.InlineKeyboardButton("Qiziriq", callback_data="qiziriq")
        btn7 = types.InlineKeyboardButton("Qumqo'rg'on", callback_data="qumqorgon")
        btn8 = types.InlineKeyboardButton("Muzrabot", callback_data="muzrabot")
        btn9 = types.InlineKeyboardButton("Oltinsoy", callback_data="oltinsoy")
        btn10 = types.InlineKeyboardButton("Sariosiyo", callback_data="sariosiyo")
        btn11 = types.InlineKeyboardButton("Sherobod", callback_data="sherobod")
        btn12 = types.InlineKeyboardButton("Sho'rchi", callback_data="shorchi")
        btn13 = types.InlineKeyboardButton("Termiz", callback_data="termiz_tuman")
        btn14 = types.InlineKeyboardButton("Uzun", callback_data="uzun")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)
        inline_m.add(btn13)
        inline_m.add(btn14)

        bot.send_message(call.message.chat.id, "Surxondaryo tumanlari:", reply_markup=inline_m)

    elif call.data == "angor":
        bot.send_message(call.message.chat.id, "Angor tumani tanlandi")

    elif call.data == "bandixon":
        bot.send_message(call.message.chat.id, "Bandixon tumani tanlandi")

    elif call.data == "boysun":
        bot.send_message(call.message.chat.id, "Boysun tumani tanlandi")

    elif call.data == "denov":
        bot.send_message(call.message.chat.id, "Denov tumani tanlandi")

    elif call.data == "jarqorgon":
        bot.send_message(call.message.chat.id, "Jarqo'rg'on tumani tanlandi")

    elif call.data == "qiziriq":
        bot.send_message(call.message.chat.id, "Qiziriq tumani tanlandi")

    elif call.data == "qumqorgon":
        bot.send_message(call.message.chat.id, "Qumqo'rg'on tumani tanlandi")

    elif call.data == "muzrabot":
        bot.send_message(call.message.chat.id, "Muzrabot tumani tanlandi")

    elif call.data == "oltinsoy":
        bot.send_message(call.message.chat.id, "Oltinsoy tumani tanlandi")

    elif call.data == "sariosiyo":
        bot.send_message(call.message.chat.id, "Sariosiyo tumani tanlandi")

    elif call.data == "sherobod":
        bot.send_message(call.message.chat.id, "Sherobod tumani tanlandi")

    elif call.data == "shorchi":
        bot.send_message(call.message.chat.id, "Sho'rchi tumani tanlandi")

    elif call.data == "termiz_tuman":
        bot.send_message(call.message.chat.id, "Termiz tumani tanlandi")

    elif call.data == "uzun":
        bot.send_message(call.message.chat.id, "Uzun tumani tanlandi")


    elif call.data == "toshkent":
        inline_m = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Bekobod", callback_data="bekobod")
        btn2 = types.InlineKeyboardButton("Bo'stonliq", callback_data="bostonliq")
        btn3 = types.InlineKeyboardButton("Bo'ka", callback_data="boka")
        btn4 = types.InlineKeyboardButton("Chinoz", callback_data="chinoz")
        btn5 = types.InlineKeyboardButton("Qibray", callback_data="qibray")
        btn6 = types.InlineKeyboardButton("Ohangaron", callback_data="ohangaron")
        btn7 = types.InlineKeyboardButton("Oqqo'rg'on", callback_data="oqqorgon")
        btn8 = types.InlineKeyboardButton("Parkent", callback_data="parkent")
        btn9 = types.InlineKeyboardButton("Piskent", callback_data="piskent")
        btn10 = types.InlineKeyboardButton("Quyi Chirchiq", callback_data="quyi_chirchiq")
        btn11 = types.InlineKeyboardButton("Zangiota", callback_data="zangiota")
        btn12 = types.InlineKeyboardButton("O'rta Chirchiq", callback_data="orta_chirchiq")
        btn13 = types.InlineKeyboardButton("Yangiyo'l", callback_data="yangiyol")
        btn14 = types.InlineKeyboardButton("Yuqori Chirchiq", callback_data="yuqori_chirchiq")
        btn15 = types.InlineKeyboardButton("Toshkent", callback_data="toshkent_tuman")

        inline_m.add(btn1)
        inline_m.add(btn2)
        inline_m.add(btn3)
        inline_m.add(btn4)
        inline_m.add(btn5)
        inline_m.add(btn6)
        inline_m.add(btn7)
        inline_m.add(btn8)
        inline_m.add(btn9)
        inline_m.add(btn10)
        inline_m.add(btn11)
        inline_m.add(btn12)
        inline_m.add(btn13)
        inline_m.add(btn14)
        inline_m.add(btn15)

        bot.send_message(call.message.chat.id, "Toshkent viloyati tumanlari:", reply_markup=inline_m)

    elif call.data == "bekobod":
        bot.send_message(call.message.chat.id, "Bekobod tumani tanlandi")

    elif call.data == "bostonliq":
        bot.send_message(call.message.chat.id, "Bo'stonliq tumani tanlandi")

    elif call.data == "boka":
        bot.send_message(call.message.chat.id, "Bo'ka tumani tanlandi")

    elif call.data == "chinoz":
        bot.send_message(call.message.chat.id, "Chinoz tumani tanlandi")

    elif call.data == "qibray":
        bot.send_message(call.message.chat.id, "Qibray tumani tanlandi")

    elif call.data == "ohangaron":
        bot.send_message(call.message.chat.id, "Ohangaron tumani tanlandi")

    elif call.data == "oqqorgon":
        bot.send_message(call.message.chat.id, "Oqqo'rg'on tumani tanlandi")

    elif call.data == "parkent":
        bot.send_message(call.message.chat.id, "Parkent tumani tanlandi")

    elif call.data == "piskent":
        bot.send_message(call.message.chat.id, "Piskent tumani tanlandi")

    elif call.data == "quyi_chirchiq":
        bot.send_message(call.message.chat.id, "Quyi Chirchiq tumani tanlandi")

    elif call.data == "zangiota":
        bot.send_message(call.message.chat.id, "Zangiota tumani tanlandi")

    elif call.data == "orta_chirchiq":
        bot.send_message(call.message.chat.id, "O'rta Chirchiq tumani tanlandi")

    elif call.data == "yangiyol":
        bot.send_message(call.message.chat.id, "Yangiyo'l tumani tanlandi")

    elif call.data == "yuqori_chirchiq":
        bot.send_message(call.message.chat.id, "Yuqori Chirchiq tumani tanlandi")

    elif call.data == "toshkent_tuman":
        bot.send_message(call.message.chat.id, "Toshkent tumani tanlandi")


bot.infinity_polling()








# import telebot
# from telebot import types

# token = "BOT_TOKEN"
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start(message):
#     inline_m = types.InlineKeyboardMarkup()

#     btn1 = types.InlineKeyboardButton("Samarqand", callback_data="samarqand")
#     btn2 = types.InlineKeyboardButton("Buxoro", callback_data="buxoro")

#     inline_m.add(btn1, btn2)

#     bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=inline_m)

# @bot.callback_query_handler(func=lambda call: True)
# def getCall(call):
#     if call.data == "samarqand":
#         inline_m = types.InlineKeyboardMarkup()

#         btn1 = types.InlineKeyboardButton("Bulung'ur", callback_data="bulungur")
#         btn2 = types.InlineKeyboardButton("Jomboy", callback_data="jomboy")
#         btn3 = types.InlineKeyboardButton("Urgut", callback_data="urgut")
#         btn4 = types.InlineKeyboardButton("Kattaqo'rg'on", callback_data="kattaqorgon")

#         inline_m.add(btn1)
#         inline_m.add(btn2)
#         inline_m.add(btn3)
#         inline_m.add(btn4)

#         bot.send_message(call.message.chat.id, "Samarqand tumanlari:", reply_markup=inline_m)

#     elif call.data == "buxoro":
#         bot.send_message(call.message.chat.id, "Buxoro tanlandi")

#     elif call.data == "bulungur":
#         bot.send_message(call.message.chat.id, "Bulung'ur tumani tanlandi")

#     elif call.data == "jomboy":
#         bot.send_message(call.message.chat.id, "Jomboy tumani tanlandi")

#     elif call.data == "urgut":
#         bot.send_message(call.message.chat.id, "Urgut tumani tanlandi")

#     elif call.data == "kattaqorgon":
#         bot.send_message(call.message.chat.id, "Kattaqo'rg'on tumani tanlandi")

# bot.infinity_polling()