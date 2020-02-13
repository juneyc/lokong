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
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (1, 1, 1, 25, '2016-02-19 06:24:49');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (2, 2, 2, 14, '2013-01-29 16:28:32');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (3, 3, 3, 43, '2009-06-17 07:04:14');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (4, 4, 4, 36, '2011-05-27 03:29:51');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (5, 5, 5, 53, '2012-05-14 02:41:06');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (6, 6, 6, 9, '2018-07-14 19:24:13');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (7, 7, 7, 55, '2012-11-03 17:00:05');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (8, 8, 8, 32, '2017-04-17 11:01:36');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (9, 9, 9, 81, '2015-10-25 22:21:27');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (10, 10, 10, 57, '2018-04-02 21:55:11');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (11, 11, 11, 78, '2014-11-10 17:59:10');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (12, 12, 12, 11, '2013-02-19 15:17:11');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (13, 13, 13, 69, '2012-01-13 21:47:25');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (14, 14, 14, 16, '2017-11-11 15:30:32');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (15, 15, 15, 3, '2016-08-10 21:47:25');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (16, 16, 16, 22, '2018-08-11 06:28:20');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (17, 17, 17, 88, '2015-09-27 10:17:35');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (18, 18, 18, 30, '2010-12-23 04:27:10');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (19, 19, 19, 83, '2013-09-10 03:21:16');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (20, 20, 20, 24, '2018-12-01 13:30:01');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (21, 21, 21, 61, '2014-12-10 13:06:54');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (22, 22, 22, 10, '2017-11-02 04:01:39');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (23, 23, 23, 3, '2015-04-15 04:25:40');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (24, 24, 24, 13, '2013-11-20 04:09:41');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (25, 25, 25, 62, '2014-05-02 18:26:58');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (26, 26, 26, 55, '2018-07-10 07:06:28');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (27, 27, 27, 96, '2012-08-14 07:12:45');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (28, 28, 28, 9, '2015-12-07 15:27:33');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (29, 29, 29, 55, '2013-06-02 03:02:58');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (30, 30, 30, 47, '2013-03-22 18:41:09');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (31, 31, 31, 66, '2009-06-18 10:05:16');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (32, 32, 32, 44, '2010-11-06 04:58:58');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (33, 33, 33, 24, '2016-10-19 19:38:31');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (34, 34, 34, 12, '2017-09-14 09:02:58');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (35, 35, 35, 70, '2017-01-20 15:18:15');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (36, 36, 36, 19, '2010-08-04 20:08:16');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (37, 37, 37, 76, '2018-10-13 11:10:39');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (38, 38, 38, 20, '2015-02-21 14:50:44');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (39, 39, 39, 88, '2016-01-17 01:06:04');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (40, 40, 40, 15, '2016-02-25 23:08:41');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (41, 41, 41, 57, '2017-10-01 10:03:18');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (42, 42, 42, 28, '2010-03-03 18:37:48');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (43, 43, 43, 90, '2018-09-07 23:29:26');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (44, 44, 44, 30, '2010-09-06 12:26:09');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (45, 45, 45, 28, '2011-04-21 12:34:39');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (46, 46, 46, 81, '2013-01-15 22:20:32');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (47, 47, 47, 51, '2018-06-26 03:39:22');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (48, 48, 48, 87, '2015-09-07 06:55:55');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (49, 49, 49, 78, '2009-07-15 13:56:17');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (50, 50, 50, 58, '2012-01-13 07:40:32');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (51, 51, 51, 84, '2011-11-27 17:36:33');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (52, 52, 52, 41, '2013-06-20 05:59:19');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (53, 53, 53, 20, '2010-06-08 06:30:58');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (54, 54, 54, 78, '2016-10-11 10:04:25');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (55, 55, 55, 99, '2011-06-16 21:21:12');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (56, 56, 56, 10, '2009-05-27 04:35:45');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (57, 57, 57, 44, '2017-09-08 07:48:36');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (58, 58, 58, 74, '2015-09-09 12:24:49');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (59, 59, 59, 9, '2010-09-29 09:44:29');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (60, 60, 60, 59, '2010-11-03 23:40:43');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (61, 61, 61, 51, '2013-10-19 08:58:23');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (62, 62, 62, 55, '2018-01-30 05:21:18');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (63, 63, 63, 3, '2011-05-13 16:06:36');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (64, 64, 64, 16, '2012-03-22 18:42:20');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (65, 65, 65, 73, '2017-08-25 22:29:13');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (66, 66, 66, 78, '2018-06-05 08:04:08');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (67, 67, 67, 99, '2011-09-26 03:30:37');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (68, 68, 68, 73, '2011-05-31 05:34:16');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (69, 69, 69, 93, '2019-02-03 09:00:59');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (70, 70, 70, 10, '2014-07-23 07:37:19');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (71, 71, 71, 82, '2013-09-16 17:42:23');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (72, 72, 72, 71, '2009-03-12 10:46:20');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (73, 73, 73, 28, '2017-07-29 10:20:13');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (74, 74, 74, 16, '2017-01-10 11:42:59');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (75, 75, 75, 26, '2017-10-03 03:26:43');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (76, 76, 76, 37, '2016-10-17 05:21:33');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (77, 77, 77, 23, '2011-08-25 03:16:53');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (78, 78, 78, 9, '2013-04-02 05:52:03');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (79, 79, 79, 6, '2018-06-11 19:17:08');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (80, 80, 80, 46, '2009-06-21 07:29:45');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (81, 81, 81, 70, '2013-04-07 05:11:28');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (82, 82, 82, 85, '2014-10-16 21:51:10');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (83, 83, 83, 83, '2009-03-19 22:40:23');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (84, 84, 84, 59, '2012-10-29 01:21:19');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (85, 85, 85, 100, '2010-07-11 05:23:34');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (86, 86, 86, 35, '2013-06-21 03:52:25');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (87, 87, 87, 78, '2016-07-30 04:03:40');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (88, 88, 88, 8, '2015-08-03 19:30:52');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (89, 89, 89, 35, '2011-02-02 15:43:42');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (90, 90, 90, 80, '2009-09-01 04:50:41');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (91, 91, 91, 6, '2010-10-27 05:05:22');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (92, 92, 92, 9, '2014-06-16 23:04:06');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (93, 93, 93, 3, '2010-03-17 00:38:08');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (94, 94, 94, 44, '2015-11-18 00:53:56');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (95, 95, 95, 99, '2017-03-05 17:37:51');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (96, 96, 96, 18, '2017-05-04 14:48:10');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (97, 97, 97, 99, '2016-09-22 13:44:57');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (98, 98, 98, 36, '2015-07-13 06:23:29');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (99, 99, 99, 42, '2016-03-10 15:45:23');
    insert into sales (id, inv_id, cust_id, quantity, created_at) values (100, 100, 100, 94, '2015-05-15 16:51:13');
       

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
