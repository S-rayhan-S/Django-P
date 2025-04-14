# search for: 
    -BaseUserManager:
    -AbstractUserManager:
    -AbstractUser: When you want all default user fields plus some custom ones
    -AbstractBaseUser: When you want to start from scratch with minimal defaults
    -BaseUserManager: Always needed when creating a custom user model
    -gettext_lazy as _() : for auto translate to users regional language when user is in the site
    -post_save()
    -@receiver() ---Must know this from doc.It remained unfinished becaused i was tired 
    -Custom user model/Auth user model ---Must know this from doc.It remained unfinished becaused i was tired 

    ,PermisssionMixin,ugettext_lazy,
    Custom User manager
     def _create_user,create_superuser in model
     post_save,receiver
     self._meta.get_fields()
     Custom usermodel
     rate limiting mechanism

    -forms in django
    -HtttpresRedirect -https://docs.djangoproject.com/en/5.1/ref/request-response/#django.http.HttpResponseRedirect
    -reverse
    -AuthenticationForm

# Messages set up
    -need to https://docs.djangoproject.com/en/5.2/topics/db/queries/
# Product Model
    -verbose name
    -ordering in db












