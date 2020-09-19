from flask import Flask
from string import Template
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Corona Scare Level Map</h1>
    
    <link rel="stylesheet" href="style.css">
    <div class="flight-types">
        <input type="radio" name="flight-type" value="coach" id="coach" />
        <label for="coach">
        Coach
        </label>
        <input type="radio" name="flight-type" value="business" id="business" checked />
        <label for="business">
        Business
        </label>
        <input type="radio" name="flight-type" value="first" id="first" />
        <label for="first">
        First
        </label>
    </div>

    <iframe title="Corona Scare Map" aria-label="Map" id="datawrapper-chart-7nMGn" src="https://datawrapper.dwcdn.net/7nMGn/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="undefined"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
    </script>
    """


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)