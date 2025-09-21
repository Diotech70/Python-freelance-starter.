while True:
			print('===== CONTACT MENU =====\n')
			print('1. add contact')
			print('2. view contact')
			print('3. search contact')
			print('4. update contact')
			print('5. delete contact')
			print('6. exit')
			choice = input('enter choice : ')
			if choice == '1':
				name = input('name : ')
				phone = input('phone : ')
				email = input('email : ')
				add_contact(name,phone,email)
			elif choice == '2':
				view_contacts()
			elif choice == '3':
				name = input('search name : ')
				search_contact(name)
			elif choice == '4':
				name = input('update name :')
				new_phone = input('update phone : ')
				new_email = input('update email : ')
				update_contact(name,new_phone,new_email)
			elif choice == '5':
				name = input('delete name : ')
				delete_contact(name)
			elif choice == '6':
				print('exiting........')
			
				break
			else:
				print('invalid syntax')