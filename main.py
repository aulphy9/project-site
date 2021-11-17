from flask import Flask, render_template, request, url_for, send_from_directory
from scraper import stock_collector
from calculator import Stats_Calc, Discrete_Distribution
import os
#bruh moment numbers 5
#initializing the flask app
app = Flask(__name__)

#making the home page for users to land on
@app.route("/")
def homepage():
    return render_template("homepage.html")

#resume page
@app.route("/Resume")
def resume():
    filepath = '/static/files/'
    return send_from_directory(filepath, 'LiamAulphResume.pdf')

#transcript page
@app.route("/Transcript")
def transcript():
    return render_template("transcript.html")

#stock analyzer tool display page
@app.route("/Stock Analyzer", methods=["POST","GET"])
def stock_analyzer():
    #action to take with post method, gathering all stock info
    if request.method == "POST":
        ticker = request.form["ticker"]
        stock = stock_collector(ticker)
        name = stock.name
        price = stock.price
        PE_ratio = stock.PE_ratio
        beta = stock.beta
        yearly_change = stock.yearly_change
        institution_hold = stock.held_by_institutions
        shares_short = stock.shares_short
        dividend = stock.dividend
        status = stock.price_to_earnings()
        volatility = stock.volatility()
        short_status = stock.short_squeeze_status()
        result,explanation = stock.classification()

        #returning proper template and render and all variables associated with
        #selected stock
        return render_template("stock_analyzer_result.html",ticker=ticker,name=name,
        price=price,PE_ratio=PE_ratio,beta=beta,yearly_change=yearly_change,
        institution_hold=institution_hold,shares_short=shares_short,dividend=dividend,
        status=status,volatility=volatility,short_status=short_status,result=result,
        explanation=explanation)
    
    #returning template for initial page visit
    else:
        return render_template("stock_analyzer.html")

#stats calculator page
@app.route("/Statistics Calculator",methods=["POST","GET"])
def stats_calc():
    function_selected1 = ""
    function_selected = ""
    #handling our post requests
    if request.method == "POST":
        #getting which method was submitted and computing result
        if 'range' in request.form:
            result = Stats_Calc(request.form['range']).range_calc()
            function_selected = "Range: {}".format(result)
        elif 'mean_abs' in request.form:
            result = Stats_Calc(request.form['mean_abs']).MAD()
            function_selected = "Mean Absolute Deviation: {}".format(result)
        elif 'pop_var' in request.form:
            result = Stats_Calc(request.form['pop_var']).pop_var()
            function_selected = "Population Variance: {}".format(result)
        elif 'pop_stddev' in request.form:
            result = Stats_Calc(request.form['pop_stddev']).pop_StdDev()
            function_selected = "Population Standard Deviation: {}".format(result)
        elif 'z_scores' in request.form:
            result = Stats_Calc(request.form['z_scores']).z_scores()
            function_selected = "Z-Scores: {}".format(result)
        elif 'coef' in request.form:
            result = Stats_Calc(request.form['coef']).pop_coef_var()
            function_selected = "Coeficient of Variation: {}".format(result)
        elif 'range_submit_v' in request.form:
            result = Discrete_Distribution(request.form['range_v'],request.form['probs_v']).variance()
            function_selected1 = "Variance: {}".format(result)
        elif 'range_submit_std' in request.form:
            result = Discrete_Distribution(request.form['range_std'],request.form['probs_std']).std_dev()
            function_selected1 = "Standard Deviation: {}".format(result)
        elif 'range_submit_b' in request.form:
            result = Discrete_Distribution(None,None).binomial_single(request.form['range_o'],request.form['probs_b'],request.form['x_b'])
            function_selected1 = "Binomial Answer: {}".format(result)
        elif 'p_submit' in request.form:
            result = Discrete_Distribution(None,None).poisson_solver(request.form['x_p'],request.form['lam'])
            function_selected1 = "Poisson Result: {}".format(result)
        return render_template("stats_calc_result.html",function_selected=function_selected,function_selected1=function_selected1)
        
    #return initial page for first visit
    else:
        return render_template("stats_calc.html")

#code to run the site from the terminal
if __name__ == '__main__':
    app.run(debug=True)

