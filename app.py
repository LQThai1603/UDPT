from flask import Flask, redirect, render_template, request, url_for, session, flash
import DBConnect.mongoconect as mongoconect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Trang đăng ký
# @app.route('/register')

# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mongoconect.dbConnect()
        ac = mongoconect.getAccount(username, password)

        # Kiểm tra username và password
        if ac is not None:   
            # Lưu thông tin người dùng vào session
            session['username'] = username
            session['role'] = ac['role']
            return redirect(url_for('home'))
        else:
            flash('Sai tên đăng nhập hoặc mật khẩu!')
    
    return render_template('login.html')

# Trang chủ (hiển thị dựa trên vai trò)
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        role = session['role']
        return render_template('index.html', username=username, role=role)
    return redirect(url_for('login'))

# Trang hồ sơ người dùng
@app.route('/profile/<username>')
def profile(username):
    # Kiểm tra người dùng đã đăng nhập chưa
    if 'username' in session and session['username'] == username:
        user_info = {
            'username': username,
            'age': 25,
            'bio': 'This is a short bio of the user.'
        }
        return render_template('profile.html', user=user_info)
    else:
        return redirect(url_for('login'))

# Đăng xuất
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

@app.route('/admin')
def admin_page():
    if 'role' in session and session['role'] == 'ADMIN':
        return "Welcome, Admin!"
    else:
        return "Access Denied", 403

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
