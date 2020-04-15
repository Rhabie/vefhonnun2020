import os
from flask import Flask, render_template, request, json
from datetime import datetime
import os
import urllib.request
app = Flask(__name__)

#with urllib.request.urlopen("https://apis.is/currency/") as url
#    data = json.loads(url.read().decode())

@app.route('/')
def homepage():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <p><a                                                                                                                                                                                                                                                                                                                                                                                     href="/sida2" title="Síða 2">Síða 2 </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <img src="http://loremflickr.com/600/400" />
    """ #.format(time=the_time)
#render_template('skra.html', data=data) VERKEFNI3
@app.route('/sida2')
def page2():
    return """
    <h1>Síða 2</h1>
    <p><a href="/" title="Forsíða">Forsíða </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <p>It is currently cathour.</p>
    <img src="http://loremflickr.com/600/400" />
    """ 
@app.route('/sida3')
def page3():
    return render_template('sida3.html')
@app.errorhandler(404)
def pagnotfound(error):
    return render_template('pagenotfound.html')
frettir=[
    ["0","Fleiri smitaðir en af SARS-Veirunni",
    "Bandarísk yfirvöld hafa fyrirskipað þegnum sínum að forðast ferðalög til Kína eftir að Alþjóðaheilbrigðismálastofnunin (WHO) lýsti yfir neyðarástandi á heimsvísu vegna kórónaveirunnar sem á upptök sín í kínversku borginni Wuhan.",
    "dsg@frettir.is"],
    ["1","Sveppi fór í risa­ferðalag með pabba sín­um",
    "Sverr­ir Þór Sverris­son sjón­varps­stjarna og grín­ari fór í heims­reisu í fyrra með pabba sín­um, Sverri Friðjóns­syni. Feðgarn­ir gerðu sjón­varpsþætti um ferðalagið sem sýnd­ir verða í Sjón­varpi Sím­ans Premium í fe­brú­ar. ",
    "rih@frettir.is"],
    ["2","Vaknaði við kyn­ferðis­lega áreitni í flugi",
    "Hin 22 ára gamla kona var í flugi með Spi­rit Air­lines frá Atlanta til Detroit í Banda­ríkj­un­um þegar at­vikið átti sér stað. Hún vaknaði stuttu fyr­ir lend­ingu og seg­ist hafa vaknað við það þegar karl­maður strauk á henni lærið. ",
    "mts@frettir.is"],
    ["3","Hafþór Júlí­us ger­ist leiðsögumaður um Ísland"
    ,"Ferðin virðist ekki vera fyr­ir hinn venju­lega ferðamann held­ur miðuð að vel efnuðum ferðamönn­um sem hafa áhuga á að upp­lifa Ísland á ann­an hátt. Um er að ræða sex daga ferð dag­ana 20. til 25. sept­em­ber. ",
    "seh@frettir.is"],
    ["4","Sagt þær væru of stór­ar fyr­ir viðskiptafar­rýmið"
    ,"Þrjár ástr­alsk­ar kon­ur segj­ast hafa verið al­gjör­lega niður­lægðar af starfs­fólki Thai Airways þegar þeim var meinaður aðgang­ur að viðskiptafar­rým­is­sæt­um sín­um vegna stærðar sinn­ar. ",
    "msd@frettir.is"]]
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, use_reloader=True)