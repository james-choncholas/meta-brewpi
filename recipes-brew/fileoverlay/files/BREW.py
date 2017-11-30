import os
import time
import threading
from subprocess import call
from flask import Flask, render_template, request, redirect, url_for
from PIDBrewLoop import PIDBrewLoop


######WEB ACTIVITIES###########
#Note: Since the webpage is set to refresh every 10s,
#       a post or get request should not be sent more than once,
#       so after a request, the page is redirected to itself (no request so refresh doesn't re-request)
app = Flask(__name__)

@app.route("/", methods=['POST','GET']) #the home page
def BrewMe():

    #button looks like <input type="submit" value="Submit" name="changeSetPT">
    if (request.args.get('changeSetPT') == 'Submit') :
        BrewLoop.SetTemperatureSetPt(float(request.args.get('newSetPT')))
        return redirect(url_for('BrewMe'))

    #button looks like <input type="submit" name="stopHeat" value="Turn Off Heat">
    if (request.args.get('stopHeat') == 'Turn Off Heat') :
        BrewLoop.SetTemperatureSetPt(0)
        return redirect(url_for('BrewMe'))

    #button looks like <input type="submit" name="boil" Value="Boil">
    if (request.args.get('boil') == 'Boil') :
        BrewLoop.SetTemperatureSetPt(100)
        return redirect(url_for('BrewMe'))
    else:
        pass #unknown request attempted

    #variables available in HTML
    BrewLoop.lock.acquire()
    templateData = {
       'tempData'   : BrewLoop.TempHistory,
       'setpt'      : str(BrewLoop.TemperatureSetPt),
       'vRegSetPt'  : str(BrewLoop.CurVRegSetPt),
    }
    BrewLoop.lock.release()
    return render_template('BrewMe.html', **templateData)

def CheckNetwork():
    # Repeat every 30 seconds
    threading.Timer(30, CheckNetwork).start()

    # Check that the network is still up
    call(["/brewpi/restartNetwork.sh"])


########Start Threads#############
BrewLoop = PIDBrewLoop()
BrewLoop.start()
CheckNetwork()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
