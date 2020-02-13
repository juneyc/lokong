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

@app.route('/about')
def about():
    # conn = psycopg2.connect("dbname= 'postgres' user='postgres' host='localhost' password= 'Vampires57'")
    # conn= psycopg2.connect("dbname= d8edv01tcu5qdj user=ageqcumlyzcwen' host='ec2-18-210-51-239.compute-1.amazonaws.com' password= 'c0fd2b34c2cae895435eec2378588310bbf2d601fcecd9282126e3dc1b274854'")
    conn= psycopg2.connect ("dbname=d8edv01tcu5qdj user=ageqcumlyzcwen host=ec2-18-210-51-239.compute-1.amazonaws.com password=c0fd2b34c2cae895435eec2378588310bbf2d601fcecd9282126e3dc1b274854")
    cur = conn.cursor
    # create table script
    cur.execute("""create table inventory (
	id INT,
	name VARCHAR(50),
	type VARCHAR(10),
	bp INT,
	sp INT
    );
    insert into inventory (id, name, type, bp, sp) values (1, 'Mountain Dew', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (2, 'Huck Towels White', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (3, 'Peas - Frozen', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (4, 'Mushroom - Lg - Cello', 'vegetables', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (5, 'Grouper - Fresh', 'cereal', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (6, 'Truffle Cups - White Paper', 'cereal', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (7, 'Squash - Pattypan, Yellow', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (8, 'Petite Baguette', 'cereal', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (9, 'Pasta - Spaghetti, Dry', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (10, 'Sauce - Balsamic Viniagrette', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (11, 'Cheese - Comte', 'vegetables', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (12, 'Bread - Multigrain Oval', 'vegetables', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (13, 'Flour - Cake', 'fruits', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (14, 'Cheese - St. Andre', 'fruits', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (15, 'Onions - White', 'cereal', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (16, 'Wine - Penfolds Koonuga Hill', 'fruits', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (17, 'Lentils - Green Le Puy', 'cereal', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (18, 'Pork - Loin, Bone - In', 'vegetables', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (19, 'Eel Fresh', 'fruits', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (20, 'Beef - Ox Tail, Frozen', 'fruits', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (21, 'Bread - Italian Corn Meal Poly', 'fruits', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (22, 'Carbonated Water - Orange', 'fruits', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (23, 'Cocoa Powder - Natural', 'vegetables', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (24, 'Mushroom - Porcini Frozen', 'fruits', 69, 86.25);
    insert into inventory (id, name, type, bp, sp) values (25, 'Marsala - Sperone, Fine, D.o.c.', 'cereal', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (26, 'Bagel - Everything Presliced', 'fruits', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (27, 'Plate Foam Laminated 9in Blk', 'fruits', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (28, 'Almonds Ground Blanched', 'vegetables', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (29, 'Breadfruit', 'fruits', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (30, 'Chestnuts - Whole,canned', 'vegetables', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (31, 'Trueblue - Blueberry', 'fruits', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (32, 'Sea Bass - Whole', 'cereal', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (33, 'Lychee', 'vegetables', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (34, 'Corn Shoots', 'vegetables', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (35, 'Pasta - Orzo, Dry', 'vegetables', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (36, 'Herb Du Provence - Primerba', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (37, 'Cheese - Cottage Cheese', 'vegetables', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (38, 'Cassis', 'cereal', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (39, 'Longos - Chicken Wings', 'fruits', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (40, 'Chicken - Leg / Back Attach', 'fruits', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (41, 'Cheese - Wine', 'vegetables', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (42, 'Soup - Clam Chowder, Dry Mix', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (43, 'Bread - Multigrain', 'fruits', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (44, 'Juice - Cranberry 284ml', 'vegetables', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (45, 'Bread - Dark Rye, Loaf', 'fruits', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (46, 'Fish - Base, Bouillion', 'cereal', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (47, 'Pear - Prickly', 'cereal', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (48, 'Olives - Morracan Dired', 'fruits', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (49, 'Chilli Paste, Hot Sambal Oelek', 'cereal', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (50, 'Bread - Calabrese Baguette', 'vegetables', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (51, 'Dooleys Toffee', 'cereal', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (52, 'Sauce - Sesame Thai Dressing', 'cereal', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (53, 'Apple - Granny Smith', 'fruits', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (54, 'Cheese - St. Paulin', 'fruits', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (55, 'Ice Cream Bar - Rolo Cone', 'fruits', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (56, 'Container - Clear 32 Oz', 'fruits', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (57, 'Dried Figs', 'vegetables', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (58, 'Mustard - Seed', 'cereal', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (59, 'Momiji Oroshi Chili Sauce', 'fruits', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (60, 'Chip - Potato Dill Pickle', 'vegetables', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (61, 'Pepper - Chipotle, Canned', 'fruits', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (62, 'Bar Mix - Lime', 'cereal', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (63, 'Jameson Irish Whiskey', 'vegetables', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (64, 'Beef - Striploin Aa', 'cereal', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (65, 'Cinnamon Rolls', 'cereal', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (66, 'Sausage - Blood Pudding', 'fruits', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (67, 'Wine - Duboeuf Beaujolais', 'vegetables', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (68, 'Appetizer - Tarragon Chicken', 'fruits', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (69, 'Rosemary - Fresh', 'fruits', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (70, 'Miso - Soy Bean Paste', 'vegetables', 78, 97.5);
    insert into inventory (id, name, type, bp, sp) values (71, 'Icecream - Dstk Cml And Fdg', 'fruits', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (72, 'Straw - Regular', 'vegetables', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (73, 'Ecolab - Hobart Washarm End Cap', 'cereal', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (74, 'Black Currants', 'vegetables', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (75, 'Bread - Pita', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (76, 'Appetizer - Escargot Puff', 'fruits', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (77, 'Food Colouring - Blue', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (78, 'Assorted Desserts', 'vegetables', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (79, 'Turkey - Breast, Double', 'cereal', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (80, 'Daikon Radish', 'cereal', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (81, 'Soup Campbells Split Pea And Ham', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (82, 'Plastic Arrow Stir Stick', 'vegetables', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (83, 'Chinese Foods - Chicken Wing', 'fruits', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (84, 'Blueberries - Frozen', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (85, 'Rabbit - Frozen', 'fruits', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (86, 'Bar - Sweet And Salty Chocolate', 'vegetables', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (87, 'Wine - Red, Harrow Estates, Cab', 'vegetables', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (88, 'Sobe - Lizard Fuel', 'fruits', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (89, 'Wine - Casillero Deldiablo', 'cereal', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (90, 'Turnip - Wax', 'vegetables', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (91, 'Canadian Emmenthal', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (92, 'Pate Pans Yellow', 'cereal', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (93, 'Shrimp - Black Tiger 16/20', 'fruits', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (94, 'Water - Mineral, Natural', 'vegetables', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (95, 'Mix - Cappucino Cocktail', 'fruits', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (96, 'Chutney Sauce - Mango', 'fruits', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (97, 'Rum - Light, Captain Morgan', 'vegetables', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (98, 'Water - Aquafina Vitamin', 'vegetables', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (99, 'Lid - Translucent, 3.5 And 6 Oz', 'vegetables', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (100, 'Bread - Rolls, Corn', 'vegetables', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (101, 'Ham - Procutinni', 'cereal', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (102, 'Juice - Apple, 341 Ml', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (103, 'Salmon - Sockeye Raw', 'fruits', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (104, 'Anisette - Mcguiness', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (105, 'Water - Spring Water 500ml', 'cereal', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (106, 'Cranberries - Dry', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (107, 'Crawfish', 'vegetables', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (108, 'Breadfruit', 'vegetables', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (109, 'Garam Masala Powder', 'fruits', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (110, 'Spinach - Spinach Leaf', 'fruits', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (111, 'Garlic - Primerba, Paste', 'vegetables', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (112, 'Plastic Arrow Stir Stick', 'cereal', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (113, 'Carbonated Water - Cherry', 'cereal', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (114, 'Spinach - Baby', 'vegetables', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (115, 'Bread - Calabrese Baguette', 'fruits', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (116, 'Tomatoes - Vine Ripe, Yellow', 'fruits', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (117, 'Doilies - 8, Paper', 'cereal', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (118, 'Sage Ground Wiberg', 'fruits', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (119, 'Calypso - Lemonade', 'vegetables', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (120, 'Tomatoes - Diced, Canned', 'cereal', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (121, 'Pepperoni Slices', 'vegetables', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (122, 'Wine - Baron De Rothschild', 'cereal', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (123, 'Dates', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (124, 'Chips Potato Swt Chilli Sour', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (125, 'Icecream Cone - Areo Chocolate', 'vegetables', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (126, 'Ostrich - Fan Fillet', 'cereal', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (127, 'Beer - Molson Excel', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (128, 'Oranges - Navel, 72', 'cereal', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (129, 'Bread - White, Sliced', 'cereal', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (130, 'Cheese - Montery Jack', 'fruits', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (131, 'Calvados - Boulard', 'vegetables', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (132, 'Lamb - Leg, Bone In', 'vegetables', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (133, 'Sauce - Caesar Dressing', 'vegetables', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (134, 'Sherry - Dry', 'cereal', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (135, 'Wine - Magnotta, Merlot Sr Vqa', 'vegetables', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (136, 'Mousse - Passion Fruit', 'fruits', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (137, 'Gloves - Goldtouch Disposable', 'fruits', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (138, 'Beef - Rouladin, Sliced', 'cereal', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (139, 'Veal - Inside Round / Top, Lean', 'fruits', 52, 65);
    insert into inventory (id, name, type, bp, sp) values (140, 'Milk - 1%', 'vegetables', 78, 97.5);
    insert into inventory (id, name, type, bp, sp) values (141, 'Cup - 3.5oz, Foam', 'fruits', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (142, 'Cream - 10%', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (143, 'Veal - Tenderloin, Untrimmed', 'cereal', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (144, 'Beef - Prime Rib Aaa', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (145, 'Food Colouring - Green', 'vegetables', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (146, 'Neckerchief Blck', 'cereal', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (147, 'Plaintain', 'vegetables', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (148, 'Sage - Fresh', 'cereal', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (149, 'Jameson Irish Whiskey', 'vegetables', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (150, 'Mushroom Morel Fresh', 'fruits', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (151, 'Beef - Tender Tips', 'vegetables', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (152, 'Bread - Bistro Sour', 'fruits', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (153, 'Lemonade - Kiwi, 591 Ml', 'cereal', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (154, 'Bonito Flakes - Toku Katsuo', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (155, 'Beer - Pilsner Urquell', 'cereal', 78, 97.5);
    insert into inventory (id, name, type, bp, sp) values (156, 'Cheese - Bakers Cream Cheese', 'cereal', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (157, 'Pastry - Lemon Danish - Mini', 'vegetables', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (158, 'Tart - Butter Plain Squares', 'fruits', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (159, 'Cranberries - Frozen', 'vegetables', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (160, 'Sauce - Black Current, Dry Mix', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (161, 'Jam - Strawberry, 20 Ml Jar', 'vegetables', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (162, 'Mayonnaise', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (163, 'Foam Espresso Cup Plain White', 'vegetables', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (164, 'Syrup - Pancake', 'vegetables', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (165, 'Chicken Breast Halal', 'vegetables', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (166, 'Nougat - Paste / Cream', 'fruits', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (167, 'Towels - Paper / Kraft', 'fruits', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (168, 'Mangoes', 'cereal', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (169, 'Brocolinni - Gaylan, Chinese', 'cereal', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (170, 'Crab - Dungeness, Whole, live', 'vegetables', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (171, 'Beef - Diced', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (172, 'Wine - Merlot Vina Carmen', 'fruits', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (173, 'Broom Handle', 'cereal', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (174, 'Kumquat', 'vegetables', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (175, 'Shrimp - Black Tiger 6 - 8', 'fruits', 52, 65);
    insert into inventory (id, name, type, bp, sp) values (176, 'Syrup - Chocolate', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (177, 'Cinnamon - Stick', 'fruits', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (178, 'Rabbit - Saddles', 'vegetables', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (179, 'Wine - Port Late Bottled Vintage', 'fruits', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (180, 'Squid - Tubes / Tenticles 10/20', 'cereal', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (181, 'Cake - Sheet Strawberry', 'vegetables', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (182, 'Beef - Tenderlion, Center Cut', 'vegetables', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (183, 'Taro Leaves', 'cereal', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (184, 'Capon - Whole', 'fruits', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (185, 'Mushroom - Chanterelle Frozen', 'fruits', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (186, 'Cake Circle, Foil, Scallop', 'vegetables', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (187, 'Red Snapper - Fresh, Whole', 'cereal', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (188, 'The Pop Shoppe - Root Beer', 'cereal', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (189, 'Soy Protein', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (190, 'Coffee Beans - Chocolate', 'fruits', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (191, 'Wine - Black Tower Qr', 'fruits', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (192, 'Soup - Cream Of Broccoli', 'cereal', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (193, 'Cinnamon - Stick', 'fruits', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (194, 'Ginger - Fresh', 'vegetables', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (195, 'Quiche Assorted', 'fruits', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (196, 'Bread - Dark Rye', 'fruits', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (197, 'Fish - Halibut, Cold Smoked', 'vegetables', 59, 73.75);
    insert into inventory (id, name, type, bp, sp) values (198, 'Mangostein', 'fruits', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (199, 'Lettuce - Iceberg', 'cereal', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (200, 'Gelatine Powder', 'vegetables', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (201, 'Soup - Campbells Broccoli', 'cereal', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (202, 'Wine - Balbach Riverside', 'vegetables', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (203, 'Sausage - Breakfast', 'cereal', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (204, 'Pear - Asian', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (205, 'Tarragon - Fresh', 'cereal', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (206, 'Jameson Irish Whiskey', 'vegetables', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (207, 'Shrimp - 16/20, Peeled Deviened', 'fruits', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (208, 'Walkers Special Old Whiskey', 'vegetables', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (209, 'Momiji Oroshi Chili Sauce', 'cereal', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (210, 'Beef Cheek Fresh', 'cereal', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (211, 'Wine - Pinot Grigio Collavini', 'fruits', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (212, 'Cheese - Sheep Milk', 'vegetables', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (213, 'Kiwi', 'fruits', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (214, 'Longos - Assorted Sandwich', 'vegetables', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (215, 'Nut - Walnut, Chopped', 'vegetables', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (216, 'Crab - Meat Combo', 'cereal', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (217, 'Barramundi', 'vegetables', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (218, 'Flavouring - Raspberry', 'vegetables', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (219, 'Coffee - Colombian, Portioned', 'fruits', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (220, 'Soup Campbells Turkey Veg.', 'vegetables', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (221, 'Compound - Raspberry', 'cereal', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (222, 'Veal - Eye Of Round', 'vegetables', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (223, 'Champagne - Brights, Dry', 'vegetables', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (224, 'Dragon Fruit', 'vegetables', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (225, 'White Baguette', 'fruits', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (226, 'Muffin Mix - Lemon Cranberry', 'cereal', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (227, 'Tea - Camomele', 'fruits', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (228, 'Anchovy Paste - 56 G Tube', 'cereal', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (229, 'Soup - Knorr, Chicken Gumbo', 'vegetables', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (230, 'Soup - Campbells, Minestrone', 'fruits', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (231, 'Caviar - Salmon', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (232, 'Napkin - Beverge, White 2 - Ply', 'vegetables', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (233, 'Fork - Plastic', 'fruits', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (234, 'Pie Filling - Cherry', 'cereal', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (235, 'Sour Cream', 'fruits', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (236, 'Wine - Hardys Bankside Shiraz', 'cereal', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (237, 'French Pastries', 'vegetables', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (238, 'Split Peas - Green, Dry', 'fruits', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (239, 'Table Cloth 54x72 Colour', 'vegetables', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (240, 'Tray - 16in Rnd Blk', 'fruits', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (241, 'Mushroom - Lg - Cello', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (242, 'Beef - Chuck, Boneless', 'fruits', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (243, 'Table Cloth 91x91 Colour', 'vegetables', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (244, 'Table Cloth 90x90 Colour', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (245, 'Wine - Prem Select Charddonany', 'cereal', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (246, 'Cream Of Tartar', 'fruits', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (247, 'Wine - Red, Lurton Merlot De', 'cereal', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (248, 'Danishes - Mini Raspberry', 'cereal', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (249, 'Lid - 10,12,16 Oz', 'cereal', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (250, 'Plums - Red', 'cereal', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (251, 'Broom And Brush Rack Black', 'cereal', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (252, 'Wine - Casillero Deldiablo', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (253, 'Soup - Campbells - Chicken Noodle', 'fruits', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (254, 'Cup - 8oz Coffee Perforated', 'cereal', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (255, 'Cup - Paper 10oz 92959', 'cereal', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (256, 'Sobe - Liz Blizz', 'vegetables', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (257, 'Wine - Magnotta, White', 'cereal', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (258, 'Beef - Short Loin', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (259, 'Oil - Shortening,liqud, Fry', 'fruits', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (260, 'Muffin Carrot - Individual', 'fruits', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (261, 'Bread - French Stick', 'fruits', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (262, 'Cheese - Taleggio D.o.p.', 'vegetables', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (263, 'Potatoes - Parissienne', 'vegetables', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (264, 'Cream - 35%', 'vegetables', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (265, 'Pepper - Chillies, Crushed', 'fruits', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (266, 'Nutmeg - Ground', 'cereal', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (267, 'Tomatoes - Cherry, Yellow', 'vegetables', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (268, 'Asparagus - Mexican', 'cereal', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (269, 'Croissants Thaw And Serve', 'fruits', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (270, 'Tea - Lemon Green Tea', 'cereal', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (271, 'Creamers - 10%', 'fruits', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (272, 'Cheese - Ermite Bleu', 'vegetables', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (273, 'Tea - Orange Pekoe', 'vegetables', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (274, 'Canada Dry', 'vegetables', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (275, 'Compound - Strawberry', 'cereal', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (276, 'Coffee - Colombian, Portioned', 'cereal', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (277, 'Capers - Pickled', 'vegetables', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (278, 'Nut - Walnut, Pieces', 'fruits', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (279, 'Beer - Heinekin', 'vegetables', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (280, 'Tea - Honey Green Tea', 'vegetables', 52, 65);
    insert into inventory (id, name, type, bp, sp) values (281, 'Napkin White - Starched', 'fruits', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (282, 'Mustard - Seed', 'fruits', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (283, 'Beer - Heinekin', 'vegetables', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (284, 'Oil - Safflower', 'vegetables', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (285, 'Beef - Sushi Flat Iron Steak', 'cereal', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (286, 'Apple - Northern Spy', 'fruits', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (287, 'Lid - 3oz Med Rec', 'cereal', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (288, 'Pepper - Gypsy Pepper', 'vegetables', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (289, 'Bandage - Finger Cots', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (290, 'Oranges - Navel, 72', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (291, 'Mustard Prepared', 'cereal', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (292, 'Persimmons', 'cereal', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (293, 'Pasta - Rotini, Colour, Dry', 'vegetables', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (294, 'Dooleys Toffee', 'fruits', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (295, 'Juice - Grape, White', 'cereal', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (296, 'Chinese Foods - Chicken', 'vegetables', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (297, 'Pie Filling - Pumpkin', 'vegetables', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (298, 'Tomato - Peeled Italian Canned', 'cereal', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (299, 'Godiva White Chocolate', 'fruits', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (300, 'Chicken - Wieners', 'vegetables', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (301, 'Lentils - Green Le Puy', 'vegetables', 37, 46.25);
    insert into inventory (id, name, type, bp, sp) values (302, 'Chestnuts - Whole,canned', 'vegetables', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (303, 'Pasta - Angel Hair', 'fruits', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (304, 'Onions - Cooking', 'cereal', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (305, 'Wine - Riesling Alsace Ac 2001', 'vegetables', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (306, 'Lychee', 'cereal', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (307, 'Wine - Fino Tio Pepe Gonzalez', 'cereal', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (308, 'Icecream - Dstk Strw Chseck', 'fruits', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (309, 'Beef - Salted', 'fruits', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (310, 'Goulash Seasoning', 'fruits', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (311, 'Juice - Pineapple, 341 Ml', 'vegetables', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (312, 'Beer - Blue Light', 'fruits', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (313, 'Cornflakes', 'vegetables', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (314, 'Nestea - Ice Tea, Diet', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (315, 'Glass - Wine, Plastic, Clear 5 Oz', 'cereal', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (316, 'Crab - Dungeness, Whole, live', 'fruits', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (317, 'Cinnamon - Stick', 'vegetables', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (318, 'Artichokes - Knobless, White', 'fruits', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (319, 'Milk 2% 500 Ml', 'fruits', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (320, 'Veal - Sweetbread', 'fruits', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (321, 'Lamb Shoulder Boneless Nz', 'cereal', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (322, 'Glass - Juice Clear 5oz 55005', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (323, 'Myers Planters Punch', 'fruits', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (324, 'Sauce - Demi Glace', 'vegetables', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (325, 'Appetizer - Smoked Salmon / Dill', 'fruits', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (326, 'Cabbage Roll', 'cereal', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (327, 'Cookies Oatmeal Raisin', 'vegetables', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (328, 'Potatoes - Idaho 80 Count', 'fruits', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (329, 'Muffins - Assorted', 'vegetables', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (330, 'Bagel - Everything Presliced', 'cereal', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (331, 'Wine - Balbach Riverside', 'cereal', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (332, 'Bouillion - Fish', 'vegetables', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (333, 'Noodles - Cellophane, Thin', 'cereal', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (334, 'Seedlings - Clamshell', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (335, 'Apricots - Dried', 'cereal', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (336, 'Tea - Herbal I Love Lemon', 'fruits', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (337, 'Flour Pastry Super Fine', 'vegetables', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (338, 'Banana - Green', 'cereal', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (339, 'Cranberry Foccacia', 'vegetables', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (340, 'Beans - Butter Lrg Lima', 'cereal', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (341, 'Wine - Casablanca Valley', 'cereal', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (342, 'Veal - Knuckle', 'vegetables', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (343, 'Wine - Pinot Grigio Collavini', 'fruits', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (344, 'Cheese - Grie Des Champ', 'fruits', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (345, 'Noodles - Steamed Chow Mein', 'fruits', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (346, 'Jolt Cola - Electric Blue', 'cereal', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (347, 'Radish', 'vegetables', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (348, 'Roe - Lump Fish, Black', 'vegetables', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (349, 'Lamb - Racks, Frenched', 'cereal', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (350, 'Bread - Rolls, Rye', 'fruits', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (351, 'Container - Foam Dixie 12 Oz', 'fruits', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (352, 'Beef - Ox Tongue, Pickled', 'vegetables', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (353, 'Water Chestnut - Canned', 'cereal', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (354, 'Beef - Top Sirloin - Aaa', 'fruits', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (355, 'Ecolab Silver Fusion', 'vegetables', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (356, 'Numi - Assorted Teas', 'vegetables', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (357, 'Pasta - Fettuccine, Egg, Fresh', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (358, 'Wine - Gewurztraminer Pierre', 'vegetables', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (359, 'Bread - Multigrain, Loaf', 'vegetables', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (360, 'Tomatoes - Yellow Hot House', 'cereal', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (361, 'Pork Casing', 'vegetables', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (362, 'Lamb Rack Frenched Australian', 'fruits', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (363, 'Olives - Morracan Dired', 'vegetables', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (364, 'Soup - Beef, Base Mix', 'fruits', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (365, 'Octopus - Baby, Cleaned', 'cereal', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (366, 'Pepper - Yellow Bell', 'vegetables', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (367, 'Jam - Marmalade, Orange', 'vegetables', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (368, 'Wine - Two Oceans Cabernet', 'cereal', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (369, 'Remy Red Berry Infusion', 'cereal', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (370, 'Sugar - Icing', 'fruits', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (371, 'Onions - Spanish', 'fruits', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (372, 'Soup Knorr Chili With Beans', 'cereal', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (373, 'Sprouts Dikon', 'fruits', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (374, 'Bread Crumbs - Panko', 'fruits', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (375, 'Wine - Pinot Noir Mondavi Coastal', 'vegetables', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (376, 'Rum - Mount Gay Eclipes', 'cereal', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (377, 'Shrimp - Baby, Cold Water', 'vegetables', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (378, 'French Kiss Vanilla', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (379, 'Trout - Rainbow, Frozen', 'vegetables', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (380, 'Watercress', 'cereal', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (381, 'Pomegranates', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (382, 'Eggs - Extra Large', 'vegetables', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (383, 'Pork - Loin, Boneless', 'cereal', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (384, 'Soup - Knorr, Chicken Gumbo', 'vegetables', 52, 65);
    insert into inventory (id, name, type, bp, sp) values (385, 'Glucose', 'fruits', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (386, 'Dried Cranberries', 'vegetables', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (387, 'Shichimi Togarashi Peppeers', 'fruits', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (388, 'Energy Drink - Franks Original', 'vegetables', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (389, 'Beef - Inside Round', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (390, 'Alize Gold Passion', 'vegetables', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (391, 'Sauce - Hollandaise', 'vegetables', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (392, 'Soup - Boston Clam Chowder', 'fruits', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (393, 'Piping - Bags Quizna', 'fruits', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (394, 'Sesame Seed Black', 'fruits', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (395, 'Container - Clear 32 Oz', 'vegetables', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (396, 'Wine La Vielle Ferme Cote Du', 'fruits', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (397, 'Sauce - Fish 25 Ozf Bottle', 'vegetables', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (398, 'Chips - Doritos', 'fruits', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (399, 'Corn - On The Cob', 'cereal', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (400, 'Rum - Dark, Bacardi, Black', 'vegetables', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (401, 'Squash - Guords', 'cereal', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (402, 'Beef Tenderloin Aaa', 'fruits', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (403, 'Tea - Camomele', 'cereal', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (404, 'Wine - Sicilia Igt Nero Avola', 'vegetables', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (405, 'Bread Foccacia Whole', 'cereal', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (406, 'Amarula Cream', 'cereal', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (407, 'Wine - Alsace Gewurztraminer', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (408, 'Chocolate Eclairs', 'cereal', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (409, 'Melon - Watermelon, Seedless', 'vegetables', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (410, 'Bread Roll Foccacia', 'fruits', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (411, 'Chilli Paste, Sambal Oelek', 'cereal', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (412, 'Salmon - Canned', 'fruits', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (413, 'Chutney Sauce', 'fruits', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (414, 'Chocolate - Milk', 'vegetables', 78, 97.5);
    insert into inventory (id, name, type, bp, sp) values (415, 'Soup - Knorr, Chicken Noodle', 'cereal', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (416, 'Compound - Strawberry', 'fruits', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (417, 'Soup - French Onion', 'fruits', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (418, 'Water - Mineral, Natural', 'fruits', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (419, 'Pork - Side Ribs', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (420, 'Wine - Chenin Blanc K.w.v.', 'cereal', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (421, 'Ginger - Pickled', 'cereal', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (422, 'Mousse - Passion Fruit', 'cereal', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (423, 'Wine - Sicilia Igt Nero Avola', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (424, 'Pastry - Banana Muffin - Mini', 'vegetables', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (425, 'Wine - White, Gewurtzraminer', 'vegetables', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (426, 'Wine - Chianti Classico Riserva', 'vegetables', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (427, 'Napkin Colour', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (428, 'Cheese - Blue', 'fruits', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (429, 'Wine - Shiraz South Eastern', 'cereal', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (430, 'Soup - Knorr, Veg / Beef', 'fruits', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (431, 'Tabasco Sauce, 2 Oz', 'fruits', 59, 73.75);
    insert into inventory (id, name, type, bp, sp) values (432, 'Wine - Magnotta - Cab Sauv', 'vegetables', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (433, 'Juice - Apple 284ml', 'fruits', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (434, 'Wine - Fume Blanc Fetzer', 'cereal', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (435, 'Cream - 35%', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (436, 'Bandage - Finger Cots', 'cereal', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (437, 'Greens Mustard', 'vegetables', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (438, 'Wine - Magnotta - Belpaese', 'cereal', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (439, 'Chick Peas - Canned', 'fruits', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (440, 'Banana Turning', 'fruits', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (441, 'Cod - Salted, Boneless', 'cereal', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (442, 'Pate - Cognac', 'vegetables', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (443, 'Bagel - Everything', 'fruits', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (444, 'Currants', 'cereal', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (445, 'Sprouts - Peppercress', 'cereal', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (446, 'Tortillas - Flour, 8', 'vegetables', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (447, 'Jerusalem Artichoke', 'fruits', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (448, 'Nut - Pecan, Pieces', 'cereal', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (449, 'Beer - Sleeman Fine Porter', 'cereal', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (450, 'Longos - Grilled Veg Sandwiches', 'vegetables', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (451, 'Oregano - Fresh', 'cereal', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (452, 'Syrup - Monin - Granny Smith', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (453, 'Stock - Beef, Brown', 'cereal', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (454, 'Mushroom - King Eryingii', 'cereal', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (455, 'Sugar - Brown', 'vegetables', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (456, 'Chip - Potato Dill Pickle', 'vegetables', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (457, 'Pork - Ham Hocks - Smoked', 'fruits', 78, 97.5);
    insert into inventory (id, name, type, bp, sp) values (458, 'Pepper - Red Chili', 'cereal', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (459, 'Wine - Vovray Sec Domaine Huet', 'cereal', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (460, 'Sprouts - China Rose', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (461, 'Pastry - Banana Tea Loaf', 'vegetables', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (462, 'Croissant, Raw - Mini', 'vegetables', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (463, 'Ecolab - Ster Bac', 'vegetables', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (464, 'Tomato - Plum With Basil', 'cereal', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (465, 'Muffin - Mix - Creme Brule 15l', 'cereal', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (466, 'Alize Gold Passion', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (467, 'Coffee - Egg Nog Capuccino', 'vegetables', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (468, 'Sour Puss Raspberry', 'cereal', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (469, 'Shrimp - 16/20, Iqf, Shell On', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (470, 'Guava', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (471, 'Wine - Sogrape Mateus Rose', 'vegetables', 78, 97.5);
    insert into inventory (id, name, type, bp, sp) values (472, 'Bread Cranberry Foccacia', 'vegetables', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (473, 'Leeks - Large', 'vegetables', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (474, 'Ginger - Ground', 'vegetables', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (475, 'Tomato Paste', 'vegetables', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (476, 'Wine - Trimbach Pinot Blanc', 'vegetables', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (477, 'True - Vue Containers', 'cereal', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (478, 'Silicone Paper 16.5x24', 'fruits', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (479, 'Crackers - Water', 'fruits', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (480, 'Nantuket Peach Orange', 'fruits', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (481, 'Chinese Foods - Plain Fried Rice', 'vegetables', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (482, 'Squid U5 - Thailand', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (483, 'Nut - Hazelnut, Ground, Natural', 'cereal', 39, 48.75);
    insert into inventory (id, name, type, bp, sp) values (484, 'Chef Hat 20cm', 'fruits', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (485, 'Cake - Mini Potato Pancake', 'vegetables', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (486, 'Oil - Olive Bertolli', 'cereal', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (487, 'Grapes - Black', 'cereal', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (488, 'Beans - Wax', 'cereal', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (489, 'Bread - Ciabatta Buns', 'fruits', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (490, 'Bread - White Epi Baguette', 'vegetables', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (491, 'Bread - Bagels, Mini', 'vegetables', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (492, 'Compound - Mocha', 'fruits', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (493, 'Lamb - Racks, Frenched', 'fruits', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (494, 'Nectarines', 'fruits', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (495, 'Wine - Remy Pannier Rose', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (496, 'Plate - Foam, Bread And Butter', 'fruits', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (497, 'Wine - Malbec Trapiche Reserve', 'vegetables', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (498, 'Mayonnaise', 'cereal', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (499, 'Ginsing - Fresh', 'cereal', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (500, 'Beef - Tenderlion, Center Cut', 'cereal', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (501, 'Oranges', 'vegetables', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (502, 'Cheese - Augre Des Champs', 'vegetables', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (503, 'Rappini - Andy Boy', 'cereal', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (504, 'Chocolate - Mi - Amere Semi', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (505, 'Chicken Giblets', 'vegetables', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (506, 'Cheese - Ermite Bleu', 'fruits', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (507, 'Chocolate Bar - Smarties', 'vegetables', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (508, 'Sugar - Palm', 'vegetables', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (509, 'Flour - Bran, Red', 'vegetables', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (510, 'Lettuce - Arugula', 'vegetables', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (511, 'Compound - Passion Fruit', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (512, 'Yeast Dry - Fleischman', 'cereal', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (513, 'Sambuca - Ramazzotti', 'vegetables', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (514, 'Chicken - Wings, Tip Off', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (515, 'Ginger - Ground', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (516, 'Chocolate Bar - Reese Pieces', 'vegetables', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (517, 'Sea Bass - Whole', 'cereal', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (518, 'Wine - Pinot Noir Stoneleigh', 'vegetables', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (519, 'Thyme - Dried', 'fruits', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (520, 'Chocolate Eclairs', 'vegetables', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (521, 'Turnip - White, Organic', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (522, 'Oil - Shortening,liqud, Fry', 'vegetables', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (523, 'Soup - Campbells - Chicken Noodle', 'fruits', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (524, 'Yogurt - Assorted Pack', 'cereal', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (525, 'Pear - Halves', 'fruits', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (526, 'Schnappes - Peach, Walkers', 'vegetables', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (527, 'Yokaline', 'cereal', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (528, 'Wine - Tio Pepe Sherry Fino', 'cereal', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (529, 'Yogurt - Banana, 175 Gr', 'fruits', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (530, 'Chips Potato Reg 43g', 'cereal', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (531, 'Cookie Dough - Chocolate Chip', 'fruits', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (532, 'Mushroom - Chantrelle, Fresh', 'vegetables', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (533, 'Hog / Sausage Casing - Pork', 'vegetables', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (534, 'Soup - Cream Of Potato / Leek', 'cereal', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (535, 'Sprouts - Brussel', 'cereal', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (536, 'Apron', 'cereal', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (537, 'Pork - Belly Fresh', 'vegetables', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (538, 'Tomatoes - Plum, Canned', 'cereal', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (539, 'Cookies Oatmeal Raisin', 'vegetables', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (540, 'Ham - Smoked, Bone - In', 'fruits', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (541, 'Beans - Soya Bean', 'vegetables', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (542, 'Cloves - Ground', 'vegetables', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (543, 'Kiwi Gold Zespri', 'vegetables', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (544, 'Bread - White Mini Epi', 'cereal', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (545, 'Cookie Dough - Double', 'fruits', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (546, 'Butter Balls Salted', 'cereal', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (547, 'Lamb - Whole, Fresh', 'cereal', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (548, 'Wine - Pinot Grigio Collavini', 'fruits', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (549, 'Carbonated Water - Blackcherry', 'cereal', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (550, 'Wine - Balbach Riverside', 'fruits', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (551, 'Cheese - Brick With Pepper', 'cereal', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (552, 'Cheese - Mozzarella', 'fruits', 69, 86.25);
    insert into inventory (id, name, type, bp, sp) values (553, 'Wine - Chateau Aqueria Tavel', 'fruits', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (554, 'Shiro Miso', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (555, 'Milk - Condensed', 'fruits', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (556, 'Crush - Grape, 355 Ml', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (557, 'Nut - Walnut, Pieces', 'cereal', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (558, 'Tia Maria', 'fruits', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (559, 'Mix Pina Colada', 'cereal', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (560, 'Mushroom - Crimini', 'fruits', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (561, 'Wine - Chardonnay South', 'vegetables', 59, 73.75);
    insert into inventory (id, name, type, bp, sp) values (562, 'Leeks - Large', 'cereal', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (563, 'Pork - Bacon, Sliced', 'vegetables', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (564, 'Longos - Chicken Cordon Bleu', 'cereal', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (565, 'Coriander - Ground', 'vegetables', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (566, 'Bread - Rolls, Corn', 'cereal', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (567, 'Pineapple - Regular', 'vegetables', 69, 86.25);
    insert into inventory (id, name, type, bp, sp) values (568, 'Water - Mineral, Carbonated', 'vegetables', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (569, 'The Pop Shoppe - Lime Rickey', 'fruits', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (570, 'Schnappes Peppermint - Walker', 'cereal', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (571, 'Wine - Rosso Toscano Igt', 'vegetables', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (572, 'Compound - Raspberry', 'fruits', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (573, 'Pan Grease', 'cereal', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (574, 'Beef Wellington', 'fruits', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (575, 'Cheese - Gorgonzola', 'vegetables', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (576, 'Veal - Inside Round / Top, Lean', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (577, 'Quail - Whole, Bone - In', 'fruits', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (578, 'Bagels Poppyseed', 'vegetables', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (579, 'Chocolate - Feathers', 'fruits', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (580, 'Apricots - Halves', 'vegetables', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (581, 'Mushroom - Crimini', 'fruits', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (582, 'Halibut - Whole, Fresh', 'cereal', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (583, 'Eel Fresh', 'vegetables', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (584, 'Pork - Bacon, Sliced', 'fruits', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (585, 'Skewers - Bamboo', 'fruits', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (586, 'Pepsi, 355 Ml', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (587, 'Beef - Diced', 'cereal', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (588, 'Squid U5 - Thailand', 'cereal', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (589, 'Kiwano', 'cereal', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (590, 'Wasabi Paste', 'fruits', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (591, 'Cheese - St. Andre', 'vegetables', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (592, 'Doilies - 12, Paper', 'fruits', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (593, 'Carbonated Water - Peach', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (594, 'Mustard - Individual Pkg', 'vegetables', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (595, 'Wine - Pinot Noir Latour', 'cereal', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (596, 'Flavouring - Rum', 'cereal', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (597, 'Laundry - Bag Cloth', 'cereal', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (598, 'Muffin Mix - Morning Glory', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (599, 'Veal - Kidney', 'vegetables', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (600, 'Mushroom - Trumpet, Dry', 'fruits', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (601, 'Thermometer Digital', 'cereal', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (602, 'Appetiser - Bought', 'fruits', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (603, 'Spinach - Baby', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (604, 'Coriander - Ground', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (605, 'Cheese - Shred Cheddar / Mozza', 'cereal', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (606, 'Juice - Grapefruit, 341 Ml', 'fruits', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (607, 'Pear - Halves', 'fruits', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (608, 'Pasta - Angel Hair', 'cereal', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (609, 'Coffee - Frthy Coffee Crisp', 'fruits', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (610, 'Scotch - Queen Anne', 'fruits', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (611, 'Cheese - Boursin, Garlic / Herbs', 'cereal', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (612, 'Bread - Bistro Sour', 'cereal', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (613, 'Piping - Bags Quizna', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (614, 'Catfish - Fillets', 'cereal', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (615, 'Red Pepper Paste', 'cereal', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (616, 'Soup - Chicken And Wild Rice', 'vegetables', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (617, 'Veal - Slab Bacon', 'cereal', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (618, 'Wine - Remy Pannier Rose', 'cereal', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (619, 'Mince Meat - Filling', 'vegetables', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (620, 'Beef - Roasted, Cooked', 'fruits', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (621, 'Schnappes Peppermint - Walker', 'cereal', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (622, 'Cinnamon Rolls', 'vegetables', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (623, 'Strawberries - California', 'fruits', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (624, 'Lotus Root', 'vegetables', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (625, 'Pastry - Butterscotch Baked', 'cereal', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (626, 'Juice - Ocean Spray Kiwi', 'cereal', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (627, 'Wine - Cahors Ac 2000, Clos', 'vegetables', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (628, 'Pork - Back, Short Cut, Boneless', 'fruits', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (629, 'Flour Dark Rye', 'vegetables', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (630, 'Bread - Focaccia Quarter', 'vegetables', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (631, 'Garam Masala Powder', 'fruits', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (632, 'Rosemary - Primerba, Paste', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (633, 'Sausage - Chorizo', 'fruits', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (634, 'Sugar - Palm', 'cereal', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (635, 'Cheese - Sheep Milk', 'vegetables', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (636, 'Bread - French Stick', 'cereal', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (637, 'Breakfast Quesadillas', 'cereal', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (638, 'Lettuce - Baby Salad Greens', 'fruits', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (639, 'Cake - Miini Cheesecake Cherry', 'fruits', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (640, 'Port - 74 Brights', 'vegetables', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (641, 'Orange - Blood', 'fruits', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (642, 'Wine - Sauvignon Blanc', 'cereal', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (643, 'Garlic Powder', 'vegetables', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (644, 'Table Cloth 81x81 Colour', 'cereal', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (645, 'Chocolate - Pistoles, White', 'fruits', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (646, 'Bandage - Fexible 1x3', 'cereal', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (647, 'Cardamon Seed / Pod', 'cereal', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (648, 'Gingerale - Diet - Schweppes', 'fruits', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (649, 'Salmon Steak - Cohoe 8 Oz', 'vegetables', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (650, 'Stock - Beef, White', 'cereal', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (651, 'Mcguinness - Blue Curacao', 'fruits', 8, 10);
    insert into inventory (id, name, type, bp, sp) values (652, 'Muffin Batt - Ban Dream Zero', 'vegetables', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (653, 'Snapple - Iced Tea Peach', 'vegetables', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (654, 'Horseradish - Prepared', 'vegetables', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (655, 'Lemonade - Natural, 591 Ml', 'vegetables', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (656, 'Basil - Seedlings Cookstown', 'cereal', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (657, 'Ranchero - Primerba, Paste', 'vegetables', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (658, 'Coffee Cup 16oz Foam', 'cereal', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (659, 'Browning Caramel Glace', 'vegetables', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (660, 'Ecolab - Hobart Washarm End Cap', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (661, 'Sour Puss Sour Apple', 'cereal', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (662, 'Pasta - Cheese / Spinach Bauletti', 'cereal', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (663, 'Mini - Vol Au Vents', 'cereal', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (664, 'Pears - Bartlett', 'fruits', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (665, 'Soup - Campbells, Chix Gumbo', 'fruits', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (666, 'Juice - Apple, 1.36l', 'vegetables', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (667, 'Beets - Candy Cane, Organic', 'vegetables', 69, 86.25);
    insert into inventory (id, name, type, bp, sp) values (668, 'Soup - Cream Of Broccoli, Dry', 'vegetables', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (669, 'Wine - Zonnebloem Pinotage', 'cereal', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (670, 'Cheese - Victor Et Berthold', 'cereal', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (671, 'Veal - Liver', 'fruits', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (672, 'Milk Powder', 'fruits', 52, 65);
    insert into inventory (id, name, type, bp, sp) values (673, 'Oil - Pumpkinseed', 'vegetables', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (674, 'Cocoa Powder - Dutched', 'fruits', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (675, 'Dry Ice', 'fruits', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (676, 'Ice Cream - Turtles Stick Bar', 'cereal', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (677, 'Sauce - Plum', 'fruits', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (678, 'Pepper - Green', 'cereal', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (679, 'Bread - Pita, Mini', 'fruits', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (680, 'Shrimp - 21/25, Peel And Deviened', 'fruits', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (681, 'Nantucket Orange Juice', 'cereal', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (682, 'Appetizer - Crab And Brie', 'cereal', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (683, 'Mikes Hard Lemonade', 'fruits', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (684, 'Cup - 4oz Translucent', 'vegetables', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (685, 'Onion Powder', 'cereal', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (686, 'Soup - Campbells, Cream Of', 'fruits', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (687, 'Soup - Campbells Bean Medley', 'cereal', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (688, 'Capon - Breast, Double, Wing On', 'vegetables', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (689, 'Beef Wellington', 'cereal', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (690, 'Sandwich Wrap', 'cereal', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (691, 'Tea Leaves - Oolong', 'fruits', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (692, 'Wine - Marlbourough Sauv Blanc', 'cereal', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (693, 'Ham - Virginia', 'vegetables', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (694, 'Pickles - Gherkins', 'vegetables', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (695, 'Capers - Pickled', 'fruits', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (696, 'Sauce - Hollandaise', 'vegetables', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (697, 'Bread Crumbs - Panko', 'cereal', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (698, 'Table Cloth 91x91 Colour', 'vegetables', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (699, 'Mushroom - Crimini', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (700, 'Beer - Fruli', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (701, 'Crackers - Soda / Saltins', 'cereal', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (702, 'Coffee - French Vanilla Frothy', 'vegetables', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (703, 'Parasol Pick Stir Stick', 'cereal', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (704, 'Chef Hat 20cm', 'fruits', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (705, 'Pasta - Fettuccine, Dry', 'vegetables', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (706, 'Cocoa Powder - Dutched', 'fruits', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (707, 'Lettuce - Curly Endive', 'vegetables', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (708, 'Coffee - Dark Roast', 'vegetables', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (709, 'Coffee Cup 16oz Foam', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (710, 'Lobak', 'cereal', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (711, 'Apple - Custard', 'cereal', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (712, 'Monkfish - Fresh', 'fruits', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (713, 'Creme De Cacao Mcguines', 'fruits', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (714, 'Oranges - Navel, 72', 'fruits', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (715, 'Mcgillicuddy Vanilla Schnap', 'cereal', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (716, 'Plate Pie Foil', 'vegetables', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (717, 'Salami - Genova', 'vegetables', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (718, 'Bagel - Everything', 'vegetables', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (719, 'Beef - Outside, Round', 'fruits', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (720, 'Tea - Lemon Green Tea', 'vegetables', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (721, 'Cheese - Woolwich Goat, Log', 'vegetables', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (722, 'Sauce - Marinara', 'vegetables', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (723, 'Veal - Striploin', 'cereal', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (724, 'Soup - French Can Pea', 'fruits', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (725, 'Vodka - Hot, Lnferno', 'fruits', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (726, 'Wine - Hardys Bankside Shiraz', 'vegetables', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (727, 'Coriander - Seed', 'cereal', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (728, 'Longos - Grilled Chicken With', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (729, 'Lettuce - Spring Mix', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (730, 'Walkers Special Old Whiskey', 'vegetables', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (731, 'Clam - Cherrystone', 'cereal', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (732, 'Flower - Potmums', 'vegetables', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (733, 'Hipnotiq Liquor', 'cereal', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (734, 'Fork - Plastic', 'fruits', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (735, 'Creme De Menthe Green', 'cereal', 59, 73.75);
    insert into inventory (id, name, type, bp, sp) values (736, 'Nutmeg - Ground', 'cereal', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (737, 'Rice - Brown', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (738, 'Poppy Seed', 'vegetables', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (739, 'Apricots - Dried', 'cereal', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (740, 'Tomatoes - Orange', 'vegetables', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (741, 'Soup Campbells - Tomato Bisque', 'cereal', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (742, 'Beef - Rib Eye Aaa', 'fruits', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (743, 'Pie Shell - 5', 'cereal', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (744, 'Wine - Niagara,vqa Reisling', 'fruits', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (745, 'Soup - Campbells Asian Noodle', 'cereal', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (746, 'Scallops - 10/20', 'vegetables', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (747, 'Sambuca - Ramazzotti', 'cereal', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (748, 'Soup - Campbells, Chix Gumbo', 'cereal', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (749, 'Cheese - Ricotta', 'cereal', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (750, 'Salmon Steak - Cohoe 8 Oz', 'fruits', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (751, 'Tomatoes - Cherry, Yellow', 'vegetables', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (752, 'Pastry - Baked Scones - Mini', 'cereal', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (753, 'Pasta - Canelloni, Single Serve', 'fruits', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (754, 'Ecolab - Solid Fusion', 'cereal', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (755, 'The Pop Shoppe - Root Beer', 'cereal', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (756, 'Skirt - 24 Foot', 'vegetables', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (757, 'Pasta - Fett Alfredo, Single Serve', 'cereal', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (758, 'Cake - Night And Day Choclate', 'cereal', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (759, 'Spinach - Packaged', 'cereal', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (760, 'Shrimp - Black Tiger 26/30', 'cereal', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (761, 'Russian Prince', 'cereal', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (762, 'Truffle Cups - Brown', 'fruits', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (763, 'Water - Spring Water 500ml', 'cereal', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (764, 'Bread - Petit Baguette', 'fruits', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (765, 'Oil - Peanut', 'cereal', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (766, 'Rum - Cream, Amarula', 'vegetables', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (767, 'Sugar - Invert', 'fruits', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (768, 'Appetizer - Escargot Puff', 'fruits', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (769, 'Pork - Side Ribs', 'cereal', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (770, 'Ice Cream - Turtles Stick Bar', 'cereal', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (771, 'Basil - Primerba, Paste', 'vegetables', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (772, 'Squeeze Bottle', 'fruits', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (773, 'Beer - Maudite', 'vegetables', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (774, 'Veal - Brisket, Provimi, Bone - In', 'fruits', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (775, 'Pur Source', 'fruits', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (776, 'Rice Wine - Aji Mirin', 'vegetables', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (777, 'Fiddlehead - Frozen', 'fruits', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (778, 'Tomatoes - Grape', 'fruits', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (779, 'Quail - Jumbo Boneless', 'cereal', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (780, 'Chinese Foods - Chicken', 'vegetables', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (781, 'Ocean Spray - Ruby Red', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (782, 'Table Cloth 62x114 Colour', 'cereal', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (783, 'Dragon Fruit', 'cereal', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (784, 'Pepper - Cayenne', 'fruits', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (785, 'Pork - Bones', 'cereal', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (786, 'Bagel - Sesame Seed Presliced', 'vegetables', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (787, 'Lamb - Whole, Fresh', 'vegetables', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (788, 'Pie Filling - Pumpkin', 'cereal', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (789, 'Long Island Ice Tea', 'vegetables', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (790, 'Appetizer - Tarragon Chicken', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (791, 'Wine - Puligny Montrachet A.', 'cereal', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (792, 'Mustard - Dijon', 'vegetables', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (793, '7up Diet, 355 Ml', 'vegetables', 16, 20);
    insert into inventory (id, name, type, bp, sp) values (794, 'Compound - Raspberry', 'fruits', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (795, 'Juice - Apple, 341 Ml', 'vegetables', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (796, 'Beef - Bones, Marrow', 'fruits', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (797, 'Beef Striploin Aaa', 'cereal', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (798, 'Cherries - Frozen', 'cereal', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (799, 'Lamb - Bones', 'fruits', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (800, 'Arctic Char - Fillets', 'vegetables', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (801, 'Wine - Zinfandel Rosenblum', 'cereal', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (802, 'Appetizer - Lobster Phyllo Roll', 'cereal', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (803, 'Coffee - 10oz Cup 92961', 'fruits', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (804, 'Nescafe - Frothy French Vanilla', 'fruits', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (805, 'Quail - Eggs, Fresh', 'vegetables', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (806, 'Lobster - Canned Premium', 'fruits', 26, 32.5);
    insert into inventory (id, name, type, bp, sp) values (807, 'Lemon Pepper', 'vegetables', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (808, 'Bar Energy Chocchip', 'vegetables', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (809, 'Muffin - Zero Transfat', 'fruits', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (810, 'Cotton Wet Mop 16 Oz', 'vegetables', 29, 36.25);
    insert into inventory (id, name, type, bp, sp) values (811, 'Island Oasis - Magarita Mix', 'cereal', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (812, 'Pears - Bosc', 'fruits', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (813, 'Bagel - Everything Presliced', 'fruits', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (814, 'Mace Ground', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (815, 'Broom Handle', 'fruits', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (816, 'Wanton Wrap', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (817, 'Wine - White, Concha Y Toro', 'vegetables', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (818, 'Petite Baguette', 'fruits', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (819, 'Cheese - Manchego, Spanish', 'cereal', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (820, 'Yogurt - Banana, 175 Gr', 'cereal', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (821, 'Wine - Sogrape Mateus Rose', 'fruits', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (822, 'Potatoes - Yukon Gold 5 Oz', 'vegetables', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (823, 'Dikon', 'vegetables', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (824, 'Crab - Back Fin Meat, Canned', 'cereal', 65, 81.25);
    insert into inventory (id, name, type, bp, sp) values (825, 'Wine - Mondavi Coastal Private', 'fruits', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (826, 'Chocolate - Chips Compound', 'vegetables', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (827, 'Capers - Ox Eye Daisy', 'fruits', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (828, 'Beer - Muskoka Cream Ale', 'vegetables', 69, 86.25);
    insert into inventory (id, name, type, bp, sp) values (829, 'Lemon Tarts', 'cereal', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (830, 'Milk - Chocolate 250 Ml', 'vegetables', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (831, 'Mustard - Dry, Powder', 'cereal', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (832, 'Coffee - Egg Nog Capuccino', 'fruits', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (833, 'Sprouts - Baby Pea Tendrils', 'fruits', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (834, 'Flour - Chickpea', 'cereal', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (835, 'Chicken - Tenderloin', 'fruits', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (836, 'Wine - Lou Black Shiraz', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (837, 'Beef - Montreal Smoked Brisket', 'fruits', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (838, 'Tart - Raisin And Pecan', 'vegetables', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (839, 'Star Anise, Whole', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (840, 'Carbonated Water - Blackcherry', 'fruits', 44, 55);
    insert into inventory (id, name, type, bp, sp) values (841, 'Dc - Sakura Fu', 'cereal', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (842, 'Artichoke - Bottom, Canned', 'vegetables', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (843, 'Ecolab - Solid Fusion', 'fruits', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (844, 'Veal - Provimi Inside', 'cereal', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (845, 'Syrup - Golden, Lyles', 'vegetables', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (846, 'Cardamon Ground', 'cereal', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (847, 'Quail - Whole, Bone - In', 'cereal', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (848, 'Rolled Oats', 'fruits', 37, 46.25);
    insert into inventory (id, name, type, bp, sp) values (849, 'Oats Large Flake', 'fruits', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (850, 'Arrowroot', 'cereal', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (851, 'Stainless Steel Cleaner Vision', 'vegetables', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (852, 'Compound - Orange', 'fruits', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (853, 'Icecream Bar - Del Monte', 'cereal', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (854, 'Cheese - Brie, Triple Creme', 'fruits', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (855, 'Coke - Classic, 355 Ml', 'fruits', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (856, 'Pie Box - Cello Window 2.5', 'cereal', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (857, 'Pepper - Paprika, Hungarian', 'cereal', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (858, 'Chilli Paste, Ginger Garlic', 'cereal', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (859, 'Pasta - Orecchiette', 'cereal', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (860, 'Laundry - Bag Cloth', 'fruits', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (861, 'Orange Roughy 4/6 Oz', 'cereal', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (862, 'Aspic - Amber', 'fruits', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (863, 'Bouq All Italian - Primerba', 'fruits', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (864, 'Island Oasis - Ice Cream Mix', 'vegetables', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (865, 'Ice Cream Bar - Drumstick', 'cereal', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (866, 'Herb Du Provence - Primerba', 'fruits', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (867, 'Beef - Top Butt Aaa', 'cereal', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (868, 'Dried Figs', 'fruits', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (869, 'Wine - Alsace Gewurztraminer', 'fruits', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (870, 'Beer - Upper Canada Lager', 'cereal', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (871, 'Cake Slab', 'cereal', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (872, 'Pail - 4l White, With Handle', 'vegetables', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (873, 'Wine - Two Oceans Cabernet', 'fruits', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (874, 'Veal - Round, Eye Of', 'vegetables', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (875, 'Coffee - Dark Roast', 'vegetables', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (876, 'Apple - Custard', 'cereal', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (877, 'Tea - Lemon Scented', 'cereal', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (878, 'Cream Of Tartar', 'vegetables', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (879, 'Pork - Caul Fat', 'cereal', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (880, 'Pastry - Banana Muffin - Mini', 'vegetables', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (881, 'Cleaner - Pine Sol', 'fruits', 31, 38.75);
    insert into inventory (id, name, type, bp, sp) values (882, 'Asparagus - Frozen', 'fruits', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (883, 'Tart Shells - Sweet, 4', 'cereal', 55, 68.75);
    insert into inventory (id, name, type, bp, sp) values (884, 'Rappini - Andy Boy', 'fruits', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (885, 'Daikon Radish', 'vegetables', 13, 16.25);
    insert into inventory (id, name, type, bp, sp) values (886, 'Kolrabi', 'cereal', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (887, 'Coconut - Shredded, Sweet', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (888, 'Beer - Labatt Blue', 'vegetables', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (889, 'Jam - Blackberry, 20 Ml Jar', 'fruits', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (890, 'Shrimp - Prawn', 'cereal', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (891, 'Tray - 12in Rnd Blk', 'fruits', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (892, 'Vinegar - Rice', 'fruits', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (893, 'Table Cloth 91x91 Colour', 'vegetables', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (894, 'Beef - Ground Medium', 'cereal', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (895, 'Sugar - Individual Portions', 'fruits', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (896, 'Pate - Peppercorn', 'cereal', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (897, 'Juice - Mango', 'fruits', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (898, 'Pork - Kidney', 'vegetables', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (899, 'Oil - Cooking Spray', 'fruits', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (900, 'Pop - Club Soda Can', 'vegetables', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (901, 'Bread - Multigrain Oval', 'cereal', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (902, 'Soup - Campbells, Butternut', 'cereal', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (903, 'Soup Campbells Turkey Veg.', 'vegetables', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (904, 'Soup Bowl Clear 8oz92008', 'vegetables', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (905, 'Fish - Atlantic Salmon, Cold', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (906, 'Soup - Campbells Beef Strogonoff', 'vegetables', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (907, 'Pur Value', 'cereal', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (908, 'Coffee Cup 8oz 5338cd', 'vegetables', 75, 93.75);
    insert into inventory (id, name, type, bp, sp) values (909, 'Juice - Apple 284ml', 'cereal', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (910, 'Cheese Cloth No 60', 'vegetables', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (911, 'Chips Potato Reg 43g', 'vegetables', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (912, 'Pheasants - Whole', 'vegetables', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (913, 'Pork - Loin, Boneless', 'cereal', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (914, 'Tortillas - Flour, 12', 'vegetables', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (915, 'Tart Shells - Barquettes, Savory', 'cereal', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (916, 'Pork - Bones', 'fruits', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (917, 'Garbag Bags - Black', 'cereal', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (918, 'Lamb - Bones', 'cereal', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (919, 'Stock - Veal, Brown', 'cereal', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (920, 'Beef - Top Butt Aaa', 'cereal', 34, 42.5);
    insert into inventory (id, name, type, bp, sp) values (921, 'Pork Loin Bine - In Frenched', 'vegetables', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (922, 'Cheese - Cream Cheese', 'vegetables', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (923, 'Trout - Rainbow, Fresh', 'vegetables', 69, 86.25);
    insert into inventory (id, name, type, bp, sp) values (924, 'Dried Apple', 'fruits', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (925, 'Cheese - Woolwich Goat, Log', 'vegetables', 70, 87.5);
    insert into inventory (id, name, type, bp, sp) values (926, 'Wine - Magnotta - Red, Baco', 'fruits', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (927, 'Broccoli - Fresh', 'cereal', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (928, 'Tray - Foam, Square 4 - S', 'cereal', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (929, 'Wine - Cotes Du Rhone', 'fruits', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (930, 'Sauce - Plum', 'vegetables', 60, 75);
    insert into inventory (id, name, type, bp, sp) values (931, 'Sponge Cake Mix - Vanilla', 'vegetables', 28, 35);
    insert into inventory (id, name, type, bp, sp) values (932, 'Juice - Clam, 46 Oz', 'vegetables', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (933, 'Mushroom Morel Fresh', 'vegetables', 56, 70);
    insert into inventory (id, name, type, bp, sp) values (934, 'Pastry - Banana Tea Loaf', 'cereal', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (935, 'Wine - Prem Select Charddonany', 'cereal', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (936, 'Cheese Cheddar Processed', 'vegetables', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (937, 'Pasta - Lasagna Noodle, Frozen', 'vegetables', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (938, 'Fennel - Seeds', 'cereal', 89, 111.25);
    insert into inventory (id, name, type, bp, sp) values (939, 'Zucchini - Green', 'fruits', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (940, 'Butter Ripple - Phillips', 'fruits', 51, 63.75);
    insert into inventory (id, name, type, bp, sp) values (941, 'Mushroom - Shitake, Fresh', 'cereal', 27, 33.75);
    insert into inventory (id, name, type, bp, sp) values (942, 'Vanilla Beans', 'fruits', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (943, 'Vodka - Lemon, Absolut', 'fruits', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (944, 'Coffee Cup 12oz 5342cd', 'vegetables', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (945, 'The Pop Shoppe - Lime Rickey', 'fruits', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (946, 'Bread - Bagels, Plain', 'fruits', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (947, 'Placemat - Scallop, White', 'fruits', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (948, 'Beef - Kindney, Whole', 'cereal', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (949, 'Wine - Rubyport', 'cereal', 71, 88.75);
    insert into inventory (id, name, type, bp, sp) values (950, 'Steel Wool', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (951, 'Bread - White Mini Epi', 'fruits', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (952, 'Turkey Tenderloin Frozen', 'cereal', 14, 17.5);
    insert into inventory (id, name, type, bp, sp) values (953, 'Oil - Olive Bertolli', 'vegetables', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (954, 'Juice - Propel Sport', 'fruits', 67, 83.75);
    insert into inventory (id, name, type, bp, sp) values (955, 'Wine - Barossa Valley Estate', 'vegetables', 52, 65);
    insert into inventory (id, name, type, bp, sp) values (956, 'Lamb - Shoulder', 'cereal', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (957, 'Eel - Smoked', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (958, 'Raspberries - Fresh', 'fruits', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (959, 'Soap - Pine Sol Floor Cleaner', 'cereal', 15, 18.75);
    insert into inventory (id, name, type, bp, sp) values (960, 'Appetizer - Shrimp Puff', 'fruits', 20, 25);
    insert into inventory (id, name, type, bp, sp) values (961, 'Wine - Jafflin Bourgongone', 'fruits', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (962, 'Bread - Focaccia Quarter', 'cereal', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (963, 'Pie Shell - 9', 'cereal', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (964, 'Wine - White, Concha Y Toro', 'vegetables', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (965, 'Chicken - Whole Fryers', 'cereal', 77, 96.25);
    insert into inventory (id, name, type, bp, sp) values (966, 'Muffin - Mix - Bran And Maple 15l', 'cereal', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (967, 'Plasticforkblack', 'fruits', 81, 101.25);
    insert into inventory (id, name, type, bp, sp) values (968, 'Bagel - Plain', 'cereal', 73, 91.25);
    insert into inventory (id, name, type, bp, sp) values (969, 'Beets - Pickled', 'cereal', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (970, 'Veal - Kidney', 'vegetables', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (971, 'Corn Meal', 'fruits', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (972, 'Shrimp - Baby, Warm Water', 'fruits', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (973, 'Steampan - Half Size Shallow', 'vegetables', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (974, 'Mushroom - Chantrelle, Fresh', 'vegetables', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (975, 'Soup - Campbellschix Stew', 'fruits', 59, 73.75);
    insert into inventory (id, name, type, bp, sp) values (976, 'Clams - Littleneck, Whole', 'fruits', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (977, 'Onions Granulated', 'cereal', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (978, 'Appetizer - Escargot Puff', 'vegetables', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (979, 'Ostrich - Fan Fillet', 'vegetables', 38, 47.5);
    insert into inventory (id, name, type, bp, sp) values (980, 'Cream - 18%', 'cereal', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (981, 'Cranberries - Fresh', 'vegetables', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (982, 'Appetizer - Mini Egg Roll, Shrimp', 'vegetables', 37, 46.25);
    insert into inventory (id, name, type, bp, sp) values (983, 'Wine - Blue Nun Qualitatswein', 'cereal', 35, 43.75);
    insert into inventory (id, name, type, bp, sp) values (984, 'Cheese Cloth', 'cereal', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (985, 'Veal Inside - Provimi', 'fruits', 68, 85);
    insert into inventory (id, name, type, bp, sp) values (986, 'Glass - Juice Clear 5oz 55005', 'fruits', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (987, 'Soup - Campbells Chicken', 'fruits', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (988, 'Compound - Orange', 'fruits', 61, 76.25);
    insert into inventory (id, name, type, bp, sp) values (989, 'Glass - Wine, Plastic, Clear 5 Oz', 'cereal', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (990, 'Wine - Segura Viudas Aria Brut', 'fruits', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (991, 'Wine - Beaujolais Villages', 'fruits', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (992, 'Country Roll', 'vegetables', 18, 22.5);
    insert into inventory (id, name, type, bp, sp) values (993, 'Chivas Regal - 12 Year Old', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (994, 'Tart Shells - Savory, 3', 'cereal', 66, 82.5);
    insert into inventory (id, name, type, bp, sp) values (995, 'Raisin - Dark', 'vegetables', 72, 90);
    insert into inventory (id, name, type, bp, sp) values (996, 'Bagel - Everything Presliced', 'fruits', 2, 2.5);
    insert into inventory (id, name, type, bp, sp) values (997, 'Glaze - Apricot', 'cereal', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (998, 'Isomalt', 'vegetables', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (999, 'Beef Tenderloin Aaa', 'fruits', 96, 120);
    insert into inventory (id, name, type, bp, sp) values (1000, 'Cleaner - Pine Sol', 'cereal', 69, 86.25);
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
