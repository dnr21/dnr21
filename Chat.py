import fbchat

id = raw_input("Please enter your facebook ID: ")

password = raw_input("Please enter your facebook password: ")

client = fbchat.Client(id , password)

user = raw_input("Enter name of friend : ")

contacts = client.getUsers(user)

for contact in contacts:

    print contact

    select = raw_input("Y/N: ")

    if select is "Y":

        friend = contact

        sent = client.send(friend.uid,"Welcome to (%s)'s first Facebook Chat Application" %(id))

        message = raw_input("Type the message you want to send : ")

        sent = client.send(friend.uid, message)

        if sent:

            print "Message has sent successfully"

        break

    elif select is "N":

        continue

    else:

        print "Enter only Y or N."
