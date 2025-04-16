# Create a custom user model
    - create a def myUserManager(inherit BaseUserManager) -in Login_model
        - create_user for saving user with unique-email & pass & so on
        - create_super_user  wth permissions like is_staff,is_superiser,is_active
    - create user mdoel in Login_model
        -add fileds email,is_active,is_staff
        -set USERNAME_FIELD to email
    - create  profile model & add attributes
    

    f=[i.name for i in self._meta.get_fields()]
    for i in f:
        val=getattr(self,i)
        .....
# Create 2 forms profile ,signup form
    -Create n2 forms ProfileForm(Custom Profile model),SignupForm(Custom User model) in AppLogin
    -Create views & templates of signup,Login,logout,userprofile 
        -templates for App_Login: change_profile,login,signup
# part 4
    -Create the profile view & change_profile template
    -Add flash me3ssages to views & show them in templates

# Design the Home page & Navbar part-6
        -Show all the featured products & their details in home page
            -name,oldProce,new discounted prce,image
        -home inherits base.html
        -add Navbar to base.html 
            -add cart & collapsable/dropsown burger  menue to navbar
            -username,profile,logout,orders 
# Cart Order model
    -





