from flask import Flask, request
#http://127.0.0.1:5000/validate-user
app = Flask(__name__)
app.config['DEBUG'] = True

user_form = """
	<style>
		.error{{ color: red; }}
	</style>
	<h1>User Form </h1>
        <form method="post"> 
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value='{username}' required> 
						<p class="error">{username_error}</p>                     
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" value='{password}' required>  
						<p class="error">{password_error}</p>                  
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password"  value='{verify}' required>   
						<p class="error">{verify_error}</p>                     
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
						<input name="email" type="text" value='{email}' />
						<p class="error">{email_error}</p>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""


@app.route('/validate-user' )
def display_user():
	return user_form.format(
		username='', username_error='', 
		password='', password_error='', 
		verify='', verify_error='', 
		email='', email_error='')
		
	
def is_integer(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

@app.route('/validate-user', methods=['POST'])			
def validate_user():
	username = request.form['username']
	password = request.form['password'] 
	verify = request.form['verify']
	email = request.form['email']
	
	username_error = ''
	password_error = ''
	verify_error = ''
	email_error = ''	
	
				
	if (len(username)  < 3) or (len(username)  > 20):
			username_error = 'Please enter at least 3 characters for username.'
			username = ''
			password = ''
			verify = ''			
	else:
			username = username
			
	if not is_integer(username):
			username = username
	else:
			username = username
			usernameerror =  'Not a alpha character'
			username_error = 'Please reenter username'
			username = ''
			password = ''
			verify = ''
		
	
			
	if (len(password)  < 3) or (len(password)  > 20):
			password_error = 'Please enter at least 3 characters for password.'
			password = ''
			verify = ''
	else:		
			password = password
			
	if not password == verify:
			password_error = 'Passwords do not match'
			password = ''
			verify = ''		
	else:
			password = password
	
	if (len(verify)  < 3) or (len(verify)  > 20):	
			verify_error = 'Please enter at least 3 characters for password verification.'
			verify = ''
	else:	
			verify = verify
		
	if not verify == password:
			password_error = 'Passwords do not match'
			password = ''
			verify = ''		
	else:
		password = password
			
	if len(email)  < 0 :
			email_error = 'Please enter at least 3 characters for email.'
			email = ''
			password = ''
			verify = ''
	else:
			email = email

	if  '@' not in email or '.' not in email :
			email_error = 'Please reenter email.'
			email = ''
			password = ''
			verify = ''
	else:			
			email = email
		
	if not username_error and not password_error and not verify_error and not email_error:
		# success message
		return "Welcome "  + username
	else:
		return user_form.format(
			username_error=username_error,
			password_error=password_error,
			verify_error=verify_error,
			email_error=email_error,

#saves username in field and returns form with field saved
			username=username,
			password='',
			verify='',
			email=email)




app.run()