from flask import Flask, render_template
import pygal
import psycopg2

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
# #
# # @app.route('/about')
# # def about():
# #     return 'WELCOME TO ABOUT'
# #
# # @app.route('/contacts')
# # def contacts():
# #     return 'WELCOME TO CONTACTS'
# #
# # @app.route('/services')
# # def services():
# #     return 'WELCOME TO SERVICES'
# #
# # @app.route('/templating')
# # def templating():
# #           return render_template('index.html')
#
# @app.route('/index')
# def index():
#     # conn= psycopg2.connect("dbname= 'sales_demo' user='postgres' host='localhost' password= 'Vampires57'")
#     #conn= psycopg2.connect("dbname= 'd8edv01tcu5qdj' user='ageqcumlyzcwen' host='ec2-18-210-51-239.compute-1.amazonaws.com' password= 'c0fd2b34c2cae895435eec2378588310bbf2d601fcecd9282126e3dc1b274854'")
#     #'cur= conn.cursor()
#
#     #cur.execute("""SELECT EXTRACT (MONTH FROM sares.created_at) AS MONTHS , SUM (sares.quantity) as "TOTAL SALES" FROM public.sares GROUP BY months ORDER BY months""")
#
#     #cur.execute("""""")
#     #records=cur.fetchall()
#     #
#     data = [('January',10),
#             ('February', 20),
#             ('March', 30),
#             ('April', 23),
#             ('May', 32),
#             ('June', 24),
#             ('August', 45),
#             ('September', 25),
#             ('October', 10),
#             ('November', 15),
#             ('December', 24)
#             ]
#
#     data1 = []
#     data2 = []
#
#     for i in data:
#         data1.append(i[0])
#         data2.append(i[1])
#
#     list = [('Internet Explorer', 19.5), ('Firefox', 36.6), ('Chrome', 36.3), ('Safari', 4.5), ('Opera', 2.3)]
#     pie_chart = pygal.Pie()
#     pie_chart.title = 'Browser usage in February 2012 (%)'
#     pie_chart.add(list[0][0], list[0][1])
#     pie_chart.add(list[1][0], list[1][1])
#     pie_chart.add(list[2][0], list[2][1])
#     pie_chart.add(list[3][0], list[3][1])
#     pie_chart.add(list[4][0], list[4][1])
#
#     pie_data = pie_chart.render_data_uri()
#
#     browser = pygal.Line()
#     browser.title = 'Change of Programming languages over the years'
#     browser.x_labels = data1
#     browser.add('Sales', data2)
#     line_graph = browser.render_data_uri()
#
#     return render_template('index.html', line_graph=line_graph, pie_data=pie_data)

