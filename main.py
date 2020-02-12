from flask import Flask, render_template
import pygal
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
#
# @app.route('/about')
# def about():
#     return 'WELCOME TO ABOUT'
#
# @app.route('/contacts')
# def contacts():
#     return 'WELCOME TO CONTACTS'
#
# @app.route('/services')
# def services():
#     return 'WELCOME TO SERVICES'
#
# @app.route('/templating')
# def templating():
#           return render_template('index.html')

@app.route('/index')
def index():
    # conn= psycopg2.connect("dbname= 'sales_demo' user='postgres' host='localhost' password= 'Vampires57'")
    #conn= psycopg2.connect("dbname= 'd8edv01tcu5qdj' user='ageqcumlyzcwen' host='ec2-18-210-51-239.compute-1.amazonaws.com' password= 'c0fd2b34c2cae895435eec2378588310bbf2d601fcecd9282126e3dc1b274854'")
    #'cur= conn.cursor()

    #cur.execute("""SELECT EXTRACT (MONTH FROM sares.created_at) AS MONTHS , SUM (sares.quantity) as "TOTAL SALES" FROM public.sares GROUP BY months ORDER BY months""")

    #cur.execute("""""")
    #records=cur.fetchall()
    #
    data = [('January',10),
            ('February', 20),
            ('March', 30),
            ('April', 23),
            ('May', 32),
            ('June', 24),
            ('August', 45),
            ('September', 25),
            ('October', 10),
            ('November', 15),
            ('December', 24)
            ]

    data1 = []
    data2 = []

    for i in data:
        data1.append(i[0])
        data2.append(i[1])

    list = [('Internet Explorer', 19.5), ('Firefox', 36.6), ('Chrome', 36.3), ('Safari', 4.5), ('Opera', 2.3)]
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (%)'
    pie_chart.add(list[0][0], list[0][1])
    pie_chart.add(list[1][0], list[1][1])
    pie_chart.add(list[2][0], list[2][1])
    pie_chart.add(list[3][0], list[3][1])
    pie_chart.add(list[4][0], list[4][1])

    pie_data = pie_chart.render_data_uri()

    browser = pygal.Line()
    browser.title = 'Change of Programming languages over the years'
    browser.x_labels = data1
    browser.add('Sales', data2)
    line_graph = browser.render_data_uri()

    return render_template('index.html', line_graph=line_graph, pie_data=pie_data)

# @app.route('/about')
# # def about():
#     #conn = psycopg2.connect("dbname= 'postgres' user='postgres' host='localhost' password= 'Vampires57'")
#     #cur = conn.cursor
#     #cur.execute("""SELECT EXTRACT (MONTH FROM sares.created_at) AS MONTHS ,
# # SUM (sares.quantity) as "TOTAL SALES" FROM public.sares
# # GROUP BY months
# # ORDER BY months""")
#
#     #records = cur.fetchall()
#     # data1 = []
#     # data2 = []
#     # for i in data:
#     #     data1.append(i[0])
#     #     data2.append(i[1])
#
#     #print(data1)
#     #print(data2)
#     #
#     # browser = pygal.Line()
#     # browser.title = 'Change of Programming languages over the years'
#     # browser.x_labels = data1
#     # browser.add('Sales', data2)
#     # line_graph = browser.render_data_uri()
#
#     # return render_template('about.html',title= 'Sheer Excitement',line_graph=line_graph)

# @app.route('/services')
# def services():
#

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run()
