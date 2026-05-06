import pymysql

def get_connection():
    return pymysql.connect(
        host="trolley.proxy.rlwy.net",
        port=19224,
        user="root",
        password="uuxudHDYCjcYFbKiVARCCuDWvbIuFtYD",
        database="resume_builder",
        cursorclass=pymysql.cursors.DictCursor
    )

# mysql://root:uuxudHDYCjcYFbKiVARCCuDWvbIuFtYD@trolley.proxy.rlwy.net:19224/resume_builder