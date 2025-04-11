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








