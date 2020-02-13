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
    cur.execute("""create table stock (
	id INT,
	inv_id INT,
	quantity INT,
	created_at DATE
    );
    insert into stock (id, inv_id, quantity, created_at) values (1, 1, 78, '2018-03-06 00:50:04');
    insert into stock (id, inv_id, quantity, created_at) values (2, 2, 10, '2016-08-08 05:48:55');
    insert into stock (id, inv_id, quantity, created_at) values (3, 3, 90, '2013-07-17 15:39:49');
    insert into stock (id, inv_id, quantity, created_at) values (4, 4, 80, '2012-07-18 19:44:00');
    insert into stock (id, inv_id, quantity, created_at) values (5, 5, 42, '2009-03-05 10:17:30');
    insert into stock (id, inv_id, quantity, created_at) values (6, 6, 14, '2016-05-29 13:08:37');
    insert into stock (id, inv_id, quantity, created_at) values (7, 7, 39, '2016-04-10 02:00:40');
    insert into stock (id, inv_id, quantity, created_at) values (8, 8, 30, '2012-02-29 19:14:26');
    insert into stock (id, inv_id, quantity, created_at) values (9, 9, 9, '2017-07-04 06:18:33');
    insert into stock (id, inv_id, quantity, created_at) values (10, 10, 56, '2013-03-30 17:01:13');
    insert into stock (id, inv_id, quantity, created_at) values (11, 11, 86, '2014-10-21 19:41:21');
    insert into stock (id, inv_id, quantity, created_at) values (12, 12, 64, '2018-06-16 22:05:46');
    insert into stock (id, inv_id, quantity, created_at) values (13, 13, 98, '2012-03-23 16:21:02');
    insert into stock (id, inv_id, quantity, created_at) values (14, 14, 16, '2017-04-30 04:09:08');
    insert into stock (id, inv_id, quantity, created_at) values (15, 15, 7, '2012-09-19 12:20:12');
    insert into stock (id, inv_id, quantity, created_at) values (16, 16, 35, '2015-01-24 20:43:02');
    insert into stock (id, inv_id, quantity, created_at) values (17, 17, 23, '2009-11-14 10:48:34');
    insert into stock (id, inv_id, quantity, created_at) values (18, 18, 73, '2017-05-02 16:07:10');
    insert into stock (id, inv_id, quantity, created_at) values (19, 19, 72, '2009-11-10 06:56:16');
    insert into stock (id, inv_id, quantity, created_at) values (20, 20, 93, '2014-12-22 20:58:49');
    insert into stock (id, inv_id, quantity, created_at) values (21, 21, 96, '2013-06-06 14:24:34');
    insert into stock (id, inv_id, quantity, created_at) values (22, 22, 82, '2012-11-10 15:34:29');
    insert into stock (id, inv_id, quantity, created_at) values (23, 23, 71, '2014-02-25 23:41:54');
    insert into stock (id, inv_id, quantity, created_at) values (24, 24, 25, '2009-12-16 02:08:00');
    insert into stock (id, inv_id, quantity, created_at) values (25, 25, 35, '2011-05-12 14:51:08');
    insert into stock (id, inv_id, quantity, created_at) values (26, 26, 8, '2012-04-25 08:43:36');
    insert into stock (id, inv_id, quantity, created_at) values (27, 27, 65, '2015-03-07 02:23:06');
    insert into stock (id, inv_id, quantity, created_at) values (28, 28, 24, '2013-01-15 18:39:07');
    insert into stock (id, inv_id, quantity, created_at) values (29, 29, 80, '2009-12-12 23:51:20');
    insert into stock (id, inv_id, quantity, created_at) values (30, 30, 8, '2016-10-29 02:11:56');
    insert into stock (id, inv_id, quantity, created_at) values (31, 31, 3, '2010-01-25 16:31:48');
    insert into stock (id, inv_id, quantity, created_at) values (32, 32, 63, '2015-08-29 07:55:10');
    insert into stock (id, inv_id, quantity, created_at) values (33, 33, 25, '2018-12-26 09:36:07');
    insert into stock (id, inv_id, quantity, created_at) values (34, 34, 24, '2010-01-05 12:35:28');
    insert into stock (id, inv_id, quantity, created_at) values (35, 35, 81, '2016-08-25 12:19:26');
    insert into stock (id, inv_id, quantity, created_at) values (36, 36, 89, '2018-07-27 12:26:08');
    insert into stock (id, inv_id, quantity, created_at) values (37, 37, 3, '2011-09-11 08:32:36');
    insert into stock (id, inv_id, quantity, created_at) values (38, 38, 89, '2014-02-24 19:57:29');
    insert into stock (id, inv_id, quantity, created_at) values (39, 39, 85, '2015-11-20 12:34:25');
    insert into stock (id, inv_id, quantity, created_at) values (40, 40, 41, '2018-09-15 10:07:56');
    insert into stock (id, inv_id, quantity, created_at) values (41, 41, 13, '2016-12-28 22:47:21');
    insert into stock (id, inv_id, quantity, created_at) values (42, 42, 47, '2014-11-14 11:42:28');
    insert into stock (id, inv_id, quantity, created_at) values (43, 43, 84, '2010-01-12 10:45:59');
    insert into stock (id, inv_id, quantity, created_at) values (44, 44, 68, '2011-12-18 12:36:59');
    insert into stock (id, inv_id, quantity, created_at) values (45, 45, 9, '2009-06-08 01:31:19');
    insert into stock (id, inv_id, quantity, created_at) values (46, 46, 25, '2015-04-26 20:15:24');
    insert into stock (id, inv_id, quantity, created_at) values (47, 47, 1, '2018-07-25 04:38:08');
    insert into stock (id, inv_id, quantity, created_at) values (48, 48, 67, '2010-02-22 06:51:48');
    insert into stock (id, inv_id, quantity, created_at) values (49, 49, 22, '2017-07-24 03:38:34');
    insert into stock (id, inv_id, quantity, created_at) values (50, 50, 16, '2015-09-19 01:24:30');
    insert into stock (id, inv_id, quantity, created_at) values (51, 51, 85, '2014-02-06 19:49:59');
    insert into stock (id, inv_id, quantity, created_at) values (52, 52, 80, '2013-02-10 05:56:40');
    insert into stock (id, inv_id, quantity, created_at) values (53, 53, 39, '2016-05-07 21:46:16');
    insert into stock (id, inv_id, quantity, created_at) values (54, 54, 39, '2014-11-08 19:53:12');
    insert into stock (id, inv_id, quantity, created_at) values (55, 55, 84, '2016-09-23 08:54:31');
    insert into stock (id, inv_id, quantity, created_at) values (56, 56, 59, '2013-03-04 12:44:26');
    insert into stock (id, inv_id, quantity, created_at) values (57, 57, 91, '2017-04-01 23:20:50');
    insert into stock (id, inv_id, quantity, created_at) values (58, 58, 99, '2013-05-14 15:48:58');
    insert into stock (id, inv_id, quantity, created_at) values (59, 59, 17, '2014-01-25 23:08:16');
    insert into stock (id, inv_id, quantity, created_at) values (60, 60, 89, '2016-08-06 13:02:04');
    insert into stock (id, inv_id, quantity, created_at) values (61, 61, 39, '2013-06-17 10:28:31');
    insert into stock (id, inv_id, quantity, created_at) values (62, 62, 8, '2012-12-03 11:18:02');
    insert into stock (id, inv_id, quantity, created_at) values (63, 63, 94, '2009-10-21 11:26:21');
    insert into stock (id, inv_id, quantity, created_at) values (64, 64, 85, '2014-05-12 17:12:43');
    insert into stock (id, inv_id, quantity, created_at) values (65, 65, 41, '2015-12-10 02:56:27');
    insert into stock (id, inv_id, quantity, created_at) values (66, 66, 25, '2017-06-06 00:29:10');
    insert into stock (id, inv_id, quantity, created_at) values (67, 67, 45, '2014-12-03 05:40:18');
    insert into stock (id, inv_id, quantity, created_at) values (68, 68, 68, '2011-10-28 01:09:11');
    insert into stock (id, inv_id, quantity, created_at) values (69, 69, 29, '2009-04-15 20:54:08');
    insert into stock (id, inv_id, quantity, created_at) values (70, 70, 73, '2009-04-12 14:22:33');
    insert into stock (id, inv_id, quantity, created_at) values (71, 71, 47, '2012-05-02 23:51:48');
    insert into stock (id, inv_id, quantity, created_at) values (72, 72, 34, '2018-11-24 20:02:59');
    insert into stock (id, inv_id, quantity, created_at) values (73, 73, 71, '2011-12-30 08:15:25');
    insert into stock (id, inv_id, quantity, created_at) values (74, 74, 83, '2012-03-07 23:52:44');
    insert into stock (id, inv_id, quantity, created_at) values (75, 75, 18, '2010-05-23 22:50:20');
    insert into stock (id, inv_id, quantity, created_at) values (76, 76, 38, '2009-04-04 22:15:38');
    insert into stock (id, inv_id, quantity, created_at) values (77, 77, 71, '2018-09-04 07:56:01');
    insert into stock (id, inv_id, quantity, created_at) values (78, 78, 4, '2017-10-18 23:47:53');
    insert into stock (id, inv_id, quantity, created_at) values (79, 79, 60, '2009-05-23 02:02:01');
    insert into stock (id, inv_id, quantity, created_at) values (80, 80, 8, '2015-03-30 21:40:16');
    insert into stock (id, inv_id, quantity, created_at) values (81, 81, 39, '2018-05-13 09:49:33');
    insert into stock (id, inv_id, quantity, created_at) values (82, 82, 71, '2011-01-28 03:26:27');
    insert into stock (id, inv_id, quantity, created_at) values (83, 83, 87, '2016-08-23 21:07:44');
    insert into stock (id, inv_id, quantity, created_at) values (84, 84, 46, '2015-05-06 12:57:51');
    insert into stock (id, inv_id, quantity, created_at) values (85, 85, 23, '2011-02-22 14:35:58');
    insert into stock (id, inv_id, quantity, created_at) values (86, 86, 20, '2016-04-02 18:10:05');
    insert into stock (id, inv_id, quantity, created_at) values (87, 87, 79, '2010-01-22 15:42:31');
    insert into stock (id, inv_id, quantity, created_at) values (88, 88, 19, '2016-06-20 05:30:35');
    insert into stock (id, inv_id, quantity, created_at) values (89, 89, 76, '2012-12-29 22:07:08');
    insert into stock (id, inv_id, quantity, created_at) values (90, 90, 92, '2018-10-03 02:52:12');
    insert into stock (id, inv_id, quantity, created_at) values (91, 91, 87, '2010-04-22 22:52:14');
    insert into stock (id, inv_id, quantity, created_at) values (92, 92, 16, '2016-01-04 21:46:25');
    insert into stock (id, inv_id, quantity, created_at) values (93, 93, 86, '2009-05-05 19:23:25');
    insert into stock (id, inv_id, quantity, created_at) values (94, 94, 40, '2016-12-10 11:53:24');
    insert into stock (id, inv_id, quantity, created_at) values (95, 95, 58, '2010-12-11 15:55:29');
    insert into stock (id, inv_id, quantity, created_at) values (96, 96, 11, '2009-12-30 00:12:24');
    insert into stock (id, inv_id, quantity, created_at) values (97, 97, 42, '2012-12-01 16:49:24');
    insert into stock (id, inv_id, quantity, created_at) values (98, 98, 98, '2012-12-17 09:13:19');
    insert into stock (id, inv_id, quantity, created_at) values (99, 99, 44, '2011-11-13 03:18:27');
    insert into stock (id, inv_id, quantity, created_at) values (100, 100, 44, '2016-06-18 02:04:21');
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