@app.route('/about')
def about():
    # conn = psycopg2.connect("dbname= 'postgres' user='postgres' host='localhost' password= 'Vampires57'")
    # conn= psycopg2.connect("dbname= d8edv01tcu5qdj user=ageqcumlyzcwen' host='ec2-18-210-51-239.compute-1.amazonaws.com' password= 'c0fd2b34c2cae895435eec2378588310bbf2d601fcecd9282126e3dc1b274854'")
    conn= psycopg2.connect ("dbname=d8edv01tcu5qdj user=ageqcumlyzcwen host=ec2-18-210-51-239.compute-1.amazonaws.com password=c0fd2b34c2cae895435eec2378588310bbf2d601fcecd9282126e3dc1b274854")
    cur = conn.cursor()
    # create table script
    cur.execute("""create table sales (
	id INT,
	inv_id INT,
	cust_id INT,
	quantity INT,
	created_at DATE
    );
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (1, 1, 1, 85, '29/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (2, 2, 2, 17, '17/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (3, 3, 3, 98, '2/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (4, 4, 4, 28, '7/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (5, 5, 5, 72, '29/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (6, 6, 6, 69, '24/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (7, 7, 7, 82, '18/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (8, 8, 8, 100, '17/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (9, 9, 9, 81, '27/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (10, 10, 10, 98, '7/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (11, 11, 11, 21, '2/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (12, 12, 12, 14, '17/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (13, 13, 13, 89, '2/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (14, 14, 14, 4, '7/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (15, 15, 15, 9, '10/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (16, 16, 16, 52, '8/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (17, 17, 17, 95, '18/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (18, 18, 18, 32, '26/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (19, 19, 19, 27, '8/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (20, 20, 20, 59, '17/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (21, 21, 21, 1, '4/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (22, 22, 22, 47, '23/7/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (23, 23, 23, 56, '14/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (24, 24, 24, 57, '25/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (25, 25, 25, 71, '12/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (26, 26, 26, 92, '21/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (27, 27, 27, 88, '9/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (28, 28, 28, 50, '9/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (29, 29, 29, 8, '28/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (30, 30, 30, 63, '10/8/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (31, 31, 31, 14, '22/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (32, 32, 32, 85, '19/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (33, 33, 33, 91, '1/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (34, 34, 34, 26, '9/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (35, 35, 35, 75, '30/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (36, 36, 36, 17, '20/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (37, 37, 37, 43, '29/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (38, 38, 38, 4, '13/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (39, 39, 39, 100, '11/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (40, 40, 40, 72, '17/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (41, 41, 41, 3, '4/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (42, 42, 42, 99, '20/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (43, 43, 43, 62, '3/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (44, 44, 44, 99, '3/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (45, 45, 45, 100, '4/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (46, 46, 46, 7, '16/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (47, 47, 47, 94, '22/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (48, 48, 48, 41, '8/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (49, 49, 49, 34, '24/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (50, 50, 50, 99, '17/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (51, 51, 51, 87, '16/4/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (52, 52, 52, 53, '31/10/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (53, 53, 53, 68, '18/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (54, 54, 54, 87, '5/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (55, 55, 55, 72, '19/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (56, 56, 56, 91, '3/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (57, 57, 57, 98, '3/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (58, 58, 58, 91, '7/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (59, 59, 59, 29, '14/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (60, 60, 60, 7, '16/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (61, 61, 61, 23, '13/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (62, 62, 62, 23, '25/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (63, 63, 63, 4, '30/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (64, 64, 64, 80, '27/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (65, 65, 65, 69, '8/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (66, 66, 66, 56, '19/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (67, 67, 67, 88, '2/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (68, 68, 68, 85, '11/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (69, 69, 69, 91, '21/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (70, 70, 70, 39, '11/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (71, 71, 71, 48, '15/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (72, 72, 72, 72, '22/2/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (73, 73, 73, 7, '8/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (74, 74, 74, 6, '26/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (75, 75, 75, 29, '27/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (76, 76, 76, 32, '31/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (77, 77, 77, 34, '26/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (78, 78, 78, 66, '24/11/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (79, 79, 79, 56, '17/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (80, 80, 80, 93, '27/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (81, 81, 81, 52, '28/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (82, 82, 82, 14, '25/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (83, 83, 83, 26, '23/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (84, 84, 84, 64, '7/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (85, 85, 85, 19, '27/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (86, 86, 86, 16, '30/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (87, 87, 87, 72, '24/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (88, 88, 88, 47, '1/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (89, 89, 89, 44, '20/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (90, 90, 90, 21, '6/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (91, 91, 91, 15, '10/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (92, 92, 92, 62, '15/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (93, 93, 93, 90, '15/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (94, 94, 94, 4, '16/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (95, 95, 95, 82, '22/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (96, 96, 96, 48, '2/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (97, 97, 97, 52, '11/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (98, 98, 98, 10, '23/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (99, 99, 99, 51, '21/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (100, 100, 100, 39, '21/9/2013');
         

    """)

    # cur.execute("insert into customers (id, first_name, last_name, email, address) values ('Hestia', 'Espine', 'hespine0@seesaa.net', '778 Buena Vista Trail');")

    conn.commit()
    cur.close()
    conn.close()
#     cur.execute("""SELECT EXTRACT (MONTH FROM sares.created_at) AS MONTHS ,
# SUM (sares.quantity) as "TOTAL SALES" FROM public.sares
# GROUP BY months
# ORDER BY months""")

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
#     ,title= 'Sheer Excitement',line_graph=line_graph
#
    return render_template('about.html')

# @app.route('/services')
# def services():
#

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run()
