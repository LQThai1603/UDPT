from pymongo import MongoClient

client = None
db = None

# Kết nối tới MongoDB
def dbConnect():
    global client
    global db
    if client is None:  # Nếu chưa kết nối
        client = MongoClient("mongodb+srv://lqt1603:XwRqYkjKV28wOwYe@demodb.ui8r6.mongodb.net/?retryWrites=true&w=majority&appName=Demodb")
        db = client['Demo']  # Chọn database 'demo'
        print("Kết nối thành công MongoDB")
    return db  # Trả về đối tượng 'db'

# Chèn một tài liệu mới vào collection Account
def insertAccount(username, password, role):
    collection = db['Account']  # Chọn collection Account
    new_account = {
        'username': username,
        'password': password,
        'role': role
    }
    collection.insert_one(new_account)

def getAccount(username, password):
    collection = db['Account']  # Chọn collection Account
    condition = {'username' : username, 'password': password}
    ac = collection.find_one(condition)
    return ac

def closeClient():
    client.close

def main():
    dbConnect()  # Kết nối đến MongoDB

    # Chèn một tài khoản mới
    #insertAccount("lqt", "lqt123", "USER")

    # Kiểm tra tài khoản đã chèn
    account = getAccount("lqt", "lqt123")
    if account:
        print("Tìm thấy tài khoản:", account)
    else:
        print("Không tìm thấy tài khoản")

    # Đóng kết nối
    closeClient()

if __name__ == "__main__":
    main()