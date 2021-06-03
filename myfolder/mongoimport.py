from pymongo import MongoClient

data_advertisements =[
    {
        "_id": "5ec34b22b5f7f6eac5f2ec3e",
        "title": "[testaccount111] Honda Tacoma pick up - low milage.",
        "description": "Manual transmission.  Great truck, clean title. Cash only.",
        "price": "$3,587.05",
        "city": "Poolsville"},\
    {
        "_id": "5ec34b22c800f5f824c21490",
        "title": "Lost cat reward if found.",
        "description": "My fat tabby disappeared last nite on 49th and Taylor.",
        "price": "0.00"},\
    {
        "_id": "5ec34b22f764357ce29a775e",
        "title": "Trailer",
        "description": "Ullamco nulla adipisicing esse occaecat ipsum deserunt. Est excepteur tempor eiusmod non. Eiusmod occaecat enim eiusmod nostrud mollit.\r\n",
        "price": "$1,703.56"},\
    {
        "_id": "5ec34b2265403b17d00ae864",
        "title": "Lawn mower",
        "description": "Sunt eiusmod occaecat deserunt magna Lorem cillum non consequat minim do.\r\n",
        "price": "$520.13"},\
    {
        "_id": "5ec34b228eac7b1667a21a9a",
        "title": "Dirt",
        "description": "Et ea officia occaecat minim adipisicing. Ut nostrud sunt mollit ex labore. Exercitation ut exercitation sint reprehenderit duis reprehenderit.\r\n",
        "price": "Free"}\
    ]

data_posts = [\
    {
        "_id": "5ec34cb625f7e6b04907fbad",
        "title": "Food distribution",
        "city": "Hyattsville",
        "description": "Hi I think —not sure— there is a food distribution at going on now in our neighborhood community center?",
        "imgUrl": "https://www.bocaratontribune.com/wp-content/uploads/2020/04/IMG_0757-768x576.jpg",
        "publishedDate": "Sun May 17 2020 23:04:22 GMT-0400 (Eastern Daylight Time)"},\
    {
        "_id": "5ec34cb6a611ef690a38dc09",
        "title": "Need a haircut!",
        "city": "Riverdale Park",
        "description": "Can someone come to my yard and cut my hair?  I will wear a mask and also provide gloves an facemasks.  Contact Jessy at jessy@example.com",
        "imgUrl": "https://i.pinimg.com/564x/57/63/87/576387d0c55bb5a3e5dead09ac578fc5.jpg",
        "publishedDate": "Mon May 18 2020 20:04:22 GMT-0400 (Eastern Daylight Time)"},\
    {
        "_id": "5ec34cb6d1d76535514b91d9",
        "title": "aliquip veniam in eiusmod qui",
        "description": "Deserunt exercitation magna consequat nisi ullamco. Ullamco id ad proident non ullamco pariatur ad enim reprehenderit tempor aute cupidatat nostrud. Eiusmod cillum qui fugiat dolor. Commodo adipisicing est est commodo nisi eiusmod Lorem.\r\n",
        "imgUrl": "http://placehold.it/32x32",
        "publishedDate": "Mon May 18 2020 01:04:22 GMT-0400 (Eastern Daylight Time)"},\
    {
        "_id": "5ec34cb666a8e2c4f3c36cfd",
        "title": "sit culpa Lorem enim pariatur",
        "description": "Aliqua sunt aliqua laborum in ex Lorem. Culpa occaecat adipisicing proident nisi elit officia duis ullamco ea exercitation eu pariatur. Qui qui pariatur magna ullamco amet.\r\n",
        "imgUrl": "http://placehold.it/32x32",
        "publishedDate": "Wed May 21 2020 03:04:22 GMT-0400 (Eastern Daylight Time)"}\
    ]


connection_str = "<Get connection str from azure portal>"
client = MongoClient(connection_str)
db = client['cosmosazuredevprj2']

#db = client.{database}
try:
    #db.command("serverStatus")
    coll_advertisements = db['advertisements']
    res = coll_advertisements.insert_many(data_advertisements)
    # print(res)
    for doc in coll_advertisements.find():
        print(doc)

    coll_posts = db['posts']
    res = coll_posts.insert_many(data_posts)
    for doc in coll_posts.find():
        print(doc )

except Exception as e: print(e)
else: print("You are connected!")
client.close()

