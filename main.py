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
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (1, 1, 1, 99, '26/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (2, 2, 2, 78, '11/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (3, 3, 3, 28, '3/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (4, 4, 4, 70, '21/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (5, 5, 5, 84, '9/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (6, 6, 6, 46, '24/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (7, 7, 7, 29, '8/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (8, 8, 8, 20, '1/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (9, 9, 9, 48, '6/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (10, 10, 10, 61, '16/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (11, 11, 11, 39, '23/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (12, 12, 12, 28, '12/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (13, 13, 13, 70, '12/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (14, 14, 14, 54, '10/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (15, 15, 15, 4, '27/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (16, 16, 16, 62, '24/11/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (17, 17, 17, 71, '21/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (18, 18, 18, 26, '3/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (19, 19, 19, 60, '19/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (20, 20, 20, 15, '7/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (21, 21, 21, 35, '11/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (22, 22, 22, 3, '31/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (23, 23, 23, 96, '24/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (24, 24, 24, 12, '28/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (25, 25, 25, 91, '9/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (26, 26, 26, 5, '20/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (27, 27, 27, 48, '29/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (28, 28, 28, 98, '17/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (29, 29, 29, 4, '4/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (30, 30, 30, 7, '24/10/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (31, 31, 31, 16, '16/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (32, 32, 32, 67, '14/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (33, 33, 33, 1, '20/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (34, 34, 34, 19, '23/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (35, 35, 35, 25, '21/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (36, 36, 36, 27, '21/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (37, 37, 37, 7, '8/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (38, 38, 38, 80, '5/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (39, 39, 39, 57, '21/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (40, 40, 40, 65, '7/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (41, 41, 41, 26, '10/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (42, 42, 42, 85, '7/12/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (43, 43, 43, 86, '27/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (44, 44, 44, 40, '30/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (45, 45, 45, 26, '28/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (46, 46, 46, 51, '17/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (47, 47, 47, 13, '30/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (48, 48, 48, 52, '25/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (49, 49, 49, 23, '4/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (50, 50, 50, 8, '14/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (51, 51, 51, 98, '15/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (52, 52, 52, 13, '2/1/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (53, 53, 53, 23, '5/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (54, 54, 54, 32, '4/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (55, 55, 55, 73, '29/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (56, 56, 56, 20, '1/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (57, 57, 57, 39, '20/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (58, 58, 58, 70, '19/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (59, 59, 59, 91, '24/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (60, 60, 60, 53, '5/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (61, 61, 61, 2, '31/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (62, 62, 62, 40, '1/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (63, 63, 63, 88, '7/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (64, 64, 64, 35, '13/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (65, 65, 65, 40, '20/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (66, 66, 66, 20, '4/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (67, 67, 67, 52, '1/3/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (68, 68, 68, 26, '31/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (69, 69, 69, 96, '27/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (70, 70, 70, 8, '24/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (71, 71, 71, 62, '5/2/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (72, 72, 72, 72, '6/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (73, 73, 73, 63, '24/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (74, 74, 74, 5, '29/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (75, 75, 75, 4, '15/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (76, 76, 76, 34, '23/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (77, 77, 77, 22, '23/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (78, 78, 78, 100, '24/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (79, 79, 79, 3, '1/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (80, 80, 80, 16, '11/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (81, 81, 81, 38, '16/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (82, 82, 82, 25, '26/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (83, 83, 83, 34, '21/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (84, 84, 84, 87, '29/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (85, 85, 85, 37, '7/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (86, 86, 86, 17, '19/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (87, 87, 87, 92, '7/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (88, 88, 88, 95, '6/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (89, 89, 89, 66, '11/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (90, 90, 90, 9, '13/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (91, 91, 91, 18, '27/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (92, 92, 92, 46, '22/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (93, 93, 93, 16, '4/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (94, 94, 94, 33, '8/2/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (95, 95, 95, 52, '2/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (96, 96, 96, 69, '23/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (97, 97, 97, 38, '25/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (98, 98, 98, 99, '17/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (99, 99, 99, 85, '29/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (100, 100, 100, 71, '7/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (101, 101, 101, 5, '7/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (102, 102, 102, 3, '15/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (103, 103, 103, 100, '13/7/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (104, 104, 104, 18, '14/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (105, 105, 105, 63, '3/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (106, 106, 106, 88, '18/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (107, 107, 107, 28, '23/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (108, 108, 108, 84, '20/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (109, 109, 109, 30, '4/7/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (110, 110, 110, 89, '4/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (111, 111, 111, 35, '4/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (112, 112, 112, 19, '17/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (113, 113, 113, 81, '31/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (114, 114, 114, 20, '20/2/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (115, 115, 115, 50, '9/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (116, 116, 116, 42, '18/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (117, 117, 117, 12, '10/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (118, 118, 118, 95, '6/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (119, 119, 119, 2, '31/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (120, 120, 120, 23, '9/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (121, 121, 121, 47, '4/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (122, 122, 122, 10, '13/1/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (123, 123, 123, 32, '14/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (124, 124, 124, 32, '21/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (125, 125, 125, 32, '7/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (126, 126, 126, 94, '11/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (127, 127, 127, 75, '18/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (128, 128, 128, 56, '17/6/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (129, 129, 129, 72, '6/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (130, 130, 130, 52, '6/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (131, 131, 131, 98, '13/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (132, 132, 132, 2, '15/2/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (133, 133, 133, 96, '31/7/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (134, 134, 134, 49, '27/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (135, 135, 135, 50, '14/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (136, 136, 136, 40, '23/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (137, 137, 137, 53, '17/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (138, 138, 138, 11, '22/9/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (139, 139, 139, 68, '21/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (140, 140, 140, 38, '29/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (141, 141, 141, 53, '30/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (142, 142, 142, 5, '9/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (143, 143, 143, 46, '31/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (144, 144, 144, 76, '28/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (145, 145, 145, 2, '18/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (146, 146, 146, 84, '9/1/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (147, 147, 147, 28, '20/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (148, 148, 148, 57, '11/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (149, 149, 149, 51, '13/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (150, 150, 150, 86, '31/10/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (151, 151, 151, 42, '25/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (152, 152, 152, 87, '27/2/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (153, 153, 153, 33, '8/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (154, 154, 154, 5, '1/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (155, 155, 155, 74, '23/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (156, 156, 156, 27, '1/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (157, 157, 157, 13, '10/2/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (158, 158, 158, 88, '12/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (159, 159, 159, 67, '24/10/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (160, 160, 160, 33, '22/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (161, 161, 161, 74, '4/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (162, 162, 162, 68, '17/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (163, 163, 163, 83, '21/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (164, 164, 164, 80, '8/7/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (165, 165, 165, 86, '19/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (166, 166, 166, 37, '22/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (167, 167, 167, 72, '26/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (168, 168, 168, 56, '9/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (169, 169, 169, 67, '11/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (170, 170, 170, 89, '17/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (171, 171, 171, 48, '14/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (172, 172, 172, 20, '26/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (173, 173, 173, 8, '19/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (174, 174, 174, 36, '16/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (175, 175, 175, 6, '14/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (176, 176, 176, 1, '24/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (177, 177, 177, 31, '25/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (178, 178, 178, 15, '14/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (179, 179, 179, 91, '22/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (180, 180, 180, 41, '21/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (181, 181, 181, 50, '26/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (182, 182, 182, 27, '20/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (183, 183, 183, 20, '24/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (184, 184, 184, 50, '14/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (185, 185, 185, 17, '10/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (186, 186, 186, 16, '2/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (187, 187, 187, 88, '30/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (188, 188, 188, 71, '13/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (189, 189, 189, 9, '14/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (190, 190, 190, 62, '26/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (191, 191, 191, 25, '15/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (192, 192, 192, 45, '5/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (193, 193, 193, 51, '1/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (194, 194, 194, 53, '23/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (195, 195, 195, 21, '21/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (196, 196, 196, 92, '12/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (197, 197, 197, 18, '24/2/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (198, 198, 198, 76, '5/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (199, 199, 199, 36, '9/4/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (200, 200, 200, 18, '8/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (201, 201, 201, 90, '8/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (202, 202, 202, 19, '9/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (203, 203, 203, 70, '28/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (204, 204, 204, 86, '16/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (205, 205, 205, 8, '3/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (206, 206, 206, 53, '21/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (207, 207, 207, 57, '30/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (208, 208, 208, 51, '3/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (209, 209, 209, 78, '2/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (210, 210, 210, 99, '2/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (211, 211, 211, 45, '20/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (212, 212, 212, 19, '20/11/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (213, 213, 213, 12, '18/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (214, 214, 214, 78, '18/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (215, 215, 215, 44, '29/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (216, 216, 216, 3, '26/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (217, 217, 217, 25, '1/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (218, 218, 218, 36, '27/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (219, 219, 219, 51, '23/11/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (220, 220, 220, 58, '6/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (221, 221, 221, 20, '31/8/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (222, 222, 222, 19, '27/2/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (223, 223, 223, 27, '1/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (224, 224, 224, 22, '17/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (225, 225, 225, 28, '24/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (226, 226, 226, 31, '3/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (227, 227, 227, 27, '2/1/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (228, 228, 228, 25, '27/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (229, 229, 229, 8, '5/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (230, 230, 230, 40, '14/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (231, 231, 231, 2, '23/11/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (232, 232, 232, 49, '3/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (233, 233, 233, 11, '26/12/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (234, 234, 234, 19, '2/8/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (235, 235, 235, 57, '11/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (236, 236, 236, 3, '6/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (237, 237, 237, 13, '23/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (238, 238, 238, 17, '20/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (239, 239, 239, 92, '17/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (240, 240, 240, 3, '4/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (241, 241, 241, 79, '14/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (242, 242, 242, 22, '17/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (243, 243, 243, 54, '17/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (244, 244, 244, 38, '31/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (245, 245, 245, 30, '28/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (246, 246, 246, 21, '21/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (247, 247, 247, 29, '10/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (248, 248, 248, 2, '14/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (249, 249, 249, 41, '24/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (250, 250, 250, 16, '18/7/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (251, 251, 251, 55, '17/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (252, 252, 252, 33, '25/3/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (253, 253, 253, 90, '11/11/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (254, 254, 254, 17, '16/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (255, 255, 255, 60, '15/2/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (256, 256, 256, 26, '15/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (257, 257, 257, 2, '26/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (258, 258, 258, 17, '16/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (259, 259, 259, 47, '20/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (260, 260, 260, 91, '25/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (261, 261, 261, 31, '25/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (262, 262, 262, 8, '29/10/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (263, 263, 263, 21, '3/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (264, 264, 264, 84, '19/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (265, 265, 265, 2, '11/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (266, 266, 266, 15, '17/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (267, 267, 267, 48, '13/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (268, 268, 268, 20, '5/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (269, 269, 269, 37, '12/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (270, 270, 270, 24, '9/1/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (271, 271, 271, 76, '7/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (272, 272, 272, 57, '21/9/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (273, 273, 273, 59, '13/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (274, 274, 274, 96, '4/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (275, 275, 275, 13, '8/1/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (276, 276, 276, 29, '13/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (277, 277, 277, 65, '23/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (278, 278, 278, 82, '10/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (279, 279, 279, 42, '19/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (280, 280, 280, 25, '18/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (281, 281, 281, 66, '23/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (282, 282, 282, 52, '23/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (283, 283, 283, 28, '10/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (284, 284, 284, 8, '23/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (285, 285, 285, 95, '11/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (286, 286, 286, 26, '22/12/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (287, 287, 287, 74, '2/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (288, 288, 288, 41, '8/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (289, 289, 289, 66, '5/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (290, 290, 290, 79, '15/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (291, 291, 291, 41, '14/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (292, 292, 292, 91, '9/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (293, 293, 293, 25, '6/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (294, 294, 294, 97, '11/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (295, 295, 295, 23, '23/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (296, 296, 296, 39, '10/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (297, 297, 297, 75, '14/8/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (298, 298, 298, 98, '5/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (299, 299, 299, 78, '10/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (300, 300, 300, 1, '5/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (301, 301, 301, 24, '14/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (302, 302, 302, 51, '5/11/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (303, 303, 303, 54, '2/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (304, 304, 304, 98, '11/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (305, 305, 305, 13, '14/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (306, 306, 306, 72, '31/7/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (307, 307, 307, 30, '30/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (308, 308, 308, 63, '20/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (309, 309, 309, 31, '21/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (310, 310, 310, 72, '11/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (311, 311, 311, 47, '24/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (312, 312, 312, 78, '28/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (313, 313, 313, 32, '1/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (314, 314, 314, 14, '27/7/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (315, 315, 315, 71, '22/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (316, 316, 316, 79, '9/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (317, 317, 317, 5, '10/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (318, 318, 318, 16, '2/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (319, 319, 319, 52, '22/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (320, 320, 320, 24, '22/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (321, 321, 321, 97, '8/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (322, 322, 322, 2, '30/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (323, 323, 323, 2, '5/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (324, 324, 324, 58, '3/1/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (325, 325, 325, 63, '26/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (326, 326, 326, 89, '14/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (327, 327, 327, 97, '17/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (328, 328, 328, 29, '17/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (329, 329, 329, 23, '11/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (330, 330, 330, 97, '19/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (331, 331, 331, 23, '9/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (332, 332, 332, 99, '25/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (333, 333, 333, 19, '23/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (334, 334, 334, 35, '26/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (335, 335, 335, 72, '5/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (336, 336, 336, 91, '4/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (337, 337, 337, 49, '25/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (338, 338, 338, 62, '11/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (339, 339, 339, 42, '27/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (340, 340, 340, 24, '4/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (341, 341, 341, 39, '16/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (342, 342, 342, 97, '6/1/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (343, 343, 343, 9, '23/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (344, 344, 344, 9, '8/9/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (345, 345, 345, 9, '26/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (346, 346, 346, 50, '17/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (347, 347, 347, 95, '6/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (348, 348, 348, 56, '12/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (349, 349, 349, 89, '26/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (350, 350, 350, 6, '26/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (351, 351, 351, 31, '7/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (352, 352, 352, 56, '10/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (353, 353, 353, 58, '18/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (354, 354, 354, 4, '2/10/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (355, 355, 355, 78, '13/1/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (356, 356, 356, 74, '4/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (357, 357, 357, 85, '22/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (358, 358, 358, 72, '1/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (359, 359, 359, 75, '5/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (360, 360, 360, 9, '12/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (361, 361, 361, 75, '3/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (362, 362, 362, 85, '8/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (363, 363, 363, 13, '11/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (364, 364, 364, 30, '17/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (365, 365, 365, 53, '18/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (366, 366, 366, 37, '18/5/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (367, 367, 367, 79, '9/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (368, 368, 368, 65, '28/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (369, 369, 369, 61, '30/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (370, 370, 370, 46, '21/4/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (371, 371, 371, 55, '23/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (372, 372, 372, 86, '4/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (373, 373, 373, 56, '5/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (374, 374, 374, 45, '5/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (375, 375, 375, 92, '25/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (376, 376, 376, 77, '8/7/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (377, 377, 377, 62, '26/11/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (378, 378, 378, 10, '31/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (379, 379, 379, 5, '13/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (380, 380, 380, 49, '12/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (381, 381, 381, 61, '2/3/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (382, 382, 382, 43, '2/11/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (383, 383, 383, 13, '18/1/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (384, 384, 384, 75, '17/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (385, 385, 385, 73, '21/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (386, 386, 386, 89, '17/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (387, 387, 387, 66, '3/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (388, 388, 388, 11, '20/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (389, 389, 389, 71, '29/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (390, 390, 390, 36, '2/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (391, 391, 391, 97, '30/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (392, 392, 392, 92, '28/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (393, 393, 393, 30, '21/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (394, 394, 394, 92, '8/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (395, 395, 395, 78, '28/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (396, 396, 396, 60, '29/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (397, 397, 397, 76, '20/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (398, 398, 398, 21, '27/3/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (399, 399, 399, 73, '2/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (400, 400, 400, 65, '22/10/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (401, 401, 401, 31, '28/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (402, 402, 402, 35, '2/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (403, 403, 403, 17, '4/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (404, 404, 404, 92, '9/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (405, 405, 405, 9, '9/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (406, 406, 406, 1, '16/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (407, 407, 407, 92, '17/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (408, 408, 408, 47, '6/2/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (409, 409, 409, 66, '9/3/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (410, 410, 410, 1, '22/4/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (411, 411, 411, 41, '6/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (412, 412, 412, 15, '6/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (413, 413, 413, 55, '25/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (414, 414, 414, 74, '11/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (415, 415, 415, 24, '15/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (416, 416, 416, 90, '2/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (417, 417, 417, 24, '20/11/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (418, 418, 418, 67, '13/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (419, 419, 419, 6, '27/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (420, 420, 420, 5, '29/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (421, 421, 421, 29, '8/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (422, 422, 422, 23, '27/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (423, 423, 423, 52, '27/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (424, 424, 424, 24, '8/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (425, 425, 425, 88, '19/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (426, 426, 426, 47, '4/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (427, 427, 427, 57, '16/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (428, 428, 428, 77, '17/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (429, 429, 429, 65, '9/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (430, 430, 430, 85, '25/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (431, 431, 431, 55, '4/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (432, 432, 432, 9, '19/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (433, 433, 433, 49, '21/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (434, 434, 434, 21, '1/9/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (435, 435, 435, 8, '25/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (436, 436, 436, 47, '1/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (437, 437, 437, 67, '19/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (438, 438, 438, 34, '26/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (439, 439, 439, 5, '18/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (440, 440, 440, 85, '14/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (441, 441, 441, 87, '14/7/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (442, 442, 442, 95, '24/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (443, 443, 443, 33, '6/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (444, 444, 444, 22, '1/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (445, 445, 445, 15, '4/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (446, 446, 446, 68, '28/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (447, 447, 447, 68, '14/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (448, 448, 448, 74, '14/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (449, 449, 449, 27, '23/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (450, 450, 450, 9, '20/2/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (451, 451, 451, 12, '16/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (452, 452, 452, 4, '24/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (453, 453, 453, 13, '31/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (454, 454, 454, 66, '12/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (455, 455, 455, 4, '29/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (456, 456, 456, 78, '16/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (457, 457, 457, 54, '10/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (458, 458, 458, 84, '26/11/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (459, 459, 459, 12, '10/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (460, 460, 460, 49, '18/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (461, 461, 461, 34, '24/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (462, 462, 462, 9, '7/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (463, 463, 463, 18, '10/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (464, 464, 464, 60, '17/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (465, 465, 465, 69, '2/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (466, 466, 466, 21, '8/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (467, 467, 467, 3, '26/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (468, 468, 468, 79, '21/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (469, 469, 469, 77, '27/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (470, 470, 470, 3, '22/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (471, 471, 471, 42, '24/1/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (472, 472, 472, 92, '26/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (473, 473, 473, 16, '13/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (474, 474, 474, 10, '22/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (475, 475, 475, 55, '20/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (476, 476, 476, 64, '2/2/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (477, 477, 477, 11, '1/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (478, 478, 478, 77, '28/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (479, 479, 479, 27, '17/4/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (480, 480, 480, 50, '13/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (481, 481, 481, 50, '7/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (482, 482, 482, 83, '13/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (483, 483, 483, 84, '16/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (484, 484, 484, 100, '17/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (485, 485, 485, 4, '10/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (486, 486, 486, 26, '8/1/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (487, 487, 487, 52, '24/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (488, 488, 488, 66, '30/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (489, 489, 489, 99, '28/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (490, 490, 490, 33, '17/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (491, 491, 491, 100, '27/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (492, 492, 492, 91, '15/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (493, 493, 493, 96, '7/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (494, 494, 494, 70, '13/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (495, 495, 495, 2, '22/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (496, 496, 496, 43, '8/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (497, 497, 497, 17, '20/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (498, 498, 498, 23, '16/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (499, 499, 499, 37, '24/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (500, 500, 500, 93, '24/11/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (501, 501, 501, 2, '20/1/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (502, 502, 502, 15, '3/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (503, 503, 503, 4, '16/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (504, 504, 504, 61, '27/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (505, 505, 505, 26, '15/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (506, 506, 506, 32, '31/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (507, 507, 507, 100, '8/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (508, 508, 508, 97, '29/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (509, 509, 509, 29, '6/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (510, 510, 510, 47, '18/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (511, 511, 511, 96, '9/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (512, 512, 512, 83, '18/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (513, 513, 513, 69, '8/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (514, 514, 514, 22, '24/11/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (515, 515, 515, 8, '14/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (516, 516, 516, 1, '27/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (517, 517, 517, 56, '24/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (518, 518, 518, 62, '1/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (519, 519, 519, 44, '17/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (520, 520, 520, 82, '20/1/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (521, 521, 521, 86, '21/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (522, 522, 522, 72, '15/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (523, 523, 523, 91, '17/4/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (524, 524, 524, 30, '10/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (525, 525, 525, 23, '18/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (526, 526, 526, 75, '22/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (527, 527, 527, 69, '16/4/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (528, 528, 528, 2, '30/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (529, 529, 529, 69, '13/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (530, 530, 530, 90, '29/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (531, 531, 531, 32, '29/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (532, 532, 532, 35, '18/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (533, 533, 533, 48, '23/11/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (534, 534, 534, 88, '18/12/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (535, 535, 535, 65, '4/8/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (536, 536, 536, 12, '19/3/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (537, 537, 537, 88, '14/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (538, 538, 538, 13, '13/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (539, 539, 539, 62, '27/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (540, 540, 540, 36, '26/6/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (541, 541, 541, 69, '26/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (542, 542, 542, 83, '15/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (543, 543, 543, 37, '21/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (544, 544, 544, 21, '5/2/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (545, 545, 545, 69, '18/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (546, 546, 546, 99, '27/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (547, 547, 547, 79, '4/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (548, 548, 548, 2, '23/7/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (549, 549, 549, 62, '1/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (550, 550, 550, 75, '4/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (551, 551, 551, 14, '16/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (552, 552, 552, 22, '24/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (553, 553, 553, 29, '13/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (554, 554, 554, 75, '30/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (555, 555, 555, 8, '27/1/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (556, 556, 556, 16, '22/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (557, 557, 557, 4, '31/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (558, 558, 558, 32, '18/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (559, 559, 559, 91, '20/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (560, 560, 560, 28, '7/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (561, 561, 561, 60, '21/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (562, 562, 562, 31, '14/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (563, 563, 563, 70, '20/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (564, 564, 564, 66, '31/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (565, 565, 565, 76, '28/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (566, 566, 566, 75, '3/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (567, 567, 567, 34, '26/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (568, 568, 568, 29, '27/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (569, 569, 569, 84, '15/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (570, 570, 570, 71, '23/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (571, 571, 571, 25, '31/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (572, 572, 572, 33, '5/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (573, 573, 573, 52, '5/3/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (574, 574, 574, 65, '9/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (575, 575, 575, 81, '30/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (576, 576, 576, 8, '20/11/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (577, 577, 577, 38, '15/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (578, 578, 578, 81, '1/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (579, 579, 579, 33, '11/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (580, 580, 580, 80, '16/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (581, 581, 581, 82, '14/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (582, 582, 582, 69, '5/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (583, 583, 583, 27, '29/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (584, 584, 584, 73, '13/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (585, 585, 585, 1, '26/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (586, 586, 586, 46, '12/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (587, 587, 587, 60, '3/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (588, 588, 588, 41, '4/10/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (589, 589, 589, 76, '7/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (590, 590, 590, 100, '26/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (591, 591, 591, 65, '2/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (592, 592, 592, 79, '3/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (593, 593, 593, 1, '25/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (594, 594, 594, 39, '27/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (595, 595, 595, 35, '8/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (596, 596, 596, 99, '30/11/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (597, 597, 597, 48, '25/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (598, 598, 598, 88, '21/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (599, 599, 599, 25, '1/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (600, 600, 600, 44, '6/11/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (601, 601, 601, 43, '30/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (602, 602, 602, 28, '6/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (603, 603, 603, 14, '26/1/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (604, 604, 604, 60, '2/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (605, 605, 605, 59, '16/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (606, 606, 606, 85, '29/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (607, 607, 607, 26, '20/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (608, 608, 608, 34, '29/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (609, 609, 609, 77, '10/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (610, 610, 610, 27, '2/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (611, 611, 611, 76, '14/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (612, 612, 612, 30, '12/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (613, 613, 613, 37, '26/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (614, 614, 614, 97, '19/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (615, 615, 615, 95, '16/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (616, 616, 616, 44, '23/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (617, 617, 617, 66, '26/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (618, 618, 618, 52, '10/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (619, 619, 619, 87, '18/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (620, 620, 620, 61, '10/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (621, 621, 621, 62, '12/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (622, 622, 622, 71, '4/12/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (623, 623, 623, 45, '9/10/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (624, 624, 624, 35, '15/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (625, 625, 625, 88, '25/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (626, 626, 626, 10, '9/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (627, 627, 627, 43, '3/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (628, 628, 628, 4, '10/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (629, 629, 629, 45, '20/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (630, 630, 630, 55, '2/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (631, 631, 631, 76, '13/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (632, 632, 632, 18, '30/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (633, 633, 633, 83, '3/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (634, 634, 634, 73, '8/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (635, 635, 635, 75, '22/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (636, 636, 636, 18, '24/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (637, 637, 637, 40, '24/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (638, 638, 638, 59, '15/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (639, 639, 639, 52, '22/7/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (640, 640, 640, 65, '9/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (641, 641, 641, 67, '28/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (642, 642, 642, 7, '7/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (643, 643, 643, 41, '6/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (644, 644, 644, 71, '1/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (645, 645, 645, 8, '19/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (646, 646, 646, 51, '3/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (647, 647, 647, 98, '11/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (648, 648, 648, 19, '5/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (649, 649, 649, 53, '20/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (650, 650, 650, 86, '27/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (651, 651, 651, 67, '14/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (652, 652, 652, 95, '13/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (653, 653, 653, 80, '4/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (654, 654, 654, 26, '30/6/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (655, 655, 655, 21, '1/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (656, 656, 656, 46, '28/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (657, 657, 657, 85, '28/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (658, 658, 658, 38, '26/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (659, 659, 659, 87, '25/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (660, 660, 660, 70, '12/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (661, 661, 661, 83, '26/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (662, 662, 662, 37, '18/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (663, 663, 663, 53, '31/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (664, 664, 664, 38, '29/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (665, 665, 665, 8, '14/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (666, 666, 666, 14, '7/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (667, 667, 667, 77, '5/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (668, 668, 668, 21, '12/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (669, 669, 669, 80, '9/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (670, 670, 670, 38, '30/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (671, 671, 671, 60, '18/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (672, 672, 672, 2, '30/9/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (673, 673, 673, 91, '22/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (674, 674, 674, 37, '25/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (675, 675, 675, 94, '27/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (676, 676, 676, 1, '17/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (677, 677, 677, 77, '8/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (678, 678, 678, 86, '15/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (679, 679, 679, 34, '27/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (680, 680, 680, 12, '18/1/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (681, 681, 681, 39, '12/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (682, 682, 682, 99, '19/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (683, 683, 683, 54, '13/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (684, 684, 684, 85, '24/2/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (685, 685, 685, 68, '10/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (686, 686, 686, 12, '12/3/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (687, 687, 687, 92, '1/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (688, 688, 688, 39, '22/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (689, 689, 689, 20, '20/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (690, 690, 690, 81, '19/10/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (691, 691, 691, 5, '24/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (692, 692, 692, 34, '27/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (693, 693, 693, 61, '29/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (694, 694, 694, 1, '27/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (695, 695, 695, 5, '27/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (696, 696, 696, 33, '17/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (697, 697, 697, 44, '16/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (698, 698, 698, 24, '3/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (699, 699, 699, 78, '11/11/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (700, 700, 700, 38, '20/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (701, 701, 701, 93, '26/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (702, 702, 702, 64, '13/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (703, 703, 703, 100, '7/11/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (704, 704, 704, 29, '30/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (705, 705, 705, 30, '7/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (706, 706, 706, 54, '6/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (707, 707, 707, 29, '26/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (708, 708, 708, 4, '18/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (709, 709, 709, 40, '27/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (710, 710, 710, 28, '21/2/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (711, 711, 711, 43, '2/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (712, 712, 712, 96, '14/1/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (713, 713, 713, 69, '29/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (714, 714, 714, 39, '9/7/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (715, 715, 715, 13, '7/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (716, 716, 716, 52, '12/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (717, 717, 717, 6, '28/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (718, 718, 718, 76, '5/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (719, 719, 719, 48, '17/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (720, 720, 720, 16, '15/8/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (721, 721, 721, 68, '29/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (722, 722, 722, 91, '13/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (723, 723, 723, 65, '6/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (724, 724, 724, 60, '23/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (725, 725, 725, 79, '26/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (726, 726, 726, 78, '28/4/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (727, 727, 727, 70, '16/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (728, 728, 728, 86, '16/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (729, 729, 729, 50, '10/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (730, 730, 730, 35, '15/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (731, 731, 731, 48, '26/4/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (732, 732, 732, 38, '31/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (733, 733, 733, 76, '1/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (734, 734, 734, 18, '3/8/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (735, 735, 735, 9, '8/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (736, 736, 736, 90, '22/1/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (737, 737, 737, 83, '23/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (738, 738, 738, 42, '2/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (739, 739, 739, 97, '28/2/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (740, 740, 740, 85, '28/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (741, 741, 741, 1, '9/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (742, 742, 742, 74, '22/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (743, 743, 743, 62, '11/3/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (744, 744, 744, 5, '25/8/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (745, 745, 745, 46, '2/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (746, 746, 746, 56, '22/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (747, 747, 747, 100, '11/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (748, 748, 748, 72, '14/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (749, 749, 749, 11, '27/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (750, 750, 750, 29, '28/3/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (751, 751, 751, 52, '2/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (752, 752, 752, 95, '3/10/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (753, 753, 753, 40, '25/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (754, 754, 754, 7, '28/12/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (755, 755, 755, 62, '16/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (756, 756, 756, 57, '14/7/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (757, 757, 757, 46, '3/1/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (758, 758, 758, 54, '26/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (759, 759, 759, 82, '3/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (760, 760, 760, 95, '16/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (761, 761, 761, 57, '16/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (762, 762, 762, 90, '19/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (763, 763, 763, 31, '28/3/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (764, 764, 764, 44, '13/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (765, 765, 765, 22, '8/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (766, 766, 766, 98, '1/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (767, 767, 767, 55, '15/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (768, 768, 768, 52, '26/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (769, 769, 769, 89, '10/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (770, 770, 770, 34, '26/6/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (771, 771, 771, 41, '30/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (772, 772, 772, 19, '26/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (773, 773, 773, 75, '26/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (774, 774, 774, 10, '6/10/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (775, 775, 775, 31, '20/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (776, 776, 776, 87, '17/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (777, 777, 777, 7, '22/1/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (778, 778, 778, 78, '24/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (779, 779, 779, 15, '12/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (780, 780, 780, 81, '22/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (781, 781, 781, 86, '9/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (782, 782, 782, 94, '8/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (783, 783, 783, 94, '13/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (784, 784, 784, 68, '7/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (785, 785, 785, 58, '8/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (786, 786, 786, 80, '19/3/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (787, 787, 787, 44, '28/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (788, 788, 788, 63, '3/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (789, 789, 789, 71, '12/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (790, 790, 790, 89, '21/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (791, 791, 791, 45, '13/8/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (792, 792, 792, 65, '23/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (793, 793, 793, 62, '17/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (794, 794, 794, 18, '3/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (795, 795, 795, 33, '14/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (796, 796, 796, 40, '25/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (797, 797, 797, 45, '9/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (798, 798, 798, 59, '6/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (799, 799, 799, 71, '30/10/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (800, 800, 800, 99, '1/2/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (801, 801, 801, 1, '17/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (802, 802, 802, 8, '6/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (803, 803, 803, 63, '20/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (804, 804, 804, 69, '8/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (805, 805, 805, 28, '4/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (806, 806, 806, 68, '27/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (807, 807, 807, 33, '5/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (808, 808, 808, 83, '15/9/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (809, 809, 809, 97, '30/10/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (810, 810, 810, 94, '23/6/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (811, 811, 811, 6, '26/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (812, 812, 812, 18, '14/1/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (813, 813, 813, 90, '5/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (814, 814, 814, 11, '3/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (815, 815, 815, 95, '16/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (816, 816, 816, 43, '24/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (817, 817, 817, 73, '22/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (818, 818, 818, 50, '14/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (819, 819, 819, 54, '13/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (820, 820, 820, 68, '21/3/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (821, 821, 821, 18, '30/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (822, 822, 822, 58, '11/10/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (823, 823, 823, 79, '8/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (824, 824, 824, 33, '17/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (825, 825, 825, 29, '2/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (826, 826, 826, 35, '3/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (827, 827, 827, 3, '15/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (828, 828, 828, 91, '13/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (829, 829, 829, 13, '23/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (830, 830, 830, 17, '8/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (831, 831, 831, 62, '25/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (832, 832, 832, 40, '2/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (833, 833, 833, 20, '18/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (834, 834, 834, 23, '1/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (835, 835, 835, 84, '5/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (836, 836, 836, 2, '19/9/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (837, 837, 837, 5, '30/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (838, 838, 838, 92, '26/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (839, 839, 839, 50, '4/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (840, 840, 840, 95, '1/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (841, 841, 841, 38, '27/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (842, 842, 842, 79, '25/7/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (843, 843, 843, 63, '11/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (844, 844, 844, 25, '11/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (845, 845, 845, 18, '23/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (846, 846, 846, 27, '19/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (847, 847, 847, 15, '26/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (848, 848, 848, 87, '16/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (849, 849, 849, 76, '1/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (850, 850, 850, 100, '23/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (851, 851, 851, 60, '6/12/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (852, 852, 852, 82, '18/6/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (853, 853, 853, 48, '29/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (854, 854, 854, 28, '8/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (855, 855, 855, 51, '31/10/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (856, 856, 856, 69, '17/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (857, 857, 857, 68, '24/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (858, 858, 858, 77, '13/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (859, 859, 859, 72, '25/3/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (860, 860, 860, 52, '24/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (861, 861, 861, 80, '11/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (862, 862, 862, 84, '7/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (863, 863, 863, 17, '14/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (864, 864, 864, 41, '20/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (865, 865, 865, 53, '8/6/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (866, 866, 866, 26, '14/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (867, 867, 867, 12, '13/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (868, 868, 868, 82, '6/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (869, 869, 869, 83, '24/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (870, 870, 870, 69, '11/9/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (871, 871, 871, 11, '1/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (872, 872, 872, 10, '15/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (873, 873, 873, 6, '2/12/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (874, 874, 874, 69, '29/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (875, 875, 875, 44, '22/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (876, 876, 876, 5, '21/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (877, 877, 877, 72, '30/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (878, 878, 878, 85, '20/7/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (879, 879, 879, 97, '2/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (880, 880, 880, 92, '1/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (881, 881, 881, 32, '15/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (882, 882, 882, 82, '12/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (883, 883, 883, 90, '23/2/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (884, 884, 884, 13, '2/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (885, 885, 885, 61, '22/3/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (886, 886, 886, 17, '8/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (887, 887, 887, 43, '14/4/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (888, 888, 888, 56, '25/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (889, 889, 889, 58, '13/2/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (890, 890, 890, 40, '15/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (891, 891, 891, 89, '13/11/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (892, 892, 892, 38, '24/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (893, 893, 893, 63, '12/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (894, 894, 894, 83, '23/5/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (895, 895, 895, 36, '28/1/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (896, 896, 896, 1, '21/8/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (897, 897, 897, 25, '15/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (898, 898, 898, 27, '21/5/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (899, 899, 899, 6, '30/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (900, 900, 900, 65, '2/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (901, 901, 901, 67, '26/9/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (902, 902, 902, 56, '10/2/2019');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (903, 903, 903, 1, '1/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (904, 904, 904, 50, '3/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (905, 905, 905, 100, '22/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (906, 906, 906, 77, '1/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (907, 907, 907, 48, '28/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (908, 908, 908, 31, '9/5/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (909, 909, 909, 29, '26/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (910, 910, 910, 82, '1/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (911, 911, 911, 60, '10/8/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (912, 912, 912, 54, '5/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (913, 913, 913, 88, '8/4/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (914, 914, 914, 72, '26/6/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (915, 915, 915, 73, '27/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (916, 916, 916, 99, '4/8/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (917, 917, 917, 93, '26/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (918, 918, 918, 74, '21/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (919, 919, 919, 41, '20/10/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (920, 920, 920, 52, '26/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (921, 921, 921, 70, '22/6/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (922, 922, 922, 67, '13/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (923, 923, 923, 88, '30/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (924, 924, 924, 80, '26/2/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (925, 925, 925, 56, '16/2/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (926, 926, 926, 65, '3/8/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (927, 927, 927, 56, '24/9/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (928, 928, 928, 58, '6/5/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (929, 929, 929, 81, '18/7/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (930, 930, 930, 1, '14/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (931, 931, 931, 90, '26/1/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (932, 932, 932, 9, '3/2/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (933, 933, 933, 44, '22/9/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (934, 934, 934, 23, '23/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (935, 935, 935, 19, '30/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (936, 936, 936, 55, '2/2/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (937, 937, 937, 23, '24/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (938, 938, 938, 4, '28/8/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (939, 939, 939, 61, '31/1/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (940, 940, 940, 35, '4/6/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (941, 941, 941, 13, '2/6/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (942, 942, 942, 93, '1/10/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (943, 943, 943, 24, '23/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (944, 944, 944, 78, '19/8/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (945, 945, 945, 44, '11/3/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (946, 946, 946, 63, '20/2/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (947, 947, 947, 46, '11/2/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (948, 948, 948, 75, '10/5/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (949, 949, 949, 22, '24/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (950, 950, 950, 9, '10/11/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (951, 951, 951, 18, '12/11/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (952, 952, 952, 13, '15/3/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (953, 953, 953, 38, '11/6/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (954, 954, 954, 50, '17/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (955, 955, 955, 5, '3/7/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (956, 956, 956, 33, '30/9/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (957, 957, 957, 29, '20/12/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (958, 958, 958, 88, '18/4/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (959, 959, 959, 42, '6/9/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (960, 960, 960, 68, '11/7/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (961, 961, 961, 66, '10/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (962, 962, 962, 2, '21/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (963, 963, 963, 43, '23/5/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (964, 964, 964, 94, '5/9/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (965, 965, 965, 55, '15/9/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (966, 966, 966, 27, '16/1/2014');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (967, 967, 967, 71, '22/7/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (968, 968, 968, 35, '3/10/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (969, 969, 969, 60, '5/5/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (970, 970, 970, 50, '17/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (971, 971, 971, 17, '24/1/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (972, 972, 972, 55, '2/10/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (973, 973, 973, 100, '27/1/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (974, 974, 974, 35, '28/11/2017');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (975, 975, 975, 48, '19/4/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (976, 976, 976, 97, '27/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (977, 977, 977, 100, '8/8/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (978, 978, 978, 50, '6/8/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (979, 979, 979, 81, '27/12/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (980, 980, 980, 43, '16/6/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (981, 981, 981, 10, '30/12/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (982, 982, 982, 4, '8/10/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (983, 983, 983, 90, '28/5/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (984, 984, 984, 4, '30/12/2010');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (985, 985, 985, 11, '7/11/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (986, 986, 986, 83, '1/6/2009');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (987, 987, 987, 95, '21/7/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (988, 988, 988, 43, '17/3/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (989, 989, 989, 35, '11/11/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (990, 990, 990, 33, '14/5/2015');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (991, 991, 991, 11, '7/4/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (992, 992, 992, 55, '10/4/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (993, 993, 993, 79, '13/11/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (994, 994, 994, 66, '28/12/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (995, 995, 995, 91, '4/3/2011');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (996, 996, 996, 2, '2/12/2018');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (997, 997, 997, 48, '1/1/2016');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (998, 998, 998, 94, '29/10/2012');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (999, 999, 999, 39, '12/12/2013');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (1000, 1000, 1000, 94, '29/10/2010');

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
