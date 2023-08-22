import instaloader 
import getpass


f = open("followers.txt","w")
old_followers = []
for line in f:
   old_followers.append(line)
f.close()

L = instaloader.instaloader()

username = input("enter username: ")
password = getpass.getpass("enter password: ")
 
L.login(username , password)
print("successfully logged in! ")

profile = instaloader.profile .from_username(L.context , "setayesh_gholami")

new_followers =[]
for follower in profile.get_followers():
  new_followers.append(follower)

for old_follower in old_followers:
   if old_follower not in new_followers:
      print(old_follower)


f = open("instegram_new_followers_finder.txt","w")
for new_follower in new_followers:
   if new_follower not in old_followers:
      f.write(new_follower + "\n")
f.close()

f = open ("followers.txt" , "w")
for follower in new_followers:
   f.write(follower + "\n")
f.close()         